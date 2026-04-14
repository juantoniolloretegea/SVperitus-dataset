"""
nondestructive_layer.py
========================
Q5 — Capas / máscaras no destructivas · AE-GD2-SV C4

Arquitectura mínima no destructiva compatible con Fase I.

Principio
─────────
La imagen fuente es inmutable. Nunca se sobreescribe.
Toda intervención produce una capa diferencial.
La composición final es: imagen_fuente + capa_diff.
Si la verificación falla, se descarta la capa y se vuelve a la fuente.

No es un sistema de capas Photoshop.
Es la garantía mínima que hace trazable y reversible cualquier intervención.

Modelo de datos
───────────────
  SourceLayer   — imagen fuente (inmutable, solo lectura)
  EditLayer     — capa de intervención (bbox autorizado, operación, resultado)
  CompositeSpec — especificación de composición final (fuente + capas)

El AE-GD2-SV no ejecuta la composición por sí mismo.
Produce el CompositeSpec y una herramienta externa lo ejecuta.
El SV verifica el resultado contra el contrato.

Autor: Diseño AE-GD2-SV C4 — 2026-04-14
ISSN 2695-6411 · CC BY-NC-ND 4.0
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime, timezone
import json
import time
import random


# ── Estructuras de datos ───────────────────────────────────────────────────────

@dataclass
class SourceLayer:
    """
    Referencia a la imagen fuente — inmutable.
    El AE-GD2-SV nunca modifica este objeto.
    """
    source_id:   str
    name:        str
    hash:        str                   # SHA o hash estable del archivo
    width_px:    float
    height_px:   float
    media_type:  str = "image/png"    # image/png | image/jpeg | image/svg+xml

    @property
    def is_immutable(self) -> bool:
        return True  # siempre True — invariante del sistema


@dataclass
class EditLayer:
    """
    Capa de intervención sobre una región autorizada.

    Una EditLayer por región intervenida.
    Solo puede afectar píxeles dentro de authorized_bbox.
    Fuera de authorized_bbox → violación del contrato.
    """
    layer_id:         str
    contract_id:      str
    region_id:        str
    semantic_label:   str
    authorized_bbox:  dict             # {x, y, w, h} — límite duro de intervención
    operation:        str              # ADJUST_MARGINS | REFLOW_TEXT | REPOSITION | etc.
    operation_params: dict             = field(default_factory=dict)
    result_ref:       Optional[str]    = None   # referencia al resultado (path, URL, etc.)
    result_hash:      Optional[str]    = None   # hash del resultado para verificación
    status:           str              = "PENDING"  # PENDING | APPLIED | VERIFIED | DISCARDED
    applied_at:       Optional[str]    = None
    discarded_reason: Optional[str]    = None
    pk_post:          dict[str, str]   = field(default_factory=dict)

    def apply(self, result_ref: str, result_hash: str) -> "EditLayer":
        """Marca la capa como aplicada con referencia al resultado."""
        self.result_ref  = result_ref
        self.result_hash = result_hash
        self.status      = "APPLIED"
        self.applied_at  = datetime.now(timezone.utc).isoformat()
        return self

    def verify(self, pk_post: dict[str, str], passed: bool) -> "EditLayer":
        """Marca la capa como verificada o descartada según el resultado."""
        self.pk_post = pk_post
        self.status  = "VERIFIED" if passed else "DISCARDED"
        return self

    def discard(self, reason: str) -> "EditLayer":
        """Descarta la capa — la fuente permanece intacta."""
        self.status           = "DISCARDED"
        self.discarded_reason = reason
        return self


@dataclass
class CompositeSpec:
    """
    Especificación de composición final: fuente + capas.

    El AE-GD2-SV produce esta especificación.
    Una herramienta externa la ejecuta.
    El SV verifica el resultado contra el contrato.

    Orden de composición
    ────────────────────
    1. Imagen fuente (base, inmutable)
    2. Capas aplicadas en orden (primera = menor prioridad)
    3. Resultado: composición verificable

    Invariante: ninguna EditLayer puede afectar píxeles fuera
    de su authorized_bbox. El executor debe respetar esto.
    """
    spec_id:      str
    run_id:       str
    source:       SourceLayer
    layers:       list[EditLayer]       = field(default_factory=list)
    status:       str                   = "DRAFT"  # DRAFT | READY | EXECUTED | VERIFIED
    created_at:   str                   = ""
    verified_at:  Optional[str]         = None
    global_hash:  Optional[str]         = None    # hash del resultado final compuesto

    def add_layer(self, layer: EditLayer) -> "CompositeSpec":
        """Añade una capa al spec. Solo capas APPLIED o PENDING."""
        if layer.status not in ("APPLIED", "PENDING"):
            raise ValueError(f"Solo se pueden añadir capas APPLIED o PENDING. Estado: {layer.status}")
        self.layers.append(layer)
        return self

    def discard_layer(self, layer_id: str, reason: str) -> "CompositeSpec":
        """Descarta una capa sin afectar la fuente ni otras capas."""
        for layer in self.layers:
            if layer.layer_id == layer_id:
                layer.discard(reason)
                return self
        raise ValueError(f"layer_id {layer_id!r} no encontrado")

    @property
    def active_layers(self) -> list[EditLayer]:
        """Capas no descartadas, en orden de aplicación."""
        return [l for l in self.layers if l.status in ("APPLIED", "VERIFIED")]

    @property
    def is_source_intact(self) -> bool:
        """
        Invariante: la fuente siempre está intacta.
        Siempre True — la fuente nunca se modifica.
        """
        return self.source.is_immutable

    def to_executor_spec(self) -> dict:
        """
        Produce la especificación que la herramienta ejecutora consume.
        Solo incluye las capas activas con sus bbox autorizados.
        """
        return {
            "spec_id":      self.spec_id,
            "run_id":       self.run_id,
            "source": {
                "source_id":  self.source.source_id,
                "name":       self.source.name,
                "hash":       self.source.hash,
                "width_px":   self.source.width_px,
                "height_px":  self.source.height_px,
                "media_type": self.source.media_type,
            },
            "layers": [
                {
                    "layer_id":        l.layer_id,
                    "region_id":       l.region_id,
                    "semantic_label":  l.semantic_label,
                    "authorized_bbox": l.authorized_bbox,
                    "operation":       l.operation,
                    "operation_params":l.operation_params,
                    "result_ref":      l.result_ref,
                }
                for l in self.active_layers
            ],
            "invariants": [
                "source_immutable",
                "no_pixels_outside_authorized_bbox",
                "append_only_event_bank",
            ],
        }

    def to_dict(self) -> dict:
        import dataclasses
        return dataclasses.asdict(self)

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=indent, default=str)


# ── Constructor ────────────────────────────────────────────────────────────────

class LayerBuilder:
    """Construye CompositeSpec a partir del contrato de intervención."""

    def __init__(self, run_id: str, source: SourceLayer):
        self.run_id = run_id
        self.source = source

    def _make_id(self, prefix: str) -> str:
        ts  = int(time.time() * 1000)
        rnd = random.randint(0, 0xFFFFFF)
        return f"{prefix}-{ts}-{rnd:06x}"

    def from_contract(self, contract: dict) -> CompositeSpec:
        """
        Construye el CompositeSpec a partir de un InterventionContract.
        Acepta dict o InterventionContract.
        """
        spec = CompositeSpec(
            spec_id    = self._make_id("SPC"),
            run_id     = self.run_id,
            source     = self.source,
            created_at = datetime.now(timezone.utc).isoformat(),
        )

        regions = (contract.get("authorized_regions", [])
                   if isinstance(contract, dict)
                   else getattr(contract, "authorized_regions", []))

        for region in regions:
            if isinstance(region, dict):
                layer = EditLayer(
                    layer_id        = self._make_id("LYR"),
                    contract_id     = contract.get("contract_id","") if isinstance(contract,dict) else contract.contract_id,
                    region_id       = region.get("region_id",""),
                    semantic_label  = region.get("semantic_label",""),
                    authorized_bbox = region.get("bbox",{}),
                    operation       = region.get("operation","CUSTOM"),
                    operation_params= region.get("operation_params",{}),
                )
            else:
                layer = EditLayer(
                    layer_id        = self._make_id("LYR"),
                    contract_id     = getattr(contract, "contract_id",""),
                    region_id       = region.region_id,
                    semantic_label  = region.semantic_label,
                    authorized_bbox = region.bbox if isinstance(region.bbox, dict) else {"x":region.bbox.x,"y":region.bbox.y,"w":region.bbox.w,"h":region.bbox.h},
                    operation       = region.operation,
                    operation_params= region.operation_params,
                )
            spec.add_layer(layer)

        return spec


# ── CLI de prueba ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    source = SourceLayer(
        source_id  = "SRC-001",
        name       = "4. Acuerdo entre humano y humanoide.png",
        hash       = "abc123def456",
        width_px   = 1200,
        height_px  = 800,
    )

    contract_mock = {
        "contract_id": "CTR-test",
        "authorized_regions": [
            {
                "region_id": "RGN-003", "semantic_label": "FOOTER",
                "bbox": {"x":0,"y":704,"w":1200,"h":96},
                "operation": "ADJUST_MARGINS",
                "operation_params": {"target_margin_min_px":24},
            }
        ]
    }

    builder = LayerBuilder("GD2-RUN-test", source)
    spec = builder.from_contract(contract_mock)

    print("=== COMPOSITE SPEC ===")
    print(f"spec_id:           {spec.spec_id}")
    print(f"source_intact:     {spec.is_source_intact}")
    print(f"capas activas:     {len(spec.active_layers)}")
    print()

    # Simular aplicación de la capa
    layer = spec.layers[0]
    layer.apply(result_ref="output/footer_v1.png", result_hash="xyz789")
    print(f"Estado capa tras apply: {layer.status}")
    print()

    # Simular verificación exitosa
    layer.verify(pk_post={"P12":"0","P17":"0","P18":"0"}, passed=True)
    print(f"Estado capa tras verify: {layer.status}")
    print(f"pk_post: {layer.pk_post}")
    print()

    # Simular fallo — descarte sin afectar fuente
    layer2 = EditLayer(
        layer_id="LYR-002", contract_id="CTR-test",
        region_id="RGN-003", semantic_label="FOOTER",
        authorized_bbox={"x":0,"y":704,"w":1200,"h":96},
        operation="REFLOW_TEXT",
    )
    layer2.apply("output/footer_v2.png","fail_hash")
    layer2.verify(pk_post={"P12":"1","P17":"1","P18":"1"}, passed=False)
    print(f"Estado tras verificación fallida: {layer2.status}")
    print(f"Fuente intacta: {spec.is_source_intact}  ← invariante siempre True")
    print()

    print("=== EXECUTOR SPEC (lo que recibe la herramienta externa) ===")
    print(json.dumps(spec.to_executor_spec(), indent=2, ensure_ascii=False))
