import kotlinx.browser.document

fun main() {
    val root = document.getElementById("root")
    root?.innerHTML = """
        <section style="padding:24px;font-family:system-ui,sans-serif;">
            <h1>SVperitus — IMMUNO-1 Kotlin Client</h1>
            <p>Cliente Kotlin inicial cargado correctamente.</p>
            <p>Próximo paso: conectar esta interfaz con el motor Rust/WASM ya existente.</p>
        </section>
    """.trimIndent()
}
