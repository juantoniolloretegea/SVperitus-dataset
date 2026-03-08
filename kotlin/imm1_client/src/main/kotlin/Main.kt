import kotlinx.browser.document
import kotlinx.browser.window
import org.w3c.dom.HTMLButtonElement
import org.w3c.dom.HTMLElement

// ═══════════════════════════════════════════════════════════════════
// SVperitus — IMMUNO-1 Kotlin Client
// Puente real Kotlin/JS → Rust/WASM (Watson F.1–F.5)
//
// Este archivo NO contiene lógica normativa.
// Kotlin construye el caso, llama al motor Rust/WASM real,
// y muestra la respuesta sin interpretarla ni modificarla.
//
// Serie: ISSN 2695-6411 · CC BY-NC-ND 4.0
// Autor: Juan Antonio Lloret Egea
// ═══════════════════════════════════════════════════════════════════

// ── Interop helpers ──────────────────────────────────────────────

/** Accede a window.__wasm (expuesto por el script de carga WASM) */
private fun wasmModule(): dynamic = js("window.__wasm")

/** Accede a window.__engine_status */
private fun engineStatus(): String =
    (js("window.__engine_status") as? String) ?: "loading"

/** Accede a window.__engine_error */
private fun engineError(): String =
    (js("window.__engine_error") as? String) ?: ""

// ── Caso fijo de demostración (Watson F.3, opción A) ────────────
//
// Paciente en remisión, buen recuento, vacunas parciales,
// profilaxis incompleta → resultado esperado: INDETERMINADO.
// Los valores se eligen para que el motor devuelva conteos
// mixtos (n0, n1, nU > 0), demostrando que la evaluación es real.

private fun buildDemoCase(): String = """
{
  "anc": 2000,
  "lymphocytes": 1200,
  "igg": 800,
  "spleen_intact": true,
  "barriers_intact": true,
  "neoplasia_phase": "remission",
  "chemo_active": false,
  "biologic_type": "none",
  "tph_cart": "none",
  "corticoid_mg": 5.0,
  "severe_bacterial_12m": false,
  "prior_ifd": false,
  "chronic_viral": "none",
  "mdr_colonization": false,
  "recent_healthcare": true,
  "flu_vaccine": "current",
  "pneumo_vaccine": null,
  "covid_vaccine": "none",
  "hepb_vaccine": null,
  "other_vaccines": "incomplete",
  "pjp_prophylaxis": "adequate",
  "antiviral_prophylaxis": null,
  "antifungal_prophylaxis": "inadequate",
  "antibacterial_prophylaxis": "adequate",
  "reevaluation_plan": "structured"
}
""".trimIndent()

// ── Renderizado ──────────────────────────────────────────────────

/** Actualiza la UI con el estado del motor */
private fun renderStatus(container: HTMLElement, status: String, error: String) {
    val statusColor = when (status) {
        "rust" -> "#22c55e"
        "error" -> "#ef4444"
        else -> "#facc15"
    }
    val statusText = when (status) {
        "rust" -> "Motor Rust/WASM cargado e inicializado"
        "error" -> "Error al cargar el motor: $error"
        else -> "Cargando motor WASM…"
    }

    val el = document.getElementById("engine-status")
    if (el != null) {
        el.innerHTML = """
            <span style="display:inline-block;width:10px;height:10px;border-radius:50%;
                         background:$statusColor;margin-right:8px;"></span>
            $statusText
        """.trimIndent()
    }

    // Habilitar/deshabilitar botones según estado (Watson F.2)
    val btnDemo = document.getElementById("btn-run-demo") as? HTMLButtonElement
    val btnInfo = document.getElementById("btn-engine-info") as? HTMLButtonElement
    val ready = status == "rust"
    btnDemo?.disabled = !ready
    btnInfo?.disabled = !ready
}

/** Muestra el resultado de evaluate_immuno1() en el panel de resultados */
private fun renderResult(json: String, elapsed: Double) {
    val panel = document.getElementById("result-panel") ?: return
    val parsed = js("JSON.parse")(json)

    val error = parsed.error
    if (error != null && error != undefined) {
        panel.innerHTML = """
            <div style="padding:16px;background:#fef2f2;border:1px solid #fecaca;border-radius:12px;color:#991b1b;">
                <strong>Error del motor:</strong> $error
            </div>
        """.trimIndent()
        return
    }

    val globalClass = parsed.global_class as String
    val n0 = parsed.n0
    val n1 = parsed.n1
    val nU = parsed.nU
    val vector = parsed.vector
    val engine = parsed.engine as String

    // Colores según clase global
    val (classBg, classBorder, classText) = when (globalClass) {
        "APTO" -> Triple("#ecfdf5", "#a7f3d0", "#065f46")
        "NO_APTO" -> Triple("#fef2f2", "#fecaca", "#991b1b")
        else -> Triple("#fffbeb", "#fde68a", "#92400e")
    }

    // Construir vector visual
    val vectorStr = buildString {
        val arr = vector
        val len = js("Array.isArray")(arr) as Boolean
        if (len) {
            val size = (js("arr.length") as? Int) ?: 0
            // Use JS interop to iterate
            append("[")
            val items = mutableListOf<String>()
            for (i in 0 until 25) {
                val v = js("parsed.vector[i]") as? String ?: "?"
                val color = when (v) {
                    "0" -> "#22c55e"
                    "1" -> "#ef4444"
                    else -> "#eab308"
                }
                items.add("""<span style="color:$color;font-weight:600;">$v</span>""")
            }
            append(items.joinToString(", "))
            append("]")
        }
    }

    panel.innerHTML = """
        <div style="margin-bottom:16px;">
            <div style="padding:16px;background:$classBg;border:1px solid $classBorder;
                        border-radius:12px;text-align:center;">
                <div style="font-size:0.85rem;color:$classText;margin-bottom:4px;">Clase global</div>
                <div style="font-size:1.5rem;font-weight:700;color:$classText;">$globalClass</div>
            </div>
        </div>
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:16px;">
            <div style="padding:12px;background:#ecfdf5;border:1px solid #a7f3d0;border-radius:10px;text-align:center;">
                <div style="font-size:0.75rem;color:#065f46;">n₀</div>
                <div style="font-size:1.5rem;font-weight:700;color:#065f46;">$n0</div>
            </div>
            <div style="padding:12px;background:#fef2f2;border:1px solid #fecaca;border-radius:10px;text-align:center;">
                <div style="font-size:0.75rem;color:#991b1b;">n₁</div>
                <div style="font-size:1.5rem;font-weight:700;color:#991b1b;">$n1</div>
            </div>
            <div style="padding:12px;background:#fffbeb;border:1px solid #fde68a;border-radius:10px;text-align:center;">
                <div style="font-size:0.75rem;color:#92400e;">nU</div>
                <div style="font-size:1.5rem;font-weight:700;color:#92400e;">$nU</div>
            </div>
        </div>
        <div style="margin-bottom:12px;">
            <div style="font-size:0.85rem;font-weight:600;margin-bottom:6px;">Vector P01–P25</div>
            <div style="font-family:monospace;font-size:0.85rem;background:#f8fafc;
                        padding:10px;border-radius:8px;border:1px solid #e2e8f0;
                        word-break:break-all;">$vectorStr</div>
        </div>
        <div style="font-size:0.8rem;color:#64748b;">
            Motor: <strong>$engine</strong> · Tiempo: ${elapsed.asDynamic().toFixed(3)} ms ·
            T(25) = 19
        </div>
    """.trimIndent()
}

/** Muestra el resultado de engine_info() */
private fun renderEngineInfo(json: String) {
    val panel = document.getElementById("info-panel") ?: return
    val parsed = js("JSON.parse")(json)

    val engine = parsed.engine as? String ?: "?"
    val module = parsed.module as? String ?: "?"
    val n = parsed.n
    val threshold = parsed.threshold
    val parity = parsed.parity as? String ?: "?"

    panel.innerHTML = """
        <table style="width:100%;border-collapse:collapse;font-size:0.9rem;">
            <tr><td style="padding:6px 8px;font-weight:600;color:#475569;">Engine</td>
                <td style="padding:6px 8px;">$engine</td></tr>
            <tr style="background:#f8fafc;">
                <td style="padding:6px 8px;font-weight:600;color:#475569;">Module</td>
                <td style="padding:6px 8px;">$module</td></tr>
            <tr><td style="padding:6px 8px;font-weight:600;color:#475569;">n</td>
                <td style="padding:6px 8px;">$n</td></tr>
            <tr style="background:#f8fafc;">
                <td style="padding:6px 8px;font-weight:600;color:#475569;">Threshold T(n)</td>
                <td style="padding:6px 8px;">$threshold</td></tr>
            <tr><td style="padding:6px 8px;font-weight:600;color:#475569;">Parity</td>
                <td style="padding:6px 8px;">$parity</td></tr>
        </table>
    """.trimIndent()
}

// ── Punto de entrada ─────────────────────────────────────────────

fun main() {
    val root = document.getElementById("root") ?: return

    // ── Construir interfaz (Watson F.5) ──
    root.innerHTML = """
        <div style="max-width:800px;margin:0 auto;padding:32px 20px;font-family:system-ui,sans-serif;
                     color:#e5e7eb;line-height:1.6;">

            <div style="margin-bottom:28px;">
                <div style="font-size:0.85rem;color:#c9a84c;font-weight:700;text-transform:uppercase;
                            letter-spacing:0.04em;margin-bottom:8px;">
                    SVperitus · Kotlin → WASM bridge
                </div>
                <h1 style="margin:0 0 12px;font-size:2rem;color:#f1f5f9;">
                    IMMUNO-1 Kotlin Client
                </h1>
                <p style="color:#94a3b8;margin:0 0 16px;">
                    Este cliente Kotlin demuestra integración real contra el motor Rust/WASM.
                    No usa iframe ni duplica lógica normativa. Kotlin construye el caso,
                    Rust lo evalúa, Kotlin muestra el resultado.
                </p>
                <div id="engine-status" style="padding:12px 16px;background:rgba(255,255,255,0.05);
                     border:1px solid #334155;border-radius:10px;font-size:0.9rem;">
                    Esperando motor WASM…
                </div>
            </div>

            <div style="display:grid;gap:12px;grid-template-columns:1fr 1fr;margin-bottom:24px;">
                <button id="btn-run-demo" disabled
                    style="padding:14px;border-radius:12px;border:none;font-weight:700;
                           font-size:0.95rem;cursor:pointer;
                           background:#c9a84c;color:#111827;transition:opacity 0.15s;">
                    Ejecutar caso demo
                </button>
                <button id="btn-engine-info" disabled
                    style="padding:14px;border-radius:12px;border:1px solid #334155;
                           font-weight:700;font-size:0.95rem;cursor:pointer;
                           background:transparent;color:#e5e7eb;transition:opacity 0.15s;">
                    Mostrar engine_info()
                </button>
            </div>

            <div id="result-panel" style="background:rgba(17,24,39,0.92);border:1px solid #334155;
                 border-radius:16px;padding:20px;margin-bottom:20px;min-height:60px;">
                <p style="color:#64748b;margin:0;font-size:0.9rem;">
                    Pulsa «Ejecutar caso demo» para enviar un caso fijo al motor Rust/WASM.
                </p>
            </div>

            <div id="info-panel" style="background:rgba(17,24,39,0.92);border:1px solid #334155;
                 border-radius:16px;padding:20px;margin-bottom:20px;min-height:40px;">
            </div>

            <div id="raw-json-panel" style="margin-bottom:24px;"></div>

            <div style="font-size:0.8rem;color:#64748b;border-top:1px solid #1e293b;padding-top:16px;">
                <p style="margin:0 0 4px;">
                    <strong>Serie:</strong> ISSN 2695-6411 ·
                    <strong>Licencia:</strong> CC BY-NC-ND 4.0 ·
                    <strong>Autor:</strong> Juan Antonio Lloret Egea
                </p>
                <p style="margin:0;">
                    Kotlin organiza la experiencia de uso. Rust evalúa.
                    Python sigue siendo la fuente canónica de verdad.
                </p>
            </div>
        </div>
    """.trimIndent()

    // ── Escuchar evento engine-ready (Watson F.2) ──
    val status = engineStatus()
    if (status != "loading") {
        renderStatus(root, status, engineError())
    }

    window.addEventListener("engine-ready", {
        renderStatus(root, engineStatus(), engineError())
    })

    // ── Botón: ejecutar caso demo (Watson F.3 + F.4) ──
    val btnDemo = document.getElementById("btn-run-demo") as? HTMLButtonElement
    btnDemo?.addEventListener("click", {
        val wasm = wasmModule()
        if (wasm == null || wasm == undefined) return@addEventListener

        val caseJson = buildDemoCase()

        // Llamada real al motor Rust/WASM (Watson F.4)
        val t0 = js("performance.now()") as Double
        val resultJson = wasm.evaluate_immuno1(caseJson) as String
        val t1 = js("performance.now()") as Double

        renderResult(resultJson, t1 - t0)

        // Mostrar JSON bruto para verificación
        val rawPanel = document.getElementById("raw-json-panel")
        if (rawPanel != null) {
            val prettyJson = js("JSON.stringify(JSON.parse(resultJson), null, 2)") as String
            rawPanel.innerHTML = """
                <details style="background:rgba(17,24,39,0.92);border:1px solid #334155;
                         border-radius:16px;padding:16px;">
                    <summary style="cursor:pointer;font-weight:600;font-size:0.9rem;color:#94a3b8;">
                        JSON bruto de respuesta
                    </summary>
                    <pre style="margin-top:12px;font-size:0.8rem;color:#cbd5e1;
                               overflow-x:auto;white-space:pre-wrap;word-break:break-all;">$prettyJson</pre>
                </details>
            """.trimIndent()
        }
    })

    // ── Botón: engine_info() (Watson F.5) ──
    val btnInfo = document.getElementById("btn-engine-info") as? HTMLButtonElement
    btnInfo?.addEventListener("click", {
        val wasm = wasmModule()
        if (wasm == null || wasm == undefined) return@addEventListener

        val infoJson = wasm.engine_info() as String
        renderEngineInfo(infoJson)
    })
}
