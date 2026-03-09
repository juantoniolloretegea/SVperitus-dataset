"""
dominios/inmunologia/fase_1/src/train_resnet.py
=========================
Entrenamiento de ResNet34 para clasificación de polígonos polares IMMUNO-1.

El orden de clases y sus índices se leen de imm_n25.yaml (class_to_idx),
garantizando coherencia con normative_engine.py, generate_polygons.py y
evaluate.py. Las carpetas ImageFolder ya han sido creadas con los nombres
canónicos por generate_polygons.py.

Uso:
    python train_resnet.py
    python train_resnet.py --epochs 50 --batch-size 64

Autor: Juan Antonio Lloret Egea  |  ORCID: 0000-0002-6634-3351
ISSN 2695-6411  |  CC BY-NC-ND 4.0
"""

import sys
import csv
import argparse
import time
from pathlib import Path
from datetime import datetime

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms, models

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.io_utils import load_config, ensure_dir

CONFIG_PATH = Path(__file__).parent / "config" / "imm_n25.yaml"
DATA_DIR    = Path(__file__).parent / "data" / "images"
MODELS_DIR  = Path(__file__).parent / "models"
RESULTS_DIR = Path(__file__).parent / "results"


def load_class_info(cfg: dict) -> tuple[list[str], dict[str, int]]:
    """
    Devuelve (classes_ordered, class_to_idx) desde el YAML.
    Punto único de verdad para el orden y los índices de clase.
    """
    class_to_idx: dict[str, int] = cfg["class_to_idx"]
    classes_ordered = sorted(class_to_idx, key=lambda c: class_to_idx[c])
    return classes_ordered, class_to_idx


def build_transforms() -> dict:
    normalize = transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std =[0.229, 0.224, 0.225],
    )
    return {
        "train": transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.RandomHorizontalFlip(),
            transforms.RandomRotation(15),
            transforms.ToTensor(),
            normalize,
        ]),
        "val": transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            normalize,
        ]),
    }


def build_dataloaders(
    batch_size: int,
    num_workers: int,
    class_to_idx_canonical: dict[str, int],
) -> dict:
    """
    Construye DataLoaders para train/val con remapeo canónico de índices.

    ImageFolder asigna índices por orden alfabético de carpetas:
        APTO=0, INDETERMINADO=1, NO_APTO=2

    El orden canónico del YAML es:
        NO_APTO=0, INDETERMINADO=1, APTO=2

    Se construye idx_map = {índice_disco → índice_canónico} y se pasa
    como target_transform, de modo que la red y las métricas trabajan
    siempre con los índices canónicos independientemente del orden en disco.

    Semántica ternaria y radios (SVcustos = SVperitus, invariante):
        0 → radio 1 (anillo interior)  — situación adecuada
        1 → radio 2 (anillo medio)     — riesgo / inadecuada
        U → radio 3 (anillo exterior)  — indeterminado
    """
    tfms    = build_transforms()
    loaders = {}

    for split in ["train", "val"]:
        split_dir = DATA_DIR / split
        if not split_dir.exists():
            raise FileNotFoundError(
                f"No se encontró {split_dir}. "
                "Ejecuta primero generate_cases.py y generate_polygons.py."
            )

        # Dataset base (sin transform) solo para leer el mapa nombre→índice de disco
        base_ds = datasets.ImageFolder(split_dir)
        class_to_idx_disk = base_ds.class_to_idx

        # Comprobación dura: el conjunto de nombres de clase debe coincidir
        if set(class_to_idx_disk.keys()) != set(class_to_idx_canonical.keys()):
            raise ValueError(
                f"Clases en disco {set(class_to_idx_disk.keys())} "
                f"!= clases canónicas {set(class_to_idx_canonical.keys())}"
            )

        # Mapa: índice_disco → índice_canónico
        # Asume la discrepancia de orden (esperada) y la resuelve en tiempo de carga.
        idx_map = {
            class_to_idx_disk[name]: class_to_idx_canonical[name]
            for name in class_to_idx_canonical
        }

        dataset = datasets.ImageFolder(
            split_dir,
            transform=tfms[split],
            target_transform=lambda idx, m=idx_map: m[idx],
        )

        loaders[split] = DataLoader(
            dataset,
            batch_size=batch_size,
            shuffle=(split == "train"),
            num_workers=num_workers,
            pin_memory=True,
        )

    return loaders


def build_model(n_classes: int, pretrained: bool = True) -> nn.Module:
    weights = models.ResNet34_Weights.IMAGENET1K_V1 if pretrained else None
    model   = models.resnet34(weights=weights)
    model.fc = nn.Linear(model.fc.in_features, n_classes)
    return model


def train_one_epoch(model, loader, criterion, optimizer, device):
    model.train()
    running_loss, correct, total = 0.0, 0, 0
    for imgs, lbls in loader:
        imgs, lbls = imgs.to(device), lbls.to(device)
        optimizer.zero_grad()
        out  = model(imgs)
        loss = criterion(out, lbls)
        loss.backward()
        optimizer.step()
        running_loss += loss.item() * imgs.size(0)
        correct      += (out.argmax(1) == lbls).sum().item()
        total        += imgs.size(0)
    return running_loss / total, correct / total


@torch.no_grad()
def evaluate_split(model, loader, criterion, device):
    model.eval()
    running_loss, correct, total = 0.0, 0, 0
    for imgs, lbls in loader:
        imgs, lbls = imgs.to(device), lbls.to(device)
        out  = model(imgs)
        loss = criterion(out, lbls)
        running_loss += loss.item() * imgs.size(0)
        correct      += (out.argmax(1) == lbls).sum().item()
        total        += imgs.size(0)
    return running_loss / total, correct / total


def main():
    parser = argparse.ArgumentParser(
        description="SVperitus IMMUNO-1 — Entrenamiento ResNet34"
    )
    parser.add_argument("--epochs",      type=int,   default=30)
    parser.add_argument("--batch-size",  type=int,   default=32)
    parser.add_argument("--lr",          type=float, default=1e-3)
    parser.add_argument("--no-pretrain", action="store_true")
    args = parser.parse_args()

    cfg = load_config(CONFIG_PATH)
    classes_ordered, class_to_idx = load_class_info(cfg)
    n_classes = len(classes_ordered)

    ensure_dir(MODELS_DIR)
    ensure_dir(RESULTS_DIR)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"\nSVperitus – IMMUNO-1  |  Entrenamiento ResNet34")
    print(f"  n=25  |  T(25)=19")
    print(f"  Clases (orden canónico YAML): {classes_ordered}")
    print(f"  class_to_idx: {class_to_idx}")
    print(f"  Device: {device}  |  Epochs: {args.epochs}  |  Batch: {args.batch_size}\n")

    loaders   = build_dataloaders(
        args.batch_size,
        cfg["training"]["num_workers"],
        class_to_idx,
    )
    model     = build_model(n_classes, pretrained=not args.no_pretrain).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=args.lr,
                           weight_decay=cfg["training"]["weight_decay"])
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)

    best_val_acc = 0.0
    timestamp    = datetime.now().strftime("%Y%m%d_%H%M%S")
    best_path    = MODELS_DIR / f"svperitus_imm1_resnet34_{timestamp}.pth"
    history      = []
    t0           = time.time()

    for epoch in range(1, args.epochs + 1):
        tr_loss, tr_acc = train_one_epoch(
            model, loaders["train"], criterion, optimizer, device
        )
        va_loss, va_acc = evaluate_split(
            model, loaders["val"], criterion, device
        )
        scheduler.step()

        history.append({
            "epoch": epoch,
            "tr_loss": tr_loss, "tr_acc": tr_acc,
            "va_loss": va_loss, "va_acc": va_acc,
        })
        print(
            f"  Epoch {epoch:03d}/{args.epochs}  "
            f"train_loss={tr_loss:.4f}  train_acc={tr_acc:.4f}  "
            f"val_loss={va_loss:.4f}  val_acc={va_acc:.4f}"
        )
        if va_acc > best_val_acc:
            best_val_acc = va_acc
            torch.save(model.state_dict(), best_path)
            print(f"    ★ Mejor modelo guardado (val_acc={best_val_acc:.4f})")

    elapsed = time.time() - t0
    print(f"\n✓ Entrenamiento completado en {elapsed/60:.1f} min.")
    print(f"  Mejor val_acc : {best_val_acc:.4f}")
    print(f"  Modelo guardado: {best_path}")

    hist_path = RESULTS_DIR / f"train_history_{timestamp}.csv"
    with open(hist_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=history[0].keys())
        writer.writeheader()
        writer.writerows(history)
    print(f"  Historial: {hist_path}")


if __name__ == "__main__":
    main()
