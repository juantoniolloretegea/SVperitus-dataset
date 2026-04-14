from __future__ import annotations
import argparse
from pathlib import Path
from .report import build_report, to_csv, Parameter
import json


def main() -> None:
    parser = argparse.ArgumentParser(description='AE-GD2-SV Fase 1 · CLI mínima')
    parser.add_argument('--mode', default='correct', choices=['correct','create'])
    parser.add_argument('--out', default='report.json')
    args = parser.parse_args()
    report = build_report(args.mode)
    out = Path(args.out)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    csv_path = out.with_suffix('.csv')
    params = [Parameter(**p) for p in report['critical_parameters']]
    csv_path.write_text(to_csv(params), encoding='utf-8')
    print(f'Reporte escrito en {out}')
    print(f'CSV escrito en {csv_path}')
