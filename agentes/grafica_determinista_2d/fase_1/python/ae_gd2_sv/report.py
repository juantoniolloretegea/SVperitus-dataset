from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Iterable
from pathlib import Path
import csv
import io
import json

PARAM_NAMES = [
    'Modo operativo','Tipo de fuente','Integridad de entrada','Localidad y cuarentena','Perfil de ejecución',
    'Clase de figura','Dominio declarado','Dimensiones del lienzo','Salidas requeridas','Restricciones duras',
    'Política de título','Política de footer','Sistema de paneles','Sistema de nodos','Sistema de aristas',
    'No colisión texto-texto','Respiración vertical suficiente','Respiración horizontal suficiente','Densidad compositiva aceptable','Canonicidad del SVG',
    'Trazabilidad append-only','Confirmación humana soberana','Coherencia del bundle','Pureza de frontera','Reproducibilidad laboratorial'
]

@dataclass
class Parameter:
    position: int
    param_id: str
    name: str
    value_k3: str
    justification: str


def build_frame(mode: str = 'correct') -> list[Parameter]:
    out: list[Parameter] = []
    for idx, name in enumerate(PARAM_NAMES, start=1):
        value = '0' if idx in {1,2,3,22,23} else ('U' if idx in {16,17,18,19,20,24,25} else '0')
        if mode == 'create' and idx == 2:
            value = '0'
        out.append(Parameter(idx, f'P{idx:02d}', name, value, 'conformidad suficiente' if value == '0' else 'indeterminación controlada'))
    return out


def build_gob(frame: list[Parameter], sequence_length: int = 4) -> list[Parameter]:
    out: list[Parameter] = []
    for p in frame:
        value = p.value_k3
        if p.param_id in {'P16','P17','P18','P19','P20'} and sequence_length < 3 and value == '0':
            value = 'U'
        out.append(Parameter(p.position, p.param_id, p.name, value, f'supervisión de {p.param_id}'))
    return out


def dictamen(cell: Iterable[Parameter]) -> str:
    values = [p.value_k3 for p in cell]
    if '1' in values:
        return 'NO APTO'
    if 'U' in values:
        return 'INDETERMINADO'
    return 'APTO'


def rows_to_csv(rows: list[dict], columns: list[str]) -> str:
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=columns)
    writer.writeheader()
    writer.writerows(rows)
    return buf.getvalue()


def parameters_to_csv(parameters: Iterable[Parameter]) -> str:
    return rows_to_csv([asdict(p) for p in parameters], ['position','param_id','name','value_k3','justification'])


def frame_view_csv(parameters: Iterable[Parameter]) -> str:
    rows = [{'position': p.position, 'param_id': p.param_id, 'value_k3': p.value_k3, 'label': p.name} for p in parameters]
    return rows_to_csv(rows, ['position','param_id','value_k3','label'])


def sovereign_sequence(frame: list[Parameter], gob: list[Parameter]) -> list[dict]:
    return [
        {'sovereign_id':'S0','epsilon_id':'ε0','label':'Frame inicial declarado','dictamen_k3':'INDETERMINADO'},
        {'sovereign_id':'S1','epsilon_id':'ε1','label':'Entrada admitida tras cuarentena','dictamen_k3':dictamen(frame)},
        {'sovereign_id':'S2','epsilon_id':'ε2','label':'Intención confirmada por el usuario','dictamen_k3':dictamen(frame)},
        {'sovereign_id':'S3','epsilon_id':'ε3','label':'Auditoría poligonal y dictamen','dictamen_k3':dictamen(gob)},
    ]


def sovereign_sequence_csv(sequence: list[dict]) -> str:
    return rows_to_csv(sequence, ['sovereign_id','epsilon_id','label','dictamen_k3'])


def make_events(run_id: str, report: dict) -> list[dict]:
    seq = report['sovereign_sequence']
    return [
        {'event_id': f'{run_id}-EVT-001', 'parent_event_id': None, 'run_id': run_id, 'event_type':'create_user_context_packet', 'dictamen_k3': None, 'timestamp_utc':'2026-04-14T00:00:00Z', 'affected_params':['P01','P02','P03']},
        {'event_id': f'{run_id}-EVT-002', 'parent_event_id': f'{run_id}-EVT-001', 'run_id': run_id, 'event_type':'translate_to_draft', 'dictamen_k3': None, 'timestamp_utc':'2026-04-14T00:00:01Z', 'affected_params':['P06','P08','P10']},
        {'event_id': f'{run_id}-EVT-003', 'parent_event_id': f'{run_id}-EVT-002', 'run_id': run_id, 'event_type':'confirm_intent', 'dictamen_k3': seq[2]['dictamen_k3'], 'timestamp_utc':'2026-04-14T00:00:02Z', 'affected_params':['P21','P22']},
        {'event_id': f'{run_id}-EVT-004', 'parent_event_id': f'{run_id}-EVT-003', 'run_id': run_id, 'event_type':'build_audit_report', 'dictamen_k3': report['dictamen_global'], 'timestamp_utc':'2026-04-14T00:00:03Z', 'affected_params':['P23','P24','P25']},
    ]


def events_jsonl(events: list[dict]) -> str:
    return '
'.join(json.dumps(e, ensure_ascii=False) for e in events)


def event_index(events: list[dict]) -> dict:
    by_event_id = {e['event_id']: i for i, e in enumerate(events)}
    by_run_id: dict[str, list[int]] = {}
    by_event_type: dict[str, list[int]] = {}
    by_param: dict[str, list[int]] = {}
    for i, e in enumerate(events):
        by_run_id.setdefault(e['run_id'], []).append(i)
        by_event_type.setdefault(e['event_type'], []).append(i)
        for p in e.get('affected_params', []):
            by_param.setdefault(p, []).append(i)
    return {'by_event_id': by_event_id, 'by_run_id': by_run_id, 'by_event_type': by_event_type, 'by_param': by_param}


def index_by_param_csv(index: dict) -> str:
    rows = []
    for param_id, positions in sorted(index['by_param'].items()):
        rows.append({'param_id': param_id, 'event_count': len(positions), 'last_position': positions[-1]})
    return rows_to_csv(rows, ['param_id','event_count','last_position'])


def index_by_type_csv(index: dict) -> str:
    rows = []
    for event_type, positions in sorted(index['by_event_type'].items()):
        rows.append({'event_type': event_type, 'count': len(positions), 'last_position': positions[-1]})
    return rows_to_csv(rows, ['event_type','count','last_position'])


def build_report(mode: str = 'correct') -> dict:
    run_id = 'PY-RUN-0001'
    frame = build_frame(mode)
    gob = build_gob(frame)
    sequence = sovereign_sequence(frame, gob)
    return {
        'run_id': run_id,
        'dictamen_global': dictamen(gob),
        'critical_parameters': [asdict(p) for p in frame],
        'gob_parameters': [asdict(p) for p in gob],
        'sovereign_sequence': sequence,
        'metrics': {
            'gradient_norm_1': sum(1 for p in frame if p.value_k3 == '1') + 0.5 * sum(1 for p in frame if p.value_k3 == 'U'),
            'jacobian_trace': sum(1 if p.value_k3 == '1' else 0.5 if p.value_k3 == 'U' else 0 for p in frame),
            'curvature': round(sum(1 for p in frame if p.value_k3 == 'U') / 25.0, 4),
            'modal_first_mode': 7.0,
            'residual_truncated': round(sum(1 for p in frame if p.value_k3 == 'U') / 10.0, 4),
            'ufe_canvas_width': 1200,
            'ufe_canvas_height': 800,
        },
        'artifacts': {
            'event_bank': 'events.jsonl',
            'event_index': 'event_index.json',
            'sovereign_sequence_csv': 'sovereign_sequence.csv',
            'critical_parameters_csv': 'critical_parameters.csv',
            'gob_parameters_csv': 'gob25.csv',
        },
    }


def write_bundle(out_dir: Path, mode: str = 'correct') -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    report = build_report(mode)
    frame = [Parameter(**p) for p in report['critical_parameters']]
    gob = [Parameter(**p) for p in report['gob_parameters']]
    events = make_events(report['run_id'], report)
    index = event_index(events)

    (out_dir / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    (out_dir / 'critical_parameters.csv').write_text(parameters_to_csv(frame), encoding='utf-8')
    (out_dir / 'frame25.csv').write_text(frame_view_csv(frame), encoding='utf-8')
    (out_dir / 'gob25.csv').write_text(frame_view_csv(gob), encoding='utf-8')
    (out_dir / 'sovereign_sequence.csv').write_text(sovereign_sequence_csv(report['sovereign_sequence']), encoding='utf-8')
    (out_dir / 'events.jsonl').write_text(events_jsonl(events), encoding='utf-8')
    (out_dir / 'event_index.json').write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding='utf-8')
    (out_dir / 'events_flat.csv').write_text(rows_to_csv(events, ['event_id','parent_event_id','run_id','event_type','dictamen_k3','timestamp_utc']), encoding='utf-8')
    (out_dir / 'index_by_param.csv').write_text(index_by_param_csv(index), encoding='utf-8')
    (out_dir / 'index_by_type.csv').write_text(index_by_type_csv(index), encoding='utf-8')
    (out_dir / 'quarantine_log.jsonl').write_text(json.dumps({'state':'PACKET_READY','timestamp_utc':'2026-04-14T00:00:00Z'}, ensure_ascii=False) + '
', encoding='utf-8')
    (out_dir / 'validator_log.jsonl').write_text(json.dumps({'state':'VALIDATED','dictamen_k3': report['dictamen_global'], 'timestamp_utc':'2026-04-14T00:00:03Z'}, ensure_ascii=False) + '
', encoding='utf-8')
    (out_dir / 'execution_log.jsonl').write_text(events_jsonl(events), encoding='utf-8')
    return report
