"""Lee el corte publicado: no recalcula/resalva Excel ni ejecuta SV."""
from pathlib import Path
import hashlib,json,zipfile,xml.etree.ElementTree as E
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
NS={'x':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
manifest=json.loads((HERE/'MANIFIESTO_ARCHIVOS_LOTE10_v0.1.json').read_text())
for item in manifest['archivos']:
 path=ROOT/item['ruta'];raw=path.read_bytes()
 assert len(raw)==item['bytes'] and hashlib.sha256(raw).hexdigest()==item['sha256'],item['ruta']
book=HERE.parent/'catalogo-profesional/CATALOGO_CURRICULAR_CIBERSEGURIDAD_v0.5.xlsx'
check=json.loads((HERE/'VERIFICACION_LOTE10_v0.1.json').read_text())
cases=json.loads((HERE/'CASOS_PREVIOS_LOTE10_v0.1.json').read_text())
with zipfile.ZipFile(book) as z:
 names=[s.attrib['name'] for s in E.fromstring(z.read('xl/workbook.xml')).findall('x:sheets/x:sheet',NS)]
 assert len(names)==56
 shared=[''.join(s.itertext()) for s in E.fromstring(z.read('xl/sharedStrings.xml'))] if 'xl/sharedStrings.xml' in z.namelist() else []
 def sheet(name):
  cells={};tree=E.fromstring(z.read(f'xl/worksheets/sheet{names.index(name)+1}.xml'))
  for c in tree.findall('.//x:sheetData/x:row/x:c',NS):
   v=c.find('x:v',NS);v='' if v is None else v.text or ''
   if c.attrib.get('t')=='s':v=shared[int(v)]
   elif c.attrib.get('t')=='inlineStr':v=''.join(c.find('x:is',NS).itertext())
   assert c.attrib.get('t')!='e',(name,c.attrib['r'],v)
   f=c.find('x:f',NS)
   if f is not None:assert len(f.text)<=8192
   cells[c.attrib['r']]=(v,c.attrib.get('t'))
  return cells
 all_sheets={n:sheet(n) for n in names};s=all_sheets['50_Testigos_lote']
 for i,c in enumerate(cases,5):
  assert s[f'A{i}'][0]==c['id'] and s[f'R{i}'][0]=='PASA'
  for col,key in [('O','clase'),('P','tri'),('Q','diagnostico')]:assert s[f'{col}{i}'][0]==c['esperado'][key]
  assert s[f'H{i}'][0]==c['valor1'] and s[f'I{i}'][0]==c['valor2']
 c=all_sheets['54_Control_lote']
 for r in range(5,19):assert c[f'C{r}'][0]==c[f'D{r}'][0]
 assert all_sheets['00_Estatuto']['B18'][0]=='0'
 assert len({all_sheets['46_Registro_diez'][f'B{r}'][0] for r in range(5,15)})==10
assert len(check['ablaciones'])==9 and all(a['proyecciones_iguales'] and a['explicaciones_distintas'] and a['mutante_detectado'] for a in check['ablaciones'])
print(json.dumps(dict(archivos=len(manifest['archivos']),hojas=len(names),parametros=10,testigos_nuevos=len(cases),ablaciones=9,resultado='PASA_DOCUMENTAL'),ensure_ascii=False))
