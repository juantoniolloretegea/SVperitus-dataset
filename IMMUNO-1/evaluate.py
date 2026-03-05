"""
IMMUNO-1/evaluate.py
=====================
Evaluación del modelo entrenado en el test set de IMMUNO-1.
Genera matriz de confusión y métricas por clase.

El orden de clases y sus índices se leen de imm_n25.yaml (class_to_idx),
garantizando coherencia con normative_engine.py y generate_polygons.py
independientemente del orden alfabético que ImageFolder asignaría por defecto.

Uso:
    python evaluate.py --model models/svperitus_imm1_resnet34_YYYYMMDD_HHMMSS.pth

Autor: Juan Antonio Lloret Egea  |  ORCID: 0000-0002-6634-3351
ISSN 2695-641X  |  CC BY-NC-ND 4.0
"""

import sys
import csv
import argparse
from pathlib import Path

import torch
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import precision_recall_fscore_support

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.io_utils import load_config, ensure_dir

CONFIG_PATH = Path(__file__).parent / "config" / "imm_n25.yaml"
DATA_DIR    = Path(__file__).parent / "data" / "images" / "test"
RESULTS_DIR = Path(__file__).parent / "results"


def load_class_info(cfg: dict) -> tuple[list[str], dict[str, int]]:
    """
    Devuelve (classes_ordered, class_to_idx) desde el YAML.

    classes_ordered : lista de nombres de clase ordenada por índice entero,
                      derivada de class_to_idx → [NO_APTO, INDETERMINADO, APTO].
    class_to_idx    : dict {nombre_clase: índice}.

    IMPORTANTE: este orden debe coincidir con el que usa generate_polygons.py
    al crear las carpetas ImageFolder. Si hay discrepancia, la matriz de
    confusión mostraría etiquetas incorrectas.
    """
    class_to_idx: dict[str, int] = cfg["class_to_idx"]
    # Ordenar por índice (valor del dict) para obtener lista canónica
    classes_ordered = sorted(class_to_idx, key=lambda c: class_to_idx[c])
    return classes_ordered, class_to_idx


def remap_imagefolder_labels(
    dataset: datasets.ImageFolder,
    class_to_idx_canonical: dict[str, int],
) -> np.ndarray:
    """
    Construye una tabla de remapeo: índice ImageFolder → índice canónico.

    ImageFolder asigna índices alfabéticamente a las carpetas que encuentra.
    El orden canónico viene de class_to_idx en el YAML.
    Si los órdenes difieren, las etiquetas numéricas devueltas por el
    DataLoader necesitan ser remapeadas antes de calcular métricas.

    Devuelve un array remap tal que:
        remap[imagefolder_idx] = canonical_idx
    """
    folder_to_idx = dataset.class_to_idx  # asignación de ImageFolder
    remap = np.zeros(len(folder_to_idx), dtype=int)
    for class_name, folder_idx in folder_to_idx.items():
        canonical_idx = class_to_idx_canonical[class_name]
        remap[folder_idx] = canonical_idx
    return remap


def build_model(n_classes: int = 3) -> torch.nn.Module:
    model = models.resnet34(weights=None)
    model.fc = torch.nn.Linear(model.fc.in_features, n_classes)
    return model


def main():
    parser = argparse.ArgumentParser(
        description="SVperitus IMMUNO-1 — Evaluación del modelo"
    )
    parser.add_argument("--model", type=Path, required=True,
                        help="Ruta al archivo .pth del modelo entrenado")
    parser.add_argument("--batch-size", type=int, default=32)
    args = parser.parse_args()

    if not args.model.exists():
        raise FileNotFoundError(f"Modelo no encontrado: {args.model}")

    cfg = load_config(CONFIG_PATH)
    classes_ordered, class_to_idx = load_class_info(cfg)
    n_classes = len(classes_ordered)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    ensure_dir(RESULTS_DIR)

    print(f"\nSVperitus – IMMUNO-1  |  Evaluación")
    print(f"  Modelo   : {args.model.name}")
    print(f"  Device   : {device}")
    print(f"  Clases   : {classes_ordered}  (orden canónico YAML)")
    print(f"  class_to_idx: {class_to_idx}\n")

    # ── Dataset de test ───────────────────────────────────────────────────────
    tfm = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    ])
    test_dataset = datasets.ImageFolder(DATA_DIR, transform=tfm)
    test_loader  = DataLoader(test_dataset, batch_size=args.batch_size,
                              shuffle=False, num_workers=4)

    # Remapeo: índice ImageFolder (alfabético) → índice canónico (YAML)
    remap = remap_imagefolder_labels(test_dataset, class_to_idx)
    print(f"  ImageFolder class_to_idx : {test_dataset.class_to_idx}")
    print(f"  Remapeo aplicado         : {remap.tolist()}\n")

    # ── Modelo ────────────────────────────────────────────────────────────────
    model = build_model(n_classes).to(device)
    model.load_state_dict(torch.load(args.model, map_location=device))
    model.eval()

    # ── Inferencia ────────────────────────────────────────────────────────────
    all_preds, all_labels = [], []
    with torch.no_grad():
        for imgs, lbls in test_loader:
            imgs = imgs.to(device)
            preds = model(imgs).argmax(1).cpu().numpy()
            # Remapear etiquetas de ImageFolder al orden canónico
            all_preds.extend(remap[preds])
            all_labels.extend(remap[lbls.numpy()])

    all_preds  = np.array(all_preds)
    all_labels = np.array(all_labels)
    acc = (all_preds == all_labels).mean()

    # Índices canónicos (0, 1, 2) según class_to_idx
    label_indices = list(range(n_classes))

    print(f"  Accuracy test: {acc:.4f}\n")
    print("  Informe por clase (orden canónico YAML):")
    print(classification_report(
        all_labels, all_preds,
        labels=label_indices,
        target_names=classes_ordered,
    ))

    # ── Matriz de confusión ───────────────────────────────────────────────────
    cm = confusion_matrix(all_labels, all_preds, labels=label_indices)
    timestamp = "_".join(args.model.stem.split("_")[-2:])

    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=classes_ordered,
                yticklabels=classes_ordered, ax=ax)
    ax.set_xlabel("Predicción")
    ax.set_ylabel("Etiqueta real")
    ax.set_title(
        f"SVperitus IMMUNO-1 — Matriz de confusión\n"
        f"(test acc={acc:.4f}  |  orden: {' > '.join(classes_ordered[::-1])})"
    )
    plt.tight_layout()

    cm_path = RESULTS_DIR / f"confusion_matrix_{timestamp}.png"
    fig.savefig(cm_path, dpi=150)
    plt.close(fig)
    print(f"  Matriz de confusión guardada: {cm_path}")

    # ── Métricas CSV ──────────────────────────────────────────────────────────
    precision, recall, f1, support = precision_recall_fscore_support(
        all_labels, all_preds, labels=label_indices
    )
    metrics_path = RESULTS_DIR / f"metrics_{timestamp}.csv"
    with open(metrics_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["class", "canonical_idx", "precision",
                          "recall", "f1", "support"])
        for i, cls in enumerate(classes_ordered):
            writer.writerow([
                cls, class_to_idx[cls],
                f"{precision[i]:.4f}", f"{recall[i]:.4f}",
                f"{f1[i]:.4f}", support[i],
            ])
        writer.writerow(["accuracy", "", f"{acc:.4f}", "", "", len(all_labels)])
    print(f"  Métricas guardadas: {metrics_path}")


if __name__ == "__main__":
    main()
