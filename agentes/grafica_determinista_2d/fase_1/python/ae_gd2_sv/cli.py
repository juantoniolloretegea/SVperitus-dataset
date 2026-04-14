from __future__ import annotations
import argparse
import json
from pathlib import Path
from .report import build_report, to_csv, Parameter


def main() -> None:
    parser = argparse.ArgumentParser(description='AE-GD2-SV Fase 1 · CLI endurecida (Inyección A)')
    parser.add_argument('--mode', default='correct', choices=['correct', 'create'])
    parser.add_argument('--out', default='report.json')
    args = parser.parse_args()

    report = build_report(args.mode)
    out = Path(args.out)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')

    params = [Parameter(**p) for p in report['critical_parameters']]
    out.with_name(out.stem + '_critical_parameters.csv').write_text(to_csv(params), encoding='utf-8')
    sovereign = report['sovereign_sequence']
    sovereign_csv = 'sovereign_id,epsilon_id,label,dictamen_k3\n' + '\n'.join(
        f"{row['sovereign_id']},{row['epsilon_id']},{row['label']},{row['dictamen_k3']}" for row in sovereign
    )
    out.with_name(out.stem + '_sovereign_sequence.csv').write_text(sovereign_csv, encoding='utf-8')
    print(f'Reporte escrito en {out}')
    print('CSV de parámetros y secuencia soberana emitidos.')
