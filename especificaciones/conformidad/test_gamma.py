"""
test_gamma.py
=============
Tests para la función de criticidad Γ(v).

Verifica los tres ejemplos del consenso más casos de frontera.
"""

import sys
sys.path.insert(0, ".")

from gamma import analyze, gamma, classify_indetermination, composition_gamma, threshold

passed = 0
failed = 0

def check(name, got, expected):
    global passed, failed
    if got == expected:
        passed += 1
    else:
        failed += 1
        print(f"  FALLO: {name} → esperado {expected}, obtenido {got}")


# ══════════════════════════════════════════════════════════════════════════════
# TEST: threshold T(n) = ⌊7n/9⌋
# ══════════════════════════════════════════════════════════════════════════════

print("=== THRESHOLD ===")
check("T(9)",  threshold(9),  7)
check("T(16)", threshold(16), 12)
check("T(25)", threshold(25), 19)
check("T(36)", threshold(36), 28)
check("T(49)", threshold(49), 38)


# ══════════════════════════════════════════════════════════════════════════════
# TEST: Los tres ejemplos del consenso
# ══════════════════════════════════════════════════════════════════════════════

print("\n=== EJEMPLO 1: n₀=14, n₁=3, m=8 → Γ=3 (resoluble) ===")
v1 = ["0"]*14 + ["1"]*3 + ["U"]*8
r1 = analyze(v1)
check("n0",    r1["n0"], 14)
check("n1",    r1["n1"], 3)
check("m",     r1["m"],  8)
check("delta0", r1["delta0"], 5)   # 19-14
check("delta1", r1["delta1"], 16)  # 19-3
check("mu",    r1["mu"], 5)
check("gamma", r1["gamma"], 3)     # 8-5
check("class", r1["classification"], "resolvable")
print(f"  Γ={r1['gamma']} → {r1['classification']}")

print("\n=== EJEMPLO 2: n₀=10, n₁=2, m=13 → Γ=4 (resoluble) ===")
v2 = ["0"]*10 + ["1"]*2 + ["U"]*13
r2 = analyze(v2)
check("n0",    r2["n0"], 10)
check("n1",    r2["n1"], 2)
check("m",     r2["m"],  13)
check("delta0", r2["delta0"], 9)
check("delta1", r2["delta1"], 17)
check("mu",    r2["mu"], 9)
check("gamma", r2["gamma"], 4)     # 13-9
check("class", r2["classification"], "resolvable")
print(f"  Γ={r2['gamma']} → {r2['classification']}")

print("\n=== EJEMPLO 3: n₀=8, n₁=8, m=9 → Γ=−2 (irreducible) ===")
v3 = ["0"]*8 + ["1"]*8 + ["U"]*9
r3 = analyze(v3)
check("n0",    r3["n0"], 8)
check("n1",    r3["n1"], 8)
check("m",     r3["m"],  9)
check("delta0", r3["delta0"], 11)
check("delta1", r3["delta1"], 11)
check("mu",    r3["mu"], 11)
check("gamma", r3["gamma"], -2)    # 9-11
check("class", r3["classification"], "irreducible")
print(f"  Γ={r3['gamma']} → {r3['classification']}")


# ══════════════════════════════════════════════════════════════════════════════
# TEST: Fronterizo (Γ = 0)
# ══════════════════════════════════════════════════════════════════════════════

print("\n=== FRONTERIZO: n₀=14, n₁=6, m=5 → Γ=0 ===")
v4 = ["0"]*14 + ["1"]*6 + ["U"]*5
r4 = analyze(v4)
check("gamma", r4["gamma"], 0)     # 5 - min(5,13) = 5-5 = 0
check("class", r4["classification"], "frontier")
print(f"  Γ={r4['gamma']} → {r4['classification']}")


# ══════════════════════════════════════════════════════════════════════════════
# TEST: Ya clasificado (no indeterminado)
# ══════════════════════════════════════════════════════════════════════════════

print("\n=== YA CLASIFICADO ===")
v_apto = ["0"]*20 + ["1"]*3 + ["U"]*2
check("APTO → classified", classify_indetermination(v_apto), "classified")

v_no_apto = ["0"]*2 + ["1"]*20 + ["U"]*3
check("NO_APTO → classified", classify_indetermination(v_no_apto), "classified")


# ══════════════════════════════════════════════════════════════════════════════
# TEST: Todo U
# ══════════════════════════════════════════════════════════════════════════════

print("\n=== TODO U (n=25, T=19) ===")
v_all_u = ["U"]*25
r_all = analyze(v_all_u)
check("n0", r_all["n0"], 0)
check("n1", r_all["n1"], 0)
check("m",  r_all["m"],  25)
check("delta0", r_all["delta0"], 19)
check("delta1", r_all["delta1"], 19)
check("mu",  r_all["mu"], 19)
check("gamma", r_all["gamma"], 6)   # 25-19 = 6
check("class", r_all["classification"], "resolvable")
print(f"  Γ={r_all['gamma']} → {r_all['classification']}")
print(f"  Margen de 6: hasta 6 U pueden salir desfavorables")


# ══════════════════════════════════════════════════════════════════════════════
# TEST: Γ función abreviada
# ══════════════════════════════════════════════════════════════════════════════

print("\n=== FUNCIÓN ABREVIADA gamma() ===")
check("gamma() ejemplo 1", gamma(v1), 3)
check("gamma() ejemplo 2", gamma(v2), 4)
check("gamma() ejemplo 3", gamma(v3), -2)
check("gamma() todo U",    gamma(v_all_u), 6)


# ══════════════════════════════════════════════════════════════════════════════
# TEST: Composición (impacto de P25 puente)
# ══════════════════════════════════════════════════════════════════════════════

print("\n=== COMPOSICIÓN: impacto de P25 ===")
# Vector de IMMUNO-2 con P25 = U (IMMUNO-1 aún no resuelta)
v_comp = ["0"]*14 + ["1"]*3 + ["U"]*7 + ["U"]  # P25 es la última U
comp = composition_gamma(v_comp, bridge_idx=24)
print(f"  Γ₂(P25=0) = {comp['gamma_bridge_0']}")
print(f"  Γ₂(P25=1) = {comp['gamma_bridge_1']}")
print(f"  ΔΓ = {comp['delta_gamma']}")
check("delta_gamma tipo", isinstance(comp["delta_gamma"], int), True)
check("gamma_bridge_0 tipo", isinstance(comp["gamma_bridge_0"], int), True)


# ══════════════════════════════════════════════════════════════════════════════
# TEST: célula SV(9,3) — meta-célula
# ══════════════════════════════════════════════════════════════════════════════

print("\n=== Γ PARA SV(9,3) — META-CÉLULA ===")
check("T(9)", threshold(9), 7)

v_meta_ok = ["0"]*9
check("meta todo 0 → classified", classify_indetermination(v_meta_ok, n=9), "classified")

v_meta_fail = ["1"]*9
check("meta todo 1 → classified", classify_indetermination(v_meta_fail, n=9), "classified")

v_meta_mix = ["0"]*4 + ["1"]*2 + ["U"]*3
r_meta = analyze(v_meta_mix, n=9)
check("meta gamma", r_meta["gamma"], 3 - min(3, 5))  # m=3, delta0=7-4=3, delta1=7-2=5, mu=3, Γ=3-3=0
print(f"  Meta: n0=4, n1=2, m=3, Γ={r_meta['gamma']} → {r_meta['classification']}")


# ══════════════════════════════════════════════════════════════════════════════
# TEST: Teorema — si Γ < 0, ninguna resolución de U cambia la clase
# ══════════════════════════════════════════════════════════════════════════════

print("\n=== VERIFICACIÓN DEL TEOREMA (Γ < 0 → ninguna U decisiva) ===")
# v3 tiene Γ = -2 (irreducible)
# Verificar exhaustivamente que ninguna resolución de las 9 U produce APTO o NO_APTO
from itertools import product

u_indices = [i for i, val in enumerate(v3) if val == "U"]
t25 = 19
all_indet = True
for combo in product(["0", "1"], repeat=len(u_indices)):
    test_v = list(v3)
    for idx, val in zip(u_indices, combo):
        test_v[idx] = val
    n0_test = test_v.count("0")
    n1_test = test_v.count("1")
    if n0_test >= t25 or n1_test >= t25:
        all_indet = False
        break

check("Γ<0 → toda resolución es INDETERMINADO", all_indet, True)
print(f"  Verificado: 2^{len(u_indices)} = {2**len(u_indices)} combinaciones, todas INDETERMINADO")


# ══════════════════════════════════════════════════════════════════════════════
# RESUMEN
# ══════════════════════════════════════════════════════════════════════════════

print(f"\n{'='*60}")
print(f"  RESULTADO: {passed} pasados, {failed} fallados de {passed+failed}")
print(f"{'='*60}")

if failed > 0:
    sys.exit(1)
