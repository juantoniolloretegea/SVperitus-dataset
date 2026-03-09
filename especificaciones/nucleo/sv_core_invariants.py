"""
sv_core_invariants.py
=====================
Invariantes constitutivos del Sistema Vectorial SV.
Artefacto verificable — ejecutar con: python sv_core_invariants.py

Toda implementación en cualquier lenguaje debe respetar estos
invariantes. Si alguno falla, la implementación no es conforme.

Fuente de verdad: Fundamentos algebraico-semánticos del SV, v1.0.0
Autor: Juan Antonio Lloret Egea · ORCID 0000-0002-6634-3351
ISSN 2695-6411 · CC BY-NC-ND 4.0
"""

from math import floor

# ═══════════════════════════════════════════════════════════
#  DEFINICIONES FORMALES
# ═══════════════════════════════════════════════════════════

# Alfabeto ternario canónico
TERNARY_ALPHABET = {"0", "1", "U"}

# Semántica canónica
SEMANTICS = {"0": "Apto", "1": "No_Apto", "U": "Indeterminado"}

# Representación polar visible
RADIUS_MAP = {"0": 1.0, "1": 2.0, "U": 3.0}

# Restricción arquitectónica: n = b², b ≥ 3
VALID_CELL_SIZES = [b * b for b in range(3, 20)]  # 9, 16, 25, 36, ...

def threshold(n: int) -> int:
    """Umbral canónico T(n) = ⌊7n/9⌋"""
    return floor(7 * n / 9)

def classify(vector: list, n: int = None, t: int = None) -> str:
    """Clasificación determinista de una célula SV."""
    if n is None:
        n = len(vector)
    if t is None:
        t = threshold(n)
    n1 = sum(1 for v in vector if v == "1")
    n0 = sum(1 for v in vector if v == "0")
    if n1 >= t:
        return "NO_APTO"
    if n0 >= t:
        return "APTO"
    return "INDETERMINADO"

def cardinality(n: int) -> int:
    """Proposición 1: |S_n| = 3^n"""
    return 3 ** n


# ═══════════════════════════════════════════════════════════
#  VERIFICACIÓN DE INVARIANTES
# ═══════════════════════════════════════════════════════════

def run_invariants():
    passed = 0
    failed = 0

    def check(name, condition):
        nonlocal passed, failed
        if condition:
            passed += 1
        else:
            failed += 1
            print(f"  ✗ FALLO: {name}")

    # ── I1. Alfabeto ternario ──
    check("Alfabeto tiene exactamente 3 símbolos",
          len(TERNARY_ALPHABET) == 3)
    check("0 pertenece al alfabeto", "0" in TERNARY_ALPHABET)
    check("1 pertenece al alfabeto", "1" in TERNARY_ALPHABET)
    check("U pertenece al alfabeto", "U" in TERNARY_ALPHABET)

    # ── I2. Semántica canónica ──
    check("0 = Apto", SEMANTICS["0"] == "Apto")
    check("1 = No_Apto", SEMANTICS["1"] == "No_Apto")
    check("U = Indeterminado", SEMANTICS["U"] == "Indeterminado")

    # ── I3. Radios polares ──
    check("Radio de 0 = 1.0", RADIUS_MAP["0"] == 1.0)
    check("Radio de 1 = 2.0", RADIUS_MAP["1"] == 2.0)
    check("Radio de U = 3.0", RADIUS_MAP["U"] == 3.0)
    check("0 es el anillo interior", RADIUS_MAP["0"] < RADIUS_MAP["1"] < RADIUS_MAP["U"])

    # ── I4. Restricción arquitectónica n = b² ──
    check("n=9 es válido (b=3)", 9 in VALID_CELL_SIZES)
    check("n=25 es válido (b=5)", 25 in VALID_CELL_SIZES)
    check("n=36 es válido (b=6)", 36 in VALID_CELL_SIZES)
    check("n=10 NO es válido", 10 not in VALID_CELL_SIZES)
    check("n=24 NO es válido", 24 not in VALID_CELL_SIZES)

    # ── I5. Umbral canónico T(n) ──
    check("T(9) = 7", threshold(9) == 7)
    check("T(25) = 19", threshold(25) == 19)
    check("T(36) = 28", threshold(36) == 28)
    check("T(49) = 38", threshold(49) == 38)

    # ── I6. Cardinalidad ──
    check("|S_9| = 3^9 = 19683", cardinality(9) == 19683)
    check("|S_25| = 3^25 = 847288609443", cardinality(25) == 847288609443)

    # ── I7. Unicidad de clasificación fuerte (Proposición 6) ──
    # Para n ≥ 9: no pueden darse simultáneamente n0 ≥ T(n) y n1 ≥ T(n)
    for b in range(3, 10):
        n = b * b
        t = threshold(n)
        check(f"Unicidad n={n}: 2T > n (2×{t} = {2*t} > {n})",
              2 * t > n)

    # ── I8. Clasificación determinista ──
    # Todo 0 → APTO
    check("Todo 0 en SV(25,5) → APTO",
          classify(["0"] * 25) == "APTO")
    # Todo 1 → NO_APTO
    check("Todo 1 en SV(25,5) → NO_APTO",
          classify(["1"] * 25) == "NO_APTO")
    # Todo U → INDETERMINADO
    check("Todo U en SV(25,5) → INDETERMINADO",
          classify(["U"] * 25) == "INDETERMINADO")
    # Exactamente T unos → NO_APTO
    check("19 unos + 6 ceros → NO_APTO",
          classify(["1"] * 19 + ["0"] * 6) == "NO_APTO")
    # Exactamente T ceros → APTO
    check("19 ceros + 6 unos → APTO",
          classify(["0"] * 19 + ["1"] * 6) == "APTO")
    # T-1 de cada → INDETERMINADO
    check("18 ceros + 7 unos → INDETERMINADO",
          classify(["0"] * 18 + ["1"] * 7) == "INDETERMINADO")

    # ── I9. Meta-célula SV(9,3) ──
    check("T(9) = 7 para meta-célula", threshold(9) == 7)
    check("7 unos en SV(9,3) → NO_APTO (INTRUSIÓN)",
          classify(["1"] * 7 + ["0"] * 2, 9, 7) == "NO_APTO")
    check("7 ceros en SV(9,3) → APTO (NORMAL)",
          classify(["0"] * 7 + ["1"] * 2, 9, 7) == "APTO")
    check("4 ceros + 3 unos + 2 U → INDETERMINADO",
          classify(["0"] * 4 + ["1"] * 3 + ["U"] * 2, 9, 7) == "INDETERMINADO")

    # ── I10. Conteo: n0 + n1 + nU = n ──
    for v in [["0"]*10+["1"]*8+["U"]*7, ["U"]*25, ["0"]*19+["1"]*6]:
        n0 = v.count("0")
        n1 = v.count("1")
        nu = v.count("U")
        check(f"Conteo {n0}+{n1}+{nu}={len(v)}", n0 + n1 + nu == len(v))

    # ── Resumen ──
    total = passed + failed
    print(f"\n{'=' * 60}")
    print(f"  INVARIANTES DEL SISTEMA VECTORIAL SV")
    print(f"  {passed} verificados, {failed} fallados de {total}")
    print(f"{'=' * 60}")
    return failed == 0


if __name__ == "__main__":
    success = run_invariants()
    exit(0 if success else 1)
