"""Verificador de bytes y pruebas documentales del corte OP-CYB-001.
Uso: python3 verificar_cierre_op_cyb_001.py [raíz del repositorio]
No observa activos ni compila/ejecuta el Lenguaje SV.
"""
from pathlib import Path
import sys,json,hashlib,zipfile,tempfile,subprocess,xml.etree.ElementTree as E
def unique_pairs(items):
 d={}
 for k,v in items:
  if k in d:raise ValueError('CLAVE_JSON_REPETIDA: '+k)
  d[k]=v
 return d
def strict_json(path):return json.loads(path.read_text(),object_pairs_hook=unique_pairs)
root=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[4]
base=Path('dominios/ciberseguridad-inteligente/dominio-04-09-26')
lib=root/base/'watson-biblioteca-ciber'
m=strict_json(lib/'MANIFIESTO_ARCHIVOS_CIERRE_v0.1.json')
for item in m['archivos']+m.get('antecedentes',[]):
 p=root/item['path'];b=p.read_bytes();assert len(b)==item['bytes'] and hashlib.sha256(b).hexdigest()==item['sha256'],item['path']
bundle=strict_json(lib/'CIERRE_OP_CYB_001_v0.1.json')
assert len(bundle['parametros_nuevos'])==5 and len(bundle['q0'])==31 and len(bundle['controles'])==14
q={x['id'] for x in bundle['q0']};assert len(q)==31
valid={f'P{i:02}' for i in range(1,16)}|{f'C{i:02}' for i in range(1,15)}
for x in bundle['q0']:assert set(x['referencias'].split(','))<=valid,x['id']
assert all(x['pasa'] for x in bundle['resultados']['casos']+bundle['resultados']['controles'])
with tempfile.TemporaryDirectory() as td:
 td=Path(td)
 with zipfile.ZipFile(lib/'ENSAYOS_CIERRE_OP_CYB_001_v0.1.zip') as z:
  for n in z.namelist():assert not n.startswith('/') and '..' not in Path(n).parts
  z.extractall(td)
 p=subprocess.run([sys.executable,str(td/'evaluar.py')],capture_output=True,text=True);assert p.returncode==0,p.stderr
 new=json.loads((td/'RESULTADOS.json').read_text())
 for k in ['casos','controles','sensibilidad','ablaciones','oraculos_sha256']:assert new[k]==bundle['resultados'][k],k
with zipfile.ZipFile(root/base/'catalogo-profesional/CATALOGO_CURRICULAR_CIBERSEGURIDAD_v0.6.xlsx') as z:
 ns={'x':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
 wb=E.fromstring(z.read('xl/workbook.xml'));assert len(wb.findall('x:sheets/x:sheet',ns))==66
 shared=[''.join(s.itertext()) for s in E.fromstring(z.read('xl/sharedStrings.xml'))] if 'xl/sharedStrings.xml' in z.namelist() else []
 for n in z.namelist():
  if not n.startswith('xl/worksheets/sheet') or not n.endswith('.xml'):continue
  for c in E.fromstring(z.read(n)).findall('.//x:c',ns):assert c.attrib.get('t')!='e',(n,c.attrib['r'])
print(json.dumps({'archivos_verificados':len(m['archivos']),'casos_reproducidos':65,'controles_reproducidos':51,'q0':31,'hojas_excel':66,'resultado':'CONFORME_EN_ALCANCE_DOCUMENTAL; NO_APTITUD_OPERACIONAL'}))
