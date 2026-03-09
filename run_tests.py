"""
run_tests.py
============
Ejecuta todos los tests de conformidad desde la raíz del repositorio.

Uso:
    python run_tests.py

Ajusta sys.path para que los tests de especificaciones/conformidad/
encuentren los módulos distribuidos por el repositorio:

    normative_engine  ← dominios/inmunologia/fase_2/src/
    gamma             ← comun/
    meta_engine       ← meta/
    compose           ← dominios/inmunologia/compositor/

Autor: Juan Antonio Lloret Egea · ORCID 0000-0002-6634-3351
ISSN 2695-6411 · CC BY-NC-ND 4.0
"""

import sys
import os
import importlib
import traceback

# ── Paths del repositorio ──
ROOT = os.path.dirname(os.path.abspath(__file__))

PATHS = [
    os.path.join(ROOT, "dominios", "inmunologia", "fase_2", "src"),
    os.path.join(ROOT, "comun"),
    os.path.join(ROOT, "meta"),
    os.path.join(ROOT, "dominios", "inmunologia", "compositor"),
    os.path.join(ROOT, "especificaciones", "conformidad"),
]

for p in PATHS:
    if p not in sys.path:
        sys.path.insert(0, p)

# ── Verificar que los módulos son importables ──
print("=" * 60)
print("  SVperitus — Tests de conformidad")
print("=" * 60)
print()

modules_ok = True
for mod_name, expected_path in [
    ("normative_engine", "dominios/inmunologia/fase_2/src/"),
    ("gamma", "comun/"),
    ("meta_engine", "meta/"),
    ("compose", "dominios/inmunologia/compositor/"),
]:
    try:
        m = importlib.import_module(mod_name)
        print(f"  ✓ {mod_name:25s} ← {expected_path}")
    except ImportError as e:
        print(f"  ✗ {mod_name:25s} ← {expected_path}  ERROR: {e}")
        modules_ok = False

if not modules_ok:
    print()
    print("  No se pueden ejecutar los tests: faltan módulos.")
    print("  Verifique que el motor Python está subido al repositorio.")
    sys.exit(1)

print()

# ── Ejecutar tests ──
TEST_DIR = os.path.join(ROOT, "especificaciones", "conformidad")
TEST_FILES = [
    "test_immuno2.py",
    "test_gamma.py",
    "test_compositor_meta.py",
]

total_passed = 0
total_failed = 0
results = []

for test_file in TEST_FILES:
    test_path = os.path.join(TEST_DIR, test_file)
    if not os.path.exists(test_path):
        print(f"  ⚠ {test_file} no encontrado — omitido")
        results.append((test_file, "no encontrado", 0, 0))
        continue

    print(f"─── {test_file} ───")
    print()

    # Capture stdout to parse results
    old_stdout = sys.stdout
    from io import StringIO
    captured = StringIO()

    class TeeOutput:
        def __init__(self, *streams):
            self.streams = streams
        def write(self, data):
            for s in self.streams:
                s.write(data)
        def flush(self):
            for s in self.streams:
                s.flush()

    sys.stdout = TeeOutput(old_stdout, captured)

    try:
        # Execute the test file
        with open(test_path, 'r') as f:
            code = f.read()
        exec(compile(code, test_path, 'exec'), {'__name__': '__main__', '__file__': test_path})
    except SystemExit:
        pass
    except Exception as e:
        print(f"  ✗ ERROR ejecutando {test_file}: {e}")
        traceback.print_exc()
    finally:
        sys.stdout = old_stdout

    # Parse results from captured output
    output = captured.getvalue()
    import re
    match = re.search(r'(\d+) pasados?, (\d+) fallados? de (\d+)', output)
    if match:
        p, f = int(match.group(1)), int(match.group(2))
        total_passed += p
        total_failed += f
        results.append((test_file, "ok", p, f))
    else:
        results.append((test_file, "sin resultado parseable", 0, 0))

    print()

# ── Resumen final ──
print("=" * 60)
print("  RESUMEN")
print("=" * 60)
for name, status, p, f in results:
    if status == "ok":
        icon = "✓" if f == 0 else "✗"
        print(f"  {icon} {name:35s} {p} pasados, {f} fallados")
    else:
        print(f"  ⚠ {name:35s} {status}")

print(f"\n  TOTAL: {total_passed} pasados, {total_failed} fallados de {total_passed + total_failed}")
print("=" * 60)

sys.exit(0 if total_failed == 0 else 1)
