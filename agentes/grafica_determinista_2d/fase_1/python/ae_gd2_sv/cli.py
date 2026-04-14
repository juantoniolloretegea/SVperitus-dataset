from __future__ import annotations
import argparse
from pathlib import Path
import zipfile
from .report import write_bundle


def main() -> None:
    parser = argparse.ArgumentParser(description='AE-GD2-SV Fase 1 · CLI B1 banco y bundle')
    parser.add_argument('--mode', default='correct', choices=['correct','create'])
    parser.add_argument('--outdir', default='ae_gd2_sv_bundle')
    args = parser.parse_args()

    out_dir = Path(args.outdir)
    report = write_bundle(out_dir, args.mode)
    zip_path = out_dir.with_suffix('.zip')
    with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(out_dir.iterdir()):
            if path.is_file():
                zf.write(path, arcname=path.name)

    print(f"Bundle escrito en {out_dir}")
    print(f"ZIP escrito en {zip_path}")
    print(f"Dictamen global: {report['dictamen_global']}")
