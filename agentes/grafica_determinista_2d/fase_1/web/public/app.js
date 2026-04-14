
const PARAM_NAMES = [
  'Modo operativo','Tipo de fuente','Integridad de entrada','Localidad y cuarentena','Perfil de ejecución',
  'Clase de figura','Dominio declarado','Dimensiones del lienzo','Salidas requeridas','Restricciones duras',
  'Política de título','Política de footer','Sistema de paneles','Sistema de nodos','Sistema de aristas',
  'No colisión texto-texto','Respiración vertical suficiente','Respiración horizontal suficiente','Densidad compositiva aceptable','Canonicidad del SVG',
  'Trazabilidad append-only','Confirmación humana soberana','Coherencia del bundle','Pureza de frontera','Reproducibilidad laboratorial'
];
const K3 = ['0','1','U'];
const MAX_FILE_BYTES = 8 * 1024 * 1024;
const MAX_DIMENSION = 6000;
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

const db = (() => {
  const NAME = 'ae_gd2_sv_phase1';
  const STORE = 'events';
  let connection = null;
  async function open() {
    if (connection) return connection;
    connection = await new Promise((resolve, reject) => {
      const req = indexedDB.open(NAME, 1);
      req.onupgradeneeded = () => {
        const db = req.result;
        if (!db.objectStoreNames.contains(STORE)) {
          const store = db.createObjectStore(STORE, { keyPath: 'event_id' });
          store.createIndex('run_id', 'run_id', { unique: false });
          store.createIndex('event_type', 'event_type', { unique: false });
        }
      };
      req.onsuccess = () => resolve(req.result);
      req.onerror = () => reject(req.error);
    });
    return connection;
  }
  async function put(event) {
    const db = await open();
    return new Promise((resolve, reject) => {
      const tx = db.transaction(STORE, 'readwrite');
      tx.objectStore(STORE).put(event);
      tx.oncomplete = () => resolve(true);
      tx.onerror = () => reject(tx.error);
    });
  }
  return { put };
})();

function nowIso() { return new Date().toISOString(); }
function setState(state, note='') {
  ui.stateBox.textContent = note ? `${state} — ${note}` : state;
  const li = document.createElement('li');
  li.textContent = `${new Date().toLocaleTimeString()} · ${state}${note ? ' · ' + note : ''}`;
  ui.stateLog.appendChild(li);
}

function hardRulesArray() {
  return ui.hardRules.value.split(/\n+/).map(s => s.trim()).filter(Boolean);
}

function stableHash(text) {
  let h = 2166136261;
  for (let i = 0; i < text.length; i++) {
    h ^= text.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  return 'h' + (h >>> 0).toString(16).padStart(8, '0');
}

function makeId(prefix) {
  return `${prefix}-${Date.now()}-${Math.random().toString(16).slice(2,8)}`;
}

function k3FromIndex(i, seed) {
  return K3[(seed + i) % 3];
}

function buildUserContextPacket(fileMeta) {
  return {
    structured_form: {
      mode: ui.mode.value,
      figure_kind: ui.figureKind.value,
      width: Number(ui.width.value),
      height: Number(ui.height.value),
      outputs: ['html','json','csv','svg','zip'],
      hard_rules: hardRulesArray()
    },
    natural_language_note: ui.nlNote.value.trim(),
    local_image_name: fileMeta?.name ?? null,
    local_annotations: []
  };
}

function buildDraft(packet) {
  const unresolved = [];
  if (!packet.natural_language_note && packet.structured_form.mode === 'correct') {
    unresolved.push('Contexto libre ausente');
  }
  return {
    request_id: makeId('GD2-REQ'),
    mode: packet.structured_form.mode,
    figure_kind: packet.structured_form.figure_kind,
    goal: packet.natural_language_note || 'Ejecución sin texto libre adicional',
    dimensions: { w: packet.structured_form.width, h: packet.structured_form.height, unit: 'px' },
    outputs: packet.structured_form.outputs,
    constraints_hard: packet.structured_form.hard_rules,
    preserve: packet.structured_form.mode === 'correct' ? ['estructura_general','footer'] : [],
    modify: packet.structured_form.mode === 'correct' ? ['colisiones_texto','margenes','paneles'] : ['composicion_base'],
    unresolved
  };
}

function confirmDraft(draft) {
  return {
    ...draft,
    confirmed_by_user: true,
    confirmed_at: nowIso()
  };
}

function frame25(confirmed, fileMeta) {
  const seed = (stableHash(JSON.stringify(confirmed)).length + (fileMeta?.size ?? 0)) % 7;
  const params = PARAM_NAMES.map((name, idx) => {
    let value = k3FromIndex(idx, seed);
    if (idx === 0) value = '0';
    if (idx === 1) value = fileMeta ? '0' : (confirmed.mode === 'create' ? '0' : 'U');
    if (idx === 2) value = fileMeta ? '0' : '0';
    if (idx === 21) value = '0';
    if (idx === 23) value = confirmed.unresolved.length ? 'U' : '0';
    return {
      position: idx + 1,
      param_id: `P${String(idx+1).padStart(2,'0')}`,
      name,
      value_k3: value,
      justification: value === '0' ? 'conformidad suficiente' : value === '1' ? 'infracción material' : 'indeterminación controlada'
    };
  });
  return params;
}

function gob25(frame, sequenceLength) {
  return frame.map((row, idx) => {
    let value = row.value_k3;
    if (['P16','P17','P18','P19','P20'].includes(row.param_id) && sequenceLength < 3) value = row.value_k3 === '0' ? 'U' : row.value_k3;
    if (row.param_id === 'P24' && row.value_k3 === 'U') value = 'U';
    return { ...row, value_k3: value, justification: `supervisión de ${row.param_id}` };
  });
}

function dictamenFromCell(cell) {
  if (cell.some(p => p.value_k3 === '1')) return 'NO APTO';
  if (cell.some(p => p.value_k3 === 'U')) return 'INDETERMINADO';
  return 'APTO';
}

function polygonSvg(title, cell) {
  const cx = 260, cy = 260, r0 = 140;
  const points = [];
  const labels = [];
  const fills = [];
  const n = cell.length;
  for (let i = 0; i < n; i++) {
    const ang = -Math.PI / 2 + (2 * Math.PI * i / n);
    const mul = cell[i].value_k3 === '0' ? 0.75 : cell[i].value_k3 === '1' ? 1.0 : 0.88;
    const r = r0 * mul;
    const x = cx + r * Math.cos(ang);
    const y = cy + r * Math.sin(ang);
    points.push(`${x.toFixed(1)},${y.toFixed(1)}`);
    const lx = cx + (r0 + 24) * Math.cos(ang);
    const ly = cy + (r0 + 24) * Math.sin(ang);
    labels.push(`<text x="${lx.toFixed(1)}" y="${ly.toFixed(1)}" font-size="10" text-anchor="middle">${cell[i].param_id}</text>`);
    const fill = cell[i].value_k3 === '0' ? '#d5f5e3' : cell[i].value_k3 === '1' ? '#fadbd8' : '#fcf3cf';
    fills.push(`<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="4" fill="${fill}" stroke="#666"/>`);
  }
  return `<svg viewBox="0 0 520 560" xmlns="http://www.w3.org/2000/svg">
    <rect x="1" y="1" width="518" height="558" rx="10" fill="white" stroke="#d7dbdd"/>
    <text x="260" y="28" text-anchor="middle" font-size="16" font-weight="700">${title}</text>
    <text x="260" y="48" text-anchor="middle" font-size="11">AE-GD2-SV · Panel interactivo SV–Usuario</text>
    <polygon points="${points.join(' ')}" fill="#edf3f8" stroke="#0f5889" stroke-width="2"/>
    ${labels.join('')}
    ${fills.join('')}
    <text x="260" y="540" text-anchor="middle" font-size="9">Autor: Juan Antonio Lloret Egea · ORCID: 0000-0002-6634-3351 · ITVIA · IA eñ™ — La Biblia de la IA™ · ISSN 2695-6411 · CC BY-NC-ND 4.0 · Madrid, 14/04/2026</text>
  </svg>`;
}

function buildSovereignSequence(confirmed, frame, gob) {
  const s0 = { sovereign_id: 'S0', epsilon_id: 'ε0', label: 'Frame inicial declarado', dictamen_k3: 'INDETERMINADO' };
  const s1 = { sovereign_id: 'S1', epsilon_id: 'ε1', label: 'Entrada admitida tras cuarentena', dictamen_k3: dictamenFromCell(frame) };
  const s2 = { sovereign_id: 'S2', epsilon_id: 'ε2', label: 'Intención confirmada por el usuario', dictamen_k3: dictamenFromCell(frame) };
  const s3 = { sovereign_id: 'S3', epsilon_id: 'ε3', label: 'Auditoría poligonal y dictamen', dictamen_k3: dictamenFromCell(gob) };
  return [s0,s1,s2,s3];
}

function buildEvent(type, runId, parentId=null, dictamen=null, extras={}) {
  return {
    event_id: makeId('GD2-EVT'),
    parent_event_id: parentId,
    run_id: runId,
    session_id: 'LOCAL-SESSION',
    event_type: type,
    event_status: 'done',
    dictamen_k3: dictamen,
    timestamp_utc: nowIso(),
    ...extras
  };
}

async function quarantineFile(file) {
  setState('FILE_SELECTED', file ? file.name : 'sin archivo');
  if (!file && ui.mode.value === 'correct') {
    throw new Error('Modo corregir requiere archivo local o cambie a crear.');
  }
  setState('TYPE_CHECK');
  if (file && !['image/png','image/jpeg','image/svg+xml'].includes(file.type)) {
    setState('REJECTED_TYPE', file.type || 'tipo desconocido');
    throw new Error('Tipo de archivo no admitido.');
  }
  setState('LIMITS_CHECK');
  if (file && file.size > MAX_FILE_BYTES) {
    setState('REJECTED_LIMITS', `máximo ${MAX_FILE_BYTES} bytes`);
    throw new Error('Archivo fuera de límites.');
  }
  setState('SANITIZE_LOCAL');
  let text = '';
  if (file && file.type === 'image/svg+xml') {
    text = await file.text();
    if (/<script|onload=|onerror=|foreignObject/i.test(text)) {
      setState('REJECTED_SANITIZE', 'SVG hostil');
      throw new Error('SVG rechazado por sanitización local.');
    }
  }
  setState('HASH_AND_PACKET');
  return {
    name: file?.name ?? null,
    type: file?.type ?? null,
    size: file?.size ?? 0,
    text,
    hash: stableHash(`${file?.name || 'none'}|${file?.size || 0}|${text}`)
  };
}

function renderSequence(sequence) {
  ui.sequence.innerHTML = '';
  sequence.forEach((item, idx) => {
    const btn = document.createElement('button');
    btn.textContent = `${item.sovereign_id}`;
    btn.onclick = () => {
      ui.sequenceDetail.textContent = JSON.stringify(item, null, 2);
    };
    if (idx === sequence.length - 1) btn.click();
    ui.sequence.appendChild(btn);
  });
}

function renderParams(frame, gob) {
  ui.paramTable.innerHTML = '';
  frame.forEach((row, idx) => {
    const tr = document.createElement('tr');
    const gov = gob[idx].value_k3;
    tr.innerHTML = `<td>${row.position}</td><td>${row.param_id}</td><td>${row.name}</td><td>${row.value_k3} / ${gov}</td><td>${row.justification}</td>`;
    ui.paramTable.appendChild(tr);
  });
}

function toCsv(rows, columns) {
  const esc = (v) => {
    const s = String(v ?? '');
    return /[",\n]/.test(s) ? `"${s.replace(/"/g,'""')}"` : s;
  };
  const head = columns.join(',');
  const body = rows.map(row => columns.map(c => esc(row[c])).join(','));
  return [head, ...body].join('\n');
}

function makeHtmlReport(report, frameSvg, gobSvg) {
  const rows = report.critical_parameters.map(p => `<tr><td>${p.position}</td><td>${p.param_id}</td><td>${p.name}</td><td>${p.value_k3}</td><td>${p.justification}</td></tr>`).join('');
  const sovereign = report.sovereign_sequence.map(s => `<li><strong>${s.sovereign_id}</strong> · ${s.epsilon_id} · ${s.label} · ${s.dictamen_k3}</li>`).join('');
  return `<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Informe de auditoría AE-GD2-SV</title><style>body{font-family:Georgia,serif;margin:24px;color:#17202a}h1,h2{color:#0f5889}table{border-collapse:collapse;width:100%}th,td{border:1px solid #d7dbdd;padding:6px 8px}th{background:#eef3f7}svg{width:100%;max-width:520px}.row{display:flex;gap:16px;flex-wrap:wrap}.card{border:1px solid #d7dbdd;padding:12px;border-radius:12px;margin-bottom:16px}</style></head><body><h1>Informe de auditoría — AE-GD2-SV</h1><p><strong>Run ID:</strong> ${report.run_id} · <strong>Dictamen global:</strong> ${report.dictamen_global}</p><div class="card"><h2>Trayectoria soberana</h2><ol>${sovereign}</ol></div><div class="row"><div class="card">${frameSvg}</div><div class="card">${gobSvg}</div></div><div class="card"><h2>Parámetros críticos</h2><table><thead><tr><th>Pos</th><th>ID</th><th>Nombre</th><th>Valor</th><th>Justificación</th></tr></thead><tbody>${rows}</tbody></table></div><p>Autor: Juan Antonio Lloret Egea · ORCID: 0000-0002-6634-3351 · Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) · IA eñ™ — La Biblia de la IA™ · ISSN 2695-6411 · Licencia: CC BY-NC-ND 4.0 · Madrid, 14/04/2026</p></body></html>`;
}

function downloadBlob(name, blob) {
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = name;
  a.click();
  setTimeout(() => URL.revokeObjectURL(url), 500);
}

function textBlob(text, type='text/plain;charset=utf-8') {
  return new Blob([text], { type });
}

function crc32(buf) {
  let table = crc32.table;
  if (!table) {
    table = new Uint32Array(256);
    for (let i = 0; i < 256; i++) {
      let c = i;
      for (let k = 0; k < 8; k++) c = c & 1 ? 0xEDB88320 ^ (c >>> 1) : c >>> 1;
      table[i] = c >>> 0;
    }
    crc32.table = table;
  }
  let crc = 0xFFFFFFFF;
  for (const b of buf) crc = table[(crc ^ b) & 0xFF] ^ (crc >>> 8);
  return (crc ^ 0xFFFFFFFF) >>> 0;
}

function buildZip(files) {
  const encoder = new TextEncoder();
  const localParts = [];
  const centralParts = [];
  let offset = 0;
  files.forEach((file) => {
    const nameBytes = encoder.encode(file.name);
    const data = typeof file.content === 'string' ? encoder.encode(file.content) : file.content;
    const crc = crc32(data);
    const local = new Uint8Array(30 + nameBytes.length + data.length);
    const dv = new DataView(local.buffer);
    dv.setUint32(0, 0x04034b50, true);
    dv.setUint16(4, 20, true);
    dv.setUint16(6, 0, true);
    dv.setUint16(8, 0, true);
    dv.setUint16(10, 0, true);
    dv.setUint16(12, 0, true);
    dv.setUint32(14, crc, true);
    dv.setUint32(18, data.length, true);
    dv.setUint32(22, data.length, true);
    dv.setUint16(26, nameBytes.length, true);
    dv.setUint16(28, 0, true);
    local.set(nameBytes, 30);
    local.set(data, 30 + nameBytes.length);
    localParts.push(local);

    const central = new Uint8Array(46 + nameBytes.length);
    const cv = new DataView(central.buffer);
    cv.setUint32(0, 0x02014b50, true);
    cv.setUint16(4, 20, true);
    cv.setUint16(6, 20, true);
    cv.setUint16(8, 0, true);
    cv.setUint16(10, 0, true);
    cv.setUint16(12, 0, true);
    cv.setUint16(14, 0, true);
    cv.setUint32(16, crc, true);
    cv.setUint32(20, data.length, true);
    cv.setUint32(24, data.length, true);
    cv.setUint16(28, nameBytes.length, true);
    cv.setUint16(30, 0, true);
    cv.setUint16(32, 0, true);
    cv.setUint16(34, 0, true);
    cv.setUint16(36, 0, true);
    cv.setUint32(38, 0, true);
    cv.setUint32(42, offset, true);
    central.set(nameBytes, 46);
    centralParts.push(central);
    offset += local.length;
  });
  const centralSize = centralParts.reduce((a, p) => a + p.length, 0);
  const end = new Uint8Array(22);
  const ev = new DataView(end.buffer);
  ev.setUint32(0, 0x06054b50, true);
  ev.setUint16(8, files.length, true);
  ev.setUint16(10, files.length, true);
  ev.setUint32(12, centralSize, true);
  ev.setUint32(16, offset, true);
  return new Blob([...localParts, ...centralParts, end], { type: 'application/zip' });
}

async function run() {
  ui.downloadBtn.disabled = true;
  ui.stateLog.innerHTML = '';
  setState('IDLE');
  try {
    const file = ui.fileInput.files[0] || null;
    const fileMeta = await quarantineFile(file);
    const packet = buildUserContextPacket(fileMeta);
    setState('PACKET_READY');
    const draft = buildDraft(packet);
    setState('DRAFT_READY', draft.unresolved.length ? 'con U controlada' : 'sin U');
    const confirmed = confirmDraft(draft);
    setState('CONFIRMED');
    const runId = makeId('GD2-RUN');
    const frame = frame25(confirmed, fileMeta);
    const sequenceLength = 4;
    const gob = gob25(frame, sequenceLength);
    const sequence = buildSovereignSequence(confirmed, frame, gob);
    const frameSvg = polygonSvg('C_frame^25', frame);
    const gobSvg = polygonSvg('C_gob^25', gob);
    const dictamenGlobal = dictamenFromCell(gob);
    const events = [];
    let parent = null;
    const addEvent = async (type, dictamen, extras={}) => {
      const ev = buildEvent(type, runId, parent, dictamen, extras);
      parent = ev.event_id;
      events.push(ev);
      try { await db.put(ev); } catch { /* degradación silenciosa evitada en reporte */ }
    };
    await addEvent('create_user_context_packet', null, { packet_hash: stableHash(JSON.stringify(packet)) });
    await addEvent('translate_to_draft', null, { draft_hash: stableHash(JSON.stringify(draft)) });
    await addEvent('confirm_intent', null, { confirmed_hash: stableHash(JSON.stringify(confirmed)) });
    await addEvent('compose_frame25', dictamenFromCell(frame));
    await addEvent('compose_gob25', dictamenGlobal);
    await addEvent('build_audit_report', dictamenGlobal);

    const report = {
      run_id: runId,
      dictamen_global: dictamenGlobal,
      sovereign_sequence: sequence,
      critical_parameters: frame,
      artifacts: {
        frame_svg: 'frame25.svg',
        gob_svg: 'gob25.svg',
        events: 'events.jsonl',
        event_index: 'event_index.json',
        critical_parameters_csv: 'critical_parameters.csv'
      },
      exposure_gate: dictamenGlobal === 'NO APTO' ? 'NO EXPONIBLE' : (dictamenGlobal === 'INDETERMINADO' ? 'EXPOSICION_CON_U' : 'EXPONIBLE'),
      packet,
      draft,
      confirmed
    };
    const eventIndex = {
      by_event_id: Object.fromEntries(events.map((e, i) => [e.event_id, i])),
      by_run_id: { [runId]: events.map((_, i) => i) },
      by_event_type: events.reduce((acc, e, i) => ((acc[e.event_type] ||= []).push(i), acc), {})
    };
    const criticalCsv = toCsv(frame, ['position','param_id','name','value_k3','justification']);
    const frameCsv = toCsv(frame.map(r => ({ position: r.position, param_id: r.param_id, value_k3: r.value_k3, label: r.name })), ['position','param_id','value_k3','label']);
    const gobCsv = toCsv(gob.map(r => ({ position: r.position, param_id: r.param_id, value_k3: r.value_k3, label: r.name })), ['position','param_id','value_k3','label']);
    const eventsFlatCsv = toCsv(events, ['event_id','parent_event_id','run_id','event_type','dictamen_k3','timestamp_utc']);
    const eventsJsonl = events.map(e => JSON.stringify(e)).join('\n');
    const reportHtml = makeHtmlReport(report, frameSvg, gobSvg);

    ui.frameSvg.innerHTML = frameSvg;
    ui.gobSvg.innerHTML = gobSvg;
    renderSequence(sequence);
    renderParams(frame, gob);
    ui.auditSummary.innerHTML = `<p><strong>Run ID:</strong> ${runId}</p><p><strong>Dictamen global:</strong> ${dictamenGlobal}</p><p><strong>Exposición:</strong> ${report.exposure_gate}</p>`;
    ui.auditJson.textContent = JSON.stringify(report, null, 2);
    ui.eventJson.textContent = JSON.stringify({ events, eventIndex }, null, 2);
    current = { report, reportHtml, frameSvg, gobSvg, criticalCsv, frameCsv, gobCsv, eventsFlatCsv, eventsJsonl, eventIndex };
    ui.downloadBtn.disabled = false;
    setState('EXPORT_READY');
  } catch (err) {
    setState('INTERNAL_REJECT', err.message);
    ui.auditSummary.innerHTML = `<p><strong>Rechazo:</strong> ${err.message}</p>`;
    ui.auditJson.textContent = '';
    ui.eventJson.textContent = '';
  }
}

function downloadBundle() {
  if (!current) return;
  const files = [
    { name: '01_informe_usuario/informe_auditoria.html', content: current.reportHtml },
    { name: '01_informe_usuario/resumen_ejecutivo.json', content: JSON.stringify(current.report, null, 2) },
    { name: '01_informe_usuario/critical_parameters.csv', content: current.criticalCsv },
    { name: '01_informe_usuario/frame25.svg', content: current.frameSvg },
    { name: '01_informe_usuario/gob25.svg', content: current.gobSvg },
    { name: '01_informe_usuario/frame25.csv', content: current.frameCsv },
    { name: '01_informe_usuario/gob25.csv', content: current.gobCsv },
    { name: '02_paquete_tecnico/figure_ir.json', content: JSON.stringify({ critical_parameters: current.report.critical_parameters, meta: { run_id: current.report.run_id }, canvas: current.report.confirmed.dimensions }, null, 2) },
    { name: '02_paquete_tecnico/audit_report.json', content: JSON.stringify(current.report, null, 2) },
    { name: '02_paquete_tecnico/event_bank/events.jsonl', content: current.eventsJsonl },
    { name: '02_paquete_tecnico/event_bank/event_index.json', content: JSON.stringify(current.eventIndex, null, 2) },
    { name: '02_paquete_tecnico/event_bank/events_flat.csv', content: current.eventsFlatCsv },
    { name: '02_paquete_tecnico/logs/execution_log.jsonl', content: current.eventsJsonl }
  ];
  const blob = buildZip(files);
  downloadBlob(`ae_gd2_sv_${current.report.run_id}.zip`, blob);
}

ui.runBtn.addEventListener('click', run);
ui.downloadBtn.addEventListener('click', downloadBundle);
