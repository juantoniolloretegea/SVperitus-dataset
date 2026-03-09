"""
comun/polygons.py
==================
Generación de polígonos polares ternarios para SVperitus.

Reutiliza la misma lógica visual de SVcustos:
  - Fondo oscuro #0D1B2A
  - Polígono dorado #C9A84C
  - Vértices coloreados por valor: 0=verde, 1=rojo, U=amarillo
  - Tres anillos de referencia (radios 1, 2, 3)
  - Resolución 224×224 px

La diferencia semántica (INTRUSIÓN↔No_Apto, NORMAL↔Apto) es
responsabilidad del módulo que llama a esta función; aquí
solo se genera la imagen a partir del vector ternario.

Autor: Juan Antonio Lloret Egea  |  ORCID: 0000-0002-6634-3351
Serie: «De SVcustos a SVperitus»  |  ISSN 2695-641X  |  CC BY-NC-ND 4.0
"""

import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path
from typing import List, Union


# ── Colores (coherentes con SVcustos) ─────────────────────────────────────────
BG_COLOR       = "#0D1B2A"
POLYGON_COLOR  = "#C9A84C"
VERTEX_COLOR   = {"0": "#4CAF50", "1": "#F44336", "U": "#FFC107"}
RING_COLOR     = "#FFFFFF"
RING_ALPHA     = 0.15

# Radio de cada valor ternario en el polígono polar
RADIUS_MAP     = {"0": 1.0, "1": 2.0, "U": 3.0}
MAX_RADIUS     = 3.5   # margen de la figura


def _ternary_to_coords(vector: List[str]) -> tuple[np.ndarray, np.ndarray]:
    """Convierte un vector ternario en coordenadas (x, y) del polígono polar."""
    n = len(vector)
    angles = [2 * math.pi * k / n - math.pi / 2 for k in range(n)]
    radii  = [RADIUS_MAP[v] for v in vector]
    xs = [r * math.cos(a) for r, a in zip(radii, angles)]
    ys = [r * math.sin(a) for r, a in zip(radii, angles)]
    return np.array(xs), np.array(ys)


def draw_polar_polygon(
    vector: List[str],
    output_path: Union[str, Path, None] = None,
    image_size: int = 224,
    show: bool = False,
) -> plt.Figure:
    """
    Dibuja el polígono polar ternario para un vector dado.

    Parámetros
    ----------
    vector      : lista de strings con valores "0", "1" o "U" (longitud n).
    output_path : ruta donde guardar la imagen PNG (None = no guardar).
    image_size  : lado de la imagen cuadrada en píxeles (defecto 224).
    show        : si True, llama a plt.show() (usar solo en modo interactivo).

    Devuelve
    --------
    fig : objeto Figure de matplotlib.
    """
    n = len(vector)
    angles = [2 * math.pi * k / n - math.pi / 2 for k in range(n)]

    dpi    = 96
    fig_px = image_size
    fig_in = fig_px / dpi

    fig, ax = plt.subplots(figsize=(fig_in, fig_in), dpi=dpi)
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)

    # Anillos de referencia
    for r in [1.0, 2.0, 3.0]:
        circle = plt.Circle((0, 0), r, color=RING_COLOR, fill=False,
                             linestyle="--", linewidth=0.6, alpha=RING_ALPHA)
        ax.add_patch(circle)

    # Ejes radiales (líneas guía)
    for a in angles:
        ax.plot([0, MAX_RADIUS * math.cos(a)],
                [0, MAX_RADIUS * math.sin(a)],
                color=RING_COLOR, linewidth=0.4, alpha=0.10)

    # Polígono
    xs, ys = _ternary_to_coords(vector)
    xs_closed = np.append(xs, xs[0])
    ys_closed = np.append(ys, ys[0])
    ax.fill(xs_closed, ys_closed, color=POLYGON_COLOR, alpha=0.25)
    ax.plot(xs_closed, ys_closed, color=POLYGON_COLOR, linewidth=1.2)

    # Vértices coloreados por valor ternario
    for xi, yi, val in zip(xs, ys, vector):
        ax.scatter(xi, yi, color=VERTEX_COLOR[val], s=18, zorder=5)

    ax.set_xlim(-MAX_RADIUS, MAX_RADIUS)
    ax.set_ylim(-MAX_RADIUS, MAX_RADIUS)
    ax.set_aspect("equal")
    ax.axis("off")
    plt.tight_layout(pad=0)

    if output_path is not None:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_path, bbox_inches="tight", pad_inches=0,
                    facecolor=BG_COLOR, dpi=dpi)

    if show:
        plt.show()

    return fig


# ── Clasificación global ───────────────────────────────────────────────────────

def threshold(n: int) -> int:
    """T(n) = floor(7n/9)  — umbral de clasificación SVperitus/SVcustos."""
    return int(7 * n // 9)


def classify_svperitus(vector: List[str]) -> str:
    """
    Clasifica un vector ternario según la semántica SVperitus.

    Devuelve una de las tres cadenas:
        "NO_APTO"       si n₁ ≥ T(n)
        "APTO"          si n₀ ≥ T(n)
        "INDETERMINADO" en el resto

    El orden de severidad es: NO_APTO > INDETERMINADO > APTO.
    """
    n  = len(vector)
    t  = threshold(n)
    n1 = vector.count("1")
    n0 = vector.count("0")

    if n1 >= t:
        return "NO_APTO"
    if n0 >= t:
        return "APTO"
    return "INDETERMINADO"


def classify_svcustos(vector: List[str]) -> str:
    """
    Clasificación SVcustos (mantenida aquí como referencia cruzada).
    NO usar en módulos SVperitus — separar semánticas.

    Devuelve: "INTRUSION" | "NORMAL" | "INDETERMINADO"
    """
    n  = len(vector)
    t  = threshold(n)
    n1 = vector.count("1")
    n0 = vector.count("0")

    if n1 >= t:
        return "INTRUSION"
    if n0 >= t:
        return "NORMAL"
    return "INDETERMINADO"
