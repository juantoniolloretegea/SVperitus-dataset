"""
comun/io_utils.py
==================
Utilidades de entrada/salida compartidas para todos los módulos SVperitus.

Autor: Juan Antonio Lloret Egea  |  ORCID: 0000-0002-6634-3351
Serie: «De SVcustos a SVperitus»  |  ISSN 2695-641X  |  CC BY-NC-ND 4.0
"""

import json
import csv
from pathlib import Path
from typing import List, Dict, Any, Union

import yaml


def load_config(config_path: Union[str, Path]) -> Dict[str, Any]:
    """
    Carga un archivo de configuración YAML.

    Parámetros
    ----------
    config_path : ruta al archivo .yaml

    Devuelve
    --------
    dict con la configuración
    """
    config_path = Path(config_path)
    if not config_path.exists():
        raise FileNotFoundError(f"Config no encontrado: {config_path}")
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def save_vectors_csv(
    vectors: List[List[str]],
    labels: List[str],
    output_path: Union[str, Path],
    param_ids: List[str] | None = None,
) -> None:
    """
    Guarda una lista de vectores ternarios con sus etiquetas en CSV.

    Columnas: [param_ids... | label]

    Parámetros
    ----------
    vectors    : lista de vectores, cada uno es lista de str ("0","1","U").
    labels     : lista de etiquetas ("NO_APTO", "INDETERMINADO", "APTO").
    output_path: ruta de destino del CSV.
    param_ids  : nombres de columna para los parámetros (opcional).
                 Si None, se usan P01, P02, … Pn.
    """
    if len(vectors) == 0:
        raise ValueError("La lista de vectores está vacía.")

    n = len(vectors[0])
    if param_ids is None:
        param_ids = [f"P{i+1:02d}" for i in range(n)]

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(param_ids + ["label"])
        for vec, lbl in zip(vectors, labels):
            writer.writerow(vec + [lbl])


def load_vectors_csv(
    csv_path: Union[str, Path],
) -> tuple[List[List[str]], List[str], List[str]]:
    """
    Carga vectores ternarios y etiquetas desde un CSV guardado con save_vectors_csv.

    Devuelve
    --------
    (vectors, labels, param_ids)
    """
    csv_path = Path(csv_path)
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        return [], [], []

    fieldnames = list(rows[0].keys())
    param_ids = fieldnames[:-1]   # última columna = label

    vectors = [[row[p] for p in param_ids] for row in rows]
    labels  = [row["label"] for row in rows]
    return vectors, labels, param_ids


def save_split_manifest(
    splits: Dict[str, List[str]],
    output_path: Union[str, Path],
) -> None:
    """
    Guarda un manifiesto JSON con los nombres de archivo por split.

    Ejemplo de splits:
        {"train": ["img_001.png", ...], "val": [...], "test": [...]}
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(splits, f, indent=2, ensure_ascii=False)


def ensure_dir(path: Union[str, Path]) -> Path:
    """Crea el directorio si no existe y devuelve el Path."""
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p
