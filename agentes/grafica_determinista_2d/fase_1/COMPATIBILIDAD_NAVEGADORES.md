# Matriz de soporte de navegadores — AE-GD2-SV Fase 1

## Soporte oficial

- Google Chrome: estable actual y anterior
- Microsoft Edge: estable actual y anterior

## Soporte verificado adicional

- Mozilla Firefox: estable actual y anterior
- Opera: estable actual y anterior

## No comprometido todavía

- Safari y otros navegadores no ensayados materialmente

## Funciones mínimas requeridas

- File API
- Blob y descarga local
- URL.createObjectURL
- Canvas 2D
- SVG embebido
- Web Workers
- IndexedDB

## Batería mínima de ensayo por navegador

1. carga local de PNG/JPEG/SVG
2. cuarentena local finita
3. construcción de `UserContextPacket`
4. traducción a `GraphicIntentDraft`
5. confirmación y paso a `GraphicIntentConfirmed`
6. cálculo de `C_frame^25`
7. cálculo de `C_gob^25`
8. render poligonal SVG
9. generación de informe HTML/JSON/CSV
10. descarga del bundle ZIP
