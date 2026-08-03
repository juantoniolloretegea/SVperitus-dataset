express-utils.js:18 [Intervention] Slow network is detected. See https://www.chromestatus.com/feature/5636954674692096 for more details. Fallback font will be used while loading: chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/browser/css/fonts/AdobeClean-Regular.otf
express-utils.js:18 [Intervention] Slow network is detected. See https://www.chromestatus.com/feature/5636954674692096 for more details. Fallback font will be used while loading: chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/browser/css/fonts/AdobeClean-Bold.otf
(index):1 Unchecked runtime.lastError: A listener indicated an asynchronous response by returning true, but the message channel closed before a response was received
(index):1 Uncaught (in promise) Error: A listener indicated an asynchronous response by returning true, but the message channel closed before a response was received
(index):1 Unchecked runtime.lastError: A listener indicated an asynchronous response by returning true, but the message channel closed before a response was received
(async () => {
  const response = await fetch(location.href, {
    cache: "no-store",
    credentials: "same-origin"
  });

  const html = await response.text();

  const documentFromServer =
    new DOMParser().parseFromString(
      html,
      "text/html"
    );

  const head =
    documentFromServer.head;

  const metadata = {
    url: location.href,

    title:
      head.querySelector("title")
        ?.textContent
        ?.trim() || null,

    htmlLang:
      documentFromServer
        .documentElement
        .getAttribute("lang"),

    meta: Array.from(
      head.querySelectorAll("meta")
    ).map((element) => ({
      name:
        element.getAttribute("name"),

      property:
        element.getAttribute("property"),

      httpEquiv:
        element.getAttribute("http-equiv"),

      content:
        element.getAttribute("content")
    })),

    links: Array.from(
      head.querySelectorAll("link")
    ).map((element) => ({
      rel:
        element.getAttribute("rel"),

      href:
        element.getAttribute("href"),

      type:
        element.getAttribute("type"),

      hreflang:
        element.getAttribute("hreflang")
    })),

    jsonLd: Array.from(
      head.querySelectorAll(
        'script[type="application/ld+json"]'
      )
    ).map((element) => {
      try {
        return JSON.parse(
          element.textContent
        );
      } catch {
        return {
          error:
            "JSON-LD no válido",

          raw:
            element.textContent
        };
      }
    })
  };

  console.log(metadata);

  console.log(
    JSON.stringify(
      metadata,
      null,
      2
    )
  );

  if (
    typeof copy ===
    "function"
  ) {
    copy(
      JSON.stringify(
        metadata,
        null,
        2
      )
    );

    console.log(
      "Resultado copiado al portapapeles."
    );
  }
})();
Promise {<pending>}
VM408:84 {url: 'https://www.itvia.online/', title: 'Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español®', htmlLang: 'en', meta: Array(22), links: Array(6), …}
VM408:86 {
  "url": "https://www.itvia.online/",
  "title": "Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español®",
  "htmlLang": "en",
  "meta": [
    {
      "name": null,
      "property": null,
      "httpEquiv": null,
      "content": null
    },
    {
      "name": null,
      "property": "og:title",
      "httpEquiv": null,
      "content": "Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español® "
    },
    {
      "name": "twitter:title",
      "property": null,
      "httpEquiv": null,
      "content": "Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español® "
    },
    {
      "name": "twitter:image:alt",
      "property": null,
      "httpEquiv": null,
      "content": "Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español® "
    },
    {
      "name": "citation_title",
      "property": null,
      "httpEquiv": null,
      "content": "Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español® "
    },
    {
      "name": "dc.title",
      "property": null,
      "httpEquiv": null,
      "content": "Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español® "
    },
    {
      "name": null,
      "property": "og:site_name",
      "httpEquiv": null,
      "content": "Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español® "
    },
    {
      "name": "citation_journal_title",
      "property": null,
      "httpEquiv": null,
      "content": "Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español® "
    },
    {
      "name": null,
      "property": "og:url",
      "httpEquiv": null,
      "content": "https://www.itvia.online/"
    },
    {
      "name": null,
      "property": "og:type",
      "httpEquiv": null,
      "content": "website"
    },
    {
      "name": "description",
      "property": null,
      "httpEquiv": null,
      "content": "Instituto tecnológico virtual de la Inteligencia Artificial para el español "
    },
    {
      "name": null,
      "property": "og:description",
      "httpEquiv": null,
      "content": "Instituto tecnológico virtual de la Inteligencia Artificial para el español "
    },
    {
      "name": "twitter:description",
      "property": null,
      "httpEquiv": null,
      "content": "Instituto tecnológico virtual de la Inteligencia Artificial para el español "
    },
    {
      "name": null,
      "property": "og:image",
      "httpEquiv": null,
      "content": "https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/4._Acuerdo_entre_humano_y_humanoide-11776112621275.png"
    },
    {
      "name": null,
      "property": "og:image:url",
      "httpEquiv": null,
      "content": "https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/4._Acuerdo_entre_humano_y_humanoide-11776112621275.png"
    },
    {
      "name": null,
      "property": "og:image:width",
      "httpEquiv": null,
      "content": "500"
    },
    {
      "name": "twitter:image",
      "property": null,
      "httpEquiv": null,
      "content": "https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/4._Acuerdo_entre_humano_y_humanoide-11776112621275.png"
    },
    {
      "name": null,
      "property": "fb:app_id",
      "httpEquiv": null,
      "content": "924988584221879"
    },
    {
      "name": "twitter:card",
      "property": null,
      "httpEquiv": null,
      "content": "summary_large_image"
    },
    {
      "name": "twitter:site",
      "property": null,
      "httpEquiv": null,
      "content": "@pubpub"
    },
    {
      "name": "viewport",
      "property": null,
      "httpEquiv": null,
      "content": "width=device-width, initial-scale=1, shrink-to-fit=no"
    },
    {
      "name": "google-site-verification",
      "property": null,
      "httpEquiv": null,
      "content": "jmmJFnkSOeIEuS54adOzGMwc0kwpsa8wQ-L4GyPpPDg"
    }
  ],
  "links": [
    {
      "rel": "alternate",
      "href": "https://www.itvia.online/rss.xml",
      "type": "application/rss+xml",
      "hreflang": null
    },
    {
      "rel": "icon",
      "href": "https://assets.pubpub.org/wlbdk7f8/61593841885420.jpg",
      "type": "image/png",
      "hreflang": null
    },
    {
      "rel": "preconnect",
      "href": "https://assets.pubpub.org",
      "type": null,
      "hreflang": null
    },
    {
      "rel": "stylesheet",
      "href": "https://assets.pubpub.org/_fonts/8da286c6/fonts.css",
      "type": null,
      "hreflang": null
    },
    {
      "rel": "stylesheet",
      "href": "/dist/main.4d119aeb5b1b71126c42.css",
      "type": "text/css",
      "hreflang": null
    },
    {
      "rel": "search",
      "href": "/opensearch.xml",
      "type": "application/opensearchdescription+xml",
      "hreflang": null
    }
  ],
  "jsonLd": []
}
