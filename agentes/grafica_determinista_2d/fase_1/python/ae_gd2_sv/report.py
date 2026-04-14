from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable
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
        value = '0' if idx in {1,2,3,22} else ('U' if idx in {16,17,18,19,20,24,25} else '0')
        if mode == 'create' and idx == 2:
            value = '0'
        out.append(Parameter(idx, f'P{idx:02d}', name, value, 'conformidad suficiente' if value == '0' else 'indeterminación controlada'))
    return out


def dictamen(cell: Iterable[Parameter]) -> str:
    values = [p.value_k3 for p in cell]
    if '1' in values:
        return 'NO APTO'
    if 'U' in values:
        return 'INDETERMINADO'
    return 'APTO'


def to_csv(parameters: Iterable[Parameter]) -> str:
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(['position','param_id','name','value_k3','justification'])
    for p in parameters:
        writer.writerow([p.position, p.param_id, p.name, p.value_k3, p.justification])
    return buf.getvalue()


def build_report(mode: str = 'correct') -> dict:
    frame = build_frame(mode)
    return {
        'run_id': 'PY-RUN-0001',
        'dictamen_global': dictamen(frame),
        'critical_parameters': [p.__dict__ for p in frame],
        'sovereign_sequence': [
            {'sovereign_id':'S0','epsilon_id':'ε0','label':'Frame inicial declarado','dictamen_k3':'INDETERMINADO'},
            {'sovereign_id':'S1','epsilon_id':'ε1','label':'Entrada admitida tras cuarentena','dictamen_k3':dictamen(frame)},
        ],
    }


def dump_report(path: str, mode: str = 'correct') -> None:
    report = build_report(mode)
    with open(path, 'w', encoding='utf-8') as fh:
        json.dump(report, fh, ensure_ascii=False, indent=2)
