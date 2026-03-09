"""
common/gamma.py
===============
Función de criticidad Γ(v) para el Sistema Vector ternario.

Contribución original de la serie SVperitus.
Matemática exacta. Sin estadística. Sin minería de datos.

Definiciones
────────────
  n₀(v) = número de valores 0 en v
  n₁(v) = número de valores 1 en v
  m(v)  = número de valores U en v
  T(n)  = ⌊7n/9⌋ (umbral de clasificación)
  δ₀(v) = T(n) − n₀(v) (distancia a frontera APTO)
  δ₁(v) = T(n) − n₁(v) (distancia a frontera NO_APTO)
  μ(v)  = min(δ₀, δ₁) (margen del vector)
  Γ(v)  = m(v) − μ(v) (función de criticidad)

Interpretación
──────────────
  Γ < 0 → Indeterminación irreducible
           Ni resolviendo todas las U se alcanza clasificación.
  Γ = 0 → Indeterminación fronteriza
           Cada U es decisiva.
  Γ > 0 → Indeterminación resoluble
           Γ dice cuántas U pueden salir desfavorables sin perder
           la clasificación.

Autor: Juan Antonio Lloret Egea  |  ORCID: 0000-0002-6634-3351
ISSN 2695-6411  |  CC BY-NC-ND 4.0
"""

from __future__ import annotations
from math import floor


def threshold(n: int) -> int:
    """T(n) = ⌊7n/9⌋"""
    return floor(7 * n / 9)


def analyze(vector: list[str], n: int | None = None, t: int | None = None) -> dict:
    """
    Análisis completo de criticidad de un vector ternario.

    Parámetros
    ----------
    vector : lista de "0", "1", "U"
    n      : tamaño de la célula (por defecto len(vector))
    t      : umbral (por defecto T(n) = ⌊7n/9⌋)

    Devuelve
    --------
    {
        "n":     int,
        "t":     int,
        "n0":    int,
        "n1":    int,
        "m":     int,     # número de U
        "delta0": int,    # T - n0 (cuántos 0 faltan para APTO)
        "delta1": int,    # T - n1 (cuántos 1 faltan para NO_APTO)
        "mu":    int,     # min(delta0, delta1)
        "gamma": int,     # m - mu
        "classification": str,  # "irreducible" | "frontier" | "resolvable"
        "interpretation": str,  # texto descriptivo
    }
    """
    if n is None:
        n = len(vector)
    if t is None:
        t = threshold(n)

    n0 = vector.count("0")
    n1 = vector.count("1")
    m  = vector.count("U")

    delta0 = t - n0
    delta1 = t - n1
    mu = min(delta0, delta1)
    gamma = m - mu

    if gamma < 0:
        classification = "irreducible"
        interpretation = (
            f"Indeterminación irreducible (Γ={gamma}). "
            f"Ni resolviendo las {m} U pendientes se alcanza clasificación. "
            f"Faltan {mu} valores concordantes pero solo hay {m} U disponibles. "
            f"No se necesitan más pruebas; se necesita que cambien los parámetros conocidos."
        )
    elif gamma == 0:
        classification = "frontier"
        interpretation = (
            f"Indeterminación fronteriza (Γ=0). "
            f"Cada U es decisiva. Con {m} U y margen {mu}, "
            f"resolver cualquiera en sentido desfavorable cierra la puerta "
            f"a clasificación definitiva. Resuelva todas."
        )
    else:
        classification = "resolvable"
        # Determinar hacia qué frontera está más cerca
        if delta0 <= delta1:
            nearest = "APTO"
            needed = delta0
        else:
            nearest = "NO_APTO"
            needed = delta1
        interpretation = (
            f"Indeterminación resoluble (Γ={gamma}). "
            f"Con {m} U pendientes y margen {mu}, "
            f"puede permitirse hasta {gamma} resultados desfavorables "
            f"y aún alcanzar clasificación definitiva. "
            f"Frontera más cercana: {nearest} (necesita {needed} valores concordantes)."
        )

    return {
        "n":     n,
        "t":     t,
        "n0":    n0,
        "n1":    n1,
        "m":     m,
        "delta0": delta0,
        "delta1": delta1,
        "mu":    mu,
        "gamma": gamma,
        "classification": classification,
        "interpretation": interpretation,
    }


def gamma(vector: list[str], n: int | None = None, t: int | None = None) -> int:
    """
    Calcula Γ(v) = m(v) − μ(v).

    Versión abreviada que devuelve solo el valor numérico.
    """
    return analyze(vector, n, t)["gamma"]


def classify_indetermination(vector: list[str], n: int | None = None,
                              t: int | None = None) -> str:
    """
    Clasifica la indeterminación: "irreducible", "frontier", o "resolvable".

    Si el vector no es INDETERMINADO (ya es APTO o NO_APTO),
    devuelve "classified".
    """
    if n is None:
        n = len(vector)
    if t is None:
        t = threshold(n)

    n0 = vector.count("0")
    n1 = vector.count("1")

    # Si ya está clasificado, no hay indeterminación
    if n1 >= t:
        return "classified"  # NO_APTO
    if n0 >= t:
        return "classified"  # APTO

    result = analyze(vector, n, t)
    return result["classification"]


def composition_gamma(vector2: list[str], bridge_idx: int = 24,
                       n: int = 25, t: int = 19) -> dict:
    """
    Calcula Γ de IMMUNO-2 condicionado a los dos posibles valores
    del puente P25 (0 o 1).

    Devuelve
    --------
    {
        "gamma_bridge_0": int,   # Γ₂ si P25 ← 0 (IMMUNO-1 APTO)
        "gamma_bridge_1": int,   # Γ₂ si P25 ← 1 (IMMUNO-1 NO_APTO)
        "delta_gamma":    int,   # diferencia (cuánto importa resolver IMMUNO-1)
        "interpretation": str,
    }
    """
    v0 = list(vector2)
    v0[bridge_idx] = "0"
    g0 = gamma(v0, n, t)

    v1 = list(vector2)
    v1[bridge_idx] = "1"
    g1 = gamma(v1, n, t)

    delta = abs(g0 - g1)

    if delta == 0:
        interp = (
            "La resolución de IMMUNO-1 no afecta a la criticidad de IMMUNO-2. "
            "Puede resolver las U propias de IMMUNO-2 en cualquier orden."
        )
    else:
        interp = (
            f"La resolución de IMMUNO-1 cambia Γ de IMMUNO-2 en {delta} unidades. "
            f"Γ₂(P25=0)={g0}, Γ₂(P25=1)={g1}. "
            f"{'Resuelva IMMUNO-1 primero.' if delta >= 2 else 'El impacto es moderado.'}"
        )

    return {
        "gamma_bridge_0": g0,
        "gamma_bridge_1": g1,
        "delta_gamma":    delta,
        "interpretation": interp,
    }
