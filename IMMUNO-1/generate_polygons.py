"""
IMMUNO-1/generate_polygons.py
==============================
Convierte vectores ternarios IMMUNO-1 (n=25) en imágenes de polígono polar
organizadas en la estructura ImageFolder de PyTorch.

El orden y los nombres de las carpetas de salida se derivan de class_to_idx
en imm_n25.yaml, garantizando coherencia con normative_engine.py y evaluate.py.

Estructura de salida:
    data/images/
      train/
        NO_APTO/       (índice 0)
        INDETERMINADO/ (índice 1)
        APTO/          (índice 2)
      val/ ...
      test/ ...

Precondición: haber ejecutado generate_cases.py (datos en data/vectors/).

Autor: Juan Antonio Lloret Egea  |  ORCID: 0000-0002-6634-3351
ISSN 2695-641X  |  CC BY-NC-ND 4.0
"""

import sys
import argparse
import matplotlib.pyplot as plt
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common.polygons import draw_polar_polygon
from common.io_utils import load_config, load_vectors_csv, ensure_dir

CONFIG_PATH = Path(__file__).parent / "config" / "imm_n25.yaml"
DATA_DIR    = Path(__file__).parent / "data"
VECTORS_DIR = DATA_DIR / "vectors"
IMAGES_DIR  = DATA_DIR / "images"
SPLITS      = ["train", "val", "test"]


def load_class_list(cfg: dict) -> list[str]:
    """
    Devuelve la lista de clases ordenada por índice canónico (class_to_idx YAML).
    Punto único de verdad: el YAML, no constantes duplicadas en el código.
    """
    class_to_idx: dict[str, int] = cfg["class_to_idx"]
    return sorted(class_to_idx, key=lambda c: class_to_idx[c])


def generate_images_for_split(
    split: str,
    classes: list[str],
    image_size: int = 224,
    verbose: bool = True,
) -> int:
    """
    Genera imágenes polares para un split a partir de su CSV de vectores.
    Las carpetas de destino usan los nombres canónicos leídos del YAML.
    """
    csv_path = VECTORS_DIR / f"{split}_vectors.csv"
    if not csv_path.exists():
        raise FileNotFoundError(
            f"No se encontró {csv_path}. Ejecuta primero generate_cases.py."
        )

    vectors, labels, _ = load_vectors_csv(csv_path)

    # Crear carpetas con nombres canónicos (evita que ImageFolder reordene)
    for cls in classes:
        ensure_dir(IMAGES_DIR / split / cls)

    count = 0
    for i, (vec, lbl) in enumerate(zip(vectors, labels)):
        img_path = IMAGES_DIR / split / lbl / f"imm1_{split}_{i:05d}.png"
        draw_polar_polygon(
            vector=vec,
            output_path=img_path,
            image_size=image_size,
            show=False,
        )
        plt.close("all")
        count += 1

        if verbose and (i + 1) % 200 == 0:
            print(f"    [{split}] {i+1}/{len(vectors)} imágenes…", flush=True)

    return count


def main():
    parser = argparse.ArgumentParser(
        description="SVperitus IMMUNO-1 — Generador de imágenes polares (n=25)"
    )
    parser.add_argument("--splits", nargs="+", default=SPLITS,
                        choices=SPLITS)
    parser.add_argument("--image-size", type=int, default=224)
    args = parser.parse_args()

    cfg     = load_config(CONFIG_PATH)
    classes = load_class_list(cfg)          # lee del YAML, no constante duplicada

    print(f"\nSVperitus – IMMUNO-1  |  Generación de polígonos polares")
    print(f"  n={cfg['n']}  |  T(n)={cfg['threshold']}")
    print(f"  Clases (orden canónico YAML): {classes}")
    print(f"  Resolución: {args.image_size}×{args.image_size} px\n")

    total = 0
    for split in args.splits:
        print(f"  Procesando split: {split}…")
        n_imgs = generate_images_for_split(
            split, classes, image_size=args.image_size
        )
        print(f"    ✓ {split}: {n_imgs} imágenes → {IMAGES_DIR / split}/")
        total += n_imgs

    print(f"\n✓ Total imágenes generadas: {total}")
    print("  Estructura ImageFolder lista para train_resnet.py")
