"""Verificación de sólo lectura del corte curricular v0.2; Python 3 estándar.

No recalcula fórmulas, no ejecuta testigos educativos, no resalva el Excel
y no atribuye suficiencia semántica a los resultados estructurales.
"""
from pathlib import Path
import hashlib
import json
import xml.etree.ElementTree as ET
import zipfile

here = Path(__file__).resolve().parent
root = here.parents[3]
manifest = json.loads((here / 'MANIFIESTO_CURRICULAR_v0.2.json').read_text())
for item in manifest['archivos']:
    path = root / item['ruta']
    data = path.read_bytes()
    assert len(data) == item['bytes'], ('TAMAÑO', item['ruta'])
    assert hashlib.sha256(data).hexdigest() == item['sha256'], ('HUELLA', item['ruta'])

ns = {'x': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with zipfile.ZipFile(root / manifest['principal']) as archive:
    workbook = ET.fromstring(archive.read('xl/workbook.xml'))
    names = [node.attrib['name'] for node in workbook.findall('x:sheets/x:sheet', ns)]
    assert len(names) == 25 and names[15] == '15_Base_universitaria'
    formulas = 0
    for i in range(1, 26):
        tree = ET.fromstring(archive.read(f'xl/worksheets/sheet{i}.xml'))
        assert tree.find('x:tableParts', ns) is not None
        for cell in tree.findall('.//x:sheetData/x:row/x:c', ns):
            assert cell.attrib.get('t') != 'e', (names[i-1], cell.attrib['r'])
            if cell.find('x:f', ns) is not None:
                formulas += 1
                assert cell.find('x:v', ns) is not None
    assert formulas == 3275
    base = ET.fromstring(archive.read('xl/worksheets/sheet16.xml'))
    cells = {c.attrib['r']: c for c in base.findall('.//x:sheetData/x:row/x:c', ns)}
    for row in range(5, 45):
        for column in ['A', 'B', 'D', 'F', 'M']:
            assert cells[f'{column}{row}'].attrib.get('t') in ['str', 's', 'inlineStr']

print(json.dumps({
    'archivos_verificados': len(manifest['archivos']),
    'hojas': len(names), 'formulas_con_resultado_guardado': formulas,
    'resultado': 'PASA_EN_ALCANCE_DE_IDENTIDAD_Y_ESTRUCTURA',
    'limites': 'No recalcula ni resalva; no prueba semántica, aprendizaje o ejecución operacional.'
}, ensure_ascii=False, indent=2))
