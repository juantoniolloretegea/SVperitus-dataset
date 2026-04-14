"""
multi_region_model.py
=====================
Q4 — Selección múltiple y evolución · AE-GD2-SV C4

Diseña el modelo de datos para múltiples regiones/objetos
desde la Fase I, sin sobredimensionar la interfaz actual.

Principio
─────────
El modelo interno nace preparado para múltiples regiones.
La UI puede exponer solo una interacción austera (una región
seleccionada a la vez) sin cambiar el modelo subyacente.
Esto evita refactorización cuando se añada selección múltiple real.

Relaciones entre regiones
──────────────────────────
Cada región en el contrato puede tener una relación con otras:
  PRESERVE   — no tocar bajo ninguna circunstancia
  MODIFY     — intervenir según los parámetros del contrato
  EXCLUDE    — excluir del análisis (no medir, no intervenir)
  DEPENDS_ON — esta región solo se puede modificar si otra región
               ya fue corregida (orden de dependencia)

Esto es lo que permite:
  - corregir footer sin tocar título
  - corregir título solo después de que el footer esté resuelto
  - excluir el fondo del análisis de colisiones

Estado de progreso multi-región
────────────────────────────────
Cada región tiene su propio ciclo: PENDING → IN_PROGRESS → DONE | FAILED | U
El ciclo del contrato completo no cierra hasta que todas las regiones
en MODIFY estén en DONE o el gate emita CLOSE/HUMAN_REVIEW.

Autor: Diseño AE-GD2-SV C4 — 2026-04-14
ISSN 2695-6411 · CC BY-NC-ND 4.0
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from enum import Enum
import json


class RegionRelation(str, Enum):
    PRESERVE   = "PRESERVE"
    MODIFY     = "MODIFY"
    EXCLUDE    = "EXCLUDE"
    DEPENDS_ON = "DEPENDS_ON"


class RegionStatus(str, Enum):
    PENDING     = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    DONE        = "DONE"
    FAILED      = "FAILED"
    U           = "U"         # indeterminado — no completado, no fallado


@dataclass
class RegionEntry:
    """
    Entrada de una región en el modelo multi-región.
    Una entrada por objeto editorial del lienzo.
    """
    region_id:      str
    semantic_label: str
    relation:       RegionRelation
    bbox:           dict                   # {x, y, w, h}
    pk_initial:     dict[str, str]         = field(default_factory=dict)
    pk_post:        dict[str, str]         = field(default_factory=dict)
    depends_on:     list[str]              = field(default_factory=list)  # region_ids
    status:         RegionStatus           = RegionStatus.PENDING
    gate_decision:  Optional[str]          = None
    notes:          str                    = ""

    @property
    def is_actionable(self) -> bool:
        """True si la región puede ser intervenida ahora."""
        return (
            self.relation == RegionRelation.MODIFY and
            self.status == RegionStatus.PENDING
        )

    @property
    def is_blocked(self) -> bool:
        """True si la región tiene dependencias sin resolver."""
        return bool(self.depends_on)


@dataclass
class MultiRegionModel:
    """
    Modelo de datos para múltiples regiones en un contrato AE-GD2-SV.

    Diseñado para escalar desde 1 región (Fase I) hasta N regiones
    sin cambiar la interfaz del contrato ni del corrector factual.
    """
    run_id:  str
    regions: list[RegionEntry] = field(default_factory=list)

    # ── Construcción desde draft ───────────────────────────────────────────

    @classmethod
    def from_draft(cls, run_id: str, draft: dict,
                   region_objects: list[dict]) -> "MultiRegionModel":
        """
        Construye el modelo desde el draft parseado y la lista de RegionObjects.

        Los objetos en draft.modify  → MODIFY
        Los objetos en draft.preserve → PRESERVE
        Los objetos no mencionados  → EXCLUDE
        """
        modify_labels   = {l.lower() for l in draft.get("modify", [])}
        preserve_labels = {l.lower() for l in draft.get("preserve", [])}

        entries: list[RegionEntry] = []
        for ro in region_objects:
            label = (ro.get("semantic_label") or "").lower()
            if label in modify_labels:
                relation = RegionRelation.MODIFY
            elif label in preserve_labels:
                relation = RegionRelation.PRESERVE
            else:
                relation = RegionRelation.EXCLUDE

            entries.append(RegionEntry(
                region_id      = ro.get("region_id", ""),
                semantic_label = ro.get("semantic_label", ""),
                relation       = relation,
                bbox           = ro.get("bbox", {}),
                pk_initial     = ro.get("pk_map", {}),
            ))

        return cls(run_id=run_id, regions=entries)

    # ── Consultas ──────────────────────────────────────────────────────────

    def get_modify_regions(self) -> list[RegionEntry]:
        return [r for r in self.regions if r.relation == RegionRelation.MODIFY]

    def get_actionable_regions(self) -> list[RegionEntry]:
        """
        Regiones que pueden intervenirse ahora: MODIFY, PENDING, sin dependencias pendientes.
        """
        done_ids = {r.region_id for r in self.regions if r.status == RegionStatus.DONE}
        return [
            r for r in self.regions
            if r.relation == RegionRelation.MODIFY and
               r.status == RegionStatus.PENDING and
               all(dep in done_ids for dep in r.depends_on)
        ]

    def add_dependency(self, region_id: str, depends_on_id: str) -> None:
        """
        Declara que region_id solo puede modificarse después de que
        depends_on_id esté en DONE.
        """
        for r in self.regions:
            if r.region_id == region_id:
                if depends_on_id not in r.depends_on:
                    r.depends_on.append(depends_on_id)
                return
        raise ValueError(f"region_id {region_id!r} no encontrado")

    def update_status(self, region_id: str, status: RegionStatus,
                      pk_post: dict[str, str] | None = None,
                      gate_decision: str | None = None,
                      notes: str = "") -> None:
        for r in self.regions:
            if r.region_id == region_id:
                r.status        = status
                r.gate_decision = gate_decision
                r.notes         = notes
                if pk_post:
                    r.pk_post = pk_post
                return
        raise ValueError(f"region_id {region_id!r} no encontrado")

    # ── Estado global ──────────────────────────────────────────────────────

    @property
    def global_status(self) -> str:
        """
        Estado global del modelo:
          DONE         — todas las regiones MODIFY en DONE
          IN_PROGRESS  — al menos una MODIFY en IN_PROGRESS o PENDING
          FAILED       — al menos una MODIFY en FAILED
          U            — al menos una MODIFY en U sin FAILED
          HUMAN_REVIEW — gate emitió HUMAN_REVIEW en alguna región
        """
        modify = self.get_modify_regions()
        if not modify:
            return "DONE"
        statuses = {r.status for r in modify}
        gates    = {r.gate_decision for r in modify if r.gate_decision}

        if "HUMAN_REVIEW" in gates:
            return "HUMAN_REVIEW"
        if RegionStatus.FAILED in statuses:
            return "FAILED"
        if all(s == RegionStatus.DONE for s in statuses):
            return "DONE"
        if RegionStatus.U in statuses:
            return "U"
        return "IN_PROGRESS"

    def consolidated_pk_state(self) -> dict[str, str]:
        """
        Estado K3 consolidado post-ejecución de todas las regiones MODIFY.
        Política: 1 > U > 0.
        """
        combined: dict[str, str] = {}
        priority = {"1": 2, "U": 1, "0": 0}
        for r in self.get_modify_regions():
            for pk, val in r.pk_post.items():
                current = combined.get(pk, "0")
                if priority.get(val, 0) > priority.get(current, 0):
                    combined[pk] = val
        return combined

    def to_dict(self) -> dict:
        return {
            "run_id":  self.run_id,
            "global_status": self.global_status,
            "regions": [
                {
                    "region_id":      r.region_id,
                    "semantic_label": r.semantic_label,
                    "relation":       r.relation.value,
                    "bbox":           r.bbox,
                    "pk_initial":     r.pk_initial,
                    "pk_post":        r.pk_post,
                    "depends_on":     r.depends_on,
                    "status":         r.status.value,
                    "gate_decision":  r.gate_decision,
                    "notes":          r.notes,
                }
                for r in self.regions
            ],
        }

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=indent)


# ── CLI de prueba ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    draft = {
        "modify":   ["footer"],
        "preserve": ["estructura_general", "titulo_superior", "cartel_izquierdo",
                     "libros", "personajes", "fondo"],
    }
    regions = [
        {"region_id":"RGN-001","semantic_label":"TITULO_SUPERIOR",  "bbox":{"x":0,"y":0,"w":1200,"h":96},   "pk_map":{"P11":"0","P17":"0"}},
        {"region_id":"RGN-002","semantic_label":"CARTEL_IZQUIERDO", "bbox":{"x":0,"y":96,"w":360,"h":608},  "pk_map":{"P19":"U"}},
        {"region_id":"RGN-003","semantic_label":"FOOTER",           "bbox":{"x":0,"y":704,"w":1200,"h":96}, "pk_map":{"P12":"1","P17":"1","P18":"1"}},
        {"region_id":"RGN-004","semantic_label":"FONDO",            "bbox":{"x":0,"y":0,"w":1200,"h":800},  "pk_map":{"P20":"U"}},
    ]

    model = MultiRegionModel.from_draft("GD2-RUN-test", draft, regions)

    print("=== MODELO MULTI-REGIÓN ===")
    for r in model.regions:
        print(f"  {r.semantic_label:20s} {r.relation.value:10s} {r.status.value}")

    print()
    print("=== REGIONES ACCIONABLES AHORA ===")
    for r in model.get_actionable_regions():
        print(f"  {r.semantic_label} pk_initial={r.pk_initial}")

    print()
    print("=== CON DEPENDENCIA: FOOTER depende de TITULO ===")
    model.add_dependency("RGN-003", "RGN-001")
    actionable = model.get_actionable_regions()
    print(f"  Accionables: {[r.semantic_label for r in actionable]}")
    print(f"  (FOOTER bloqueado porque TITULO no está en DONE)")

    print()
    # Simular completar TITULO y luego FOOTER
    model.update_status("RGN-001", RegionStatus.DONE, pk_post={"P11":"0","P17":"0"}, gate_decision="CLOSE")
    actionable2 = model.get_actionable_regions()
    print(f"  Tras TITULO→DONE, accionables: {[r.semantic_label for r in actionable2]}")

    model.update_status("RGN-003", RegionStatus.DONE, pk_post={"P12":"0","P17":"0","P18":"0"}, gate_decision="CLOSE")
    print(f"  Estado global: {model.global_status}")
    print(f"  pk_post consolidado: {model.consolidated_pk_state()}")
