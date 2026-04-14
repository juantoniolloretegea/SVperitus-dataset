from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable
import csv
import io
import json
import math

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


def k3_to_aux(value: str) -> float:
    return {'0': 0.0, '1': 1.0, 'U': 0.5}[value]


def build_frame(mode: str = 'correct') -> list[Parameter]:
    out: list[Parameter] = []
    for idx, name in enumerate(PARAM_NAMES, start=1):
        value = '0' if idx in {1,2,3,4,21,22} else ('U' if idx in {16,17,18,19,20,24,25} else '0')
        if mode == 'create' and idx == 2:
            value = '0'
        out.append(Parameter(idx, f'P{idx:02d}', name, value, 'conformidad suficiente' if value == '0' else 'indeterminación controlada'))
    return out


def build_gob(frame: Iterable[Parameter]) -> list[Parameter]:
    out: list[Parameter] = []
    for p in frame:
        value = p.value_k3
        if p.param_id in {'P16','P17','P18','P19','P20'} and value == '0':
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


def differential_metrics(frame: Iterable[Parameter], gob: Iterable[Parameter]) -> dict:
    frame_list = list(frame)
    gob_list = list(gob)
    values = [k3_to_aux(p.value_k3) for p in frame_list]
    grad = [round(values[i + 1] - values[i], 3) for i in range(len(values) - 1)]
    norm1 = round(sum(abs(g) for g in grad), 3)
    jacobian_diag = [round((k3_to_aux(frame_list[i].value_k3) + k3_to_aux(gob_list[i].value_k3)) / 2, 3) for i in range(len(frame_list))]
    curvature = round(sum(abs(grad[i + 1] - grad[i]) for i in range(len(grad) - 1)), 3) if len(grad) > 1 else 0.0
    return {'gradient': grad, 'jacobian_diag': jacobian_diag, 'jacobian_norm_l1': norm1, 'curvature': curvature}


def modal_metrics(frame: Iterable[Parameter]) -> dict:
    x = [k3_to_aux(p.value_k3) for p in frame]
    n = len(x)
    modes = []
    for k in range(5):
        re = 0.0
        im = 0.0
        for m, value in enumerate(x):
            ang = 2 * math.pi * k * m / n
            re += value * math.cos(ang)
            im -= value * math.sin(ang)
        amp = math.sqrt(re * re + im * im) / n
        modes.append({'k': k, 'amplitude': round(amp, 4)})
    total_energy = round(sum(v * v for v in x), 4)
    kept = sum(m['amplitude'] * m['amplitude'] for m in modes[:3])
    residual = round(max(total_energy - kept, 0.0), 4)
    return {'first_modes': modes, 'total_energy': total_energy, 'residual_trunc_k2': residual}


def metrology(width: int = 1200, height: int = 800) -> dict:
    ufe = 8
    return {
        'primitive': 'UFE',
        'base_unit_px': ufe,
        'width_ufe': round(width / ufe, 2),
        'height_ufe': round(height / ufe, 2),
        'margin_ufe': 6,
        'minimum_spacing_ufe': 2,
        'title_band_ufe': 8,
    }


def to_csv(parameters: Iterable[Parameter]) -> str:
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(['position', 'param_id', 'name', 'value_k3', 'justification'])
    for p in parameters:
        writer.writerow([p.position, p.param_id, p.name, p.value_k3, p.justification])
    return buf.getvalue()


def build_report(mode: str = 'correct') -> dict:
    frame = build_frame(mode)
    gob = build_gob(frame)
    return {
        'run_id': 'PY-RUN-0001',
        'dictamen_global': dictamen(gob),
        'critical_parameters': [p.__dict__ for p in frame],
        'governability_parameters': [p.__dict__ for p in gob],
        'sovereign_sequence': [
            {'sovereign_id': 'S0', 'epsilon_id': 'ε0', 'label': 'Frame inicial declarado', 'dictamen_k3': 'INDETERMINADO'},
            {'sovereign_id': 'S1', 'epsilon_id': 'ε1', 'label': 'Entrada admitida tras cuarentena local', 'dictamen_k3': dictamen(frame)},
            {'sovereign_id': 'S2', 'epsilon_id': 'ε2', 'label': 'Intención tipada en borrador', 'dictamen_k3': dictamen(frame)},
            {'sovereign_id': 'S3', 'epsilon_id': 'ε3', 'label': 'Intención confirmada por el usuario', 'dictamen_k3': dictamen(frame)},
            {'sovereign_id': 'S4', 'epsilon_id': 'ε4', 'label': 'Auditoría poligonal y dictamen de exposición', 'dictamen_k3': dictamen(gob)},
        ],
        'auxiliary_metrics': {
            'differential': differential_metrics(frame, gob),
            'modal': modal_metrics(frame),
            'metrology': metrology(),
        },
    }


def dump_report(path: str, mode: str = 'correct') -> None:
    report = build_report(mode)
    with open(path, 'w', encoding='utf-8') as fh:
        json.dump(report, fh, ensure_ascii=False, indent=2)
