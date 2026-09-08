#!/usr/bin/env python3
"""Verificación de sólo lectura del corte G5. No resalva, recalcula ni ejecuta SV."""
from pathlib import Path
import hashlib,json,zipfile,xml.etree.ElementTree as ET
here=Path(__file__).resolve().parent
manifest=json.loads((here/'MANIFIESTO_PRIMER_PARAMETRO_v0.1.json').read_text())
root=next(p for p in here.parents if (p/'dominios/ciberseguridad-inteligente/dominio-04-09-26').is_dir())
for item in manifest['archivos']:
 p=root/item['ruta'];b=p.read_bytes()
 assert len(b)==int(item['bytes']),('TAMANO',item['ruta'])
 assert hashlib.sha256(b).hexdigest()==item['sha256'],('HUELLA',item['ruta'])
v=json.loads((here/'VERIFICACION_PRIMER_PARAMETRO_v0.1.json').read_text())
book=root/manifest['libro_principal'];ns={'x':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with zipfile.ZipFile(book) as z:
 names=[x.attrib['name'] for x in ET.fromstring(z.read('xl/workbook.xml')).findall('x:sheets/x:sheet',ns)]
 assert len(names)==45
 shared=[''.join(x.itertext()) for x in ET.fromstring(z.read('xl/sharedStrings.xml'))]
 def read(name):
  i=names.index(name)+1;r=ET.fromstring(z.read(f'xl/worksheets/sheet{i}.xml'));cells={}
  for c in r.findall('.//x:sheetData/x:row/x:c',ns):
   t=c.attrib.get('t');q=c.find('x:v',ns);x='' if q is None else q.text or ''
   assert t!='e',(name,c.attrib['r'],x)
   if t=='s':x=shared[int(x)]
   elif t=='inlineStr':x=''.join(c.find('x:is',ns).itertext())
   cells[c.attrib['r']]=x
  return cells
 t=read('41_Testigos_G5');g=read('44_Control_G5')
 for i,row in enumerate(v['casos'],5):
  assert t[f'A{i}']==row[0] and t[f'Q{i}']=='PASA'
  for a,b in [('K','N'),('L','O'),('M','P')]:assert t[a+str(i)]==t[b+str(i)],(i,a,b)
 assert len(v['casos'])==28
 for i in range(5,17):assert g[f'C{i}']==g[f'D{i}'],i
 assert read('00_Estatuto')['B18']=='0'
 assert v['ablacion']['proyecciones_iguales'] and v['ablacion']['obligaciones_distintas']
 assert v['sensibilidad'][0]['detectada']
print(json.dumps({'resultado':'PASA_BYTES_Y_CONCORDANCIA_DOCUMENTAL','archivos':len(manifest['archivos']),'hojas':len(names),'testigos':len(v['casos']),'limite':'No acredita verdad de datos, atomicidad semántica, ejecución de SV, captura WUA ni suficiencia de la operación.'},ensure_ascii=False))
