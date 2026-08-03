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
VM317:84 {url: 'https://www.itvia.online/pub/un-numero-sin-razon-r…r-un-enfermo/release/1?readingCollection=8719c263', title: 'Un número sin razón registrada puede acabar decidiendo por un enfermo · Artículos del Director', htmlLang: 'en', meta: Array(35), links: Array(7), …}
VM317:86 {
  "url": "https://www.itvia.online/pub/un-numero-sin-razon-registrada-puede-acabar-decidiendo-por-un-enfermo/release/1?readingCollection=8719c263",
  "title": "Un número sin razón registrada puede acabar decidiendo por un enfermo · Artículos del Director",
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
      "content": "Un número sin razón registrada puede acabar decidiendo por un enfermo"
    },
    {
      "name": "twitter:title",
      "property": null,
      "httpEquiv": null,
      "content": "Un número sin razón registrada puede acabar decidiendo por un enfermo · Artículos del Director"
    },
    {
      "name": "twitter:image:alt",
      "property": null,
      "httpEquiv": null,
      "content": "Un número sin razón registrada puede acabar decidiendo por un enfermo · Artículos del Director"
    },
    {
      "name": "citation_title",
      "property": null,
      "httpEquiv": null,
      "content": "Un número sin razón registrada puede acabar decidiendo por un enfermo"
    },
    {
      "name": "dc.title",
      "property": null,
      "httpEquiv": null,
      "content": "Un número sin razón registrada puede acabar decidiendo por un enfermo"
    },
    {
      "name": null,
      "property": "og:site_name",
      "httpEquiv": null,
      "content": "Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español® "
    },
    {
      "name": null,
      "property": "og:url",
      "httpEquiv": null,
      "content": "https://www.itvia.online/pub/un-numero-sin-razon-registrada-puede-acabar-decidiendo-por-un-enfermo/release/1"
    },
    {
      "name": null,
      "property": "og:type",
      "httpEquiv": null,
      "content": "book"
    },
    {
      "name": "citation_publisher",
      "property": null,
      "httpEquiv": null,
      "content": "IA eñ™ — La Biblia de la IA™ · ISSN 2695-6411 · Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA)."
    },
    {
      "name": "citation_book_title",
      "property": null,
      "httpEquiv": null,
      "content": "Artículos del Director"
    },
    {
      "name": "citation_isbn",
      "property": null,
      "httpEquiv": null,
      "content": null
    },
    {
      "name": "citation_date",
      "property": null,
      "httpEquiv": null,
      "content": null
    },
    {
      "name": "citation_pdf_url",
      "property": null,
      "httpEquiv": null,
      "content": "https://www.itvia.online/pub/un-numero-sin-razon-registrada-puede-acabar-decidiendo-por-un-enfermo/download/pdf"
    },
    {
      "name": "description",
      "property": null,
      "httpEquiv": null,
      "content": "La transparencia de la inteligencia artificial se ha convertido en un problema de procedencia. La procedencia dice de dónde viene un contenido; no dice por qué se decidió lo que en él se afirma."
    },
    {
      "name": null,
      "property": "og:description",
      "httpEquiv": null,
      "content": "La transparencia de la inteligencia artificial se ha convertido en un problema de procedencia. La procedencia dice de dónde viene un contenido; no dice por qué se decidió lo que en él se afirma."
    },
    {
      "name": "twitter:description",
      "property": null,
      "httpEquiv": null,
      "content": "La transparencia de la inteligencia artificial se ha convertido en un problema de procedencia. La procedencia dice de dónde viene un contenido; no dice por qué se decidió lo que en él se afirma."
    },
    {
      "name": null,
      "property": "og:image",
      "httpEquiv": null,
      "content": "https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/Logo_ITVIA_Terna-61783068097712.png"
    },
    {
      "name": null,
      "property": "og:image:url",
      "httpEquiv": null,
      "content": "https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/Logo_ITVIA_Terna-61783068097712.png"
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
      "content": "https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/Logo_ITVIA_Terna-61783068097712.png"
    },
    {
      "name": "citation_author",
      "property": null,
      "httpEquiv": null,
      "content": "Juan Antonio Lloret Egea"
    },
    {
      "name": "dc.creator",
      "property": null,
      "httpEquiv": null,
      "content": "Juan Antonio Lloret Egea"
    },
    {
      "name": null,
      "property": "article:published_time",
      "httpEquiv": null,
      "content": "Mon Aug 03 2026 00:00:00 GMT+0000 (Coordinated Universal Time)"
    },
    {
      "name": null,
      "property": "dc.date",
      "httpEquiv": null,
      "content": "2026-7-3"
    },
    {
      "name": "citation_publication_date",
      "property": null,
      "httpEquiv": null,
      "content": "2026/8/3"
    },
    {
      "name": null,
      "property": "dc.publisher",
      "httpEquiv": null,
      "content": "IA eñ™ — La Biblia de la IA™ · ISSN 2695-6411 · Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA)."
    },
    {
      "name": "citation_doi",
      "property": null,
      "httpEquiv": null,
      "content": "doi:10.21428/39829d0b.55593db8"
    },
    {
      "name": null,
      "property": "dc.identifier",
      "httpEquiv": null,
      "content": "doi:10.21428/39829d0b.55593db8"
    },
    {
      "name": null,
      "property": "prism.doi",
      "httpEquiv": null,
      "content": "doi:10.21428/39829d0b.55593db8"
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
      "content": "summary"
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
      "rel": "canonical",
      "href": "https://www.itvia.online/pub/un-numero-sin-razon-registrada-puede-acabar-decidiendo-por-un-enfermo",
      "type": null,
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
1?readingCollection=8719c263:1 Unchecked runtime.lastError: A listener indicated an asynchronous response by returning true, but the message channel closed before a response was received
1?readingCollection=8719c263:1 Unchecked runtime.lastError: A listener indicated an asynchronous response by returning true, but the message channel closed before a response was received
1?readingCollection=8719c263:1 Uncaught (in promise) Error: A listener indicated an asynchronous response by returning true, but the message channel closed before a response was received
1?readingCollection=8719c263:1 Uncaught (in promise) Error: A listener indicated an asynchronous response by returning true, but the message channel closed before a response was received
1?readingCollection=8719c263:1 Uncaught (in promise) Error: A listener indicated an asynchronous response by returning true, but the message channel closed before a response was received
