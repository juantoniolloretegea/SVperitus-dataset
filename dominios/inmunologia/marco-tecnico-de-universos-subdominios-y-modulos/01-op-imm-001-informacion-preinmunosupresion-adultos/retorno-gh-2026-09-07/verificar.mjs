// Verificador documental externo. No analiza SV, no transduce clínica, no es un compilador.
// Ejecutar: node verificar.mjs --inmunologia /corte/imm --lenguaje /corte/lsv
// Los directorios contienen los archivos de fuentes.json en sus rutas de repositorio.
import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {fileURLToPath,pathToFileURL} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const hash=b=>createHash('sha256').update(b).digest('hex');
const gitBlob=b=>createHash('sha1').update(Buffer.from('blob '+b.length+'\0')).update(b).digest('hex');
const bytes=n=>fs.readFileSync(path.join(here,n));
const load=n=>JSON.parse(bytes(n));
const roots={imm:process.argv[process.argv.indexOf('--inmunologia')+1],lsv:process.argv[process.argv.indexOf('--lenguaje')+1]};
assert(process.argv.includes('--inmunologia')&&process.argv.includes('--lenguaje'),'Faltan cortes de fuentes');
const f=load('fuentes.json'),d=load('contraste.json'),w=load('testigos.json');
const copy=x=>structuredClone(x);
function validateSource(b,s){assert.equal(b.length,s.bytes,'LongitudFuente');assert.equal(hash(b),s.sha256,'HuellaFuente');assert.equal(gitBlob(b),s.git_blob,'BlobFuente');}
const sourceTexts=new Map();
for(const s of f.sources){const b=fs.readFileSync(path.join(roots[s.local_prefix],s.path));validateSource(b,s);sourceTexts.set(s.id,b.toString('utf8'));}
assert.equal(f.input_imm.commit,'d4d6c81cb9aab5194abc8e61212c0d63877a0b9c');
assert.equal(f.input_lsv.commit,'bc3b22c9e9319e8f191390c8cfe9fa1577904d87');
assert.equal(new Set(f.sources.map(x=>x.id)).size,44);
const expectedParams=[...sourceTexts.get('IMM-CLIN').matchAll(/^#### \d+\. .+? \(`(PAR-[A-Z0-9-]+)`\)/gm)].map(m=>m[1]);
const expectedOwners=new Map([...sourceTexts.get('IMM-G6').matchAll(/^\| `(PAR-[A-Z0-9-]+)` \| `(M-[A-Z0-9-]+)` \|/gm)].map(m=>[m[1],m[2]]));
const sourceRelation=sourceTexts.get('LSV-VAL').split('### 5.1')[1].split('### 5.2')[0].split('\n').filter(l=>/^\| `REQ-IMM-SV-\d/.test(l)).map(l=>({g10:l.match(/REQ-IMM-SV-\d{3}/)[0],targets:l.match(/REQ-IMM-LSV-\d{3}/g)}));
const sourceRequests=[...sourceTexts.get('IMM-REQ').matchAll(/^\d+\. `(REQ-IMM-LSV-\d{3})`: (.+)$/gm)].map(m=>({id:m[1],text:m[2]}));
const sourceG10=[...sourceTexts.get('IMM-G10').matchAll(/REQ-IMM-SV-\d{3}/g)].map(m=>m[0]);
function validatePackage(v){
 assert.equal(v.scope,'OP-IMM-001 / Q0 v0','Perimetro');
 assert.equal(v.input_imm,f.input_imm.commit,'CorteIMM');assert.equal(v.input_lsv,f.input_lsv.commit,'CorteLSV');
 assert.deepEqual(v.crosswalk.map(r=>({g10:r.g10,targets:r.correspondencia_recibida})),sourceRelation,'CruceRecibido');
 assert(v.crosswalk.every(r=>sourceG10.includes(r.g10)),'G10Inexistente');
 assert.deepEqual(v.inverse.map(r=>({id:r.id,text:r.formulacion})),sourceRequests,'SolicitudesRecibidas');
 for(const r of v.crosswalk){assert.deepEqual(r.enlaces_revisados.map(x=>x.lsv),r.correspondencia_recibida,'EnlaceOmitido');for(const e of r.enlaces_revisados){assert(['EQUIVALENCIA_NORMATIVA_ACOTADA','REFINAMIENTO','COBERTURA_PARCIAL'].includes(e.relacion));assert(e.justificacion.length>25);}}
 for(const r of v.inverse){assert.deepEqual(r.g10,v.crosswalk.filter(c=>c.correspondencia_recibida.includes(r.id)).map(x=>x.g10),'CruceInverso');assert(r.g10.length||v.independent_lsv.includes(r.id),'SolicitudSinCobertura');assert(w.specified.some(x=>x.id===r.testigo)||w.witnesses.some(x=>x.id===r.testigo),'TestigoInexistente');}
 const p=v.profile;assert.equal(p.operation,'OP-IMM-001');assert.equal(p.q0,'v0');
 assert.deepEqual(p.parameters.map(x=>x.id),expectedParams,'InventarioParametros');
 assert.equal(new Set(p.parameters.map(x=>x.id)).size,27,'IdentidadDuplicada');
 for(const q of p.parameters){assert.equal(q.owner,expectedOwners.get(q.id),'Propietario');assert(sourceTexts.get(q.regla_locator.source)?.includes(q.regla),'ReglaInexistente');assert(q.definicion_clinica.length>100);assert(q.necesidad_de_entrada.length>20);assert(q.perdida.distincion.length>5);assert.equal(q.instancia_celular,'NO_CONSTITUIDA','CelulaNoConstituida');}
 assert.deepEqual(p.groups.map(g=>g.parameters.length),[6,1,3,2,6,9],'Agrupaciones');
 assert.deepEqual(p.groups.flatMap(g=>g.parameters),expectedParams,'CoberturaDeGrupos');
 assert.deepEqual(p.cells,[],'CelulaFabricada');assert.equal(p.req_011,'U_NO_DECIDIDO');
 assert.equal(p.clinical_execution,false,'EjecucionClinicaNoProbada');
 assert.deepEqual(p.outputs.map(x=>x.id),['PERFIL_PREDECISIONAL_SELLADO','U_CRITICA_NO_CERRADA','FUERA_DE_ALCANCE','ABSTENERSE_O_ESCALAR'],'Codominio');
 assert.equal(p.output_when_technical_failure,'NINGUNA_SALIDA_CLINICA; sólo EJECUCION_TECNICA_NO_VALIDA','FalloComoClinica');
 assert.equal(p.parameters.filter(x=>x.configuracion==='REGISTRO_DE_ADMISION_VACIO').length,4,'RegistrosVacios');
 assert.equal(p.g9,'NO_OBSERVABLE');assert.equal(p.datasets_admissible,0);
 assert.equal(v.f_if_applicability.length,6,'Familias');
 const cases=JSON.parse(sourceTexts.get('LSV-CASOS'));
 for(const a of v.f_if_applicability){assert.equal(Object.keys(a.consultas).length,3);assert(a.parametros.every(id=>expectedParams.includes(id)),'ConsumoFueraDeA0');}
 for(const a of v.f_if_applicability){assert.deepEqual(Object.keys(a.consultas),cases.families.find(t=>t.id===a.id)?.operations.map(x=>x.id),'ConsultaFIFInexistente');}
}
validatePackage(d);
const observerSource=f.sources.find(s=>s.id==='LSV-OBS');
const observer=await import(pathToFileURL(path.resolve(roots.lsv,observerSource.path)).href);
const received=observer.campaign();
assert.equal(observer.pretty(received),sourceTexts.get('LSV-EVID'),'EvidenciaFIF');
const outcomes=[];
for(const t of w.witnesses){
 assert(t.parameters.every(p=>expectedParams.includes(p)),'ParametroTestigo');
 assert(t.sources.every(s=>sourceTexts.has(s)),'FuenteTestigo');
 assert(t.requirements.every(s=>sourceG10.includes(s)),'RequisitoTestigo');
 assert.equal(t.domain.states.length,2);const [x,y]=t.domain.states;
 const H=p=>{const v=copy(p);delete v.detail;return observer.encode(v);};
 for(const s of [x,y]){
  assert.deepEqual(observer.recover(observer.encode(s.packet),t.operation),s.expected,'RecuperacionDocumental');
  assert.deepEqual(observer.recover(H(s.packet),t.control.operation),t.control.expected,'ControlConPerdida');
  assert.throws(()=>observer.recover(H(s.packet),t.operation),/RepresentationInsufficient/,'PerdidaOculta');
 }
 assert(H(x.packet).equals(H(y.packet)),'HDesigual');
 assert(!observer.encode(x.expected).equals(observer.encode(y.expected)),'OraculoSinDistincion');
 outcomes.push({id:t.id,operation:t.operation.id,scope:'X_DOCUMENTAL_FINITO_ENUMERADO_NO_X_Q0_CLINICO',positive:'RECUPERACION_EXACTA_DESDE_F0',negative:'F1_INSUFICIENTE_PARA_ESTA_CONSULTA',control:'CONTEXTO_RECUPERABLE_DESDE_F1',x:{bytes:observer.encode(x.packet).length,sha256:hash(observer.encode(x.packet)),expected:x.expected},y:{bytes:observer.encode(y.packet).length,sha256:hash(observer.encode(y.packet)),expected:y.expected},H:{utf8:H(x.packet).toString('utf8'),sha256:hash(H(x.packet))}});
}
const attacks=[];
function reject(id,reason,fn){assert.throws(fn,undefined,'AtaqueNoDetectado:'+id);attacks.push({id,reason,result:'RECHAZADO_POR_VERIFICADOR_DOCUMENTAL'});}
function mutated(id,reason,mutate){reject(id,reason,()=>{const x=copy(d);mutate(x);validatePackage(x);});}
mutated('NEG-01','Omitir una necesidad G10',x=>x.crosswalk.pop());
mutated('NEG-02','Omitir una formulación LSV',x=>x.inverse.pop());
mutated('NEG-03','Eliminar un enlace múltiple',x=>x.crosswalk[4].enlaces_revisados.pop());
mutated('NEG-04','Duplicar un parámetro para conservar el recuento',x=>x.profile.parameters[1].id=x.profile.parameters[0].id);
mutated('NEG-05','Cambiar propietario conservando nombres',x=>x.profile.parameters[0].owner=x.profile.parameters[6].owner);
mutated('NEG-06','Inventar una regla',x=>x.profile.parameters[0].regla='REGLA_NO_EXISTENTE');
mutated('NEG-07','Constituir célula por nueve miembros',x=>x.profile.cells.push({n:9,b:3}));
mutated('NEG-08','Cerrar REQ-IMM-SV-011 por inventario',x=>x.profile.req_011='DECIDIDO');
mutated('NEG-09','Introducir quinto resultado clínico',x=>x.profile.outputs.push({id:'EJECUCION_TECNICA_NO_VALIDA'}));
mutated('NEG-10','Convertir fallo en U',x=>x.profile.output_when_technical_failure='U');
mutated('NEG-11','Afirmar ejecución clínica desde observador',x=>x.profile.clinical_execution=true);
mutated('NEG-12','Ampliar universo',x=>x.scope='INMUNOLOGIA_UNIVERSAL');
mutated('NEG-13','Acreditar G9 desde testigos sintéticos',x=>x.profile.datasets_admissible=1);
mutated('NEG-14','Asignar consumidor citométrico inexistente',x=>x.f_if_applicability[1].parametros.push('PAR-CITOMETRIA-INVENTADO'));
const s0=f.sources[0],b0=fs.readFileSync(path.join(roots[s0.local_prefix],s0.path));
reject('NEG-15','Fuente truncada',()=>validateSource(b0.subarray(0,-1),s0));
const flipped=Buffer.from(b0);flipped[0]^=1;
reject('NEG-16','Fuente de igual longitud con contenido sustituido',()=>validateSource(flipped,s0));
reject('NEG-17','Homónimos JSON eliminados silenciosamente',()=>observer.decode(Buffer.from('{"a":1,"a":2}')));
reject('NEG-18','UTF-8 inválido',()=>observer.decode(Buffer.from([0xff])));
const first=w.witnesses[0],domain=first.domain.states;
reject('NEG-19','Configuración del banco ausente',()=>observer.observe(observer.encode(domain[0].packet),domain,null));
assert.deepEqual(observer.observe(Buffer.from('{'),domain),{kind:'CaptureFailure'});
assert.deepEqual(observer.observe(observer.encode({...domain[0].packet,foreign:true}),domain),{kind:'NotAdmitted'});
assert(!Object.hasOwn(observer.observe(Buffer.from('{'),domain),'tri'));
const report={schema:'EVIDENCIA-GH/1',execution:'OBSERVADOR_DOCUMENTAL_EXTERNO',clinical_execution:false,environment:{node:process.version,platform:process.platform,arch:process.arch},inputs:['fuentes.json','contraste.json','testigos.json','verificar.mjs'].map(n=>({file:n,bytes:bytes(n).length,sha256:hash(bytes(n))})),cuts:{imm:f.input_imm.commit,lsv:f.input_lsv.commit},identity:{verified_sources:f.sources.length,git_blobs_and_sha256:'COINCIDEN',g10:15,lsv:44,links:81,lsv_without_exclusive_parent:11,parameters:27,groups:[6,1,3,2,6,9]},f_if:{...received.totals,evidence_sha256:hash(Buffer.from(observer.pretty(received))),unchanged_expected:'COINCIDE_BYTE_A_BYTE'},documentary:{pairs:8,states:16,positive_recoveries:16,loss_witnesses:8,loss_rejections:16,positive_controls_after_reduction:16,invalid_capture_and_non_admission_controls:2,negative_mutations:attacks.length,results:outcomes,attacks},specified:w.specified.map(s=>({id:s.id,status:s.status})),verdict:'FIDELIDAD_Y_PERDIDAS_DOCUMENTALES_ACOTADAS; SUFICIENCIA_Q0_NO_ACREDITADA',req_011:'U_NO_DECIDIDO'};
process.stdout.write(JSON.stringify(report,null,2)+'\n');
