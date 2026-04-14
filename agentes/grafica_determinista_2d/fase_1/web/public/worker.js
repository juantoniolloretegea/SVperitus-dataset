self.onmessage = (event) => { self.postMessage({ ok: true, echo: event.data }); };
