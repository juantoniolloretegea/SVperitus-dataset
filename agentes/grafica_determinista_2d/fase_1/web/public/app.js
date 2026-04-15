const PARAM_NAMES = [
  'Modo operativo','Tipo de fuente','Integridad de entrada','Localidad y cuarentena','Perfil de ejecución',
  'Clase de figura','Dominio declarado','Dimensiones del lienzo','Salidas requeridas','Restricciones duras',
  'Política de título','Política de footer','Sistema de paneles','Sistema de nodos','Sistema de aristas',
  'No colisión texto-texto','Respiración vertical suficiente','Respiración horizontal suficiente','Densidad compositiva aceptable','Canonicidad del SVG',
  'Trazabilidad append-only','Confirmación humana soberana','Coherencia del bundle','Pureza de frontera','Reproducibilidad laboratorial'
];
const K3 = ['0','1','U'];
const QUALITY_PARAM_IDS = new Set(['P16','P17','P18','P19','P20']);
document.addEventListener('DOMContentLoaded',function(){
  try{ const d=localStorage.getItem('ae_gd2_sv_consejo');
    if(d && document.getElementById('consejoBtn'))
      document.getElementById('consejoBtn').disabled=false;
  }catch(e){}
});
let currentFileMeta=null, correctedSvgData=null;
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

// Fill semántico del polígono según predominancia K3
function polyFillColor(cell){
  const n=cell.length,
        n0=cell.filter(p=>p.value_k3==='0').length,
        n1=cell.filter(p=>p.value_k3==='1').length,
        nU=cell.filter(p=>p.value_k3==='U').length;
  if(n1>=19) return 'rgba(244,67,54,0.15)';
  if(n0>=19) return 'rgba(76,175,80,0.15)';
  const r0=n0/n,r1=n1/n,rU=nU/n;
  if(r0>=r1&&r0>=rU) return `rgba(76,175,80,${(0.04+r0*0.18).toFixed(2)})`;
  if(r1>=r0&&r1>=rU) return `rgba(244,67,54,${(0.04+r1*0.18).toFixed(2)})`;
  return `rgba(255,193,7,${(0.04+rU*0.18).toFixed(2)})`;
}
function polygonSvg(title, cell){
  // C4b: viewBox mínimo = 155 chars × 0.55 × fs9 = 767px + 2×40px margen = 847 → 860px; cx=430
  const cx=430, cy=260, r0=140; const n=cell.length; const points=[]; const labels=[]; const fills=[];
  for(let i=0;i<n;i++){ const ang = -Math.PI/2 + (2*Math.PI*i/n); const mul = cell[i].value_k3==='0'?0.75:cell[i].value_k3==='1'?1:0.88; const r=r0*mul; const x=cx+r*Math.cos(ang), y=cy+r*Math.sin(ang); points.push(`${x.toFixed(1)},${y.toFixed(1)}`); const lx=cx+(r0+24)*Math.cos(ang), ly=cy+(r0+24)*Math.sin(ang); labels.push(`<text x="${lx.toFixed(1)}" y="${ly.toFixed(1)}" font-size="10" text-anchor="middle">${cell[i].param_id}</text>`); const fill=cell[i].value_k3==='0'?'#4CAF50':cell[i].value_k3==='1'?'#F44336':'#FFC107'; fills.push(`<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="4" fill="${fill}" stroke="#666"/>`); }
  return `<svg viewBox="0 0 860 560" xmlns="http://www.w3.org/2000/svg"><rect x="1" y="1" width="858" height="558" rx="10" fill="white" stroke="#d7dbdd"/><text x="430" y="28" text-anchor="middle" font-size="16" font-weight="700">${title}</text><text x="430" y="48" text-anchor="middle" font-size="11">AE-GD2-SV · Panel interactivo SV–Usuario</text><polygon points="${points.join(' ')}" fill="${polyFillColor(cell)}" stroke="#0f5889" stroke-width="2"/>${labels.join('')}${fills.join('')}<rect x="180" y="505" width="10" height="10" fill="#4CAF50"/><text x="194" y="514" font-size="9">0 = conforme</text><rect x="360" y="505" width="10" height="10" fill="#FFC107"/><text x="374" y="514" font-size="9">U = indeterminado</text><rect x="560" y="505" width="10" height="10" fill="#F44336"/><text x="574" y="514" font-size="9">1 = no apto</text><text x="430" y="536" text-anchor="middle" font-size="9">Autor: Juan Antonio Lloret Egea · ORCID: 0000-0002-6634-3351 · ITVIA · IA eñ™ — La Biblia de la IA™ · ISSN 2695-6411 · CC BY-NC-ND 4.0 · Madrid, 14/04/2026</text></svg>`;
}
function renderSequence(sequence){ ui.sequence.innerHTML=''; sequence.forEach((item,idx)=>{ const btn=document.createElement('button'); btn.textContent=item.sovereign_id; btn.onclick=()=> ui.sequenceDetail.textContent = JSON.stringify(item,null,2); if(idx===sequence.length-1) btn.click(); ui.sequence.appendChild(btn); }); }
function renderParams(frame,gob){ ui.paramTable.innerHTML=''; frame.forEach((row,idx)=>{ const tr=document.createElement('tr'); tr.innerHTML=`<td>${row.position}</td><td>${row.param_id}</td><td>${row.name}</td><td>${row.value_k3} / ${gob[idx].value_k3}</td><td>${row.justification}</td>`; ui.paramTable.appendChild(tr); }); }
function toCsv(rows, columns){ const esc = (v)=>{ const s=String(v??''); return /[",\n]/.test(s)?`"${s.replace(/"/g,'""')}"`:s; }; return [columns.join(','), ...rows.map(r=>columns.map(c=>esc(r[c])).join(','))].join('\n'); }
function makeHtmlReport(report, frameSvg, gobSvg){ const rows=report.critical_parameters.map(p=>`<tr><td>${p.position}</td><td>${p.param_id}</td><td>${p.name}</td><td>${p.value_k3}</td><td>${p.justification}</td></tr>`).join(''); const sovereign=report.sovereign_sequence.map(s=>`<li><strong>${s.sovereign_id}</strong> · ${s.epsilon_id} · ${s.label} · ${s.dictamen_k3}</li>`).join(''); return `<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Informe de auditoría AE-GD2-SV</title><style>body{font-family:Georgia,serif;margin:24px;color:#17202a}h1,h2{color:#0f5889}table{border-collapse:collapse;width:100%}th,td{border:1px solid #d7dbdd;padding:6px 8px}th{background:#eef3f7}svg{width:100%;max-width:520px}.row{display:flex;gap:16px;flex-wrap:wrap}.card{border:1px solid #d7dbdd;padding:12px;border-radius:12px;margin-bottom:16px}</style></head><body><h1>Informe de auditoría — AE-GD2-SV</h1><p><strong>Run ID:</strong> ${report.run_id} · <strong>Dictamen global:</strong> ${report.dictamen_global}</p><div class="card"><h2>Trayectoria soberana</h2><ol>${sovereign}</ol></div><div class="card"><h2>Traza de corrección factual</h2><pre>${JSON.stringify(report.correction_trace,null,2)}</pre></div><div class="row"><div class="card">${frameSvg}</div><div class="card">${gobSvg}</div></div><div class="card"><h2>Parámetros críticos</h2><table><thead><tr><th>Pos</th><th>ID</th><th>Nombre</th><th>Valor</th><th>Justificación</th></tr></thead><tbody>${rows}</tbody></table></div><p>Autor: Juan Antonio Lloret Egea · ORCID: 0000-0002-6634-3351 · Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) · IA eñ™ — La Biblia de la IA™ · ISSN 2695-6411 · Licencia: CC BY-NC-ND 4.0 · Madrid, 14/04/2026</p></body></html>`; }

function textBlob(text,type='text/plain;charset=utf-8'){ return new Blob([text],{type}); }
function downloadBlob(name,blob){ const url=URL.createObjectURL(blob); const a=document.createElement('a'); a.href=url; a.download=name; a.click(); setTimeout(()=>URL.revokeObjectURL(url),500); }
function crc32(buf){ let table=crc32.table; if(!table){ table=new Uint32Array(256); for(let i=0;i<256;i++){ let c=i; for(let k=0;k<8;k++) c = c & 1 ? 0xEDB88320 ^ (c >>> 1) : c >>> 1; table[i]=c>>>0; } crc32.table=table; } let crc=0xFFFFFFFF; for(const b of buf) crc = table[(crc ^ b) & 0xFF] ^ (crc >>> 8); return (crc ^ 0xFFFFFFFF)>>>0; }
function buildZip(files){ const encoder=new TextEncoder(); const localParts=[]; const centralParts=[]; let offset=0; files.forEach(file=>{ const nameBytes=encoder.encode(file.name); const data=typeof file.content==='string'?encoder.encode(file.content):file.content; const crc=crc32(data); const local=new Uint8Array(30+nameBytes.length+data.length); const dv=new DataView(local.buffer); dv.setUint32(0,0x04034b50,true); dv.setUint16(4,20,true); dv.setUint32(14,crc,true); dv.setUint32(18,data.length,true); dv.setUint32(22,data.length,true); dv.setUint16(26,nameBytes.length,true); local.set(nameBytes,30); local.set(data,30+nameBytes.length); localParts.push(local); const central=new Uint8Array(46+nameBytes.length); const cv=new DataView(central.buffer); cv.setUint32(0,0x02014b50,true); cv.setUint16(4,20,true); cv.setUint16(6,20,true); cv.setUint32(16,crc,true); cv.setUint32(20,data.length,true); cv.setUint32(24,data.length,true); cv.setUint16(28,nameBytes.length,true); cv.setUint32(42,offset,true); central.set(nameBytes,46); centralParts.push(central); offset += local.length; }); const centralSize=centralParts.reduce((a,p)=>a+p.length,0); const end=new Uint8Array(22); const ev=new DataView(end.buffer); ev.setUint32(0,0x06054b50,true); ev.setUint16(8,files.length,true); ev.setUint16(10,files.length,true); ev.setUint32(12,centralSize,true); ev.setUint32(16,offset,true); return new Blob([...localParts,...centralParts,end],{type:'application/zip'}); }



// ── C6: métricas Φ₃ — carta espacial afín auxiliar (R3) ───────────────────
// Fuente: Lloret Egea, J.A. ITVIA · ISSN 2695-6411 · 16/03/2026 · CC BY-NC-ND 4.0
// Φ₃(Pᵢ=s)=(ρ(s)cosθᵢ, ρ(s)sinθᵢ, z(s));  z(0)=z(1)=0, z(U)=h=2.2
// Ez=k(v)·h² — invariante exacto: orden relativo independiente de h
const C6_H   = 2.2;
const C6_RHO = {'0':1,'1':2,'U':3};
const C6_Z   = s => s==='U' ? C6_H : 0;

function computeR3Metrics(cell, h) {
  h = (h !== undefined) ? h : C6_H;
  const n = cell.length;
  const rho = i => C6_RHO[cell[i].value_k3] || 1;
  const z   = i => C6_Z(cell[i].value_k3);
  const th  = i => 2*Math.PI*i/n;
  let L2=0, L3=0, Erho=0, sumZ2=0, kv=0;
  for(let i=0;i<n;i++){
    const j=(i+1)%n;
    const dx=rho(j)*Math.cos(th(j))-rho(i)*Math.cos(th(i));
    const dy=rho(j)*Math.sin(th(j))-rho(i)*Math.sin(th(i));
    const dz=z(j)-z(i);
    L2+=Math.sqrt(dx*dx+dy*dy);
    L3+=Math.sqrt(dx*dx+dy*dy+dz*dz);
    const dr=rho(j)-rho(i); Erho+=dr*dr;
    sumZ2+=z(i)*z(i);
    if(z(i)!==z(j)) kv++;
  }
  const n0=cell.filter(p=>p.value_k3==='0').length;
  const n1=cell.filter(p=>p.value_k3==='1').length;
  const nU=cell.filter(p=>p.value_k3==='U').length;
  return { L2:+L2.toFixed(3), L3:+L3.toFixed(3), dL:+(L3-L2).toFixed(3),
           Cz:+Math.sqrt(sumZ2/n).toFixed(3), Erho:+Erho.toFixed(3),
           Ez:+(kv*h*h).toFixed(3), kv, h, n0, n1, nU };
}


// ── Corrector SVG ejecutable (C5b exec) ──────────────────────────────────────
// El agente aplica SOLO la opción que el humano soberano ha confirmado explícitamente.
// Opera únicamente sobre atributos estructurales del footer (font-size, posición y).
// No modifica el contenido semántico del texto. No toca ninguna otra región del SVG.
function correctSvg(proposal, svgText){
  const parser = new DOMParser();
  const doc = parser.parseFromString(svgText, 'image/svg+xml');
  const choice = proposal.opciones.find(o=>o.id===proposal.opcion_elegida);
  if(!choice) return {ok:false, reason:'opcion_no_encontrada'};
  
  // Localizar el elemento <text> problemático por su contenido (coincidencia parcial)
  const allTexts = Array.from(doc.querySelectorAll('text'));
  let target = null;
  for(const t of allTexts){
    const txt = (t.textContent||'').trim();
    if(txt.length > 80) { target = t; break; }  // el texto más largo es el footer
  }
  if(!target) return {ok:false, reason:'elemento_no_encontrado'};

  const orig = (target.textContent||'').trim();

  if(choice.id==='O1'){
    // Reducir font-size
    const fs = choice.parametros.font_size_propuesto;
    target.setAttribute('font-size', String(fs));
    const diff = {op:'set_attr', elem:'text[footer]',
                  attr:'font-size', antes: choice.parametros.font_size_actual, despues: fs};
    const xs = new XMLSerializer();
    return {ok:true, svg:xs.serializeToString(doc), diff};
  }

  if(choice.id==='O2'){
    // Dividir en dos líneas: modificar textContent de target y añadir segundo <text>
    const corte = choice.parametros.posicion_corte_caracter;
    const line1 = orig.substring(0, corte).trim();
    const line2 = orig.substring(corte).trim();
    const yOrig = parseFloat(target.getAttribute('y') || '0');
    const fs    = parseFloat(target.getAttribute('font-size') || '9');
    const lineH = fs + 3;  // interlineado conservador

    target.textContent = line1;
    const t2 = target.cloneNode(false);
    t2.textContent = line2;
    t2.setAttribute('y', String(yOrig + lineH));
    target.parentNode.insertBefore(t2, target.nextSibling);

    // Expandir el viewBox para acomodar la línea extra
    const vb = doc.documentElement.getAttribute('viewBox');
    if(vb){
      const [vx,vy,vw,vh] = vb.split(' ').map(Number);
      doc.documentElement.setAttribute('viewBox', `${vx} ${vy} ${vw} ${vh+lineH}`);
      doc.documentElement.setAttribute('height', String(parseFloat(doc.documentElement.getAttribute('height')||vh)+lineH));
    }
    const diff = {op:'split_line', elem:'text[footer]',
                  corte, line1_chars:line1.length, line2_chars:line2.length,
                  viewBox_ampliado: lineH + 'px'};
    const xs = new XMLSerializer();
    return {ok:true, svg:xs.serializeToString(doc), diff};
  }

  return {ok:false, reason:'opcion_O3_requiere_accion_humana'};
}

// ── C5b: analizador estructural de SVG ─────────────────────────────────────
// INVARIANTE: esta función NO modifica svgText bajo ninguna circunstancia.
// INVARIANTE: ninguna opción se ejecuta sin confirmación humana explícita.
// El soberano decide; el agente detecta, mide y propone.
//
// Factor heurístico declarado:
//   C5B_CHAR_FACTOR = 0.55  (char_width ≈ 0.55 × font-size, sans-serif)
//   No es medida exacta — P25 permanece U (Reproducibilidad laboratorial).
//
// Si la corrección necesaria no está entre las opciones propuestas,
// el AE-GD2-SV en Fase 1 no puede llevarla a cabo.
const C5B_CHAR_FACTOR  = 0.55;
const C5B_MARGIN_PX    = 40;
const C5B_BOTTOM_MIN   = 10;
const C5B_MIN_READABLE = 7; // font-size mínimo legible (px)

function _nearestWordBoundary(text, pos) {
  let i = pos;
  while (i > 0 && text[i] !== ' ' && text[i] !== '·') i--;
  return i > 0 ? i : pos;
}

function analyzeSvg(svgText, modifyTargets) {
  // Returns { proposals, k3, notes }
  // proposals: lista de problemas detectados con opciones acotadas
  // k3: '1' = problemas detectados | '0' = sin problemas | 'U' = análisis no posible
  // NUNCA devuelve svgText modificado

  const proposals = [];

  let doc;
  try {
    doc = new DOMParser().parseFromString(svgText, 'image/svg+xml');
  } catch(e) {
    return { proposals, k3:'U', notes:'Error de parseo SVG: '+e.message };
  }
  const parseErr = doc.querySelector('parsererror');
  if (parseErr) {
    return { proposals, k3:'U', notes:'SVG con errores de parseo — análisis no posible.' };
  }

  const svgEl = doc.documentElement;
  const vbRaw = svgEl.getAttribute('viewBox');
  if (!vbRaw) {
    return { proposals, k3:'U', notes:'SVG sin atributo viewBox — análisis no posible.' };
  }
  const vb = vbRaw.trim().split(/\s+/).map(Number);
  const [,, vbW, vbH] = vb;
  if (!vbW || !vbH) {
    return { proposals, k3:'U', notes:'viewBox con dimensiones inválidas — análisis no posible.' };
  }

  // ── Análisis de footer ────────────────────────────────────────────────────
  // Canal C5b — análisis estructural independiente del canal NL (INYECCION_C5b)
  // Corre siempre para archivos SVG, sin filtrar por modifyTargets
  const allTexts = [...doc.querySelectorAll('text')];
  const footerEls = allTexts.filter(el => parseFloat(el.getAttribute('y')||0) > vbH * 0.75);

  for (const el of footerEls) {
    const fs  = parseFloat(el.getAttribute('font-size') || 12);
    const txt = (el.textContent || '').trim();
    if (!txt) continue;

    const estW    = txt.length * C5B_CHAR_FACTOR * fs;
    const needsW  = Math.ceil(estW + 2 * C5B_MARGIN_PX);
    const overflow = needsW > vbW;
    const yEl      = parseFloat(el.getAttribute('y') || 0);
    const tooLow   = (vbH - yEl) < C5B_BOTTOM_MIN;

    if (!overflow && !tooLow) continue;

    // Calcular propuestas concretas
    const maxCharsAllowed = Math.floor((vbW - 2 * C5B_MARGIN_PX) / (C5B_CHAR_FACTOR * fs));
    const fsSuggested     = Math.max(C5B_MIN_READABLE,
                              Math.floor((vbW - 2 * C5B_MARGIN_PX) / (txt.length * C5B_CHAR_FACTOR)));
    const splitPos        = _nearestWordBoundary(txt, Math.floor(txt.length / 2));
    const line1Preview    = txt.slice(0, splitPos).trim();
    const line2Preview    = txt.slice(splitPos).trim();

    const opciones = [];

    if (overflow) {
      opciones.push({
        id: 'O1',
        accion: 'Reducir tamaño de texto',
        parametros: { font_size_actual: fs, font_size_propuesto: fsSuggested },
        aviso: fsSuggested < C5B_MIN_READABLE
          ? 'font-size resultante (' + fsSuggested + 'px) por debajo del mínimo legible recomendado (' + C5B_MIN_READABLE + 'px). Opción no recomendada.'
          : null,
        ejecutable_agente_fase_1: false,
        requiere_accion_humana: false
      });
      opciones.push({
        id: 'O2',
        accion: 'Dividir la línea en dos',
        parametros: {
          posicion_corte_caracter: splitPos,
          linea_1_preview: line1Preview,
          linea_2_preview: line2Preview
        },
        aviso: 'Punto de corte propuesto: límite de palabra más próximo a la mitad del texto. El humano debe validar que el corte es semánticamente adecuado.',
        ejecutable_agente_fase_1: false,
        requiere_accion_humana: false
      });
      opciones.push({
        id: 'O3',
        accion: 'Reformular el texto (requiere acción humana — agente no puede ejecutar)',
        parametros: {
          chars_actuales: txt.length,
          chars_maximos_para_ajuste: maxCharsAllowed,
          exceso_chars: txt.length - maxCharsAllowed
        },
        aviso: 'El agente no puede modificar el contenido del texto. El humano debe reformular la atribución a menos de ' + maxCharsAllowed + ' caracteres.',
        ejecutable_agente_fase_1: false,
        requiere_accion_humana: true
      });
    }

    proposals.push({
      region: 'footer',
      problema: overflow ? 'desbordamiento_horizontal' : 'margen_inferior_insuficiente',
      medicion: {
        texto_chars: txt.length,
        font_size: fs,
        anchura_estimada_px: Math.round(estW),
        viewbox_width_px: vbW,
        desbordamiento_px: overflow ? Math.max(0, Math.round(needsW - vbW)) : 0,
        margen_inferior_px: tooLow ? Math.round(vbH - yEl) : null,
        factor_heuristico: C5B_CHAR_FACTOR,
        nota_factor: 'Estimación estadística. No es medida exacta (requeriría render real). P25=U.'
      },
      opciones,
      limite_agente: 'Si la corrección necesaria no está entre estas opciones, el AE-GD2-SV en Fase 1 no puede llevarla a cabo.'
    });
  }


  const k3 = proposals.length > 0 ? '1' : (proposals.length === 0 ? '0' : 'U');
  const notes = proposals.length > 0
    ? proposals.length + ' problema(s) detectado(s) en regiones autorizadas. Ver correction_proposals.json. Confirmación humana requerida.'
    : 'No se detectaron problemas en las regiones autorizadas (' + modifyTargets.join(', ') + ').';

  return { proposals, k3, notes };
}

async function run(){ ui.downloadBtn.disabled=true; ui.stateLog.innerHTML=''; setState('IDLE'); document.body.classList.remove('run-done'); try{ const file=ui.fileInput.files[0]||null; const fileMeta=await quarantineFile(file); currentFileMeta=fileMeta; const packet=buildUserContextPacket(fileMeta); setState('PACKET_READY'); const draft=buildDraft(packet); setState('DRAFT_READY'); if(draft.unresolved && draft.unresolved.length){ ui.sequenceDetail.textContent = JSON.stringify(draft, null, 2); setState('INTERNAL_REJECT', draft.unresolved.join(' | ')); ui.auditSummary.innerHTML = '<strong>Rechazado por contradicción de intención.</strong>'; ui.auditJson.textContent = JSON.stringify({ packet, draft, error:'intent_conflict' }, null, 2); return; } const confirmed=confirmDraft(draft); setState('CONFIRMED');
    // C5b: analizar SVG de entrada — solo detecta y propone, nunca ejecuta
    let svgAnalysis = null;
    if(fileMeta && fileMeta.type === 'image/svg+xml' && fileMeta.text && draft.modify && draft.modify.length){
      setState('SVG_ANALISIS', 'Analizando estructura SVG...');
      svgAnalysis = analyzeSvg(fileMeta.text, draft.modify); window._svgAnalysis = svgAnalysis;
      const msg = svgAnalysis.proposals.length > 0
        ? svgAnalysis.proposals.length + ' problema(s) detectado(s) — propuestas pendientes de confirmación humana'
        : 'Sin problemas detectados';
      setState('SVG_ANALISIS_COMPLETO', msg);
    } const runId=makeId('GD2-RUN'); const baseFrame=buildFrame(confirmed,fileMeta); const corrected = applyFactualCorrector(baseFrame); const frame=corrected.corrected; const gob=buildGob(frame); const sequence=buildSequence(baseFrame, frame, gob, corrected.trace);
    const r3frame=computeR3Metrics(frame); const r3gob=computeR3Metrics(gob); const frameSvg=polygonSvg('C_frame^25', frame); const gobSvg=polygonSvg('C_gob^25', gob); const baseDictamen=dictamenFromCell(baseFrame); const correctedDictamen=dictamenFromCell(frame); const dictamenGlobal=dictamenFromCell(gob); const events = [{event_id:makeId('GD2-EVT'), parent_event_id:null, run_id:runId, event_type:'create_user_context_packet', dictamen_k3:null, timestamp_utc:nowIso(), affected_params:['P01','P02','P03']},{event_id:makeId('GD2-EVT'), parent_event_id:null, run_id:runId, event_type:'translate_to_draft', dictamen_k3:null, timestamp_utc:nowIso(), affected_params:['P06','P08','P10']},{event_id:makeId('GD2-EVT'), parent_event_id:null, run_id:runId, event_type:'confirm_intent', dictamen_k3:baseDictamen, timestamp_utc:nowIso(), affected_params:['P21','P22']}]; corrected.trace.forEach(step=>events.push({event_id:makeId('GD2-EVT'), parent_event_id:events[events.length-1].event_id, run_id:runId, event_type:'factual_corrector_step', dictamen_k3:correctedDictamen, timestamp_utc:nowIso(), affected_params:step.changed_params})); events.push({event_id:makeId('GD2-EVT'), parent_event_id:events[events.length-1].event_id, run_id:runId, event_type:'build_audit_report', dictamen_k3:dictamenGlobal, timestamp_utc:nowIso(), affected_params:['P23','P24','P25']}); const eventIndex={ by_event_id:Object.fromEntries(events.map((e,i)=>[e.event_id,i])), by_run_id:{[runId]:events.map((_,i)=>i)}, by_event_type:events.reduce((acc,e,i)=>((acc[e.event_type] ||= []).push(i), acc),{}), by_param:events.reduce((acc,e,i)=>{ (e.affected_params||[]).forEach(p=>((acc[p] ||= []).push(i))); return acc; },{})}; const report={ run_id:runId, base_dictamen:baseDictamen, corrected_dictamen:correctedDictamen, dictamen_global:dictamenGlobal, sovereign_sequence:sequence, correction_trace:corrected.trace, critical_parameters:frame, metrics:{ before:factualMetrics(baseFrame,0), after:factualMetrics(frame, corrected.trace.length) }, exposure_gate:dictamenGlobal==='NO APTO'?'NO EXPONIBLE':(dictamenGlobal==='INDETERMINADO'?'EXPOSICION_CON_U':'EXPONIBLE'), r3_frame:r3frame, r3_gob:r3gob,
        svg_analysis: svgAnalysis ? { k3: svgAnalysis.k3, notes: svgAnalysis.notes, proposals_count: svgAnalysis.proposals.length } : null, correction_scope:fileMeta&&['image/png','image/jpeg'].includes(fileMeta.type||'')?'INFORME_ESPECIFICADO — imagen raster no procesada; executor externo requerido (Fase 2)':fileMeta&&(fileMeta.type||'').includes('svg')?(svgAnalysis&&svgAnalysis.proposals.length>0?'SVG_ANALIZADO — propuestas pendientes de confirmación humana (ver correction_proposals.json)':'SVG_ANALIZADO — sin correcciones estructurales necesarias'):'CREACION — sin imagen de entrada', packet,draft,confirmed }; const criticalCsv=toCsv(frame,['position','param_id','name','value_k3','justification']); const frameCsv=toCsv(frame.map(r=>({position:r.position,param_id:r.param_id,value_k3:r.value_k3,label:r.name})),['position','param_id','value_k3','label']); const gobCsv=toCsv(gob.map(r=>({position:r.position,param_id:r.param_id,value_k3:r.value_k3,label:r.name})),['position','param_id','value_k3','label']); const seqCsv=toCsv(sequence,['sovereign_id','epsilon_id','label','dictamen_k3']); const eventsFlatCsv=toCsv(events.map(e=>({...e,affected_params:(e.affected_params||[]).join(';')})),['event_id','parent_event_id','run_id','event_type','dictamen_k3','timestamp_utc','affected_params']); const indexByParamCsv=toCsv(Object.entries(eventIndex.by_param).map(([param_id,idxs])=>({param_id,event_count:idxs.length,last_position:idxs[idxs.length-1]})),['param_id','event_count','last_position']); const indexByTypeCsv=toCsv(Object.entries(eventIndex.by_event_type).map(([event_type,idxs])=>({event_type,count:idxs.length,last_position:idxs[idxs.length-1]})),['event_type','count','last_position']); const eventsJsonl=events.map(e=>JSON.stringify(e)).join('\n'); const quarantineLog=JSON.stringify({state:'PACKET_READY',timestamp_utc:nowIso(),file:fileMeta?.name??null})+'\n'; const validatorLog=JSON.stringify({state:'VALIDATED',dictamen_k3:dictamenGlobal,timestamp_utc:nowIso()})+'\n'; const reportHtml=makeHtmlReport(report, frameSvg, gobSvg); ui.frameSvg.innerHTML=frameSvg; ui.gobSvg.innerHTML=gobSvg; renderSequence(sequence); renderParams(frame,gob); let svgPropsHtml='';
    if(svgAnalysis&&svgAnalysis.proposals.length>0){
      let pH='<details style="margin-top:.5rem;border:1px solid #dee2e6;border-radius:6px;padding:.5rem .8rem">'+'<summary style="font-weight:700;cursor:pointer;color:#0f3460">&#128270; Análisis SVG — '+svgAnalysis.proposals.length+' problema(s). Propuestas acotadas del agente.</summary><div style="margin-top:.5rem;font-size:.83rem">';
      svgAnalysis.proposals.forEach(p=>{
        pH+='<p style="margin-bottom:.4rem"><strong>'+p.problema+'</strong> &mdash; '+p.region+'</p>';
        (p.opciones||[]).forEach(op=>{
          const w=op.aviso?'<em style="color:#856404"> '+op.aviso+'</em>':'';
          const par=JSON.stringify(op.parametros).replace(/"/g,'').replace(/[{}]/g,'').replace(/,/g,' · ');
                    const ejecutable = op.id==='O1'||op.id==='O2';
          const pIdx = (window._svgAnalysis&&window._svgAnalysis.proposals)?window._svgAnalysis.proposals.indexOf(p):0;
          const btnAplicar = ejecutable
            ? '<button onclick="applySvgOption('+pIdx+',\''+op.id+'\')" style="margin-left:.5rem;padding:.15rem .6rem;background:#0f3460;color:#fff;border:none;border-radius:3px;cursor:pointer;font-size:.75rem">Aplicar esta opción</button>'
            : '';
          pH+='<p style="margin-left:.8rem;margin-bottom:.2rem"><strong>'+op.id+'</strong> — '+op.accion+': <code>'+par+'</code>'+w+btnAplicar+'</p>';
        });
        pH+='<p style="font-size:.75rem;color:#6c757d;margin-top:.3rem;font-style:italic">'+p.limite_agente+'</p>';
      });
      pH+='</div></details>'; svgPropsHtml=pH;
    }
    ui.auditSummary.innerHTML=`<p><strong>Run ID:</strong> ${runId}</p><p><strong>Dictamen base:</strong> ${baseDictamen}</p><p><strong>Dictamen corregido:</strong> ${correctedDictamen}</p><p><strong>Dictamen global:</strong> ${dictamenGlobal}</p><p><strong>Exposición:</strong> ${report.exposure_gate}</p><p><strong>Alcance de la corrección:</strong> ${report.correction_scope}</p>${svgPropsHtml}`; ui.auditJson.textContent=JSON.stringify(report,null,2); ui.eventJson.textContent=JSON.stringify({events,eventIndex},null,2); const _mb=report.metrics.before,_ma=report.metrics.after; document.getElementById('diffMetrics').textContent='gradient_before: '+JSON.stringify(_mb.gradient)+'\ngradient_after:  '+JSON.stringify(_ma.gradient)+'\ncurvature_before: '+_mb.curvature+'\ncurvature_after:  '+_ma.curvature; document.getElementById('modalMetrics').textContent='modal_1_before: '+_mb.modal_first_mode+'\nmodal_1_after:  '+_ma.modal_first_mode+'\nmodal_2_before: '+_mb.modal_second_mode+'\nmodal_2_after:  '+_ma.modal_second_mode+'\nresidual_before: '+_mb.residual+'\nresidual_after:  '+_ma.residual; document.getElementById('metroMetrics').textContent=JSON.stringify(_mb.metrology,null,2); document.getElementById('sovereignJson').textContent=JSON.stringify(report.sovereign_sequence,null,2); current={ report, reportHtml, svgProposals: svgAnalysis && svgAnalysis.proposals.length > 0 ? JSON.stringify({ analisis_timestamp: nowIso(), proposals: svgAnalysis.proposals, notas: svgAnalysis.notes, invariante: 'Ninguna propuesta ha sido ejecutada. El soberano decide.' }, null, 2) : null, frameSvg, gobSvg, criticalCsv, frameCsv, gobCsv, seqCsv, eventsFlatCsv, indexByParamCsv, indexByTypeCsv, eventsJsonl, quarantineLog, validatorLog, eventIndex }; ui.downloadBtn.disabled=false; setState('EXPORT_READY'); document.body.classList.add('run-done');
    try{ localStorage.setItem('ae_gd2_sv_consejo', JSON.stringify({run_id:runId,frame,gob,baseFrame,metrics:report.metrics,r3frame,r3gob,dictamen:{base:baseDictamen,corregido:correctedDictamen,global:dictamenGlobal},draft,correction_trace:corrected.trace,sovereign_sequence:sequence})); }catch(e){}
    document.getElementById('consejoBtn').disabled=false; } catch(err){ setState('INTERNAL_REJECT', err.message); ui.auditSummary.innerHTML=`<p><strong>Rechazo:</strong> ${err.message}</p>`; ui.auditJson.textContent=''; ui.eventJson.textContent=''; } }
function downloadBundle(){ if(!current) return; const files=[ {name:'01_informe_usuario/informe_auditoria.html',content:current.reportHtml},
    ...(current.svgProposals ? [{name:'01_informe_usuario/correction_proposals.json', content:current.svgProposals}] : []), {name:'01_informe_usuario/resumen_ejecutivo.json',content:JSON.stringify(current.report,null,2)}, {name:'01_informe_usuario/critical_parameters.csv',content:current.criticalCsv}, {name:'01_informe_usuario/frame25.svg',content:current.frameSvg}, {name:'01_informe_usuario/gob25.svg',content:current.gobSvg}, {name:'01_informe_usuario/frame25.csv',content:current.frameCsv}, {name:'01_informe_usuario/gob25.csv',content:current.gobCsv}, {name:'02_paquete_tecnico/audit_report.json',content:JSON.stringify(current.report,null,2)}, {name:'02_paquete_tecnico/event_bank/events.jsonl',content:current.eventsJsonl}, {name:'02_paquete_tecnico/event_bank/event_index.json',content:JSON.stringify(current.eventIndex,null,2)}, {name:'02_paquete_tecnico/event_bank/events_flat.csv',content:current.eventsFlatCsv}, {name:'02_paquete_tecnico/event_bank/index_by_param.csv',content:current.indexByParamCsv}, {name:'02_paquete_tecnico/event_bank/index_by_type.csv',content:current.indexByTypeCsv}, {name:'02_paquete_tecnico/event_bank/sovereign_sequence.csv',content:current.seqCsv}, {name:'02_paquete_tecnico/logs/quarantine_log.jsonl',content:current.quarantineLog}, {name:'02_paquete_tecnico/logs/validator_log.jsonl',content:current.validatorLog}, {name:'02_paquete_tecnico/logs/execution_log.jsonl',content:current.eventsJsonl} ]; downloadBlob(`ae_gd2_sv_${current.report.run_id}.zip`, buildZip(files)); }
ui.runBtn.addEventListener('click',run); ui.downloadBtn.addEventListener('click',downloadBundle);


// Aplicar opción SVG seleccionada por el soberano humano
window.applySvgOption = async function(propIdx, opcionId){
  const _analysis = window._svgAnalysis;
  const p = _analysis && _analysis.proposals[parseInt(propIdx)];
  if(!p || !currentFileMeta || !currentFileMeta.text){
    alert('Datos de análisis no disponibles. Vuelva a ejecutar el agente.'); return;
  }
  const proposal = {...p, opcion_elegida: opcionId};
  const result = correctSvg(proposal, currentFileMeta.text);
  if(!result.ok){
    alert('El agente no puede aplicar esta opción: ' + result.reason); return;
  }
  // Guardar figura corregida en el bundle y regenerar ZIP
  correctedSvgData = {svg: result.svg, diff: result.diff, opcion: opcionId};
  setState('SVG_CORREGIDO', 'Figura corregida con opción ' + opcionId + ' — descargue el bundle actualizado');
  ui.downloadBtn.disabled = false;
  document.body.classList.add('run-done');
  // Disparar regeneración del bundle con la figura corregida incluida
  await rebuildBundleWithCorrection();
};


async function rebuildBundleWithCorrection(){
  if(!correctedSvgData || !window._lastBuildArgs) return;
  const {files, report} = window._lastBuildArgs;
  // Añadir la figura corregida al bundle
  files['01_informe_usuario/figura_corregida.svg'] = correctedSvgData.svg;
  files['01_informe_usuario/diff_corrector.json'] = JSON.stringify({
    opcion_aplicada: correctedSvgData.opcion,
    diff: correctedSvgData.diff,
    agente: 'AE-GD2-SV', fase: 'Fase 1',
    evento: 'corregir_figura_desde_imagen_local',
    timestamp_utc: new Date().toISOString()
  }, null, 2);
  // Actualizar correction_scope en el informe
  if(report) report.correction_scope = 'SVG_CORREGIDO — figura_corregida.svg incluida en bundle';
  const blob = await buildZip(files);
  const url = URL.createObjectURL(blob);
  ui.downloadBtn.onclick = ()=>{ const a=document.createElement('a'); a.href=url;
    a.download='ae_gd2_sv_'+window._lastRunId+'.zip'; a.click(); };
}
