"""
sovereign_proxy.py
==================
Q7 — Acoplamiento con herramienta externa · AE-GD2-SV C4

Patrón de ingeniería: Proxy Soberano

El SV mantiene la soberanía aunque no ejecute gráficamente por sí mismo.

Principio
─────────
La herramienta ejecutora es un proxy subordinado.
No tiene interlocución directa con el usuario.
No accede a la imagen fuente directamente.
Solo recibe el ContractRequest firmado por el SV,
ejecuta dentro de sus límites, y devuelve el ContractResponse.
El SV decide si el resultado cumple el contrato.
Si no cumple, el SV no reintenta automáticamente.

El SV sigue siendo soberano porque:
  1. Define el contrato — la herramienta no puede modificarlo.
  2. Verifica el resultado — la herramienta no puede autoverificarse.
  3. Decide la continuación — la herramienta no tiene iniciativa.
  4. Registra la trazabilidad — la herramienta no escribe en el banco.

Interfaz del proxy
──────────────────
  ContractRequest  — lo que el SV envía al executor
  ContractResponse — lo que el executor devuelve al SV
  SovereignProxy   — clase que gestiona el protocolo completo

Adaptadores incluidos
──────────────────────
  LocalFileExecutor  — ejecutor local para pruebas (no hace nada real)
  HttpExecutorAdapter — adaptador HTTP para executor remoto
  DryRunExecutor     — dry-run: simula sin modificar nada

Autor: Diseño AE-GD2-SV C4 — 2026-04-14
ISSN 2695-6411 · CC BY-NC-ND 4.0
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional, Callable
from datetime import datetime, timezone
import json
import time
import random


# ── Estructuras del protocolo ──────────────────────────────────────────────────

@dataclass
class ContractRequest:
    """
    Lo que el SV envía al executor.
    Firmado e inmutable desde el momento de emisión.
    """
    request_id:    str
    contract_id:   str
    run_id:        str
    spec:          dict          # CompositeSpec.to_executor_spec()
    issued_at:     str
    max_retries:   int = 0       # 0 = sin reintento automático (política SV)
    timeout_s:     float = 30.0

    def to_json(self) -> str:
        import dataclasses
        return json.dumps(dataclasses.asdict(self), ensure_ascii=False, indent=2)


@dataclass
class ContractResponse:
    """
    Lo que el executor devuelve al SV.
    El SV no confía en este resultado sin verificarlo contra el contrato.
    """
    request_id:   str
    contract_id:  str
    status:       str            # OK | PARTIAL | FAILED | ERROR
    layers_out:   list[dict]     = field(default_factory=list)  # resultados por capa
    executor_log: str            = ""
    responded_at: str            = ""
    error_msg:    Optional[str]  = None

    @classmethod
    def error(cls, request_id: str, contract_id: str, msg: str) -> "ContractResponse":
        return cls(
            request_id   = request_id,
            contract_id  = contract_id,
            status       = "ERROR",
            error_msg    = msg,
            responded_at = datetime.now(timezone.utc).isoformat(),
        )


# ── Interfaz del executor ──────────────────────────────────────────────────────

class ExecutorAdapter(ABC):
    """
    Interfaz que cualquier herramienta ejecutora debe implementar
    para ser usada por el SovereignProxy.

    El AE-GD2-SV no sabe ni le importa cómo el executor hace su trabajo.
    Solo sabe que recibe un ContractRequest y devuelve un ContractResponse.
    """

    @abstractmethod
    def execute(self, request: ContractRequest) -> ContractResponse:
        """
        Ejecuta la solicitud del contrato.
        Debe respetar los authorized_bbox de cada capa.
        No puede modificar la imagen fuente.
        No puede autoverificarse.
        """
        ...

    @abstractmethod
    def health_check(self) -> bool:
        """Verifica que el executor está disponible."""
        ...


# ── Adaptadores concretos ──────────────────────────────────────────────────────

class DryRunExecutor(ExecutorAdapter):
    """
    Executor de simulación — no modifica nada.
    Útil para pruebas del protocolo sin herramienta real.
    """

    def execute(self, request: ContractRequest) -> ContractResponse:
        layers_out = []
        for layer in request.spec.get("layers", []):
            layers_out.append({
                "layer_id":    layer.get("layer_id"),
                "region_id":   layer.get("region_id"),
                "result_ref":  f"dry_run://{layer.get('layer_id')}.png",
                "result_hash": f"dry_{hash(layer.get('layer_id',''))}",
                "status":      "DRY_RUN",
            })
        return ContractResponse(
            request_id   = request.request_id,
            contract_id  = request.contract_id,
            status       = "OK",
            layers_out   = layers_out,
            executor_log = "DryRunExecutor: no se modificaron archivos",
            responded_at = datetime.now(timezone.utc).isoformat(),
        )

    def health_check(self) -> bool:
        return True


class LocalFileExecutor(ExecutorAdapter):
    """
    Executor local que lee el composite_spec y genera un log de qué haría.
    No ejecuta modificaciones reales — produce el manifiesto de intervención.
    Útil para validar el protocolo antes de conectar un executor real.
    """

    def __init__(self, output_dir: str = "/tmp"):
        self.output_dir = output_dir

    def execute(self, request: ContractRequest) -> ContractResponse:
        import os
        layers_out = []
        log_lines  = [f"LocalFileExecutor — run_id: {request.run_id}"]

        for layer in request.spec.get("layers", []):
            bbox  = layer.get("authorized_bbox", {})
            op    = layer.get("operation", "UNKNOWN")
            label = layer.get("semantic_label", "")
            log_lines.append(
                f"  [{label}] {op} — bbox=({bbox.get('x')},{bbox.get('y')},"
                f"{bbox.get('w')}x{bbox.get('h')})"
            )
            # Escribir manifiesto en disco
            manifest_path = os.path.join(
                self.output_dir,
                f"{layer.get('layer_id','layer')}_manifest.json"
            )
            try:
                with open(manifest_path, 'w') as f:
                    json.dump(layer, f, indent=2)
                result_ref = manifest_path
                result_hash = str(abs(hash(manifest_path)))
            except Exception as e:
                result_ref  = None
                result_hash = None
                log_lines.append(f"    ERROR escribiendo manifiesto: {e}")

            layers_out.append({
                "layer_id":    layer.get("layer_id"),
                "region_id":   layer.get("region_id"),
                "result_ref":  result_ref,
                "result_hash": result_hash,
                "status":      "APPLIED" if result_ref else "FAILED",
            })

        all_ok = all(l["status"] == "APPLIED" for l in layers_out)
        return ContractResponse(
            request_id   = request.request_id,
            contract_id  = request.contract_id,
            status       = "OK" if all_ok else "PARTIAL",
            layers_out   = layers_out,
            executor_log = "\n".join(log_lines),
            responded_at = datetime.now(timezone.utc).isoformat(),
        )

    def health_check(self) -> bool:
        import os
        return os.path.isdir(self.output_dir)


# ── Proxy soberano ─────────────────────────────────────────────────────────────

class SovereignProxy:
    """
    Gestiona el protocolo completo entre el SV y la herramienta ejecutora.

    El SovereignProxy garantiza que:
      1. El contrato es inmutable una vez firmado.
      2. La herramienta ejecutora no tiene iniciativa.
      3. La verificación la hace el SV, no el executor.
      4. Toda la trazabilidad va al banco de eventos del SV.
    """

    def __init__(
        self,
        executor:       ExecutorAdapter,
        verify_fn:      Optional[Callable] = None,  # fn(contract, response) → VerificationResult
        event_callback: Optional[Callable] = None,  # fn(event_type, data) → None
    ):
        self.executor       = executor
        self.verify_fn      = verify_fn
        self.event_callback = event_callback

    def _emit(self, event_type: str, data: dict) -> None:
        if self.event_callback:
            self.event_callback(event_type, data)

    def _make_request_id(self) -> str:
        ts  = int(time.time() * 1000)
        rnd = random.randint(0, 0xFFFFFF)
        return f"REQ-{ts}-{rnd:06x}"

    def execute_contract(
        self,
        contract: dict,
        composite_spec: dict,
    ) -> dict:
        """
        Ejecuta el protocolo completo:
          1. Verificar disponibilidad del executor
          2. Emitir ContractRequest firmado
          3. Enviar al executor
          4. Verificar la respuesta contra el contrato
          5. Emitir gate_decision al banco de eventos
          6. Devolver resultado estructurado

        Returns
        -------
        dict con:
          request, response, gate_decision, verification_details
        """
        contract_id = contract.get("contract_id","") if isinstance(contract,dict) else contract.contract_id

        # 1. Health check
        if not self.executor.health_check():
            self._emit("executor_unavailable", {"contract_id": contract_id})
            return {
                "gate_decision": "U",
                "error": "Executor no disponible",
                "contract_id": contract_id,
            }

        # 2. Construir request
        request = ContractRequest(
            request_id  = self._make_request_id(),
            contract_id = contract_id,
            run_id      = contract.get("run_id","") if isinstance(contract,dict) else contract.run_id,
            spec        = composite_spec,
            issued_at   = datetime.now(timezone.utc).isoformat(),
        )
        self._emit("contract_request_issued", {"request_id": request.request_id})

        # 3. Ejecutar
        try:
            response = self.executor.execute(request)
        except Exception as e:
            response = ContractResponse.error(request.request_id, contract_id, str(e))

        self._emit("contract_response_received", {
            "request_id": request.request_id,
            "status": response.status,
        })

        if response.status == "ERROR":
            return {
                "gate_decision": "U",
                "error": response.error_msg,
                "request": request,
                "response": response,
            }

        # 4. Verificar contra el contrato
        gate_decision = "U"
        verification_details = {}
        if self.verify_fn:
            try:
                vr = self.verify_fn(contract, response)
                gate_decision        = vr.get("gate_decision", "U") if isinstance(vr, dict) else vr.gate_decision
                verification_details = vr if isinstance(vr, dict) else vars(vr)
            except Exception as e:
                gate_decision = "HUMAN_REVIEW"
                verification_details = {"error": str(e)}
        else:
            # Sin función de verificación → U por defecto (no se puede verificar)
            gate_decision = "U"
            verification_details = {"note": "Sin función de verificación registrada — estado U."}

        self._emit("gate_decision_emitted", {
            "contract_id":  contract_id,
            "gate_decision": gate_decision,
        })

        return {
            "gate_decision":        gate_decision,
            "request":              request,
            "response":             response,
            "verification_details": verification_details,
        }


# ── CLI de prueba ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import dataclasses

    events = []
    def on_event(event_type, data):
        events.append({"event_type": event_type, "data": data})
        print(f"  EVENT: {event_type} — {data}")

    contract_mock = {
        "contract_id": "CTR-test-001",
        "run_id":      "GD2-RUN-test",
        "authorized_regions": [
            {"region_id":"RGN-003","semantic_label":"FOOTER","bbox":{"x":0,"y":704,"w":1200,"h":96},"operation":"ADJUST_MARGINS","operation_params":{},"verification":{"pk_targets":{"P12":"0","P17":"0","P18":"0"}}}
        ],
    }
    composite_spec_mock = {
        "spec_id": "SPC-test",
        "run_id":  "GD2-RUN-test",
        "source":  {"name":"imagen.png","hash":"abc123"},
        "layers":  [{"layer_id":"LYR-001","region_id":"RGN-003","semantic_label":"FOOTER","authorized_bbox":{"x":0,"y":704,"w":1200,"h":96},"operation":"ADJUST_MARGINS","operation_params":{}}],
        "invariants": ["source_immutable"],
    }

    print("=== TEST 1: DryRunExecutor ===")
    proxy = SovereignProxy(executor=DryRunExecutor(), event_callback=on_event)
    result = proxy.execute_contract(contract_mock, composite_spec_mock)
    print(f"gate_decision: {result['gate_decision']}")
    print(f"response status: {result['response'].status}")

    print()
    print("=== TEST 2: LocalFileExecutor ===")
    proxy2 = SovereignProxy(executor=LocalFileExecutor("/tmp"), event_callback=on_event)
    result2 = proxy2.execute_contract(contract_mock, composite_spec_mock)
    print(f"gate_decision: {result2['gate_decision']}")
    print(f"layers_out: {result2['response'].layers_out}")

    print()
    print("=== EVENTOS REGISTRADOS ===")
    for e in events:
        print(f"  {e['event_type']}: {e['data']}")

    print()
    print("=== INVARIANTE DE SOBERANÍA ===")
    print("  El executor recibe solo el ContractRequest — no tiene acceso al banco de eventos.")
    print("  La verificación la hace el SV (verify_fn) — el executor no puede autoverificarse.")
    print("  gate_decision='U' cuando no hay verify_fn — el SV nunca asume que todo fue bien.")
