#!/usr/bin/env python3
"""Verifica por lectura el corte candidato. No recalcula ni escribe Excel.
Uso: python verificar_corte.py [directorio watson-biblioteca-ciber]
Salida: informe JSON en stdout; código no cero si falla una comprobación.
No produce una proyección del catálogo ni prueba suficiencia semántica.
"""
from pathlib import Path
import collections, gzip, hashlib, io, json, re, sys, tarfile, zipfile
import xml.etree.ElementTree as ET

base=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent
book=base.parent/'catalogo-profesional/CATALOGO_PROFESIONAL.xlsx'
sha=lambda b:hashlib.sha256(b).hexdigest()
NS={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
issues=[]
def check(test,message):
    if not test:issues.append(message)
def need(test,message):
    if not test:raise ValueError(message)

original=book.read_bytes();archive=zipfile.ZipFile(io.BytesIO(original))
shared=[]
if 'xl/sharedStrings.xml' in archive.namelist():
    shared=[''.join(n.itertext()) for n in ET.fromstring(archive.read('xl/sharedStrings.xml')).findall('s:si',NS)]
wb=ET.fromstring(archive.read('xl/workbook.xml'));relations=ET.fromstring(archive.read('xl/_rels/workbook.xml.rels'))
targets={r.attrib['Id']:r.attrib['Target'] for r in relations}
sheets={};formula_count=0
for sheet in wb.find('s:sheets',NS):
    target=targets[sheet.attrib['{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id']]
    path=target.lstrip('/') if target.startswith('/') else 'xl/'+target
    root=ET.fromstring(archive.read(path));cells={}
    for c in root.findall('.//s:c',NS):
        kind=c.get('t','n');v=c.findtext('s:v',default='',namespaces=NS)
        if kind=='s':v=shared[int(v)]
        elif kind=='inlineStr':v=''.join(c.find('s:is',NS).itertext())
        check(kind!='e',f'Error Excel: {sheet.attrib["name"]}!{c.get("r")}={v}')
        if c.find('s:f',NS) is not None:
            formula_count+=1;check(c.find('s:v',NS) is not None,'Fórmula sin valor calculado: '+c.get('r'))
        cells[c.get('r')]=(v,kind)
    sheets[sheet.attrib['name']]=cells
need(len(sheets)==14,'Cantidad de hojas inesperada')
def val(sh,cell):return sheets[sh].get(cell,('',None))[0]
def records(sh,ncols):
    rows=[];row=5
    while val(sh,'A'+str(row)):
        rows.append([val(sh,chr(65+i)+str(row)) for i in range(ncols)]);row+=1
    return rows

tables=[p for p in archive.namelist() if p.startswith('xl/tables/') and p.endswith('.xml')]
check(len(tables)==14,'Tablas incompletas')
for p in tables:check(ET.fromstring(archive.read(p)).find('s:autoFilter',NS) is not None,'Tabla sin filtro: '+p)
for r in range(5,15):check(val('11_Controles','C'+str(r))=='0' and val('11_Controles','E'+str(r))=='PASA','Control no superado: '+str(r))
check(val('11_Controles','C20')=='0','Restauración final incorrecta')
for sh,cols in [('02_Custodia',['D','G','H']),('03_Rector',['A','J']),('04_TKS',['A','H']),('08_Trazas',['A','H','I','J'])]:
    for c,(v,kind) in sheets[sh].items():
        column=re.match(r'[A-Z]+',c).group();row=int(re.search(r'\d+',c).group())
        if row>=5 and column in cols and v:check(kind in ['str','s','inlineStr'],f'Dato exacto convertido a número: {sh}!{c}')

nice_raw=gzip.decompress((base/'NICE_2.2.0.json.gz').read_bytes());nice=json.loads(nice_raw)
check(sha(nice_raw)=='3ad1d9d7e0d6b32895cb569f86c3bc05af2937a68e96eab4d1c9b3d9fa6e575e','JSON NICE original alterado')
elements={r['element_identifier']:r for r in nice['elements']}
roles=records('03_Rector',12);tks=records('04_TKS',10);comps=records('05_Complementos',12);traces=records('08_Trazas',12);rels=records('13_Relaciones_NICE',6)
check({r[0] for r in roles}=={r['element_identifier'] for r in nice['elements'] if r['element_type'] in ['work_role','competency_area']},'Roles/áreas incompletos o añadidos')
for r in roles:check(r[2]==elements[r[0]]['title'] and r[3]==elements[r[0]]['text'],'Original de rol distinto: '+r[0])
for r in tks:check(r[2]==elements[r[0]]['text'],'Original TKS distinto: '+r[0])
fragment_data=json.loads((base/'EXTRACTOS_DE_FUENTES.json').read_text());fragments={r['extraccion']:r for r in fragment_data['fragmentos']}
check(len(fragments)==123,'Fragmentos no únicos o incompletos')
for r in traces:
    if r[6]=='JSON_ORIGINAL_UTF8':
        off=int(r[7]);n=int(r[8]);b=nice_raw[off:off+n];check(sha(b)==r[9],'Huella de objeto NICE distinta: '+r[0]);check(json.loads(b)['element_identifier']==r[0],'Identidad NICE distinta: '+r[0])
    else:
        f=fragments[r[0]];b=f['texto_original'].encode();check(sha(b)==r[9]==f['sha256_utf8'],'Huella de fragmento distinta: '+r[0]);check(str(len(b))==r[8],'Longitud de fragmento distinta: '+r[0])
for r in comps:
    f=fragments[r[0]];check(r[1]==f['fuente'] and r[2]==f['captura'] and r[3]==f['localizador_de_lectura'],'Procedencia de complemento distinta: '+r[0])
    check(' '.join(r[4].casefold().split())==' '.join(f['texto_original'].casefold().split()),'Rótulo original normalizado distinto: '+r[0])
selected={r[0] for r in roles+tks}
expected={(r['source_element_identifier'],r['dest_element_identifier'],r['relationship_identifier'],r['provenance_doc_identifier']) for r in nice['relationships'] if r['source_element_identifier'] in selected and r['dest_element_identifier'] in selected}
check({tuple(r[1:5]) for r in rels}==expected,'Relaciones oficiales alteradas o incompletas')

receipt=json.loads((base/'RECEPCION_FILA7.json').read_text());b=(base/receipt['archivo_preservado']).read_bytes();check(sha(b)==receipt['zip_sha256'],'ZIP del relevo alterado');check(str(len(b))==receipt['zip_bytes'],'Tamaño ZIP distinto')
z=zipfile.ZipFile(io.BytesIO(b));tarbytes=z.read('paquete/fila7-fuentes.tar.gz');check(sha(tarbytes)==receipt['tar_sha256'],'Tar de relevo alterado')
check(sha(z.read('ejecucion/gh.json'))==receipt['gh_json_sha256'],'gh.json distinto')
t=tarfile.open(fileobj=io.BytesIO(tarbytes),mode='r:gz');members={m.name.removeprefix('./'):m for m in t.getmembers() if m.isfile()}
def read_member(name):return t.extractfile(members[name]).read()
inventory=read_member('fuentes/INVENTARIO.sha256').decode();n=0
for line in inventory.splitlines():
    h,path=line.split(maxsplit=1);b=read_member('fuentes/'+path.lstrip('*').removeprefix('./'));check(sha(b)==h,'Inventario de relevo: '+path);n+=1
check(n==228,'Inventario de fuentes incompleto')
check(sha(read_member('fuentes/tests/row7_gh/resolucion.json'))==receipt['matriz_resolucion_sha256'],'Matriz histórica distinta')
check(book.read_bytes()==original,'El libro cambió durante su lectura')
checks=json.loads((base/'PRUEBAS_FORMULAS.json').read_text());check(checks['baseline']==checks['final']==0 and len(checks['tests'])==5 and all(r['incidencias']>0 and r['restaurado']==0 for r in checks['tests']),'Registro de mutaciones incompleto')
result={'naturaleza':'Verificación de lectura; no proyección ni recálculo del catálogo','resultado':'PASA' if not issues else 'FALLA','xlsx_bytes':str(len(original)),'xlsx_sha256':sha(original),'hojas':len(sheets),'tablas_con_filtro':len(tables),'formulas_con_cache':formula_count,'roles_y_areas':len(roles),'TKS':len(tks),'complementos':len(comps),'trazas':len(traces),'relaciones_NICE':len(rels),'inventario_relevo_verificado':n,'mutaciones_detectadas_y_restauradas':5,'incidencias':issues,'limites':['No prueba verdad o suficiencia de las síntesis','No establece aplicabilidad jurídica','No constituye ni ejecuta un universo','No recalcula las fórmulas: comprueba sus valores exportados y registro de sensibilidad previo']}
print(json.dumps(result,ensure_ascii=False,indent=2));sys.exit(1 if issues else 0)
