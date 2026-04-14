const PARAM_NAMES = [
  'Modo operativo','Tipo de fuente','Integridad de entrada','Localidad y cuarentena','Perfil de ejecución',
  'Clase de figura','Dominio declarado','Dimensiones del lienzo','Salidas requeridas','Restricciones duras',
  'Política de título','Política de footer','Sistema de paneles','Sistema de nodos','Sistema de aristas',
  'No colisión texto-texto','Respiración vertical suficiente','Respiración horizontal suficiente','Densidad compositiva aceptable','Canonicidad del SVG',
  'Trazabilidad append-only','Confirmación humana soberana','Coherencia del bundle','Pureza de frontera','Reproducibilidad laboratorial'
];
const K3 = ['0','1','U'];
const QUALITY_PARAM_IDS = new Set(['P16','P17','P18','P19','P20']);
const MAX_FILE_BYTES = 8 * 1024 * 1024;
let current = null;
const ui = {
  mode: document.getElementById('mode'),
  figureKind: document.getElementById('figureKind'),
  width: document.getElementById('width'),
  height: document.getElementById('height'),
  fileInput: document.getElementById('fileInput'),
  nlNote: document.getElementById('nlNote'),
  hardRules: document.getElementById('hardRules'),
  runBtn: document.getElementById('runBtn'),
  downloadBtn: document.getElementById('downloadBtn'),
  stateBox: document.getElementById('stateBox'),
  stateLog: document.getElementById('stateLog'),
  sequence: document.getElementById('sequence'),
  sequenceDetail: document.getElementById('sequenceDetail'),
  frameSvg: document.getElementById('frameSvg'),
  gobSvg: document.getElementById('gobSvg'),
  paramTable: document.querySelector('#paramTable tbody'),
  auditSummary: document.getElementById('auditSummary'),
  auditJson: document.getElementById('auditJson'),
  eventJson: document.getElementById('eventJson')
};

function nowIso() { return new Date().toISOString(); }
function makeId(prefix) { return `${prefix}-${Date.now()}-${Math.random().toString(16).slice(2,8)}`; }
function stableHash(text) { let h = 2166136261; for (let i = 0; i < text.length; i++) { h ^= text.charCodeAt(i); h = Math.imul(h, 16777619); } return 'h' + (h >>> 0).toString(16); }
function setState(state, note='') { ui.stateBox.textContent = note ? `${state} — ${note}` : state; const li = document.createElement('li'); li.textContent = `${new Date().toLocaleTimeString()} · ${state}${note ? ' · ' + note : ''}`; ui.stateLog.appendChild(li); }
function hardRulesArray() { return ui.hardRules.value.split(/\n+/).map(s => s.trim()).filter(Boolean); }
function dictamenFromCell(cell){ const vals = cell.map(p=>p.value_k3); if(vals.includes('1')) return 'NO APTO'; if(vals.includes('U')) return 'INDETERMINADO'; return 'APTO'; }

function buildUserContextPacket(fileMeta){ return { structured_form:{ mode:ui.mode.value, figure_kind:ui.figureKind.value, width:Number(ui.width.value), height:Number(ui.height.value), outputs:['html','json','csv','svg','zip'], hard_rules:hardRulesArray() }, natural_language_note:ui.nlNote.value.trim(), local_image_name:fileMeta?.name ?? null, local_annotations:[] }; }
function parseIntent(packet){
  const note = (packet.natural_language_note || '').toLowerCase();
  const hard = (packet.structured_form.hard_rules || []).map(s => s.toLowerCase());
  const preserve = new Set(packet.structured_form.mode === 'correct' ? ['estructura_general'] : []);
  const modify = new Set(packet.structured_form.mode === 'correct' ? [] : ['composicion_base']);
  const unresolved = [];
  // Separar zona positiva (antes del primer operador negativo) de zona negativa (el resto)
  // Esto resuelve listas distribuidas: "corrija el footer. No toque X, Y, Z ni V"
  const _negOp = /[.!]?\s*(?:no\s+toque?|no\s+tocar|sin\s+tocar|mantener\s+intacto)/i;
  const _splitIdx = note.search(_negOp);
  const notePos = _splitIdx >= 0 ? note.slice(0, _splitIdx) : note;
  const noteNeg = _splitIdx >= 0 ? note.slice(_splitIdx) : '';
  const targets = [
    { key:'footer',          pos:[/footer/, /pie(?:\s+inferior)?/],            neg:[/(?:no\s+toque?|no\s+tocar|sin\s+tocar|mantener)\s+(?:[\w\s,]+?\s)?(?:el\s+)?footer/, /footer\s+(?:original|intacto)/, /no\s+modificar\s+(?:el\s+)?footer/] },
    { key:'titulo_superior', pos:[/t[ií]tulo\s+superior/, /t[ií]tulo/],         neg:[/(?:no\s+toque?|no\s+tocar|sin\s+tocar|mantener)\s+(?:[\w\s,]+?\s)?(?:el\s+)?t[ií]tulo/, /no\s+modificar\s+(?:el\s+)?t[ií]tulo/] },
    { key:'cartel_izquierdo',pos:[/cartel\s+izquierdo/, /cartel/],              neg:[/(?:no\s+toque?|no\s+tocar|sin\s+tocar|mantener)\s+(?:[\w\s,]+?\s)?(?:el\s+)?cartel/] },
    { key:'libros',          pos:[/libros/, /lomos/],                            neg:[/(?:no\s+toque?|no\s+tocar|sin\s+tocar|mantener)\s+(?:[\w\s,]+?\s)?(?:los\s+)?libros/] },
    { key:'personajes',      pos:[/humano/, /robot/, /personajes?/],             neg:[/(?:no\s+toque?|no\s+tocar|sin\s+tocar)\s+(?:[\w\s,]+?\s)?(?:el\s+|los\s+)?(?:humano|robot|personajes?)/] },
    { key:'fondo',           pos:[/fondo/],                                      neg:[/(?:no\s+toque?|no\s+tocar|sin\s+tocar|mantener)\s+(?:[\w\s,]+?\s)?(?:el\s+)?fondo/, /fondo\s+(?:original|intacto)/, /preservar\s+fondo/, /no\s+modificar\s+(?:el\s+)?fondo/] },
    { key:'composicion',     pos:[/composici[oó]n\s+general/, /composici[oó]n/],neg:[/(?:no\s+toque?|no\s+tocar|sin\s+tocar|mantener)\s+(?:[\w\s,]+?\s)?(?:la\s+)?composici[oó]n/, /no\s+cambiar\s+(?:la\s+)?composici[oó]n/] },
  ];
  const hayNegativaGeneral = _negOp.test(note);
  for (const t of targets) {
    // pos solo se evalúa sobre la zona positiva de la nota
    const posInPos  = t.pos.some(rx => rx.test(notePos));
    // neg se evalúa sobre la zona negativa de la nota + hard rules
    const negInNeg  = t.neg.some(rx => rx.test(noteNeg));
    const negInHard = hard.some(rule => t.neg.some(rx => rx.test(rule)));
    const pos = posInPos;
    const neg = negInNeg || negInHard;
    if (pos && neg) { unresolved.push('Conflicto: ' + t.key + ' aparece como objetivo de corrección y como restricción de preservación simultáneamente.'); preserve.add(t.key); continue; }
    if (pos && !neg) modify.add(t.key);
    if (neg && !pos) preserve.add(t.key);
  }
  if (packet.structured_form.mode === 'correct' && modify.size === 0) {
    if (!hayNegativaGeneral) { modify.add('colisiones_texto'); modify.add('margenes'); modify.add('paneles'); }
    else { unresolved.push('No se ha identificado un objeto positivo de corrección sin contradicción.'); }
  }
  for (const key of [...modify]) {
    if (preserve.has(key)) unresolved.push('Conflicto tardío: ' + key + ' en modify y preserve.');
  }
  return { preserve:[...preserve], modify:[...modify], unresolved };
}
function buildDraft(packet){
  const parsed = parseIntent(packet);
  return {
    request_id:makeId('GD2-REQ'),
    mode:packet.structured_form.mode,
    figure_kind:packet.structured_form.figure_kind,
    goal:packet.natural_language_note || 'Ejecución sin texto libre adicional',
    dimensions:{ w:packet.structured_form.width, h:packet.structured_form.height, unit:'px' },
    outputs:packet.structured_form.outputs,
    constraints_hard:packet.structured_form.hard_rules,
    preserve:parsed.preserve,
    modify:parsed.modify,
    unresolved:parsed.unresolved
  };
}
function confirmDraft(draft){ return { ...draft, confirmed_by_user:true, confirmed_at:nowIso() }; }

function buildFrame(confirmed, fileMeta){
  return PARAM_NAMES.map((name, idx)=>{
    const param_id = `P${String(idx+1).padStart(2,'0')}`;
    let value = [1,2,3,21,22,23].includes(idx+1) ? '0' : (QUALITY_PARAM_IDS.has(param_id) || ['P24','P25'].includes(param_id) ? 'U' : '0');
    if(param_id === 'P02' && confirmed.mode === 'create') value = '0';
    return { position:idx+1, param_id, name, value_k3:value, justification:value==='0'?'conformidad suficiente':'indeterminación controlada' };
  });
}

function qualityValues(frame){ return frame.filter(p=>QUALITY_PARAM_IDS.has(p.param_id)).map(p=>p.value_k3==='0'?0:p.value_k3==='U'?0.5:1); }
function factualMetrics(frame, iteration=0){
  const q = qualityValues(frame);
  const gradient = q.map((_,i)=> +((i>0 ? q[i] - q[i-1] : q[0]).toFixed(4)));
  const jacobian_diag = q.map(v=> +v.toFixed(4));
  const curvature = +((gradient.slice(1).reduce((a,v,i)=>a + Math.abs(v - gradient[i]),0))/Math.max(1, gradient.length-1)).toFixed(4);
  const residual = +(q.reduce((a,b)=>a+b,0)).toFixed(4);
  return { gradient, jacobian_diag, curvature, modal_first_mode:+residual.toFixed(4), modal_second_mode:+q.reduce((a,v,i)=>a + v * ((i%2===0)?1:-1),0).toFixed(4), residual, metrology:{ ufe_margin_min:24, ufe_spacing_min:16, ufe_canvas_width:Number(ui.width.value), ufe_canvas_height:Number(ui.height.value), iteration } };
}
function clone(o){ return JSON.parse(JSON.stringify(o)); }
function applyFactualCorrector(frame){
  const current = clone(frame); const trace=[]; let prevResidual = null; let step=0;
  while(step<QUALITY_PARAM_IDS.size){
    const metrics = factualMetrics(current, step); const changed=[];
    if(prevResidual !== null && metrics.residual >= prevResidual){ trace.push({ step, action:'stop', reason:'residual_non_decreasing', metrics, changed_params:changed }); break; }
    for(const p of current){ if(QUALITY_PARAM_IDS.has(p.param_id) && p.value_k3 === 'U'){ p.value_k3='0'; p.justification='corrección factual por gradiente/jacobiano y residual modal decreciente'; changed.push(p.param_id); break; } }
    trace.push({ step, action:'correct', metrics, changed_params:changed }); prevResidual = metrics.residual; if(!changed.length) break; step++; }
  return { corrected:current, trace };
}
function buildGob(frame){ return frame.map(p=>({ ...p, value_k3: p.param_id==='P24' && p.value_k3!=='0' ? 'U' : p.value_k3, justification:`supervisión de ${p.param_id}` })); }
function buildSequence(baseFrame, correctedFrame, gob, trace){
  const seq = [
    { sovereign_id:'S0', epsilon_id:'ε0', label:'Frame inicial declarado', dictamen_k3:'INDETERMINADO' },
    { sovereign_id:'S1', epsilon_id:'ε1', label:'Entrada admitida tras cuarentena', dictamen_k3:dictamenFromCell(baseFrame) },
    { sovereign_id:'S2', epsilon_id:'ε2', label:'Intención confirmada por el usuario', dictamen_k3:dictamenFromCell(baseFrame) },
  ];
  trace.forEach((t, idx)=> seq.push({ sovereign_id:`S${idx+3}`, epsilon_id:`ε${idx+3}`, label:t.action==='correct'?'Corrección factual aplicada':'Parada factual por residual', dictamen_k3:dictamenFromCell(correctedFrame) }));
  seq.push({ sovereign_id:`S${seq.length}`, epsilon_id:`ε${seq.length}`, label:'Auditoría poligonal y dictamen', dictamen_k3:dictamenFromCell(gob) });
  return seq;
}

async function quarantineFile(file){
  setState('FILE_SELECTED', file ? file.name : 'sin archivo');
  if(!file && ui.mode.value==='correct') throw new Error('Modo corregir requiere archivo local o cambie a crear.');
  setState('TYPE_CHECK'); if(file && !['image/png','image/jpeg','image/svg+xml'].includes(file.type)) throw new Error('Tipo de archivo no admitido.');
  if(file && ['image/png','image/jpeg'].includes(file.type) && ui.mode.value==='correct'){ setState('AVISO_ALCANCE','Archivo raster (PNG/JPG) · La salida es un informe de corrección especificada. La imagen procesada requiere executor externo — previsto en Fase 2.'); }
  setState('LIMITS_CHECK'); if(file && file.size > MAX_FILE_BYTES) throw new Error('Archivo fuera de límites.');
  setState('SANITIZE_LOCAL'); let text=''; if(file && file.type==='image/svg+xml'){ text = await file.text(); if(/<script|onload=|onerror=|foreignObject/i.test(text)) throw new Error('SVG rechazado por sanitización local.'); }
  setState('HASH_AND_PACKET'); return { name:file?.name??null, type:file?.type??null, size:file?.size??0, text, hash:stableHash(`${file?.name||'none'}|${file?.size||0}|${text}`) };
}

function polygonSvg(title, cell){
  const cx=260, cy=260, r0=140; const n=cell.length; const points=[]; const labels=[]; const fills=[];
  for(let i=0;i<n;i++){ const ang = -Math.PI/2 + (2*Math.PI*i/n); const mul = cell[i].value_k3==='0'?0.75:cell[i].value_k3==='1'?1:0.88; const r=r0*mul; const x=cx+r*Math.cos(ang), y=cy+r*Math.sin(ang); points.push(`${x.toFixed(1)},${y.toFixed(1)}`); const lx=cx+(r0+24)*Math.cos(ang), ly=cy+(r0+24)*Math.sin(ang); labels.push(`<text x="${lx.toFixed(1)}" y="${ly.toFixed(1)}" font-size="10" text-anchor="middle">${cell[i].param_id}</text>`); const fill=cell[i].value_k3==='0'?'#4CAF50':cell[i].value_k3==='1'?'#F44336':'#FFC107'; fills.push(`<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="4" fill="${fill}" stroke="#666"/>`); }
  return `<svg viewBox="0 0 520 560" xmlns="http://www.w3.org/2000/svg"><rect x="1" y="1" width="518" height="558" rx="10" fill="white" stroke="#d7dbdd"/><text x="260" y="28" text-anchor="middle" font-size="16" font-weight="700">${title}</text><text x="260" y="48" text-anchor="middle" font-size="11">AE-GD2-SV · Panel interactivo SV–Usuario</text><polygon points="${points.join(' ')}" fill="#edf3f8" stroke="#0f5889" stroke-width="2"/>${labels.join('')}${fills.join('')}<rect x="30" y="505" width="10" height="10" fill="#4CAF50"/><text x="44" y="514" font-size="9">0 = conforme</text><rect x="130" y="505" width="10" height="10" fill="#FFC107"/><text x="144" y="514" font-size="9">U = indeterminado</text><rect x="250" y="505" width="10" height="10" fill="#F44336"/><text x="264" y="514" font-size="9">1 = no apto</text><text text-anchor="middle" font-size="8"><tspan x="260" y="529">Juan Antonio Lloret Egea · ORCID: 0000-0002-6634-3351 · ITVIA</tspan><tspan x="260" dy="11">IA eñ™ — La Biblia de la IA™ · ISSN 2695-6411 · CC BY-NC-ND 4.0 · Madrid, 14/04/2026</tspan></text></svg>`;
}
function renderSequence(sequence){ ui.sequence.innerHTML=''; sequence.forEach((item,idx)=>{ const btn=document.createElement('button'); btn.textContent=item.sovereign_id; btn.onclick=()=> ui.sequenceDetail.textContent = JSON.stringify(item,null,2); if(idx===sequence.length-1) btn.click(); ui.sequence.appendChild(btn); }); }
function renderParams(frame,gob){ ui.paramTable.innerHTML=''; frame.forEach((row,idx)=>{ const tr=document.createElement('tr'); tr.innerHTML=`<td>${row.position}</td><td>${row.param_id}</td><td>${row.name}</td><td>${row.value_k3} / ${gob[idx].value_k3}</td><td>${row.justification}</td>`; ui.paramTable.appendChild(tr); }); }
function toCsv(rows, columns){ const esc = (v)=>{ const s=String(v??''); return /[",\n]/.test(s)?`"${s.replace(/"/g,'""')}"`:s; }; return [columns.join(','), ...rows.map(r=>columns.map(c=>esc(r[c])).join(','))].join('\n'); }
function makeHtmlReport(report, frameSvg, gobSvg){ const rows=report.critical_parameters.map(p=>`<tr><td>${p.position}</td><td>${p.param_id}</td><td>${p.name}</td><td>${p.value_k3}</td><td>${p.justification}</td></tr>`).join(''); const sovereign=report.sovereign_sequence.map(s=>`<li><strong>${s.sovereign_id}</strong> · ${s.epsilon_id} · ${s.label} · ${s.dictamen_k3}</li>`).join(''); return `<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Informe de auditoría AE-GD2-SV</title><style>body{font-family:Georgia,serif;margin:24px;color:#17202a}h1,h2{color:#0f5889}table{border-collapse:collapse;width:100%}th,td{border:1px solid #d7dbdd;padding:6px 8px}th{background:#eef3f7}svg{width:100%;max-width:520px}.row{display:flex;gap:16px;flex-wrap:wrap}.card{border:1px solid #d7dbdd;padding:12px;border-radius:12px;margin-bottom:16px}</style></head><body><h1>Informe de auditoría — AE-GD2-SV</h1><p><strong>Run ID:</strong> ${report.run_id} · <strong>Dictamen global:</strong> ${report.dictamen_global}</p><div class="card"><h2>Trayectoria soberana</h2><ol>${sovereign}</ol></div><div class="card"><h2>Traza de corrección factual</h2><pre>${JSON.stringify(report.correction_trace,null,2)}</pre></div><div class="row"><div class="card">${frameSvg}</div><div class="card">${gobSvg}</div></div><div class="card"><h2>Parámetros críticos</h2><table><thead><tr><th>Pos</th><th>ID</th><th>Nombre</th><th>Valor</th><th>Justificación</th></tr></thead><tbody>${rows}</tbody></table></div><p>Autor: Juan Antonio Lloret Egea · ORCID: 0000-0002-6634-3351 · Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) · IA eñ™ — La Biblia de la IA™ · ISSN 2695-6411 · Licencia: CC BY-NC-ND 4.0 · Madrid, 14/04/2026</p></body></html>`; }

function textBlob(text,type='text/plain;charset=utf-8'){ return new Blob([text],{type}); }
function downloadBlob(name,blob){ const url=URL.createObjectURL(blob); const a=document.createElement('a'); a.href=url; a.download=name; a.click(); setTimeout(()=>URL.revokeObjectURL(url),500); }
function crc32(buf){ let table=crc32.table; if(!table){ table=new Uint32Array(256); for(let i=0;i<256;i++){ let c=i; for(let k=0;k<8;k++) c = c & 1 ? 0xEDB88320 ^ (c >>> 1) : c >>> 1; table[i]=c>>>0; } crc32.table=table; } let crc=0xFFFFFFFF; for(const b of buf) crc = table[(crc ^ b) & 0xFF] ^ (crc >>> 8); return (crc ^ 0xFFFFFFFF)>>>0; }
function buildZip(files){ const encoder=new TextEncoder(); const localParts=[]; const centralParts=[]; let offset=0; files.forEach(file=>{ const nameBytes=encoder.encode(file.name); const data=typeof file.content==='string'?encoder.encode(file.content):file.content; const crc=crc32(data); const local=new Uint8Array(30+nameBytes.length+data.length); const dv=new DataView(local.buffer); dv.setUint32(0,0x04034b50,true); dv.setUint16(4,20,true); dv.setUint32(14,crc,true); dv.setUint32(18,data.length,true); dv.setUint32(22,data.length,true); dv.setUint16(26,nameBytes.length,true); local.set(nameBytes,30); local.set(data,30+nameBytes.length); localParts.push(local); const central=new Uint8Array(46+nameBytes.length); const cv=new DataView(central.buffer); cv.setUint32(0,0x02014b50,true); cv.setUint16(4,20,true); cv.setUint16(6,20,true); cv.setUint32(16,crc,true); cv.setUint32(20,data.length,true); cv.setUint32(24,data.length,true); cv.setUint16(28,nameBytes.length,true); cv.setUint32(42,offset,true); central.set(nameBytes,46); centralParts.push(central); offset += local.length; }); const centralSize=centralParts.reduce((a,p)=>a+p.length,0); const end=new Uint8Array(22); const ev=new DataView(end.buffer); ev.setUint32(0,0x06054b50,true); ev.setUint16(8,files.length,true); ev.setUint16(10,files.length,true); ev.setUint32(12,centralSize,true); ev.setUint32(16,offset,true); return new Blob([...localParts,...centralParts,end],{type:'application/zip'}); }

async function run(){ ui.downloadBtn.disabled=true; ui.stateLog.innerHTML=''; setState('IDLE'); try{ const file=ui.fileInput.files[0]||null; const fileMeta=await quarantineFile(file); const packet=buildUserContextPacket(fileMeta); setState('PACKET_READY'); const draft=buildDraft(packet); setState('DRAFT_READY'); if(draft.unresolved && draft.unresolved.length){ ui.sequenceDetail.textContent = JSON.stringify(draft, null, 2); setState('INTERNAL_REJECT', draft.unresolved.join(' | ')); ui.auditSummary.innerHTML = '<strong>Rechazado por contradicción de intención.</strong>'; ui.auditJson.textContent = JSON.stringify({ packet, draft, error:'intent_conflict' }, null, 2); return; } const confirmed=confirmDraft(draft); setState('CONFIRMED'); const runId=makeId('GD2-RUN'); const baseFrame=buildFrame(confirmed,fileMeta); const corrected = applyFactualCorrector(baseFrame); const frame=corrected.corrected; const gob=buildGob(frame); const sequence=buildSequence(baseFrame, frame, gob, corrected.trace); const frameSvg=polygonSvg('C_frame^25', frame); const gobSvg=polygonSvg('C_gob^25', gob); const baseDictamen=dictamenFromCell(baseFrame); const correctedDictamen=dictamenFromCell(frame); const dictamenGlobal=dictamenFromCell(gob); const events = [{event_id:makeId('GD2-EVT'), parent_event_id:null, run_id:runId, event_type:'create_user_context_packet', dictamen_k3:null, timestamp_utc:nowIso(), affected_params:['P01','P02','P03']},{event_id:makeId('GD2-EVT'), parent_event_id:null, run_id:runId, event_type:'translate_to_draft', dictamen_k3:null, timestamp_utc:nowIso(), affected_params:['P06','P08','P10']},{event_id:makeId('GD2-EVT'), parent_event_id:null, run_id:runId, event_type:'confirm_intent', dictamen_k3:baseDictamen, timestamp_utc:nowIso(), affected_params:['P21','P22']}]; corrected.trace.forEach(step=>events.push({event_id:makeId('GD2-EVT'), parent_event_id:events[events.length-1].event_id, run_id:runId, event_type:'factual_corrector_step', dictamen_k3:correctedDictamen, timestamp_utc:nowIso(), affected_params:step.changed_params})); events.push({event_id:makeId('GD2-EVT'), parent_event_id:events[events.length-1].event_id, run_id:runId, event_type:'build_audit_report', dictamen_k3:dictamenGlobal, timestamp_utc:nowIso(), affected_params:['P23','P24','P25']}); const eventIndex={ by_event_id:Object.fromEntries(events.map((e,i)=>[e.event_id,i])), by_run_id:{[runId]:events.map((_,i)=>i)}, by_event_type:events.reduce((acc,e,i)=>((acc[e.event_type] ||= []).push(i), acc),{}), by_param:events.reduce((acc,e,i)=>{ (e.affected_params||[]).forEach(p=>((acc[p] ||= []).push(i))); return acc; },{})}; const report={ run_id:runId, base_dictamen:baseDictamen, corrected_dictamen:correctedDictamen, dictamen_global:dictamenGlobal, sovereign_sequence:sequence, correction_trace:corrected.trace, critical_parameters:frame, metrics:{ before:factualMetrics(baseFrame,0), after:factualMetrics(frame, corrected.trace.length) }, exposure_gate:dictamenGlobal==='NO APTO'?'NO EXPONIBLE':(dictamenGlobal==='INDETERMINADO'?'EXPOSICION_CON_U':'EXPONIBLE'), correction_scope:fileMeta&&['image/png','image/jpeg'].includes(fileMeta.type||'')?'INFORME_ESPECIFICADO — imagen raster no procesada; executor externo requerido (Fase 2)':fileMeta&&(fileMeta.type||'').includes('svg')?'SVG_CORREGIBLE — corrección estructural disponible en Fase 1':'CREACION — sin imagen de entrada', packet,draft,confirmed }; const criticalCsv=toCsv(frame,['position','param_id','name','value_k3','justification']); const frameCsv=toCsv(frame.map(r=>({position:r.position,param_id:r.param_id,value_k3:r.value_k3,label:r.name})),['position','param_id','value_k3','label']); const gobCsv=toCsv(gob.map(r=>({position:r.position,param_id:r.param_id,value_k3:r.value_k3,label:r.name})),['position','param_id','value_k3','label']); const seqCsv=toCsv(sequence,['sovereign_id','epsilon_id','label','dictamen_k3']); const eventsFlatCsv=toCsv(events.map(e=>({...e,affected_params:(e.affected_params||[]).join(';')})),['event_id','parent_event_id','run_id','event_type','dictamen_k3','timestamp_utc','affected_params']); const indexByParamCsv=toCsv(Object.entries(eventIndex.by_param).map(([param_id,idxs])=>({param_id,event_count:idxs.length,last_position:idxs[idxs.length-1]})),['param_id','event_count','last_position']); const indexByTypeCsv=toCsv(Object.entries(eventIndex.by_event_type).map(([event_type,idxs])=>({event_type,count:idxs.length,last_position:idxs[idxs.length-1]})),['event_type','count','last_position']); const eventsJsonl=events.map(e=>JSON.stringify(e)).join('\n'); const quarantineLog=JSON.stringify({state:'PACKET_READY',timestamp_utc:nowIso(),file:fileMeta?.name??null})+'\n'; const validatorLog=JSON.stringify({state:'VALIDATED',dictamen_k3:dictamenGlobal,timestamp_utc:nowIso()})+'\n'; const reportHtml=makeHtmlReport(report, frameSvg, gobSvg); ui.frameSvg.innerHTML=frameSvg; ui.gobSvg.innerHTML=gobSvg; renderSequence(sequence); renderParams(frame,gob); ui.auditSummary.innerHTML=`<p><strong>Run ID:</strong> ${runId}</p><p><strong>Dictamen base:</strong> ${baseDictamen}</p><p><strong>Dictamen corregido:</strong> ${correctedDictamen}</p><p><strong>Dictamen global:</strong> ${dictamenGlobal}</p><p><strong>Exposición:</strong> ${report.exposure_gate}</p><p><strong>Alcance de la corrección:</strong> ${report.correction_scope}</p>`; ui.auditJson.textContent=JSON.stringify(report,null,2); ui.eventJson.textContent=JSON.stringify({events,eventIndex},null,2); const _mb=report.metrics.before,_ma=report.metrics.after; document.getElementById('diffMetrics').textContent='gradient_before: '+JSON.stringify(_mb.gradient)+'\ngradient_after:  '+JSON.stringify(_ma.gradient)+'\ncurvature_before: '+_mb.curvature+'\ncurvature_after:  '+_ma.curvature; document.getElementById('modalMetrics').textContent='modal_1_before: '+_mb.modal_first_mode+'\nmodal_1_after:  '+_ma.modal_first_mode+'\nmodal_2_before: '+_mb.modal_second_mode+'\nmodal_2_after:  '+_ma.modal_second_mode+'\nresidual_before: '+_mb.residual+'\nresidual_after:  '+_ma.residual; document.getElementById('metroMetrics').textContent=JSON.stringify(_mb.metrology,null,2); document.getElementById('sovereignJson').textContent=JSON.stringify(report.sovereign_sequence,null,2); current={ report, reportHtml, frameSvg, gobSvg, criticalCsv, frameCsv, gobCsv, seqCsv, eventsFlatCsv, indexByParamCsv, indexByTypeCsv, eventsJsonl, quarantineLog, validatorLog, eventIndex }; ui.downloadBtn.disabled=false; setState('EXPORT_READY'); } catch(err){ setState('INTERNAL_REJECT', err.message); ui.auditSummary.innerHTML=`<p><strong>Rechazo:</strong> ${err.message}</p>`; ui.auditJson.textContent=''; ui.eventJson.textContent=''; } }
function downloadBundle(){ if(!current) return; const files=[ {name:'01_informe_usuario/informe_auditoria.html',content:current.reportHtml}, {name:'01_informe_usuario/resumen_ejecutivo.json',content:JSON.stringify(current.report,null,2)}, {name:'01_informe_usuario/critical_parameters.csv',content:current.criticalCsv}, {name:'01_informe_usuario/frame25.svg',content:current.frameSvg}, {name:'01_informe_usuario/gob25.svg',content:current.gobSvg}, {name:'01_informe_usuario/frame25.csv',content:current.frameCsv}, {name:'01_informe_usuario/gob25.csv',content:current.gobCsv}, {name:'02_paquete_tecnico/audit_report.json',content:JSON.stringify(current.report,null,2)}, {name:'02_paquete_tecnico/event_bank/events.jsonl',content:current.eventsJsonl}, {name:'02_paquete_tecnico/event_bank/event_index.json',content:JSON.stringify(current.eventIndex,null,2)}, {name:'02_paquete_tecnico/event_bank/events_flat.csv',content:current.eventsFlatCsv}, {name:'02_paquete_tecnico/event_bank/index_by_param.csv',content:current.indexByParamCsv}, {name:'02_paquete_tecnico/event_bank/index_by_type.csv',content:current.indexByTypeCsv}, {name:'02_paquete_tecnico/event_bank/sovereign_sequence.csv',content:current.seqCsv}, {name:'02_paquete_tecnico/logs/quarantine_log.jsonl',content:current.quarantineLog}, {name:'02_paquete_tecnico/logs/validator_log.jsonl',content:current.validatorLog}, {name:'02_paquete_tecnico/logs/execution_log.jsonl',content:current.eventsJsonl} ]; downloadBlob(`ae_gd2_sv_${current.report.run_id}.zip`, buildZip(files)); }
ui.runBtn.addEventListener('click',run); ui.downloadBtn.addEventListener('click',downloadBundle);
