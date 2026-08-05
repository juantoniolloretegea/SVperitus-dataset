<html lang="en"><head><title>Línea del Umbral SV, circulación de retorno del dominio-universo y átomo formal de ascendencia no agotada</title><meta charSet="utf-8"/><link rel="stylesheet" href="https://assets.pubpub.org/_fonts/8da286c6/fonts.css"/><style type="text/css">/* Imports the equivalent of components/Editor/styles/base.scss,
but without the media query mixin, which breaks PagedJS-cli:
https://gitlab.pagedmedia.org/tools/pagedjs-cli/issues/11 */
.ProseMirror {
  position: relative;
}

.ProseMirror {
  word-wrap: break-word;
  white-space: pre-wrap;
  white-space: break-spaces;
  -webkit-font-variant-ligatures: none;
  font-variant-ligatures: none;
  font-feature-settings: "liga" 0; /* the above doesn't seem to work in Edge */
}

.ProseMirror pre {
  white-space: pre-wrap;
}

.ProseMirror li {
  position: relative;
}

.ProseMirror-hideselection *::selection {
  background: transparent;
}

.ProseMirror-hideselection *::-moz-selection {
  background: transparent;
}

.ProseMirror-hideselection {
  caret-color: transparent;
}

/* See https://github.com/ProseMirror/prosemirror/issues/1421#issuecomment-1759320191 */
.ProseMirror [draggable][contenteditable=false] {
  user-select: text;
}

.ProseMirror-selectednode {
  outline: 2px solid #8cf;
}

/* Make sure li selections wrap around markers */
li.ProseMirror-selectednode {
  outline: none;
}

li.ProseMirror-selectednode:after {
  content: "";
  position: absolute;
  left: -32px;
  right: -2px;
  top: -2px;
  bottom: -2px;
  border: 2px solid #8cf;
  pointer-events: none;
}

/* Protect against generic img rules */
img.ProseMirror-separator {
  display: inline !important;
  border: none !important;
  margin: 0 !important;
}

.ProseMirror-gapcursor {
  display: none;
  pointer-events: none;
  position: absolute;
}

.ProseMirror-gapcursor:after {
  content: "";
  display: block;
  position: absolute;
  top: -2px;
  width: 20px;
  border-top: 1px solid black;
  animation: ProseMirror-cursor-blink 1.1s steps(2, start) infinite;
}

@keyframes ProseMirror-cursor-blink {
  to {
    visibility: hidden;
  }
}
.ProseMirror-focused .ProseMirror-gapcursor {
  display: block;
}

.ProseMirror .tableWrapper {
  overflow-x: auto;
}

.ProseMirror table {
  border-collapse: collapse;
  table-layout: fixed;
  width: 100%;
  overflow: hidden;
}

.ProseMirror td,
.ProseMirror th {
  vertical-align: top;
  box-sizing: border-box;
  position: relative;
}

.ProseMirror td:not([data-colwidth]):not(.column-resize-dragging),
.ProseMirror th:not([data-colwidth]):not(.column-resize-dragging) {
  /* if there's no explicit width set and the column is not being resized, set a default width */
  min-width: var(--default-cell-min-width);
}

.ProseMirror .column-resize-handle {
  position: absolute;
  right: -2px;
  top: 0;
  bottom: 0;
  width: 4px;
  z-index: 20;
  background-color: #adf;
  pointer-events: none;
}

.ProseMirror.resize-cursor {
  cursor: ew-resize;
  cursor: col-resize;
}

/* Give selected cells a blue overlay */
.ProseMirror .selectedCell:after {
  z-index: 2;
  position: absolute;
  content: "";
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  background: rgba(200, 200, 255, 0.4);
  pointer-events: none;
}

/*---------------------------------------------------------
 *  Author: Benjamin R. Bray
 *  License: MIT (see LICENSE in project root for details)
 *--------------------------------------------------------*/
/* == Math Nodes ======================================== */
.math-node {
  min-width: 1em;
  min-height: 1em;
  font-size: 0.95em;
  font-family: "Consolas", "Ubuntu Mono", monospace;
  cursor: auto;
}

.math-node.empty-math .math-render::before {
  content: "(empty)";
  color: red;
}

.math-node .math-render.parse-error::before {
  content: "(math error)";
  color: red;
  cursor: help;
}

.math-node.ProseMirror-selectednode {
  outline: none;
}

.math-node .math-src {
  display: none;
  color: rgb(132, 33, 162);
  tab-size: 4;
}

.math-node.ProseMirror-selectednode .math-src {
  display: inline;
}

.math-node.ProseMirror-selectednode .math-render {
  display: none;
}

/* -- Inline Math --------------------------------------- */
math-inline {
  display: inline;
  white-space: nowrap;
}

math-inline .math-render {
  display: inline-block;
  font-size: 0.85em;
  cursor: pointer;
}

math-inline .math-src .ProseMirror {
  display: inline;
  /* Necessary to fix FireFox bug with contenteditable, https://bugzilla.mozilla.org/show_bug.cgi?id=1252108 */
  border-right: 1px solid transparent;
  border-left: 1px solid transparent;
}

math-inline .math-src::after, math-inline .math-src::before {
  content: "$";
  color: #b0b0b0;
}

/* -- Block Math ---------------------------------------- */
math-display {
  display: block;
}

math-display .math-render {
  display: block;
}

math-display.ProseMirror-selectednode {
  background-color: #eee;
}

math-display .math-src .ProseMirror {
  width: 100%;
  display: block;
}

math-display .math-src::after, math-display .math-src::before {
  content: "$$";
  text-align: left;
  color: #b0b0b0;
}

math-display .katex-display {
  margin: 0;
}

/* -- Selection Plugin ---------------------------------- */
p::selection, p > *::selection {
  background-color: #c0c0c0;
}

.katex-html *::selection {
  background-color: none !important;
}

.math-node.math-select .math-render {
  background-color: silver;
}

math-inline.math-select .math-render {
  padding-top: 2px;
}

@font-face {
  font-family: KaTeX_AMS;
  font-style: normal;
  font-weight: 400;
  src: url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_AMS-Regular.woff2) format("woff2"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_AMS-Regular.woff) format("woff"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_AMS-Regular.ttf) format("truetype");
}
@font-face {
  font-family: KaTeX_Caligraphic;
  font-style: normal;
  font-weight: 700;
  src: url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Caligraphic-Bold.woff2) format("woff2"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Caligraphic-Bold.woff) format("woff"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Caligraphic-Bold.ttf) format("truetype");
}
@font-face {
  font-family: KaTeX_Caligraphic;
  font-style: normal;
  font-weight: 400;
  src: url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Caligraphic-Regular.woff2) format("woff2"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Caligraphic-Regular.woff) format("woff"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Caligraphic-Regular.ttf) format("truetype");
}
@font-face {
  font-family: KaTeX_Fraktur;
  font-style: normal;
  font-weight: 700;
  src: url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Fraktur-Bold.woff2) format("woff2"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Fraktur-Bold.woff) format("woff"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Fraktur-Bold.ttf) format("truetype");
}
@font-face {
  font-family: KaTeX_Fraktur;
  font-style: normal;
  font-weight: 400;
  src: url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Fraktur-Regular.woff2) format("woff2"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Fraktur-Regular.woff) format("woff"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Fraktur-Regular.ttf) format("truetype");
}
@font-face {
  font-family: KaTeX_Main;
  font-style: normal;
  font-weight: 700;
  src: url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Main-Bold.woff2) format("woff2"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Main-Bold.woff) format("woff"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Main-Bold.ttf) format("truetype");
}
@font-face {
  font-family: KaTeX_Main;
  font-style: italic;
  font-weight: 700;
  src: url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Main-BoldItalic.woff2) format("woff2"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Main-BoldItalic.woff) format("woff"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Main-BoldItalic.ttf) format("truetype");
}
@font-face {
  font-family: KaTeX_Main;
  font-style: italic;
  font-weight: 400;
  src: url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Main-Italic.woff2) format("woff2"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Main-Italic.woff) format("woff"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Main-Italic.ttf) format("truetype");
}
@font-face {
  font-family: KaTeX_Main;
  font-style: normal;
  font-weight: 400;
  src: url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Main-Regular.woff2) format("woff2"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Main-Regular.woff) format("woff"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Main-Regular.ttf) format("truetype");
}
@font-face {
  font-family: KaTeX_Math;
  font-style: italic;
  font-weight: 700;
  src: url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Math-BoldItalic.woff2) format("woff2"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Math-BoldItalic.woff) format("woff"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Math-BoldItalic.ttf) format("truetype");
}
@font-face {
  font-family: KaTeX_Math;
  font-style: italic;
  font-weight: 400;
  src: url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Math-Italic.woff2) format("woff2"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Math-Italic.woff) format("woff"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Math-Italic.ttf) format("truetype");
}
@font-face {
  font-family: "KaTeX_SansSerif";
  font-style: normal;
  font-weight: 700;
  src: url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_SansSerif-Bold.woff2) format("woff2"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_SansSerif-Bold.woff) format("woff"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_SansSerif-Bold.ttf) format("truetype");
}
@font-face {
  font-family: "KaTeX_SansSerif";
  font-style: italic;
  font-weight: 400;
  src: url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_SansSerif-Italic.woff2) format("woff2"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_SansSerif-Italic.woff) format("woff"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_SansSerif-Italic.ttf) format("truetype");
}
@font-face {
  font-family: "KaTeX_SansSerif";
  font-style: normal;
  font-weight: 400;
  src: url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_SansSerif-Regular.woff2) format("woff2"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_SansSerif-Regular.woff) format("woff"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_SansSerif-Regular.ttf) format("truetype");
}
@font-face {
  font-family: KaTeX_Script;
  font-style: normal;
  font-weight: 400;
  src: url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Script-Regular.woff2) format("woff2"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Script-Regular.woff) format("woff"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Script-Regular.ttf) format("truetype");
}
@font-face {
  font-family: KaTeX_Size1;
  font-style: normal;
  font-weight: 400;
  src: url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Size1-Regular.woff2) format("woff2"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Size1-Regular.woff) format("woff"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Size1-Regular.ttf) format("truetype");
}
@font-face {
  font-family: KaTeX_Size2;
  font-style: normal;
  font-weight: 400;
  src: url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Size2-Regular.woff2) format("woff2"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Size2-Regular.woff) format("woff"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Size2-Regular.ttf) format("truetype");
}
@font-face {
  font-family: KaTeX_Size3;
  font-style: normal;
  font-weight: 400;
  src: url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Size3-Regular.woff2) format("woff2"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Size3-Regular.woff) format("woff"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Size3-Regular.ttf) format("truetype");
}
@font-face {
  font-family: KaTeX_Size4;
  font-style: normal;
  font-weight: 400;
  src: url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Size4-Regular.woff2) format("woff2"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Size4-Regular.woff) format("woff"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Size4-Regular.ttf) format("truetype");
}
@font-face {
  font-family: KaTeX_Typewriter;
  font-style: normal;
  font-weight: 400;
  src: url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Typewriter-Regular.woff2) format("woff2"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Typewriter-Regular.woff) format("woff"), url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.18/fonts/KaTeX_Typewriter-Regular.ttf) format("truetype");
}
.katex {
  text-rendering: auto;
  font: normal 1.21em KaTeX_Main, Times New Roman, serif;
  line-height: 1.2;
  text-indent: 0;
}

.katex * {
  -ms-high-contrast-adjust: none !important;
  border-color: currentColor;
}

.katex .katex-version:after {
  content: "0.13.24";
}

.katex .katex-mathml {
  clip: rect(1px, 1px, 1px, 1px);
  border: 0;
  height: 1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  width: 1px;
}

.katex .katex-html > .newline {
  display: block;
}

.katex .base {
  position: relative;
  white-space: nowrap;
  width: -webkit-min-content;
  width: -moz-min-content;
  width: min-content;
}

.katex .base, .katex .strut {
  display: inline-block;
}

.katex .textbf {
  font-weight: 700;
}

.katex .textit {
  font-style: italic;
}

.katex .textrm {
  font-family: KaTeX_Main;
}

.katex .textsf {
  font-family: KaTeX_SansSerif;
}

.katex .texttt {
  font-family: KaTeX_Typewriter;
}

.katex .mathnormal {
  font-family: KaTeX_Math;
  font-style: italic;
}

.katex .mathit {
  font-family: KaTeX_Main;
  font-style: italic;
}

.katex .mathrm {
  font-style: normal;
}

.katex .mathbf {
  font-family: KaTeX_Main;
  font-weight: 700;
}

.katex .boldsymbol {
  font-family: KaTeX_Math;
  font-style: italic;
  font-weight: 700;
}

.katex .amsrm, .katex .mathbb, .katex .textbb {
  font-family: KaTeX_AMS;
}

.katex .mathcal {
  font-family: KaTeX_Caligraphic;
}

.katex .mathfrak, .katex .textfrak {
  font-family: KaTeX_Fraktur;
}

.katex .mathtt {
  font-family: KaTeX_Typewriter;
}

.katex .mathscr, .katex .textscr {
  font-family: KaTeX_Script;
}

.katex .mathsf, .katex .textsf {
  font-family: KaTeX_SansSerif;
}

.katex .mathboldsf, .katex .textboldsf {
  font-family: KaTeX_SansSerif;
  font-weight: 700;
}

.katex .mathitsf, .katex .textitsf {
  font-family: KaTeX_SansSerif;
  font-style: italic;
}

.katex .mainrm {
  font-family: KaTeX_Main;
  font-style: normal;
}

.katex .vlist-t {
  border-collapse: collapse;
  display: inline-table;
  table-layout: fixed;
}

.katex .vlist-r {
  display: table-row;
}

.katex .vlist {
  display: table-cell;
  position: relative;
  vertical-align: bottom;
}

.katex .vlist > span {
  display: block;
  height: 0;
  position: relative;
}

.katex .vlist > span > span {
  display: inline-block;
}

.katex .vlist > span > .pstrut {
  overflow: hidden;
  width: 0;
}

.katex .vlist-t2 {
  margin-right: -2px;
}

.katex .vlist-s {
  display: table-cell;
  font-size: 1px;
  min-width: 2px;
  vertical-align: bottom;
  width: 2px;
}

.katex .vbox {
  align-items: baseline;
  display: inline-flex;
  flex-direction: column;
}

.katex .hbox {
  width: 100%;
}

.katex .hbox, .katex .thinbox {
  display: inline-flex;
  flex-direction: row;
}

.katex .thinbox {
  max-width: 0;
  width: 0;
}

.katex .msupsub {
  text-align: left;
}

.katex .mfrac > span > span {
  text-align: center;
}

.katex .mfrac .frac-line {
  border-bottom-style: solid;
  display: inline-block;
  width: 100%;
}

.katex .hdashline, .katex .hline, .katex .mfrac .frac-line, .katex .overline .overline-line, .katex .rule, .katex .underline .underline-line {
  min-height: 1px;
}

.katex .mspace {
  display: inline-block;
}

.katex .clap, .katex .llap, .katex .rlap {
  position: relative;
  width: 0;
}

.katex .clap > .inner, .katex .llap > .inner, .katex .rlap > .inner {
  position: absolute;
}

.katex .clap > .fix, .katex .llap > .fix, .katex .rlap > .fix {
  display: inline-block;
}

.katex .llap > .inner {
  right: 0;
}

.katex .clap > .inner, .katex .rlap > .inner {
  left: 0;
}

.katex .clap > .inner > span {
  margin-left: -50%;
  margin-right: 50%;
}

.katex .rule {
  border: 0 solid;
  display: inline-block;
  position: relative;
}

.katex .hline, .katex .overline .overline-line, .katex .underline .underline-line {
  border-bottom-style: solid;
  display: inline-block;
  width: 100%;
}

.katex .hdashline {
  border-bottom-style: dashed;
  display: inline-block;
  width: 100%;
}

.katex .sqrt > .root {
  margin-left: 0.27777778em;
  margin-right: -0.55555556em;
}

.katex .fontsize-ensurer.reset-size1.size1, .katex .sizing.reset-size1.size1 {
  font-size: 1em;
}

.katex .fontsize-ensurer.reset-size1.size2, .katex .sizing.reset-size1.size2 {
  font-size: 1.2em;
}

.katex .fontsize-ensurer.reset-size1.size3, .katex .sizing.reset-size1.size3 {
  font-size: 1.4em;
}

.katex .fontsize-ensurer.reset-size1.size4, .katex .sizing.reset-size1.size4 {
  font-size: 1.6em;
}

.katex .fontsize-ensurer.reset-size1.size5, .katex .sizing.reset-size1.size5 {
  font-size: 1.8em;
}

.katex .fontsize-ensurer.reset-size1.size6, .katex .sizing.reset-size1.size6 {
  font-size: 2em;
}

.katex .fontsize-ensurer.reset-size1.size7, .katex .sizing.reset-size1.size7 {
  font-size: 2.4em;
}

.katex .fontsize-ensurer.reset-size1.size8, .katex .sizing.reset-size1.size8 {
  font-size: 2.88em;
}

.katex .fontsize-ensurer.reset-size1.size9, .katex .sizing.reset-size1.size9 {
  font-size: 3.456em;
}

.katex .fontsize-ensurer.reset-size1.size10, .katex .sizing.reset-size1.size10 {
  font-size: 4.148em;
}

.katex .fontsize-ensurer.reset-size1.size11, .katex .sizing.reset-size1.size11 {
  font-size: 4.976em;
}

.katex .fontsize-ensurer.reset-size2.size1, .katex .sizing.reset-size2.size1 {
  font-size: 0.83333333em;
}

.katex .fontsize-ensurer.reset-size2.size2, .katex .sizing.reset-size2.size2 {
  font-size: 1em;
}

.katex .fontsize-ensurer.reset-size2.size3, .katex .sizing.reset-size2.size3 {
  font-size: 1.16666667em;
}

.katex .fontsize-ensurer.reset-size2.size4, .katex .sizing.reset-size2.size4 {
  font-size: 1.33333333em;
}

.katex .fontsize-ensurer.reset-size2.size5, .katex .sizing.reset-size2.size5 {
  font-size: 1.5em;
}

.katex .fontsize-ensurer.reset-size2.size6, .katex .sizing.reset-size2.size6 {
  font-size: 1.66666667em;
}

.katex .fontsize-ensurer.reset-size2.size7, .katex .sizing.reset-size2.size7 {
  font-size: 2em;
}

.katex .fontsize-ensurer.reset-size2.size8, .katex .sizing.reset-size2.size8 {
  font-size: 2.4em;
}

.katex .fontsize-ensurer.reset-size2.size9, .katex .sizing.reset-size2.size9 {
  font-size: 2.88em;
}

.katex .fontsize-ensurer.reset-size2.size10, .katex .sizing.reset-size2.size10 {
  font-size: 3.45666667em;
}

.katex .fontsize-ensurer.reset-size2.size11, .katex .sizing.reset-size2.size11 {
  font-size: 4.14666667em;
}

.katex .fontsize-ensurer.reset-size3.size1, .katex .sizing.reset-size3.size1 {
  font-size: 0.71428571em;
}

.katex .fontsize-ensurer.reset-size3.size2, .katex .sizing.reset-size3.size2 {
  font-size: 0.85714286em;
}

.katex .fontsize-ensurer.reset-size3.size3, .katex .sizing.reset-size3.size3 {
  font-size: 1em;
}

.katex .fontsize-ensurer.reset-size3.size4, .katex .sizing.reset-size3.size4 {
  font-size: 1.14285714em;
}

.katex .fontsize-ensurer.reset-size3.size5, .katex .sizing.reset-size3.size5 {
  font-size: 1.28571429em;
}

.katex .fontsize-ensurer.reset-size3.size6, .katex .sizing.reset-size3.size6 {
  font-size: 1.42857143em;
}

.katex .fontsize-ensurer.reset-size3.size7, .katex .sizing.reset-size3.size7 {
  font-size: 1.71428571em;
}

.katex .fontsize-ensurer.reset-size3.size8, .katex .sizing.reset-size3.size8 {
  font-size: 2.05714286em;
}

.katex .fontsize-ensurer.reset-size3.size9, .katex .sizing.reset-size3.size9 {
  font-size: 2.46857143em;
}

.katex .fontsize-ensurer.reset-size3.size10, .katex .sizing.reset-size3.size10 {
  font-size: 2.96285714em;
}

.katex .fontsize-ensurer.reset-size3.size11, .katex .sizing.reset-size3.size11 {
  font-size: 3.55428571em;
}

.katex .fontsize-ensurer.reset-size4.size1, .katex .sizing.reset-size4.size1 {
  font-size: 0.625em;
}

.katex .fontsize-ensurer.reset-size4.size2, .katex .sizing.reset-size4.size2 {
  font-size: 0.75em;
}

.katex .fontsize-ensurer.reset-size4.size3, .katex .sizing.reset-size4.size3 {
  font-size: 0.875em;
}

.katex .fontsize-ensurer.reset-size4.size4, .katex .sizing.reset-size4.size4 {
  font-size: 1em;
}

.katex .fontsize-ensurer.reset-size4.size5, .katex .sizing.reset-size4.size5 {
  font-size: 1.125em;
}

.katex .fontsize-ensurer.reset-size4.size6, .katex .sizing.reset-size4.size6 {
  font-size: 1.25em;
}

.katex .fontsize-ensurer.reset-size4.size7, .katex .sizing.reset-size4.size7 {
  font-size: 1.5em;
}

.katex .fontsize-ensurer.reset-size4.size8, .katex .sizing.reset-size4.size8 {
  font-size: 1.8em;
}

.katex .fontsize-ensurer.reset-size4.size9, .katex .sizing.reset-size4.size9 {
  font-size: 2.16em;
}

.katex .fontsize-ensurer.reset-size4.size10, .katex .sizing.reset-size4.size10 {
  font-size: 2.5925em;
}

.katex .fontsize-ensurer.reset-size4.size11, .katex .sizing.reset-size4.size11 {
  font-size: 3.11em;
}

.katex .fontsize-ensurer.reset-size5.size1, .katex .sizing.reset-size5.size1 {
  font-size: 0.55555556em;
}

.katex .fontsize-ensurer.reset-size5.size2, .katex .sizing.reset-size5.size2 {
  font-size: 0.66666667em;
}

.katex .fontsize-ensurer.reset-size5.size3, .katex .sizing.reset-size5.size3 {
  font-size: 0.77777778em;
}

.katex .fontsize-ensurer.reset-size5.size4, .katex .sizing.reset-size5.size4 {
  font-size: 0.88888889em;
}

.katex .fontsize-ensurer.reset-size5.size5, .katex .sizing.reset-size5.size5 {
  font-size: 1em;
}

.katex .fontsize-ensurer.reset-size5.size6, .katex .sizing.reset-size5.size6 {
  font-size: 1.11111111em;
}

.katex .fontsize-ensurer.reset-size5.size7, .katex .sizing.reset-size5.size7 {
  font-size: 1.33333333em;
}

.katex .fontsize-ensurer.reset-size5.size8, .katex .sizing.reset-size5.size8 {
  font-size: 1.6em;
}

.katex .fontsize-ensurer.reset-size5.size9, .katex .sizing.reset-size5.size9 {
  font-size: 1.92em;
}

.katex .fontsize-ensurer.reset-size5.size10, .katex .sizing.reset-size5.size10 {
  font-size: 2.30444444em;
}

.katex .fontsize-ensurer.reset-size5.size11, .katex .sizing.reset-size5.size11 {
  font-size: 2.76444444em;
}

.katex .fontsize-ensurer.reset-size6.size1, .katex .sizing.reset-size6.size1 {
  font-size: 0.5em;
}

.katex .fontsize-ensurer.reset-size6.size2, .katex .sizing.reset-size6.size2 {
  font-size: 0.6em;
}

.katex .fontsize-ensurer.reset-size6.size3, .katex .sizing.reset-size6.size3 {
  font-size: 0.7em;
}

.katex .fontsize-ensurer.reset-size6.size4, .katex .sizing.reset-size6.size4 {
  font-size: 0.8em;
}

.katex .fontsize-ensurer.reset-size6.size5, .katex .sizing.reset-size6.size5 {
  font-size: 0.9em;
}

.katex .fontsize-ensurer.reset-size6.size6, .katex .sizing.reset-size6.size6 {
  font-size: 1em;
}

.katex .fontsize-ensurer.reset-size6.size7, .katex .sizing.reset-size6.size7 {
  font-size: 1.2em;
}

.katex .fontsize-ensurer.reset-size6.size8, .katex .sizing.reset-size6.size8 {
  font-size: 1.44em;
}

.katex .fontsize-ensurer.reset-size6.size9, .katex .sizing.reset-size6.size9 {
  font-size: 1.728em;
}

.katex .fontsize-ensurer.reset-size6.size10, .katex .sizing.reset-size6.size10 {
  font-size: 2.074em;
}

.katex .fontsize-ensurer.reset-size6.size11, .katex .sizing.reset-size6.size11 {
  font-size: 2.488em;
}

.katex .fontsize-ensurer.reset-size7.size1, .katex .sizing.reset-size7.size1 {
  font-size: 0.41666667em;
}

.katex .fontsize-ensurer.reset-size7.size2, .katex .sizing.reset-size7.size2 {
  font-size: 0.5em;
}

.katex .fontsize-ensurer.reset-size7.size3, .katex .sizing.reset-size7.size3 {
  font-size: 0.58333333em;
}

.katex .fontsize-ensurer.reset-size7.size4, .katex .sizing.reset-size7.size4 {
  font-size: 0.66666667em;
}

.katex .fontsize-ensurer.reset-size7.size5, .katex .sizing.reset-size7.size5 {
  font-size: 0.75em;
}

.katex .fontsize-ensurer.reset-size7.size6, .katex .sizing.reset-size7.size6 {
  font-size: 0.83333333em;
}

.katex .fontsize-ensurer.reset-size7.size7, .katex .sizing.reset-size7.size7 {
  font-size: 1em;
}

.katex .fontsize-ensurer.reset-size7.size8, .katex .sizing.reset-size7.size8 {
  font-size: 1.2em;
}

.katex .fontsize-ensurer.reset-size7.size9, .katex .sizing.reset-size7.size9 {
  font-size: 1.44em;
}

.katex .fontsize-ensurer.reset-size7.size10, .katex .sizing.reset-size7.size10 {
  font-size: 1.72833333em;
}

.katex .fontsize-ensurer.reset-size7.size11, .katex .sizing.reset-size7.size11 {
  font-size: 2.07333333em;
}

.katex .fontsize-ensurer.reset-size8.size1, .katex .sizing.reset-size8.size1 {
  font-size: 0.34722222em;
}

.katex .fontsize-ensurer.reset-size8.size2, .katex .sizing.reset-size8.size2 {
  font-size: 0.41666667em;
}

.katex .fontsize-ensurer.reset-size8.size3, .katex .sizing.reset-size8.size3 {
  font-size: 0.48611111em;
}

.katex .fontsize-ensurer.reset-size8.size4, .katex .sizing.reset-size8.size4 {
  font-size: 0.55555556em;
}

.katex .fontsize-ensurer.reset-size8.size5, .katex .sizing.reset-size8.size5 {
  font-size: 0.625em;
}

.katex .fontsize-ensurer.reset-size8.size6, .katex .sizing.reset-size8.size6 {
  font-size: 0.69444444em;
}

.katex .fontsize-ensurer.reset-size8.size7, .katex .sizing.reset-size8.size7 {
  font-size: 0.83333333em;
}

.katex .fontsize-ensurer.reset-size8.size8, .katex .sizing.reset-size8.size8 {
  font-size: 1em;
}

.katex .fontsize-ensurer.reset-size8.size9, .katex .sizing.reset-size8.size9 {
  font-size: 1.2em;
}

.katex .fontsize-ensurer.reset-size8.size10, .katex .sizing.reset-size8.size10 {
  font-size: 1.44027778em;
}

.katex .fontsize-ensurer.reset-size8.size11, .katex .sizing.reset-size8.size11 {
  font-size: 1.72777778em;
}

.katex .fontsize-ensurer.reset-size9.size1, .katex .sizing.reset-size9.size1 {
  font-size: 0.28935185em;
}

.katex .fontsize-ensurer.reset-size9.size2, .katex .sizing.reset-size9.size2 {
  font-size: 0.34722222em;
}

.katex .fontsize-ensurer.reset-size9.size3, .katex .sizing.reset-size9.size3 {
  font-size: 0.40509259em;
}

.katex .fontsize-ensurer.reset-size9.size4, .katex .sizing.reset-size9.size4 {
  font-size: 0.46296296em;
}

.katex .fontsize-ensurer.reset-size9.size5, .katex .sizing.reset-size9.size5 {
  font-size: 0.52083333em;
}

.katex .fontsize-ensurer.reset-size9.size6, .katex .sizing.reset-size9.size6 {
  font-size: 0.5787037em;
}

.katex .fontsize-ensurer.reset-size9.size7, .katex .sizing.reset-size9.size7 {
  font-size: 0.69444444em;
}

.katex .fontsize-ensurer.reset-size9.size8, .katex .sizing.reset-size9.size8 {
  font-size: 0.83333333em;
}

.katex .fontsize-ensurer.reset-size9.size9, .katex .sizing.reset-size9.size9 {
  font-size: 1em;
}

.katex .fontsize-ensurer.reset-size9.size10, .katex .sizing.reset-size9.size10 {
  font-size: 1.20023148em;
}

.katex .fontsize-ensurer.reset-size9.size11, .katex .sizing.reset-size9.size11 {
  font-size: 1.43981481em;
}

.katex .fontsize-ensurer.reset-size10.size1, .katex .sizing.reset-size10.size1 {
  font-size: 0.24108004em;
}

.katex .fontsize-ensurer.reset-size10.size2, .katex .sizing.reset-size10.size2 {
  font-size: 0.28929605em;
}

.katex .fontsize-ensurer.reset-size10.size3, .katex .sizing.reset-size10.size3 {
  font-size: 0.33751205em;
}

.katex .fontsize-ensurer.reset-size10.size4, .katex .sizing.reset-size10.size4 {
  font-size: 0.38572806em;
}

.katex .fontsize-ensurer.reset-size10.size5, .katex .sizing.reset-size10.size5 {
  font-size: 0.43394407em;
}

.katex .fontsize-ensurer.reset-size10.size6, .katex .sizing.reset-size10.size6 {
  font-size: 0.48216008em;
}

.katex .fontsize-ensurer.reset-size10.size7, .katex .sizing.reset-size10.size7 {
  font-size: 0.57859209em;
}

.katex .fontsize-ensurer.reset-size10.size8, .katex .sizing.reset-size10.size8 {
  font-size: 0.69431051em;
}

.katex .fontsize-ensurer.reset-size10.size9, .katex .sizing.reset-size10.size9 {
  font-size: 0.83317261em;
}

.katex .fontsize-ensurer.reset-size10.size10, .katex .sizing.reset-size10.size10 {
  font-size: 1em;
}

.katex .fontsize-ensurer.reset-size10.size11, .katex .sizing.reset-size10.size11 {
  font-size: 1.19961427em;
}

.katex .fontsize-ensurer.reset-size11.size1, .katex .sizing.reset-size11.size1 {
  font-size: 0.20096463em;
}

.katex .fontsize-ensurer.reset-size11.size2, .katex .sizing.reset-size11.size2 {
  font-size: 0.24115756em;
}

.katex .fontsize-ensurer.reset-size11.size3, .katex .sizing.reset-size11.size3 {
  font-size: 0.28135048em;
}

.katex .fontsize-ensurer.reset-size11.size4, .katex .sizing.reset-size11.size4 {
  font-size: 0.32154341em;
}

.katex .fontsize-ensurer.reset-size11.size5, .katex .sizing.reset-size11.size5 {
  font-size: 0.36173633em;
}

.katex .fontsize-ensurer.reset-size11.size6, .katex .sizing.reset-size11.size6 {
  font-size: 0.40192926em;
}

.katex .fontsize-ensurer.reset-size11.size7, .katex .sizing.reset-size11.size7 {
  font-size: 0.48231511em;
}

.katex .fontsize-ensurer.reset-size11.size8, .katex .sizing.reset-size11.size8 {
  font-size: 0.57877814em;
}

.katex .fontsize-ensurer.reset-size11.size9, .katex .sizing.reset-size11.size9 {
  font-size: 0.69453376em;
}

.katex .fontsize-ensurer.reset-size11.size10, .katex .sizing.reset-size11.size10 {
  font-size: 0.83360129em;
}

.katex .fontsize-ensurer.reset-size11.size11, .katex .sizing.reset-size11.size11 {
  font-size: 1em;
}

.katex .delimsizing.size1 {
  font-family: KaTeX_Size1;
}

.katex .delimsizing.size2 {
  font-family: KaTeX_Size2;
}

.katex .delimsizing.size3 {
  font-family: KaTeX_Size3;
}

.katex .delimsizing.size4 {
  font-family: KaTeX_Size4;
}

.katex .delimsizing.mult .delim-size1 > span {
  font-family: KaTeX_Size1;
}

.katex .delimsizing.mult .delim-size4 > span {
  font-family: KaTeX_Size4;
}

.katex .nulldelimiter {
  display: inline-block;
  width: 0.12em;
}

.katex .delimcenter, .katex .op-symbol {
  position: relative;
}

.katex .op-symbol.small-op {
  font-family: KaTeX_Size1;
}

.katex .op-symbol.large-op {
  font-family: KaTeX_Size2;
}

.katex .accent > .vlist-t, .katex .op-limits > .vlist-t {
  text-align: center;
}

.katex .accent .accent-body {
  position: relative;
}

.katex .accent .accent-body:not(.accent-full) {
  width: 0;
}

.katex .overlay {
  display: block;
}

.katex .mtable .vertical-separator {
  display: inline-block;
  min-width: 1px;
}

.katex .mtable .arraycolsep {
  display: inline-block;
}

.katex .mtable .col-align-c > .vlist-t {
  text-align: center;
}

.katex .mtable .col-align-l > .vlist-t {
  text-align: left;
}

.katex .mtable .col-align-r > .vlist-t {
  text-align: right;
}

.katex .svg-align {
  text-align: left;
}

.katex svg {
  fill: currentColor;
  stroke: currentColor;
  fill-rule: nonzero;
  fill-opacity: 1;
  stroke-width: 1;
  stroke-linecap: butt;
  stroke-linejoin: miter;
  stroke-miterlimit: 4;
  stroke-dasharray: none;
  stroke-dashoffset: 0;
  stroke-opacity: 1;
  display: block;
  height: inherit;
  position: absolute;
  width: 100%;
}

.katex svg path {
  stroke: none;
}

.katex img {
  border-style: none;
  max-height: none;
  max-width: none;
  min-height: 0;
  min-width: 0;
}

.katex .stretchy {
  display: block;
  overflow: hidden;
  position: relative;
  width: 100%;
}

.katex .stretchy:after, .katex .stretchy:before {
  content: "";
}

.katex .hide-tail {
  overflow: hidden;
  position: relative;
  width: 100%;
}

.katex .halfarrow-left {
  left: 0;
  overflow: hidden;
  position: absolute;
  width: 50.2%;
}

.katex .halfarrow-right {
  overflow: hidden;
  position: absolute;
  right: 0;
  width: 50.2%;
}

.katex .brace-left {
  left: 0;
  overflow: hidden;
  position: absolute;
  width: 25.1%;
}

.katex .brace-center {
  left: 25%;
  overflow: hidden;
  position: absolute;
  width: 50%;
}

.katex .brace-right {
  overflow: hidden;
  position: absolute;
  right: 0;
  width: 25.1%;
}

.katex .x-arrow-pad {
  padding: 0 0.5em;
}

.katex .cd-arrow-pad {
  padding: 0 0.55556em 0 0.27778em;
}

.katex .mover, .katex .munder, .katex .x-arrow {
  text-align: center;
}

.katex .boxpad {
  padding: 0 0.3em;
}

.katex .fbox, .katex .fcolorbox {
  border: 0.04em solid;
  box-sizing: border-box;
}

.katex .cancel-pad {
  padding: 0 0.2em;
}

.katex .cancel-lap {
  margin-left: -0.2em;
  margin-right: -0.2em;
}

.katex .sout {
  border-bottom-style: solid;
  border-bottom-width: 0.08em;
}

.katex .angl {
  border-right: 0.049em solid;
  border-top: 0.049em solid;
  box-sizing: border-box;
  margin-right: 0.03889em;
}

.katex .anglpad {
  padding: 0 0.03889em;
}

.katex .eqn-num:before {
  content: "(" counter(katexEqnNo) ")";
  counter-increment: katexEqnNo;
}

.katex .mml-eqn-num:before {
  content: "(" counter(mmlEqnNo) ")";
  counter-increment: mmlEqnNo;
}

.katex .mtr-glue {
  width: 50%;
}

.katex .cd-vert-arrow {
  display: inline-block;
  position: relative;
}

.katex .cd-label-left {
  display: inline-block;
  position: absolute;
  right: calc(50% + 0.3em);
  text-align: left;
}

.katex .cd-label-right {
  display: inline-block;
  left: calc(50% + 0.3em);
  position: absolute;
  text-align: right;
}

.katex-display {
  display: block;
  margin: 1em 0;
  text-align: center;
}

.katex-display > .katex {
  display: block;
  text-align: center;
  white-space: nowrap;
}

.katex-display > .katex > .katex-html {
  display: block;
  position: relative;
}

.katex-display > .katex > .katex-html > .tag {
  position: absolute;
  right: 0;
}

.katex-display.leqno > .katex > .katex-html > .tag {
  left: 0;
  right: auto;
}

.katex-display.fleqn > .katex {
  padding-left: 2em;
  text-align: left;
}

body {
  counter-reset: katexEqnNo mmlEqnNo;
}

[data-node-type=math-inline] {
  font-size: 0.9em;
  display: inline-block;
  vertical-align: middle;
  max-width: 100%;
}

[data-node-type=math-block] {
  font-size: 20px;
  text-align: center;
  max-width: 100%;
  position: relative;
  display: flex;
}
[data-node-type=math-block] > span {
  flex-grow: 1;
}
[data-node-type=math-block] > span:first-child {
  flex-shrink: 2;
}
[data-node-type=math-block] > span:nth-child(2) {
  flex-shrink: 0;
}
[data-node-type=math-block] > span:last-child {
  flex-shrink: 1;
  text-align: right;
}

.math-label {
  text-align: center;
  font-family: "Source Serif 4", Georgia, Cambria, "Times New Roman", Times, serif;
}

.equation-label {
  text-align: center;
  font-family: "Source Serif 4", Georgia, Cambria, "Times New Roman", Times, serif;
}

.editor {
  /*! fileicon.css v0.1.1 | MIT License | github.com/picturepan2/fileicon.css */
  /* fileicon.basic */
  /* fileicons */
  /* fileicon.types */
  /* This clunky table, tableWrapper thing is because */
  /* isReadOnly removes the wrapping div, so margins don't */
  /* collapse as expected in all situations. */
}
.editor:focus {
  outline: none !important;
}
.editor .prosemirror-placeholder {
  opacity: 0.5;
  white-space: nowrap;
  position: relative;
}
.editor .prosemirror-placeholder:after {
  position: absolute;
  top: 0;
  content: attr(data-content);
}
.editor .ProseMirror-selectednode {
  outline: 2px solid #bbbdc0;
}
.editor.read-only .ProseMirror-selectednode {
  outline: 0px solid #bbbdc0;
}
.editor h1 a,
.editor h2 a,
.editor h3 a,
.editor h4 a,
.editor h5 a,
.editor h6 a {
  text-decoration: none;
  color: inherit;
}
.editor .footnote {
  vertical-align: super;
  font-size: 0.85em;
  line-height: 1;
}
.editor span.citation {
  color: #808080;
  font-weight: bold;
}
.editor a.reference.missing {
  color: darkred;
}
.editor table {
  /* Prosemirror requires white-space: pre-wrap, but it's overriden by the quirks.css */
  /* built-in that Firefox provides, breaking the editor. */
  /* See https://github.com/ProseMirror/prosemirror/issues/651#issuecomment-313436150 */
  white-space: pre-wrap !important;
}
.editor sup,
.editor sub {
  position: static;
}
.editor sub {
  vertical-align: sub;
}
.editor sup {
  vertical-align: super;
}
.editor .collab-cursor {
  position: relative;
  font-family: -apple-system, "BlinkMacSystemFont", "Segoe UI", "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Open Sans", "Helvetica Neue", sans-serif;
  color: white;
  user-select: none;
  vertical-align: top;
}
.editor .collab-cursor .inner-bar {
  position: absolute;
  height: calc(1em + 5px);
  width: 2px;
  background-color: rgb(0, 25, 150);
  bottom: 0px;
  left: 0;
}
.editor .collab-cursor .inner-bar .inner-circle-small {
  position: absolute;
  height: 8px;
  width: 8px;
  border-radius: 8px;
  background-color: rgb(0, 25, 150);
  bottom: calc(100% + 0px);
  left: -3px;
}
.editor .collab-cursor .inner-bar .hover-wrapper {
  transform: scale(0.4);
  opacity: 0;
  transform-origin: bottom left;
  transition: 0.1s 0.3s linear transform, 0s 0.4s linear opacity;
  display: block;
  position: absolute;
  bottom: 100%;
  pointer-events: none;
  z-index: 1;
}
.editor .collab-cursor .inner-bar .hover-wrapper .inner-circle-big {
  position: absolute;
  height: 24px;
  width: 24px;
  border-radius: 24px;
  background-color: rgb(0, 25, 150);
  bottom: 0px;
  left: -11px;
}
.editor .collab-cursor .inner-bar .hover-wrapper .initials:after {
  display: block;
  position: absolute;
  width: 20px;
  height: 20px;
  bottom: 2px;
  left: -9px;
  font-size: 12px;
  font-weight: bold;
  line-height: 20px;
  text-align: center;
  z-index: 4;
  white-space: nowrap;
  user-select: none;
}
.editor .collab-cursor .inner-bar .hover-wrapper .name:after {
  position: absolute;
  display: block;
  padding: 2px 12px;
  border-radius: 2px;
  color: white;
  background-color: #777;
  font-size: 12px;
  line-height: 16px;
  font-weight: 400;
  bottom: 2px;
  left: 6px;
  white-space: nowrap;
  z-index: 3;
  user-select: none;
}
.editor .collab-cursor .inner-bar .hover-wrapper .image:after {
  position: absolute;
  bottom: 2px;
  left: -9px;
  z-index: 5;
  border-radius: 10px;
  width: 20px;
  height: 20px;
  background-size: cover;
  content: "";
  max-width: none;
  margin-top: 0px;
}
.editor .collab-cursor:hover .hover-wrapper {
  opacity: 1;
  transform: scale(1);
  transition: 0.1s linear transform, 0s 0s linear opacity;
}
.editor figure {
  display: block;
  text-align: center;
  margin: 0;
}
.editor figure > * {
  pointer-events: none;
  width: 100%;
}
.editor figure > a > img {
  width: 100%;
}
.editor figure.ProseMirror-selectednode {
  outline: 2px solid #bbbdc0;
}
.editor figure.ProseMirror-selectednode > * {
  pointer-events: auto;
}
.editor figure[data-align=left] {
  float: left;
  margin: 0.5em 1.5em 0.5em 0em;
}
.editor figure[data-align=right] {
  float: right;
  margin: 0.5em 0em 0.5em 1.5em;
}
.editor figure[data-align=center] {
  margin: 0 auto;
}
.editor figure[data-size="1"] {
  width: 1%;
}
.editor figure[data-size="2"] {
  width: 2%;
}
.editor figure[data-size="3"] {
  width: 3%;
}
.editor figure[data-size="4"] {
  width: 4%;
}
.editor figure[data-size="5"] {
  width: 5%;
}
.editor figure[data-size="6"] {
  width: 6%;
}
.editor figure[data-size="7"] {
  width: 7%;
}
.editor figure[data-size="8"] {
  width: 8%;
}
.editor figure[data-size="9"] {
  width: 9%;
}
.editor figure[data-size="10"] {
  width: 10%;
}
.editor figure[data-size="11"] {
  width: 11%;
}
.editor figure[data-size="12"] {
  width: 12%;
}
.editor figure[data-size="13"] {
  width: 13%;
}
.editor figure[data-size="14"] {
  width: 14%;
}
.editor figure[data-size="15"] {
  width: 15%;
}
.editor figure[data-size="16"] {
  width: 16%;
}
.editor figure[data-size="17"] {
  width: 17%;
}
.editor figure[data-size="18"] {
  width: 18%;
}
.editor figure[data-size="19"] {
  width: 19%;
}
.editor figure[data-size="20"] {
  width: 20%;
}
.editor figure[data-size="21"] {
  width: 21%;
}
.editor figure[data-size="22"] {
  width: 22%;
}
.editor figure[data-size="23"] {
  width: 23%;
}
.editor figure[data-size="24"] {
  width: 24%;
}
.editor figure[data-size="25"] {
  width: 25%;
}
.editor figure[data-size="26"] {
  width: 26%;
}
.editor figure[data-size="27"] {
  width: 27%;
}
.editor figure[data-size="28"] {
  width: 28%;
}
.editor figure[data-size="29"] {
  width: 29%;
}
.editor figure[data-size="30"] {
  width: 30%;
}
.editor figure[data-size="31"] {
  width: 31%;
}
.editor figure[data-size="32"] {
  width: 32%;
}
.editor figure[data-size="33"] {
  width: 33%;
}
.editor figure[data-size="34"] {
  width: 34%;
}
.editor figure[data-size="35"] {
  width: 35%;
}
.editor figure[data-size="36"] {
  width: 36%;
}
.editor figure[data-size="37"] {
  width: 37%;
}
.editor figure[data-size="38"] {
  width: 38%;
}
.editor figure[data-size="39"] {
  width: 39%;
}
.editor figure[data-size="40"] {
  width: 40%;
}
.editor figure[data-size="41"] {
  width: 41%;
}
.editor figure[data-size="42"] {
  width: 42%;
}
.editor figure[data-size="43"] {
  width: 43%;
}
.editor figure[data-size="44"] {
  width: 44%;
}
.editor figure[data-size="45"] {
  width: 45%;
}
.editor figure[data-size="46"] {
  width: 46%;
}
.editor figure[data-size="47"] {
  width: 47%;
}
.editor figure[data-size="48"] {
  width: 48%;
}
.editor figure[data-size="49"] {
  width: 49%;
}
.editor figure[data-size="50"] {
  width: 50%;
}
.editor figure[data-size="51"] {
  width: 51%;
}
.editor figure[data-size="52"] {
  width: 52%;
}
.editor figure[data-size="53"] {
  width: 53%;
}
.editor figure[data-size="54"] {
  width: 54%;
}
.editor figure[data-size="55"] {
  width: 55%;
}
.editor figure[data-size="56"] {
  width: 56%;
}
.editor figure[data-size="57"] {
  width: 57%;
}
.editor figure[data-size="58"] {
  width: 58%;
}
.editor figure[data-size="59"] {
  width: 59%;
}
.editor figure[data-size="60"] {
  width: 60%;
}
.editor figure[data-size="61"] {
  width: 61%;
}
.editor figure[data-size="62"] {
  width: 62%;
}
.editor figure[data-size="63"] {
  width: 63%;
}
.editor figure[data-size="64"] {
  width: 64%;
}
.editor figure[data-size="65"] {
  width: 65%;
}
.editor figure[data-size="66"] {
  width: 66%;
}
.editor figure[data-size="67"] {
  width: 67%;
}
.editor figure[data-size="68"] {
  width: 68%;
}
.editor figure[data-size="69"] {
  width: 69%;
}
.editor figure[data-size="70"] {
  width: 70%;
}
.editor figure[data-size="71"] {
  width: 71%;
}
.editor figure[data-size="72"] {
  width: 72%;
}
.editor figure[data-size="73"] {
  width: 73%;
}
.editor figure[data-size="74"] {
  width: 74%;
}
.editor figure[data-size="75"] {
  width: 75%;
}
.editor figure[data-size="76"] {
  width: 76%;
}
.editor figure[data-size="77"] {
  width: 77%;
}
.editor figure[data-size="78"] {
  width: 78%;
}
.editor figure[data-size="79"] {
  width: 79%;
}
.editor figure[data-size="80"] {
  width: 80%;
}
.editor figure[data-size="81"] {
  width: 81%;
}
.editor figure[data-size="82"] {
  width: 82%;
}
.editor figure[data-size="83"] {
  width: 83%;
}
.editor figure[data-size="84"] {
  width: 84%;
}
.editor figure[data-size="85"] {
  width: 85%;
}
.editor figure[data-size="86"] {
  width: 86%;
}
.editor figure[data-size="87"] {
  width: 87%;
}
.editor figure[data-size="88"] {
  width: 88%;
}
.editor figure[data-size="89"] {
  width: 89%;
}
.editor figure[data-size="90"] {
  width: 90%;
}
.editor figure[data-size="91"] {
  width: 91%;
}
.editor figure[data-size="92"] {
  width: 92%;
}
.editor figure[data-size="93"] {
  width: 93%;
}
.editor figure[data-size="94"] {
  width: 94%;
}
.editor figure[data-size="95"] {
  width: 95%;
}
.editor figure[data-size="96"] {
  width: 96%;
}
.editor figure[data-size="97"] {
  width: 97%;
}
.editor figure[data-size="98"] {
  width: 98%;
}
.editor figure[data-size="99"] {
  width: 99%;
}
.editor figure[data-size="100"] {
  width: 100%;
}
.editor figure[data-align=full] {
  width: 100%;
}
.editor figure figcaption {
  opacity: 0.75;
  margin: 1em auto;
  margin-top: 5px;
}
.editor.ProseMirror.read-only figure > * {
  pointer-events: auto;
}
.editor.ProseMirror.read-only figure.ProseMirror-selectednode {
  outline: none;
}
.editor .file-icon {
  font-family: Arial, Tahoma, sans-serif;
  font-weight: 300;
  display: inline-block;
  width: 24px;
  height: 32px;
  background: #018fef;
  flex-shrink: 0;
  position: relative;
  border-radius: 2px;
  text-align: left;
  -webkit-font-smoothing: antialiased;
}
.editor .file-icon::before {
  display: block;
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  width: 0;
  height: 0;
  border-bottom-left-radius: 2px;
  border-width: 5px;
  border-style: solid;
  border-color: #fff #fff rgba(255, 255, 255, 0.35) rgba(255, 255, 255, 0.35);
}
.editor .file-icon::after {
  display: block;
  content: attr(data-type);
  position: absolute;
  bottom: 0;
  left: 0;
  font-size: 10px;
  color: #fff;
  text-transform: lowercase;
  width: 100%;
  padding: 2px;
  white-space: nowrap;
  overflow: hidden;
}
.editor .file-icon-xs {
  width: 12px;
  height: 16px;
  border-radius: 2px;
}
.editor .file-icon-xs::before {
  border-bottom-left-radius: 1px;
  border-width: 3px;
}
.editor .file-icon-xs::after {
  content: "";
  border-bottom: 2px solid rgba(255, 255, 255, 0.45);
  width: auto;
  left: 2px;
  right: 2px;
  bottom: 3px;
}
.editor .file-icon-sm {
  width: 18px;
  height: 24px;
  border-radius: 2px;
}
.editor .file-icon-sm::before {
  border-bottom-left-radius: 2px;
  border-width: 4px;
}
.editor .file-icon-sm::after {
  font-size: 7px;
  padding: 2px;
}
.editor .file-icon-lg {
  width: 48px;
  height: 64px;
  border-radius: 3px;
}
.editor .file-icon-lg::before {
  border-bottom-left-radius: 2px;
  border-width: 8px;
}
.editor .file-icon-lg::after {
  font-size: 16px;
  padding: 4px 6px;
}
.editor .file-icon-xl {
  width: 96px;
  height: 128px;
  border-radius: 4px;
}
.editor .file-icon-xl::before {
  border-bottom-left-radius: 4px;
  border-width: 16px;
}
.editor .file-icon-xl::after {
  font-size: 24px;
  padding: 4px 10px;
}
.editor .file-icon[data-type=zip],
.editor .file-icon[data-type=rar] {
  background: #acacac;
}
.editor .file-icon[data-type^=doc] {
  background: #307cf1;
}
.editor .file-icon[data-type^=xls] {
  background: #0f9d58;
}
.editor .file-icon[data-type^=ppt] {
  background: #d24726;
}
.editor .file-icon[data-type=pdf] {
  background: #e13d34;
}
.editor .file-icon[data-type=txt] {
  background: #5eb533;
}
.editor .file-icon[data-type=mp3],
.editor .file-icon[data-type=wma],
.editor .file-icon[data-type=m4a],
.editor .file-icon[data-type=flac] {
  background: #8e44ad;
}
.editor .file-icon[data-type=mp4],
.editor .file-icon[data-type=wmv],
.editor .file-icon[data-type=mov],
.editor .file-icon[data-type=avi],
.editor .file-icon[data-type=mkv] {
  background: #7a3ce7;
}
.editor .file-icon[data-type=bmp],
.editor .file-icon[data-type=jpg],
.editor .file-icon[data-type=jpeg],
.editor .file-icon[data-type=gif],
.editor .file-icon[data-type=png] {
  background: #f48c00;
}
.editor [data-node-type=file] {
  width: 65%;
}
.editor [data-node-type=file] .details {
  display: flex;
  align-items: center;
  text-align: left;
}
.editor [data-node-type=file] .details .extension {
  text-transform: uppercase;
  font-family: "Courier", monospace;
  font-weight: 600;
  font-size: 1.5em;
}
.editor [data-node-type=file] .details .file-name {
  flex-grow: 1;
  flex-shrink: 1;
  margin: 0em 1em;
  word-wrap: break-word;
}
.editor [data-node-type=file] .details .file-name a {
  color: inherit;
}
.editor [data-node-type=file] .details .file-name a:hover {
  cursor: pointer;
  text-decoration: underline !important;
}
.editor [data-node-type=file] .details .file-size {
  margin: 0em 1em;
}
.editor .tableWrapper {
  margin: 1em 0;
}
@media screen and (max-width: 750px) {
  .editor .tableWrapper {
    overflow-x: scroll;
  }
}
.editor .tableWrapper table {
  margin: 0em;
}
@media screen and (max-width: 750px) {
  .editor .tableWrapper table {
    font-size: 0.8em;
    width: auto;
    max-width: fit-content;
    table-layout: auto;
  }
}
.editor .tableWrapper[data-smaller-font=true] table {
  font-size: 0.8em;
}
.editor th {
  font-weight: bold;
  text-align: left;
  background-color: #f0f0f4;
}
.editor th,
.editor td,
.editor table caption {
  min-width: 1em;
  border: 1px solid #ddd;
  padding: 3px 5px;
  /* Two :last-of-type as a selector specificity hack */
  /* :last-child does not work here because the table plugin inserts nodes when resizing */
}
.editor th > p:last-of-type:last-of-type,
.editor td > p:last-of-type:last-of-type,
.editor table caption > p:last-of-type:last-of-type {
  margin-bottom: 0;
}
@media screen and (max-width: 750px) {
  .editor th,
  .editor td {
    min-width: 140px;
    width: auto;
  }
}
.editor table {
  margin: 1em 0;
  max-width: 100%;
}
.editor table caption {
  text-align: left;
  border-bottom: none;
  padding: 3px 5px;
}
.editor > [data-text-align=center] {
  text-align: center;
}
.editor > [data-text-align=right] {
  text-align: right;
}
.editor td > [data-text-align=center],
.editor th > [data-text-align=center] {
  text-align: center;
}
.editor td > [data-text-align=right],
.editor th > [data-text-align=right] {
  text-align: right;
}
.editor > blockquote > [data-text-align=center] {
  text-align: center;
}
.editor > blockquote > [data-text-align=right] {
  text-align: right;
}
.editor [data-rtl=true] {
  direction: rtl;
}

/* Import some global variables and styles */
/* The fraction of the screen used for the pub margin -- converted to CSS units below */
/* Below this width, comments will be forced to a minimized view */
/* The pub won't grow beyond this width */
/* The space available for comments */
/* The space available for comments on smaller screens */
/* The maximum width of all the content */
/* Full width of the gutter */
/* The pub won't shrink beyond this width */
/* Compact width of the gutter */
/* The margin between the edge of the pub and the viewport (applied to the left and right side) */
/* Used to determine when `minmax($pub-margin, auto) = $pub-margin`, which indicates that we should
   treat the .breakout calculation differently.
   Calculated as: 2 * $pub-margin-fraction * x + $compact-cutoff-width = x */
.pub-body-component .editor.ProseMirror h1#abstract:first-child,
.pub-body-styles h1#abstract:first-child {
  color: var(--community-accent-dark);
  text-transform: uppercase;
  font-size: 1em;
  font-weight: 650;
  padding-top: 1em;
}
.pub-body-component .editor.ProseMirror h1#abstract:first-child + p,
.pub-body-styles h1#abstract:first-child + p {
  border-bottom: 1px solid #ccc;
  padding-bottom: 1em;
}
.pub-body-component .editor.ProseMirror h1,
.pub-body-component .editor.ProseMirror h2,
.pub-body-component .editor.ProseMirror h3,
.pub-body-component .editor.ProseMirror h4,
.pub-body-component .editor.ProseMirror h5,
.pub-body-component .editor.ProseMirror h6,
.pub-body-styles h1,
.pub-body-styles h2,
.pub-body-styles h3,
.pub-body-styles h4,
.pub-body-styles h5,
.pub-body-styles h6 {
  margin-bottom: 0.5em;
  line-height: 1em;
  font-weight: 500;
  font-family: "Source Sans 3", -apple-system, "BlinkMacSystemFont", "Segoe UI", "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Open Sans", "Helvetica Neue", sans-serif, "Noto Sans TC", "Noto Sans KR", "Noto Sans JP", "Noto Sans SC";
  letter-spacing: 1px;
}
@media only screen and (max-width: 750px) {
  .pub-body-component .editor.ProseMirror h1,
  .pub-body-component .editor.ProseMirror h2,
  .pub-body-component .editor.ProseMirror h3,
  .pub-body-component .editor.ProseMirror h4,
  .pub-body-component .editor.ProseMirror h5,
  .pub-body-component .editor.ProseMirror h6,
  .pub-body-styles h1,
  .pub-body-styles h2,
  .pub-body-styles h3,
  .pub-body-styles h4,
  .pub-body-styles h5,
  .pub-body-styles h6 {
    overflow-y: hidden;
    overflow-x: auto;
  }
}
.pub-body-component .editor.ProseMirror h1 a,
.pub-body-component .editor.ProseMirror h2 a,
.pub-body-component .editor.ProseMirror h3 a,
.pub-body-component .editor.ProseMirror h4 a,
.pub-body-component .editor.ProseMirror h5 a,
.pub-body-component .editor.ProseMirror h6 a,
.pub-body-styles h1 a,
.pub-body-styles h2 a,
.pub-body-styles h3 a,
.pub-body-styles h4 a,
.pub-body-styles h5 a,
.pub-body-styles h6 a {
  text-decoration: underline;
}
.pub-body-component .editor.ProseMirror h1,
.pub-body-styles h1 {
  font-size: 1.6em;
  font-weight: 700;
  line-height: 1.1em;
  letter-spacing: 0px;
}
.pub-body-component .editor.ProseMirror h2,
.pub-body-styles h2 {
  font-size: 1.4em;
  line-height: 1.1em;
  font-weight: 600;
  letter-spacing: 0px;
}
.pub-body-component .editor.ProseMirror h3,
.pub-body-styles h3 {
  font-size: 1.25em;
  line-height: 0.8em;
  font-weight: 400;
  letter-spacing: 0px;
}
.pub-body-component .editor.ProseMirror h4,
.pub-body-styles h4 {
  font-size: 1em;
  line-height: 1.3em;
  font-weight: 600;
  letter-spacing: 0px;
}
.pub-body-component .editor.ProseMirror h5,
.pub-body-styles h5 {
  font-size: 1em;
  line-height: 1.3em;
  font-weight: 500;
  letter-spacing: 0px;
}
.pub-body-component .editor.ProseMirror h6,
.pub-body-styles h6 {
  font-size: 1em;
  line-height: 1.3em;
  font-weight: 300;
  letter-spacing: 0px;
}
.pub-body-component .editor.ProseMirror h1 strong, .pub-body-component .editor.ProseMirror h2 strong, .pub-body-component .editor.ProseMirror h3 strong, .pub-body-component .editor.ProseMirror h4 strong, .pub-body-component .editor.ProseMirror h5 strong, .pub-body-component .editor.ProseMirror h6 strong,
.pub-body-styles h1 strong,
.pub-body-styles h2 strong,
.pub-body-styles h3 strong,
.pub-body-styles h4 strong,
.pub-body-styles h5 strong,
.pub-body-styles h6 strong {
  font-weight: inherit;
}
.pub-body-component .editor.ProseMirror * + h1,
.pub-body-component .editor.ProseMirror * + h2,
.pub-body-component .editor.ProseMirror * + h3,
.pub-body-component .editor.ProseMirror * + h4,
.pub-body-component .editor.ProseMirror * + h5,
.pub-body-component .editor.ProseMirror * + h6,
.pub-body-styles * + h1,
.pub-body-styles * + h2,
.pub-body-styles * + h3,
.pub-body-styles * + h4,
.pub-body-styles * + h5,
.pub-body-styles * + h6 {
  margin-top: 1.4em;
}
.pub-body-component .editor.ProseMirror p,
.pub-body-component .editor.ProseMirror li,
.pub-body-styles p,
.pub-body-styles li {
  font-family: "Source Serif 4", Georgia, Cambria, "Times New Roman", Times, serif;
  font-weight: 400;
  font-style: normal;
  line-height: 1.7;
  letter-spacing: -0.023em;
  word-break: break-word;
}
.pub-body-component .editor.ProseMirror li,
.pub-body-styles li {
  margin: 0;
}
.pub-body-component .editor.ProseMirror li > p,
.pub-body-styles li > p {
  margin: 0;
}
.pub-body-component .editor.ProseMirror p,
.pub-body-styles p {
  margin: 0em 0em 1em;
}
@media only screen and (max-width: 750px) {
  .pub-body-component .editor.ProseMirror p,
  .pub-body-styles p {
    overflow-y: hidden;
    overflow-x: auto;
  }
}
.pub-body-component .editor.ProseMirror ul > li::marker,
.pub-body-styles ul > li::marker {
  font-size: 0.8em;
}
.pub-body-component .editor.ProseMirror ul,
.pub-body-component .editor.ProseMirror ol,
.pub-body-styles ul,
.pub-body-styles ol {
  padding-left: 1em;
  margin: 0em 0em 1em;
}
.pub-body-component .editor.ProseMirror ul ul,
.pub-body-component .editor.ProseMirror ul ol,
.pub-body-component .editor.ProseMirror ol ul,
.pub-body-component .editor.ProseMirror ol ol,
.pub-body-styles ul ul,
.pub-body-styles ul ol,
.pub-body-styles ol ul,
.pub-body-styles ol ol {
  margin-bottom: 0em;
}
.pub-body-component .editor.ProseMirror td ol,
.pub-body-styles td ol {
  padding-left: 0;
  list-style-position: inside;
}
.pub-body-component .editor.ProseMirror td ol li p,
.pub-body-styles td ol li p {
  word-break: break-word;
}
.pub-body-component .editor.ProseMirror td ol li p:first-child,
.pub-body-styles td ol li p:first-child {
  display: inline;
}
.pub-body-component .editor.ProseMirror hr,
.pub-body-styles hr {
  margin: 1em 0em;
}
.pub-body-component .editor.ProseMirror pre,
.pub-body-styles pre {
  box-shadow: none;
  white-space: pre;
  overflow: hidden;
  overflow-x: auto;
}
.pub-body-component .editor.ProseMirror pre code,
.pub-body-styles pre code {
  display: block;
  white-space: pre;
  background-color: transparent;
  padding: 0em;
}
.pub-body-component .editor.ProseMirror pre.codeblock-wrapper,
.pub-body-styles pre.codeblock-wrapper {
  margin-bottom: 0;
  padding-bottom: 30px;
}
.pub-body-component .editor.ProseMirror code,
.pub-body-styles code {
  background-color: rgba(27, 31, 35, 0.06);
  border-radius: 2px;
  font-size: 0.8em;
  margin: 0;
  padding: 0.2em 0.4em;
}
.pub-body-component .editor.ProseMirror blockquote,
.pub-body-styles blockquote {
  line-height: inherit;
  font-size: 1em;
  margin: 0 0 1em;
  border-left: solid 4px rgba(181, 181, 181, 0.5);
  padding: 0 1em;
}
.pub-body-component .editor.ProseMirror .file,
.pub-body-styles .file {
  font-size: 0.75em;
}
.pub-body-component .editor.ProseMirror figcaption,
.pub-body-styles figcaption {
  font-size: 15px;
}
.pub-body-component .editor.ProseMirror figcaption p,
.pub-body-styles figcaption p {
  margin-bottom: 0em;
  line-height: 1.2em;
  font-family: -apple-system, "BlinkMacSystemFont", "Segoe UI", "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Open Sans", "Helvetica Neue", sans-serif;
}
.pub-body-component .editor.ProseMirror iframe,
.pub-body-styles iframe {
  border: 0px solid transparent;
}
.pub-body-component .editor.ProseMirror *:first-child:not(.discussion-thread),
.pub-body-styles *:first-child:not(.discussion-thread) {
  margin-top: 0em;
}

.pub-body-component {
  position: relative;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  -moz-font-feature-settings: "liga" on;
  font-feature-settings: "liga" on;
  font-size: 13px;
  min-height: 300px;
  margin-top: 25px;
}
.pub-body-component .editor.ProseMirror {
  min-height: 150px;
}
.pub-body-component .bp3-callout.working-draft {
  display: flex;
  align-items: center;
}
.pub-body-component .bp3-callout.working-draft span {
  flex-grow: 1;
  flex-shrink: 1;
}
.pub-body-component .permanent {
  background-color: #ffc940;
}

.pub-body-alert .error-time {
  font-weight: bold;
}

body {
  font-family: -apple-system, "BlinkMacSystemFont", "Segoe UI", "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Open Sans", "Helvetica Neue", sans-serif;
}

/* Paged-specific overrides */
.csl-bib-body,
.csl-entry {
  display: inline;
}

.pub-body-component .editor.ProseMirror .pub-notes ol > li {
  list-style-position: inside;
  margin: inherit;
}
.pub-body-component .editor.ProseMirror .pub-notes ol > li:target {
  background: cornsilk;
}
.pub-body-component .editor.ProseMirror .pub-notes ol > li p:last-child {
  display: inline;
}
.pub-body-component .editor.ProseMirror .pub-notes ol > li p:last-child:before {
  display: inline;
  content: " ";
}
.pub-body-component .editor.ProseMirror .pub-notes ol > li .return-link {
  font-size: 0.75em;
}
.pub-body-component .editor.ProseMirror figure > * {
  pointer-events: auto;
}

section.cover {
  font-family: "Source Sans 3", -apple-system, "BlinkMacSystemFont", "Segoe UI", "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Open Sans", "Helvetica Neue", sans-serif, "Noto Sans TC", "Noto Sans KR", "Noto Sans JP", "Noto Sans SC";
}
section.cover .title {
  margin-top: 0;
  font-size: 3em;
  font-weight: 800;
  letter-spacing: -1.1px;
  line-height: 1.4em;
}
section.cover .byline h3 {
  margin: 0;
}
section.cover .byline h3 span.name {
  white-space: nowrap;
  display: inline-block;
  margin-right: 0.2em;
}
section.cover .byline h5 {
  margin: 0;
  margin-top: 0.5em;
}
section.cover .byline h5 span.affiliation {
  white-space: break-word;
  display: inline-block;
  margin-right: 0.2em;
}
section.cover .details > *:not(:last-child) {
  margin-bottom: 7px;
}
section.cover .title,
section.cover .byline,
section.cover .details {
  margin-bottom: 30px !important;
}

@media screen {
  body > * {
    max-width: 700px;
    margin: 0 auto;
  }
  body > *.pub-body-component {
    font-size: 20px !important;
  }
}
@media print {
  /* Baseline page styles */
  @page {
    size: Letter;
    @top-left {
      color: #666;
      font-size: 10px;
      font-family: "Source Sans 3", -apple-system, "BlinkMacSystemFont", "Segoe UI", "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Open Sans", "Helvetica Neue", sans-serif, "Noto Sans TC", "Noto Sans KR", "Noto Sans JP", "Noto Sans SC";
      content: string(top-heading-items);
      vertical-align: top;
      padding-top: 1cm;
    }
    @top-right {
      color: #666;
      font-size: 10px;
      font-family: "Source Sans 3", -apple-system, "BlinkMacSystemFont", "Segoe UI", "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Open Sans", "Helvetica Neue", sans-serif, "Noto Sans TC", "Noto Sans KR", "Noto Sans JP", "Noto Sans SC";
      content: string(title);
      vertical-align: top;
      padding-top: 1cm;
    }
    @top-center {
      content: "";
      width: 1cm;
    }
    @bottom-center {
      color: #666;
      font-size: 10px;
      font-family: "Source Sans 3", -apple-system, "BlinkMacSystemFont", "Segoe UI", "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Open Sans", "Helvetica Neue", sans-serif, "Noto Sans TC", "Noto Sans KR", "Noto Sans JP", "Noto Sans SC";
      content: counter(page);
    }
  }
  /* Avoid being the last element on the page */
  h1,
  h2,
  h3,
  h4,
  h5,
  h6 {
    break-after: avoid;
  }
  tr,
  th {
    break-inside: avoid;
    max-height: 90vh;
    overflow-y: hidden;
  }
  .editor figure {
    break-inside: avoid;
    display: flex;
    flex-direction: column;
    max-height: 800px;
  }
  .editor figure img,
  .editor figure video {
    break-inside: avoid;
    width: 100%;
    min-height: 0;
    max-height: 100%;
    flex-shrink: 1;
    object-fit: contain;
  }
  figcaption {
    font-size: 10px;
    color: #555;
    flex-shrink: 0;
  }
  table {
    font-size: 12px;
    border-collapse: collapse;
    table-layout: fixed;
    width: 100%;
    overflow: hidden;
  }
  table caption {
    text-align: left;
  }
  table,
  tr,
  th,
  td {
    border: 1px #ccc solid;
    padding: 5px;
  }
  th {
    font-weight: bold;
    text-align: left;
    background-color: #f0f0f4;
  }
  td,
  a {
    word-break: break-word;
  }
  a.footnote {
    vertical-align: super;
    font-size: 10px;
  }
  [data-node-type=math-block] {
    font-size: unset;
    break-inside: avoid;
  }
  section.cover {
    page: cover;
  }
  @page cover {
    @top-left {
      content: "";
    }
    @top-right {
      content: "";
    }
    @bottom-center {
      content: "";
    }
  }
  .top-heading-items {
    string-set: top-heading-items content();
  }
  .title {
    string-set: title content();
  }
}</style></head><body><section class="cover"><h3 class="top-heading-items">IA eñ ™ - (La Biblia de la IA - The Bible of AI ™ ISSN 2695-6411) • Bases de la física del Universo</h3><h1 class="title" style="color:#0f5889">Línea del Umbral SV, circulación de retorno del dominio-universo y átomo formal de ascendencia no agotada</h1><div class="byline"><h3><span class="name">Juan Antonio Lloret Egea</span></h3></div><h4>IA eñ ™ - (La Biblia de la IA - The Bible of AI ™ ISSN 2695-6411)</h4><div class="details"><div><strong>Published on: </strong> Jun 04, 2026</div><div><strong>DOI: </strong><a href="https://doi.org/10.21428/39829d0b.30dfd78b">https://doi.org/10.21428/39829d0b.30dfd78b</a></div><div><strong>License:</strong> <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC-BY-NC-ND 4.0)</a></div></div></section><div class="pub-body-component"><div class="editor Prosemirror"><div><hr/></div><figure id="nihecqyixe2" data-node-type="image" data-size="80" data-align="breakout" data-url="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/portada-71780535369828.png" data-caption="" data-href="" data-alt-text="" data-hide-label="false"><img srcSet="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/portada-71780535369828.png?width=1920&amp;fit=bounds 1x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/portada-71780535369828.png?width=1920&amp;fit=bounds&amp;dpr=2 2x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/portada-71780535369828.png?width=1920&amp;fit=bounds&amp;dpr=3 3x" src="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/portada-71780535369828.png?width=1920&amp;fit=bounds" alt=""/><figcaption id="nihecqyixe2-figure-caption"><div><div></div></div></figcaption></figure><div><hr/></div><p id="nstivuwketo"><strong>© 2026. Todos los derechos reservados.</strong> | [<strong>DOI</strong>: pendiente] | <strong>Juan Antonio Lloret Egea</strong> | ORCID: <a href="https://orcid.org/0000-0002-6634-3351">0000-0002-6634-3351</a> | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA) | IA eñ™ — La Biblia de la IA™ | <strong>ISSN 2695-6411</strong> | <strong>Licencia CC BY-NC-ND 4.0</strong> | Madrid, 04/06/2026 |</p><div><hr/></div><h2 id="resumen"><strong>Resumen</strong></h2><p id="nrnzd2sfvwe">La cosmología física contemporánea fija el régimen observacional de rotación, vorticidad, anisotropía y momento angular cosmológico mediante el CMB, <code>ΛCDM</code> y los límites de isotropía (Planck Collaboration, Aghanim, <em>et al</em>., 2020; Planck Collaboration, Akrami, <em>et al</em>., 2020; Saadeh et al., 2016). Este trabajo sitúa ahí la frontera externa de traducción y formula la tesis propia del <strong>S</strong>istema <strong>V</strong>ectorial <strong>SV</strong>: el dominio-universo físico realizado presenta circulación de retorno bajo dominio, frontera, potencial, intensidad, centro de lectura, brazo, traza, residual y conservación <em>append-only</em>. Cuando esa circulación conserva centro, brazo y momento interno de retorno, el régimen se identifica como giro. <strong>Ante una lectura externa superior, el dominio-universo físico comparece como átomo formal de clausura</strong>, es decir, como unidad indivisa de dominio realizada bajo frontera, identidad, residual y retorno. La demostración no parte de la cosmología contemporánea, de la mecánica cuántica, de la geodinamo ni de la tabla periódica convencional como fuentes de verdad del SV; <strong>esos marcos actúan como referencias externas de contraste y retorno..</strong>. La formulación parte de la <strong>Línea del Umbral SV</strong>, de la teoría de persistencia energética estructural desarrollada en la génesis del hidrógeno, del dominio extendido Ω₄₄₃ y del Catálogo de Pares Estructurales, donde <strong>ya</strong> se demuestra que el SV <strong>extiende un dominio no empírico</strong>, <strong>lo recorre de modo determinista y concluye formalmente su realización mediante criterios internos</strong>. La cadena resultante avanza por dominio, frontera, persistencia, traza, residual, retorno, conclusión formal y no agotamiento. La formulación incorpora el <strong>vector directriz</strong> de la Línea del Umbral SV, <code>υ_U^SV=(1,1)</code>, y su extensión al tránsito entre dominios mediante <code>u_D^SV:=𝔇_ΓΩ_D^SV</code>; así, la orientación polar, la variación factual y el vector residual ingresan en una misma condición de paso. El tránsito perfecto exige residual nulo; el tránsito gobernado admite residual declarado, acotado y visible, sin resolución simulada.</p><div><hr/></div><figure id="n23suhqapfx" data-node-type="image" data-size="70" data-align="center" data-url="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-41780608282651.png" data-caption="&lt;p id=&quot;nj4uxrn6j83&quot; data-reactroot=&quot;&quot;&gt;La imagen representa la instancia observable situada en dominio declarado, con frontera, identidad, soporte, traza, residual y retorno; circularidad de retorno, reactivación espiral y medición transducida convergen hacia la frontera sutural del dominio-universo, sin identificarla con TODO/NADA, Totalidad absoluta, materia oscura sustancial ni límite del espacio. &lt;strong&gt;(Es una representación contextual de la forma del Universo físico, desde el plano matemático del SV)&lt;/strong&gt;&lt;/p&gt;" data-href="" data-alt-text="" data-hide-label="false"><img srcSet="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-41780608282651.png?width=800&amp;fit=bounds 1x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-41780608282651.png?width=800&amp;fit=bounds&amp;dpr=2 2x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-41780608282651.png?width=800&amp;fit=bounds&amp;dpr=3 3x" src="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-41780608282651.png?width=800&amp;fit=bounds" alt="" aria-labelledby="n23suhqapfx-figure-caption"/><figcaption id="n23suhqapfx-figure-caption"><div><div><p id="nj4uxrn6j83" data-reactroot="">La imagen representa la instancia observable situada en dominio declarado, con frontera, identidad, soporte, traza, residual y retorno; circularidad de retorno, reactivación espiral y medición transducida convergen hacia la frontera sutural del dominio-universo, sin identificarla con TODO/NADA, Totalidad absoluta, materia oscura sustancial ni límite del espacio. <strong>(Es una representación contextual de la forma del Universo físico, desde el plano matemático del SV)</strong></p></div></div></figcaption></figure><div><hr/></div><figure id="ni0l7iq67jw" data-node-type="image" data-size="70" data-align="center" data-url="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/Universo_como_átomo-31780609922150.png" data-caption="&lt;p id=&quot;nvu0sh76m21&quot; data-reactroot=&quot;&quot;&gt;&lt;strong&gt;Dominio-universo como átomo formal de clausura.&lt;/strong&gt; Representación contextual tridimensional del dominio-universo físico realizado como unidad de lectura superior: el núcleo luminoso, las órbitas internas, los retornos direccionales y la frontera envolvente expresan centro, intensidad, traza, residual y retorno bajo conservación &lt;em&gt;append-only&lt;/em&gt;. La imagen no identifica el universo con un átomo químico, una esfera física ni una rotación rígida externa; sitúa el patrón atómico-sutural como figura formal de clausura, tránsito y ascendencia no agotada, en continuidad con la reducción del Anexo A a dominio, frontera, identidad, potencial, intensidad, traza, residual, retorno y conclusión formal.&lt;/p&gt;" data-href="" data-alt-text="" data-hide-label="false"><img srcSet="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/Universo_como_átomo-31780609922150.png?width=800&amp;fit=bounds 1x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/Universo_como_átomo-31780609922150.png?width=800&amp;fit=bounds&amp;dpr=2 2x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/Universo_como_átomo-31780609922150.png?width=800&amp;fit=bounds&amp;dpr=3 3x" src="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/Universo_como_átomo-31780609922150.png?width=800&amp;fit=bounds" alt="" aria-labelledby="ni0l7iq67jw-figure-caption"/><figcaption id="ni0l7iq67jw-figure-caption"><div><div><p id="nvu0sh76m21" data-reactroot=""><strong>Dominio-universo como átomo formal de clausura.</strong> Representación contextual tridimensional del dominio-universo físico realizado como unidad de lectura superior: el núcleo luminoso, las órbitas internas, los retornos direccionales y la frontera envolvente expresan centro, intensidad, traza, residual y retorno bajo conservación <em>append-only</em>. La imagen no identifica el universo con un átomo químico, una esfera física ni una rotación rígida externa; sitúa el patrón atómico-sutural como figura formal de clausura, tránsito y ascendencia no agotada, en continuidad con la reducción del Anexo A a dominio, frontera, identidad, potencial, intensidad, traza, residual, retorno y conclusión formal.</p></div></div></figcaption></figure><div><hr/></div><h2 id="ndice"><strong>Índice</strong></h2><p id="n88wb1xz06p">Resumen</p><p id="nfnl9hf7b74">Estado del arte físico y formal de referencia</p><ol id="npafqru8qks" start="0"><li><p id="n83rchujmrk">Tesis rectoras</p></li></ol><p id="nmjli5j2fes">I. Jerarquía de verdad, transducción y función de los retornos externos</p><p id="nk393cubkn0">II. Línea del Umbral SV: neutralización polar, potencial, intensidad y giro</p><p id="nxms7uckqg7">III. Vector directriz de la Línea del Umbral SV y tránsito entre dominios</p><p id="nzw46amlbz2">IV. Persistencia energética estructural como fórmula rectora de la cadena</p><p id="nmuzn0s2o1h">V. Del régimen preatómico al hidrógeno como primer caso conocido</p><p id="n2h5ib1z03c">VI. Helio, perfil radial de clausura y patrón atómico-sutural</p><p id="ni1wr4vl24l">VII. CPS-SV: extensión periódica, 325 candidatos estructurales y pares realizados</p><p id="n5qu2rqq665">VIII. Circulación de retorno de dominio: definición de giro, momento y reducción al absurdo</p><p id="ng088sbfeh3">IX. Circulación de retorno del dominio-universo físico realizado</p><p id="npr5nmrq9jq">X. Átomo formal de clausura</p><p id="nvvex6qc91n">XI. Dominio-universo como átomo formal ante lectura externa</p><p id="n5fb25mbt4v">XII. Ascendencia no agotada de dominios y no identificación con TODO/NADA</p><p id="n18bmr3fq9o">XIII. Dipolo electromagnético, inversión geomagnética y adopción lateral</p><p id="nujkufm6ntk">XIV. Fórmula rectora de identificación de pasos anteriores y posteriores a lo observado</p><p id="nrvpiw5yg61">XV. Teorema conjunto: circulación de retorno, átomo formal y ascendencia no agotada</p><p id="ny2skq6h2wk">XVI. Corolarios</p><p id="nyaiwk343xt">XVII. Criterios de refutación, conservación de U y error de plano</p><p id="niz292qaq4z">Conclusión</p><p id="n20vguzm6jj">Conclusión final del autor</p><p id="nmyw9yj1o4h">Anexo A. Trivialización, TODO/NADA e Imperfección: la terna <code>1-0-U</code>, la U honesta y el corolario de transducción no confinante</p><p id="ncaz795wnku">Bibliografía</p><div><hr/></div><h2 id="estado-del-arte-fsico-y-formal-de-referencia"><strong>Estado del arte físico y formal de referencia</strong></h2><p id="n15gizlriqx">El estado del arte externo se incorpora como referencia de retorno, <strong>no como fuente constitutiva de verdad del SV</strong>… La cosmología observacional contemporánea permanece organizada en torno al modelo ΛCDM, con ajuste robusto de parámetros cosmológicos al fondo cósmico de microondas, mediciones de temperatura, polarización y lente gravitacional (Planck Collaboration, Aghanim, <em>et al</em>., 2020). Al mismo tiempo, los análisis de isotropía y estadística del CMB <strong>reconocen anomalías de gran escala y límites residuales</strong> en ciertas pruebas de no gaussianidad e isotropía, sin convertirlas en sustitución del modelo estándar (Planck Collaboration, Akrami, <em>et al</em>., 2020). Esta situación delimita el retorno cosmológico: si &quot;giro&quot; se traduce como rotación rígida, vorticidad métrica o anisotropía global convencional, la transducción externa se contrasta con restricciones CMB y con modelos anisótropos muy acotados (Saadeh <em>et al</em>., 2016; Planck Collaboration, Akrami, <em>et al</em>., 2020). El SV no toma esos límites como prohibición de la definición interna de giro; los conserva como frontera de traducción cuando se devuelva una magnitud cosmológica externa. En el dominio atómico, la física externa dispone de referencias de alta precisión sobre espectros, niveles, transiciones e ionización. La base de datos atómica del NIST ofrece datos críticamente evaluados de niveles de energía, longitudes de onda y probabilidades de transición; para el helio neutro se registra la configuración fundamental <code>1s²</code> y el nivel <code>¹S₀</code> (NIST ASD Team, s. f.; Kramida <em>et al</em>., s. f.). En el hidrógeno, la descripción cuántica externa del orbital <code>1s</code> conserva simetría esférica en lectura radial; esa simetría <strong>no entra al SV como probabilidad fundante</strong>, sino como retorno de perfil (LibreTexts, 2026). Hidrógeno y helio no fundan la tesis del dominio-universo como átomo formal: suministran retornos de clausura atómica ligera que permiten distinguir átomo químico, átomo formal y unidad de dominio bajo lectura superior. El problema contemporáneo de los elementos superpesados obliga a mantener visible la frontera entre descubrimiento empírico y extensión estructural. IUPAC aprobó en 2016 los nombres y símbolos de los elementos 113, 115, 117 y 118; <strong>por tanto, la ciencia contemporánea reconoce oficialmente hasta el elemento 118</strong> (IUPAC, 2016). Más allá de ese límite existen predicciones teóricas, modelos relativistas y programas experimentales de síntesis. Pyykkö (2011) propuso una tabla periódica extendida hasta <code>Z≤172</code> mediante cálculos Dirac--Fock de átomos e iones, mientras que el trabajo reciente de Berkeley Lab con haces de titanio-50 comunicó una vía para producir livermorio y preparar la búsqueda del elemento 120 (Lawrence Berkeley National Laboratory, 2024; Pyykkö, 2011). Este marco no valida por sí mismo los 325 candidatos estructurales del CPS-SV; sí muestra que la extensión del dominio periódico es científicamente pertinente cuando se distingue predicción, candidato estructural y descubrimiento experimental. </p><div><hr/></div><figure id="njl27ng4lwi" data-node-type="image" data-size="100" data-align="breakout" data-url="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-01780615841098.png" data-caption="" data-href="" data-alt-text="" data-hide-label="false"><img srcSet="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-01780615841098.png?width=1920&amp;fit=bounds 1x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-01780615841098.png?width=1920&amp;fit=bounds&amp;dpr=2 2x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-01780615841098.png?width=1920&amp;fit=bounds&amp;dpr=3 3x" src="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-01780615841098.png?width=1920&amp;fit=bounds" alt=""/><figcaption id="njl27ng4lwi-figure-caption"><div><div></div></div></figcaption></figure><div><hr/></div><p id="nxk9gcvymvv">El CPS-SV entra en esta discusión como precedente interno decisivo. No declara empiria inexistente; declara dominio estructural extendido, función conclusiva y recorrido reproducible sobre <code>Ω₄₄₃</code>. La diferencia con el estado externo es precisa: la ciencia contemporánea avanza por síntesis nuclear, detección de cadenas de decaimiento, evaluación de prioridad y aprobación nominal; el SV, en este punto, avanza por dominio, criterios de admisibilidad, residual visible y conclusión formal. Por eso los candidatos <code>119–443</code> (véase la imagen superior) se leen como candidatos estructurales, no como elementos descubiertos. La potencia del precedente no reside en sustituir a IUPAC, sino en demostrar que el SV extiende un dominio, lo recorre determinísticamente y conserva la diferencia entre construcción y retorno empírico (Lloret Egea, 2026e). En electromagnetismo, la referencia externa fija la interpretación clásica de dipolo, momento, par y circulación de campo. La formulación convencional de un lazo de corriente en campo magnético permite definir momento magnético, par y energía de orientación; las ecuaciones de Maxwell describen que un campo magnético variable induce campo eléctrico y que corrientes o campos eléctricos variables generan campo magnético (OpenStax, 2016e, 2016f). La lectura en clave SV no niega ese marco; <strong>lo transduce</strong>. En el caso magnético, <code>Div_SV(B)=0</code> impide sustancializar polos magnéticos aislados. El dipolo se formula como orientación no separable de campo, circulación, corriente, frontera, traza, residual y retorno. La atracción entre dipolos se lee como compatibilidad de configuraciones con menor residual de retorno, y el giro de campo como régimen operatorio de rotor y circulación. El marco geofísico refuerza esta adopción lateral. El British Geological Survey describe la inversión como transformación de norte magnético en sur y viceversa; el USGS señala que lavas y sedimentos conservan firmas del campo ambiental en el momento de solidificación; NOAA NCEI indica que durante una inversión el campo seguiría existiendo, aunque debilitado y posiblemente con múltiples polos magnéticos (British Geological Survey, s. f.; NOAA National Centers for Environmental Information [NOAA NCEI], s. f.; U.S. Geological Survey, 2024). En el <strong>S</strong>istema <strong>V</strong>ectorial, esa información <strong>no prueba</strong> la circulación de retorno del dominio-universo; retorna como caso local donde orientación, campo, frontera y traza cambian sin borrar identidad de dominio. La inversión geomagnética muestra, por vía lateral, que una instancia de campo conserva inscripción y retorna con orientación no idéntica. El estado contemporáneo de las referencias externas deja una conclusión metodológica precisa. La cosmología estándar restringe la rotación física externa del universo; la física atómica describe hidrógeno y helio con precisión espectroscópica; la química <em>oficial</em> reconoce hasta el elemento 118; la física de superpesados explora <code>119–120</code> y modelos extendidos; el electromagnetismo formaliza dipolos, par y circulación; la geofísica documenta inversiones de polaridad y registros paleomagnéticos. </p><blockquote id="nebhibglhla"><p id="ny42bsos07s"><strong>Ninguno de esos marcos ocupa el lugar de fundamento interno del SV.</strong></p></blockquote><p id="nprxtsy6vxa"> Cada uno delimita una traducción posible, un retorno, una tensión o un residual. La tesis del SV se formula primero por Línea del Umbral, persistencia energética, frontera, traza, residual, retorno, conclusión formal y <em>append-only</em>; después se transduce hacia esos marcos para evitar confusión de planos. De este estado del arte surge el punto de partida operativo de la tesis. La pregunta no es si <code>ΛCDM</code> autoriza la circulación de retorno del dominio-universo, si NIST convierte el universo en helio, si IUPAC valida los candidatos <code>119–443</code> o si la geodinamo prueba una cosmología. La pregunta es si un dominio realizado con frontera, traza, residual y retorno niega circulación de retorno sin contradecir su condición de observable; si una clausura con traza y retorno niega lectura superior sin anular <em>append-only</em>; y si una cadena de dominios se detiene en un último observable físico sin identificarlo indebidamente con TODO/NADA. El estado externo sitúa esas preguntas; la demostración pertenece al SV.</p><h2 id="tesis-rectoras"><strong>0. Tesis rectoras</strong></h2><p id="n9lvqbadypg">Este trabajo sostiene dos tesis principales. <strong>La primera</strong> afirma que el dominio-universo físico realizado <strong>presenta circulación de retorno</strong> en el análisis del SV: todo observable realizado con frontera, traza, residual, retorno y conservación <em>append-only</em> exige circulación de retorno; si esa circulación dispone de potencial, intensidad, centro de lectura y brazo, adquiere momento; si el momento conserva traza y retorno bajo <em>append-only</em>, el régimen se identifica como giro. <strong>La segunda</strong> afirma que el dominio-universo <strong>comparece</strong> <strong>ante una lectura externa superior</strong> (un observador que mirase el Universo desde fuera) <strong>como átomo</strong> formal de clausura: unidad indivisa de dominio realizada, capaz de operar como unidad de lectura en una ascendencia no agotada. La relación con el átomo material es de patrón tipado ---centro de lectura, frontera, intensidad, persistencia, traza, residual y retorno---, no de identidad química o sustancial. En las fórmulas que siguen se distinguen dos usos de la salida ternaria. Cuando una expresión nombrada como tesis, error, tránsito o teorema toma el valor <code>0</code>, el valor designa conclusión sin error dentro del criterio declarado; cuando un predicado positivo toma el valor <code>1</code>, el valor designa presencia, admisión o realización de la propiedad. Por eso no hay contradicción entre escribir <code>T1_GiroΩU^SV=0</code> como conclusión de tesis y escribir <code>Giro_SV(o,Ω)=1</code> como admisión positiva del giro. <code>Ω</code> designa dominio; <code>o</code>, instancia u observable; <code>Tr</code>, traza; <code>Res</code>, residual; <code>Ret</code>, retorno; <code>Cl</code>, clausura; <code>Ctr</code>, centro de lectura; <code>Brazo</code>, separación situada respecto de ese centro; y <code>AppendOnly_SV</code>, conservación irreversible y acumulativa de inscripción. La forma en formulación lógica formal compacta de las dos tesis es: </p><p id="nmbkewhk345"><code>T1_GiroΩU^SV=0 ⇔ Obs_real(o_U,Ω_U)=1 ∧ Fron_sut(Ω_U) ∧ I_ΩU(o_U)&gt;0 ∧ CircRet_ΩU(o_U) ∧ Ctr_ΩU(o_U) ∧ Brazo_ΩU(o_U) ∧ Tr_ΩU(o_U) ∧ Res_ΩU(o_U) ∧ Ret_ΩU(o_U) ∧ AppendOnly_SV</code>; <code>T2_AtomoFormalΩU^SV=0 ⇔ Obs_real(o_U,Ω_U)=1 ∧ Cl_ΩU(o_U)=1 ∧ Tr_ΩU(o_U) ∧ Res_ΩU(o_U) ∧ Ret_{Ω_U→Ω_{U+1}}(o_U) ∧ Dom(Ω_{U+1}) ∧ UnidadCl_{Ω_{U+1}}(o_U)=1 ∧ ¬(Ω_U=TODO/NADA)</code>. </p><p id="nio41h7sfrt">El resultado conjunto no exige que la referencia externa devuelva una rotación rígida cosmológica. Exige que se demuestre giro como circulación de retorno de dominio. Tampoco exige que el universo observable sea un átomo químico, <strong>aunque lo presuponga</strong>. Exige que, bajo lectura superior, el dominio-universo opere como átomo formal de clausura. La ciencia contemporánea podrá devolver retornos, tensiones o residuales al traducir estas tesis a vorticidad, anisotropía, espectro atómico, geodinamo, estructura a gran escala o límites observacionales; </p><blockquote id="njigw8ydt39"><p id="nrq1j2copps"><strong>esos marcos no fundan ni cancelan el teorema que formulamos</strong>.</p></blockquote><h2 id="i-jerarqua-de-verdad-transduccin-y-funcin-de-los-retornos-externos"><strong>I. Jerarquía de verdad, transducción y función de los retornos externos</strong></h2><blockquote id="n04ulk0ll80"><p id="ntiu7iyaihz"><strong>El SV no toma la ciencia contemporánea como fuente constitutiva de sus tesis</strong>. </p></blockquote><p id="naq2w72trd3">La ciencia contemporánea entra como retorno, contraste y transducción disciplinaria. Por tanto, Planck-ΛCDM, el fondo cósmico de microondas, NIST, IUPAC, la geodinamo terrestre, Maxwell o la mecánica cuántica no deciden si el SV formula circulación de retorno de dominio, giro y átomo formal; indican qué devuelve cada lenguaje externo cuando la tesis SV se transduce a sus magnitudes y restricciones. </p><p id="nk43j8mbyd3">La jerarquía correcta es: definición, demostración interna, transducción externa, residual y conclusión formal. Esta distinción impide dos errores simétricos. El primero consistiría en <strong>pedir permiso a la cosmología estándar</strong> para definir circulación de retorno de dominio; el segundo, en presentar una tesis SV como si estuviera confirmada empíricamente en el mismo sentido que una magnitud física externa. Planck 2018 informa de un ajuste robusto del CMB al modelo base ΛCDM (Planck Collaboration, Aghanim, <em>et al</em>., 2020). Ese resultado pertenece al marco cosmológico externo. IUPAC reconoce oficialmente hasta el elemento 118 y aprobó los nombres de los elementos 113, 115, 117 y 118 en 2016 (IUPAC, 2016). Ese resultado pertenece al marco químico externo. NIST proporciona datos atómicos críticamente evaluados sobre niveles, longitudes de onda y transiciones (NIST ASD Team, s. f.). Ese resultado pertenece al marco espectroscópico externo. </p><blockquote id="nqbu40qd8ui"><p id="n6adt236iqz">En el Sistema Vectorial (SV), todos esos retornos se conservan como contraste, <strong>no como fundamento interno ni de verdad</strong>.</p></blockquote><h2 id="ii-lnea-del-umbral-sv-neutralizacin-polar-potencial-intensidad-y-giro"><strong>II. Línea del Umbral SV: neutralización polar, potencial, intensidad y giro</strong></h2><div><hr/></div><figure id="nfaf79k1iie" data-node-type="image" data-size="70" data-align="full" data-url="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/Línea_Umbral_del_SV-21780611006256.png" data-caption="&lt;p id=&quot;nyjvobzpw1r&quot; data-reactroot=&quot;&quot;&gt;&lt;strong&gt;Línea del Umbral SV: neutralización polar, potencial, intensidad y giro.&lt;/strong&gt; La recta μ=λ representa el umbral de igualdad polar, donde el potencial se neutraliza, &lt;code&gt;P=μ−λ=0&lt;/code&gt;, sin confundirse con el origen. El punto &lt;code&gt;(0,0)&lt;/code&gt; reúne simultáneamente potencial nulo e intensidad nula, mientras que todo punto no nulo &lt;code&gt;(a,a)&lt;/code&gt; pertenece también a la línea, pero con intensidad positiva, &lt;code&gt;I=μ+λ&amp;gt;0&lt;/code&gt;. Por encima y por debajo del umbral comparece la separación polar orientada, con distinción entre Nada/Ausencia y Exceso/Totalidad. La figura incorpora, además, la referencia trigonométrica del primer cuadrante en &lt;code&gt;45°&lt;/code&gt;, donde &lt;code&gt;sin(x)=cos(x)=√2/2&lt;/code&gt;, como caso externo de representación no clausurada. Bajo retorno, la separación orientada puede adquirir momento respecto de un centro de lectura y expresarse como giro.&lt;/p&gt;" data-href="" data-alt-text="" data-hide-label="false"><img srcSet="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/Línea_Umbral_del_SV-21780611006256.png?width=800&amp;fit=bounds 1x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/Línea_Umbral_del_SV-21780611006256.png?width=800&amp;fit=bounds&amp;dpr=2 2x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/Línea_Umbral_del_SV-21780611006256.png?width=800&amp;fit=bounds&amp;dpr=3 3x" src="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/Línea_Umbral_del_SV-21780611006256.png?width=800&amp;fit=bounds" alt="" aria-labelledby="nfaf79k1iie-figure-caption"/><figcaption id="nfaf79k1iie-figure-caption"><div><div><p id="nyjvobzpw1r" data-reactroot=""><strong>Línea del Umbral SV: neutralización polar, potencial, intensidad y giro.</strong> La recta μ=λ representa el umbral de igualdad polar, donde el potencial se neutraliza, <code>P=μ−λ=0</code>, sin confundirse con el origen. El punto <code>(0,0)</code> reúne simultáneamente potencial nulo e intensidad nula, mientras que todo punto no nulo <code>(a,a)</code> pertenece también a la línea, pero con intensidad positiva, <code>I=μ+λ&gt;0</code>. Por encima y por debajo del umbral comparece la separación polar orientada, con distinción entre Nada/Ausencia y Exceso/Totalidad. La figura incorpora, además, la referencia trigonométrica del primer cuadrante en <code>45°</code>, donde <code>sin(x)=cos(x)=√2/2</code>, como caso externo de representación no clausurada. Bajo retorno, la separación orientada puede adquirir momento respecto de un centro de lectura y expresarse como giro.</p></div></div></figcaption></figure><div><hr/></div><p id="n00wrcbnbbq"><strong>Línea del Umbral SV </strong>es la recta de igualdad polar μ=λ: el umbral donde Totalidad y Nada se neutralizan como predominio, sin confundirse con el origen. En el plano del <strong>potencial de un suceso</strong> coincide con el lugar donde <code>P=μ−λ=0</code>; sin embargo, no todo punto de la línea equivale al origen, porque la intensidad polar I=μ+λ  conserva valor positivo cuando μ=λ=a y a&gt;0. Sólo (0,0) reúne potencial nulo e intensidad nula. Cualquier punto no nulo (a,a) pertenece a la Línea del Umbral SV como igualdad polar con intensidad positiva. <strong>La línea contiene el origen, pero no se identifica con él</strong>: actúa como <strong>umbral de transición</strong> entre neutralización polar, Exceso/Totalidad y Nada/Ausencia. En el plano SV una separación, un retorno o una superficie de dominio se determinan por potencial, intensidad, dominio, frontera, traza, residual y retorno sin que su expresión metrológica externa agote la representación. <strong>La Línea del Umbral</strong> ordena esa lectura: sobre ella el potencial se neutraliza; fuera de ella aparece separación polar orientada. <strong>El potencial</strong> fija sentido y grado de separación; <strong>la intensidad</strong> fija presencia polar total y evita confundir igualdad con origen. La inagotabilidad representacional no define el SV, pero permite comprender que una magnitud esté determinada y no se agote en retorno numérico finito. Cuando la separación polar se sitúa bajo retorno, la Línea del Umbral actúa como referencia de giro. Si el suceso permanece sobre ella, la diferencia polar se neutraliza; si se separa por encima o por debajo, comparece orientación hacia Exceso/Totalidad o hacia Nada/Ausencia. Esa orientación no depende de una constante geométrica externa, sino de potencial, intensidad, dominio, frontera, traza, residual, retorno y conservación <em>append-only</em>. Si P≠0, aparece orientación polar; si esa orientación se sitúa bajo dominio, frontera y brazo respecto de un centro de lectura, adquiere momento; si conserva traza, residual y retorno, el momento se expresa como giro.</p><h2 id="iii-vector-directriz-de-la-lnea-del-umbral-y-trnsito-entre-dominios"><strong>III. Vector directriz de la Línea del Umbral y tránsito entre dominios</strong></h2><div><hr/></div><figure id="nd558pg343s" data-node-type="image" data-size="80" data-align="full" data-url="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/Vector_directriz-51780616724049.png" data-caption="" data-href="" data-alt-text="" data-hide-label="false"><img srcSet="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/Vector_directriz-51780616724049.png?width=800&amp;fit=bounds 1x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/Vector_directriz-51780616724049.png?width=800&amp;fit=bounds&amp;dpr=2 2x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/Vector_directriz-51780616724049.png?width=800&amp;fit=bounds&amp;dpr=3 3x" src="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/Vector_directriz-51780616724049.png?width=800&amp;fit=bounds" alt=""/><figcaption id="nd558pg343s-figure-caption"><div><div></div></div></figcaption></figure><div><hr/></div><p id="nu90hp4sc8d">Una recta no sólo fija un lugar; también fija una dirección. En geometría externa, una recta se declara mediante un punto y un vector paralelo a ella, <strong>denominado vector de dirección o vector directriz</strong> (Feldman, Rechnitzer, &amp; Yeager, 2022; OpenStax, 2016a). Esta regla se recibe sin convertirla en fundamento externo. La Línea del Umbral <code>μ=λ</code> recibe un vector directriz propio, y ese vector distingue tres funciones: neutralización, orientación y tránsito. La directriz de la línea es <code>υ_U^SV=(1,1)</code>, porque todo desplazamiento de la forma <code>(a,a)</code> permanece sobre <code>μ=λ</code>; su vector normal polar es <code>n_U^SV=(1,−1)</code>, porque mide la salida de la igualdad. </p><p id="n1f5v04da6m">Para un punto polar <code>x=(μ,λ)</code>, el potencial actúa como componente normal <code>P=n_U^SV·x=μ−λ</code>, mientras la intensidad actúa como componente directriz <code>I=υ_U^SV·x=μ+λ</code>. </p><p id="n321qj5st51">Sobre la Línea del Umbral el potencial se neutraliza, pero la intensidad crece en dirección directriz; fuera de la línea, el potencial mide separación polar respecto de esa directriz. Esta distinción impide confundir <code>(0,0)</code> con <code>(a,a)</code>, y permite entender que la igualdad polar no es inmovilidad, sino permanencia sobre una dirección de intensidad positiva cuando <code>a&gt;0</code>. El vector directriz de la Línea del Umbral se articula con el vector director ya fijado para el tránsito por dominios. <em><a href="https://www.itvia.online/pub/hidrogeno-helio-y-materia-ordinaria-regimen-hhe-referencia-solar-tabla-periodica-estructural-moleculas-y-vida-biologica#i11-definicin-general-de-trnsito-por-dominios" target="_blank">El origen material ordinario del universo observable</a></em><a href="https://www.itvia.online/pub/hidrogeno-helio-y-materia-ordinaria-regimen-hhe-referencia-solar-tabla-periodica-estructural-moleculas-y-vida-biologica#i11-definicin-general-de-trnsito-por-dominios" target="_blank"> formula el tránsito entre dominios</a> (ver enlace) mediante dominio de salida, dominio de llegada, identidad tipada, frontera, canal, traza, residual y retorno; además incorpora el vector director termodinámico <code>u_SV:=𝔇_ΓΩ_SV</code>, entendido como variación factual de sección entre sucesos consecutivos y no como cociente temporal externo (Lloret Egea, 2026f). Esta conexión permite elevar la lectura: <code>υ_U^SV</code> orienta la recta polar; <code>u_D^SV:=𝔇_ΓΩ_D^SV</code> orienta el tránsito entre dominios; y el vector residual decide el rango del paso. La forma unificada algebraica es: </p><p id="nc5z8y5ni4v"><code>υ_U^SV=(1,1)</code>; <code>n_U^SV=(1,−1)</code>; <code>P(μ,λ)=n_U^SV·(μ,λ)=μ−λ</code>; <code>I(μ,λ)=υ_U^SV·(μ,λ)=μ+λ</code>; <code>u_D^SV(D_i,D_j;x):=𝔇_ΓΩ_D^SV(D_i,D_j;x)</code>; <code>R_D^SV(D_i,D_j;x)=(Δ_dom,Δ_id,Δ_estado,Δ_F,Δ_C,Δ_Tr,Δ_R).</code></p><p id="n6cs16duznv"> La condición de tránsito no consiste en proclamar continuidad por nombre común, sino en alinear dirección, dominio y residual. Si el tránsito sale de un dominio <code>D_i</code> hacia un dominio <code>D_j</code>, el vector director <code>u_D^SV</code> debe estar declarado; si falta, la flecha entre dominios permanece como notación sin gobierno. Si el vector existe, el residual decide el rango del paso. Residual nulo y residual gobernado no son equivalentes: el primero autoriza tránsito perfecto; el segundo autoriza tránsito gobernado bajo control explícito de las componentes no anuladas. </p><p id="nqbzwa0kglk">La forma como álgebra compacta se separa de la siguiente manera: <code>TrPerf_D^SV(D_i,D_j;x)=0 ⇔ u_D^SV(D_i,D_j;x) declarado ∧ R_D^SV(D_i,D_j;x)=0 ∧ Ret(D_i,D_j;x) ∧ 𝓔★(Γ_U;τ)=0</code>; <code>TrGob_D^SV(D_i,D_j;x)=0 ⇔ u_D^SV(D_i,D_j;x) declarado ∧ R_D^SV(D_i,D_j;x)≠0 ∧ Gov(R_D^SV(D_i,D_j;x))=1 ∧ Ret(D_i,D_j;x) ∧ 𝓔★(Γ_U;τ)=0</code>; <code>Err_Tr_D^SV=1 ⇔ u_D^SV no declarado ∨ Δ_dom no gobernado ∨ Δ_id no gobernado ∨ Δ_estado no gobernado ∨ Δ_F no gobernado ∨ Δ_C no gobernado ∨ Δ_Tr no gobernado ∨ Δ_R no gobernado</code>; <code>U_Tr_D^SV ⇔ u_D^SV, dominio, frontera, canal, traza, residual o retorno insuficientes sin contradicción</code>; <code>Gov(R_D^SV)=1:</code> significa que cada componente residual se declara, se acota, permanece visible y no se usa como resolución simulada. </p><p id="niycy1k77x8">Con ello, la cadena de tránsito se tipa: tránsito perfecto cuando no hay residual; tránsito gobernado cuando el residual no se anula pero permanece bajo control material; error cuando alguna componente se oculta o se trata como irrelevante; <code>U</code> cuando faltan datos sin contradicción. En la <strong>Línea del Umbral SV</strong> la directriz <code>υ_U^SV</code> conserva la igualdad polar con intensidad positiva; en el paso entre dominios, <code>u_D^SV</code> conserva la dirección factual de tránsito; en el régimen hidrógeno-helio, el residual <code>R_Uk^SV(D_i,D_j;x)=Δ_dom ⊕ Δ_id ⊕ Δ_Ereg ⊕ Δ_F ⊕ Δ_C ⊕ Δ_Tr ⊕ Δ_R</code> decide si el umbral se atraviesa sin defecto o bajo gobierno; en la clausura de observables, <strong>la reactivación espiral </strong>(ver imagen inferior) sólo procede si <code>Tr</code>, <code>Res</code> y <code>Ret</code> autorizan lectura nueva sin deshacer la instancia clausurada. Con ello, la cadena <code>Línea del Umbral → ruptura polar → persistencia → hidrógeno → CPS-SV → dipolo → dominio-universo → átomo formal superior</code> deja de depender de sucesión verbal: toda recta posee directriz, todo tránsito admisible posee vector director y todo tránsito exige residual nulo o residual gobernado.</p><div><hr/></div><figure id="nckdc9eyp21" data-node-type="image" data-size="50" data-align="full" data-url="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-61780584994343.png" data-caption="" data-href="" data-alt-text="" data-hide-label="false"><img srcSet="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-61780584994343.png?width=800&amp;fit=bounds 1x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-61780584994343.png?width=800&amp;fit=bounds&amp;dpr=2 2x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-61780584994343.png?width=800&amp;fit=bounds&amp;dpr=3 3x" src="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-61780584994343.png?width=800&amp;fit=bounds" alt=""/><figcaption id="nckdc9eyp21-figure-caption"><div><div></div></div></figcaption></figure><div><hr/></div><h2 id="iv-persistencia-energtica-estructural-como-frmula-rectora-de-la-cadena"><strong>IV. Persistencia energética estructural como fórmula rectora de la cadena</strong></h2><p id="nw9us895tcc">Nuestro trabajo <em><a href="https://doi.org/10.17613/qq4q9-sd847" target="_blank">Génesis del hidrógeno y teoría de la persistencia energética estructural</a></em> aporta la fórmula rectora que identifica cualquier paso de la cadena sin depender de analogía de escala. La cuestión física se desplaza desde la materia como punto de partida hacia la persistencia como problema transversal: una configuración energética persiste si conserva identidad compatible frente a redistribución y residual bajo frontera declarada (Lloret Egea, 2026d). La ecuación formal mínima es: <code>𝓟_min(Γ,n)=𝓕_∂(Γ,n)−𝒬(Γ,n)−ℛ_Γ(n)</code>. La lectura es directa: <code>𝓕_∂</code> representa orientación y confinamiento de frontera; <code>𝒬</code>, redistribución energética efectiva; <code>ℛ_Γ</code>, residual estructural. Si <code>𝓟_min&gt;0</code>, la configuración conserva persistencia compatible; si <code>𝓟_min≈0</code>, alcanza régimen crítico; si <code>𝓟_min&lt;0</code>, la dispersión domina sobre la frontera.</p><p id="nfopx550xu4">La masa estructural, bajo esta lectura, no es sustancia primaria, sino persistencia efectiva de frontera frente a redistribución y residual. Esta fórmula integra polos, régimen preatómico, hidrógeno, helio, <a href="https://doi.org/10.21428/39829d0b.a56b9cd7">pares estructurales</a>, dipolos, campo geomagnético, estrellas, galaxias y dominio-universo bajo una disciplina común. No porque todos sean materialmente idénticos, sino porque todo paso de cadena debe declarar dominio, frontera, redistribución, residual, identidad y retorno. </p><p id="nmz0duubed1">La fórmula general de admisión como formulación lógica formal es: <code>Cad_SV(R_i)=0 ⇔ Dom(R_i) ∧ ∂Ω_i declarado ∧ 𝓟_min^{R_i}&gt;0 ∧ Id_i compatible ∧ Tr_i ∧ Res_i visible ∧ Ret_i ∧ 𝓔★(Γ_U;τ)=0</code>. El rechazo es: <code>Err_Cad_SV(R_i)=1 ⇔ Dom(R_i) no declarado ∨ ∂Ω_i ausente ∨ 𝓟_min^{R_i}≤0 ∨ Res_i omitido ∨ Ret_i inexistente ∨ 𝓔★(Γ_U;τ)≠0</code>.  Y la indeterminación: <code>U_Cad_SV(R_i) ⇔ datos, dominio, frontera, residual o retorno insuficientes sin contradicción.</code></p><div><hr/></div><figure id="nyltxdlmec4" data-node-type="image" data-size="70" data-align="full" data-url="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-31780617351559.png" data-caption="&lt;p id=&quot;n7ufkbv2d5h&quot; data-reactroot=&quot;&quot;&gt;Pulsar sobre  la imagen para leer: &lt;em&gt;&lt;a href=&quot;https://doi.org/10.21428/39829d0b.a56b9cd7&quot;&gt;Catálogo de Pares Estructurales SV (CPS-SV): enlace, aleación y compatibilidad posicional desde los 118 elementos base hasta los 443 candidatos del dominio extendido&lt;/a&gt;&lt;/em&gt;&lt;/p&gt;" data-href="https://doi.org/10.21428/39829d0b.a56b9cd7" data-alt-text="" data-hide-label="false"><a href="https://doi.org/10.21428/39829d0b.a56b9cd7" target="_blank"><img srcSet="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-31780617351559.png?width=800&amp;fit=bounds 1x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-31780617351559.png?width=800&amp;fit=bounds&amp;dpr=2 2x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-31780617351559.png?width=800&amp;fit=bounds&amp;dpr=3 3x" src="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-31780617351559.png?width=800&amp;fit=bounds" alt="" aria-labelledby="nyltxdlmec4-figure-caption"/></a><figcaption id="nyltxdlmec4-figure-caption"><div><div><p id="n7ufkbv2d5h" data-reactroot="">Pulsar sobre  la imagen para leer: <em><a href="https://doi.org/10.21428/39829d0b.a56b9cd7">Catálogo de Pares Estructurales SV (CPS-SV): enlace, aleación y compatibilidad posicional desde los 118 elementos base hasta los 443 candidatos del dominio extendido</a></em></p></div></div></figcaption></figure><h2 id="v-del-rgimen-preatmico-al-hidrgeno-como-primer-caso-conocido"><strong>V. Del régimen preatómico al hidrógeno como primer caso conocido</strong></h2><p id="nw2k9z7vdb2">El hidrógeno no opera como fundamento absoluto del <strong>S</strong>istema <strong>V</strong>ectorial, ni como universal clausurado, ni como sustituto de ε−0. Opera como primer caso conocido de persistencia atómica discreta estable dentro del dominio físico ordinario. La génesis del hidrógeno establece que el átomo no debe entenderse como entidad ontológica primaria, sino como régimen discreto conocido de persistencia energética estructural estable; el hidrógeno se define como caso particular de esa condición, no como clausura del problema general (Lloret Egea, 2026d). La condición estructural del hidrógeno estable es: <code>𝓟_min^H(Γ,n)&gt;0 ∧ δ(∂Ω_H)&lt;Λ_H ∧ ℛ_H(n)&lt;Λ_H ∧ Δ𝓗_H∈𝓢_disc^H ∧ 𝓔★(Γ_U;τ)=0</code>.  Y la transición correspondiente  <code>Ω_pre → Ω_H</code> en la que <code>Ω_pre</code> designa persistencia parcial sin frontera atómica plenamente estabilizada, y <code>Ω_H</code> designa régimen hidrógeno con frontera discreta, residual acotado, intercambio compatible e identidad conservada. La ciencia externa describe recombinación, estructura atómica, espectros y abundancia cosmológica; el SV conserva esos retornos como contraste, <strong>pero formula el resultado de otro modo</strong>: el hidrógeno aparece cuando una configuración preatómica estabiliza frontera discreta, acota residual y conserva identidad bajo intercambio energético compatible.</p><h2 id="vi-helio-perfil-radial-de-clausura-y-patrn-atmico-sutural"><strong>VI. Helio, perfil radial de clausura y patrón atómico-sutural</strong></h2><p id="nxnxbmzb5eu">El helio sirve como segundo retorno de clausura atómica ligera, con simetría central y configuración fundamental <code>1s² ¹S₀</code> en el registro espectroscópico externo. Hidrógeno y helio no fundan nuestro sistema; muestran que el patrón de dominio, centro de lectura, frontera, perfil radial, residual y retorno desciende a un régimen físico real. La igualdad con el dominio-universo no es química ni material: es patrón de clausura.</p><h2 id="vii-cps-sv-extensin-peridica-325-candidatos-estructurales-y-pares-realizados"><strong>VII. </strong><strong><a href="https://doi.org/10.21428/39829d0b.a56b9cd7">CPS-SV</a></strong><strong>: extensión periódica, 325 candidatos estructurales y pares realizados</strong></h2><p id="nq0hlw2qmcm">El desarrollo de <em><a href="https://doi.org/10.21428/39829d0b.a56b9cd7">Catálogo de Pares Estructurales SV (CPS-SV)</a></em> aporta el precedente matemático decisivo para la cadena ascendente. La ciencia contemporánea reconoce oficialmente hasta el elemento 118, y los candidatos 119--443 del SV no deben presentarse como elementos empíricamente descubiertos. En el CPS-SV comparecen como candidatos estructurales del dominio extendido. Esta precisión fortalece la tesis, porque el Sistema Vectorial no finge empiria donde opera una construcción de dominio. </p><blockquote id="nzs1at4a3ae"><p id="ngafbnv33x0">El CPS-SV  declara: <code>Ω₄₄₃=Ω₁₁₈∪Ω_ext</code>; <code>Ω₁₁₈={1,…,118}</code>; <code>Ω_ext={119,…,443}</code>; <code>|Ω_ext|=325</code> y el espacio completo de pares no ordenados: <code>𝒫₄₄₃={ {A,B} | A,B∈Ω₄₄₃, A≠B }</code>; <code>|𝒫₄₄₃|=C(443,2)=97.903</code>. </p></blockquote><p id="n97zckirfkt">La función conclusiva del CPS-SV recorre ese dominio y devuelve: <code>D(A,B)∈{APTO-M, APTO-C, APTO-I, NO-APTO}</code>. El resultado no es intuición de extensión, sino recorrido determinista de dominio: 9.515 pares APTO-M, 37.580 APTO-C, 5.075 APTO-I y 45.733 NO-APTO, con criterios de admisibilidad B.1--B.5, subdominios, familias tipológicas y laboratorio reproducible. </p><blockquote id="nhpjc52cjyc"><p id="nlqxxmbqg1t">La consecuencia para este trabajo es inmediata: el Sistema Vectorial (SV) ya ha demostrado que declara un dominio extendido no empírico, lo recorre, lo concluye formalmente y conserva refutabilidad. </p></blockquote><blockquote id="nol8mssnwvb"><p id="nqdky8pkzpv">Por tanto, la cadena ascendente hacia el dominio-universo no se introduce como intuición nueva; continúa una lógica ya demostrada: dominio → frontera → persistencia → conclusión formal → realización → retorno. </p></blockquote><p id="n9ek8dkkmcb">El CPS-SV también fija el principio transferible: allí donde exista arquitectura de cascada con niveles de evaluación, régimen de imperfección activa y salida reproducible, el enfoque se traslada a dominios superiores sin salto de plano. Para este trabajo, esa transferibilidad se reescribe así algebraicamente: <code>Transf_Cadena^SV(R)=0 ⇔ Dom(R) ∧ Cascada_R declarada ∧ D_R total ∧ Res_R visible ∧ Ret_R ∧ NoEmpiriaFingida=1 ∧ NoIdentMat=1 ∧ 𝓔★(Γ_U;τ)=0.</code></p><h2 id="viii-circulacin-de-retorno-de-dominio-definicin-de-giro-momento-y-reduccin-al-absurdo"><strong>VIII. Circulación de retorno de dominio: definición de giro, momento y reducción al absurdo</strong></h2><p id="np8von4x7i9">Se define giro de dominio como circulación de retorno de una instancia bajo potencial, intensidad, dominio, frontera, centro de lectura, brazo, traza, residual y conservación <em>append-only </em>(es decir ningún suceso se reescribe). El término &quot;giro&quot; no se toma como rotación rígida externa de un cuerpo, salvo cuando una referencia física lo devuelva expresamente. </p><p id="n9wv13teh81">La forma formal lógica es: <code>Giro_SV(o,Ω)=1 ⇔ Obs_real(o,Ω)=1 ∧ I_Ω(o)&gt;0 ∧ Ret_Ω(o) ∧ CircRet_Ω(o) ∧ Ctr_Ω(o) ∧ Brazo_Ω(o) ∧ Tr_Ω(o) ∧ Res_Ω(o) ∧ AppendOnly_SV</code>.</p><p id="n238nz663l6">En esta definición, <code>Ctr_Ω(o)</code> designa centro de lectura de dominio, no necesariamente centro material; <code>Brazo_Ω(o)</code> designa separación situada respecto de ese centro, no radio geométrico ordinario; <code>Ret_Ω(o)</code> designa retorno de la instancia a lectura bajo dominio; <code>CircRet_Ω(o)</code> designa régimen de retorno clausural, no imagen circular externa ni rotación rígida importada; <code>Tr_Ω(o)</code> conserva inscripción; <code>Res_Ω(o)</code> conserva el resto visible; <code>AppendOnly_SV</code> impide borrar inscripción para simular repetición idéntica. La Línea del Umbral SV ordena la transición: sobre <code>μ=λ</code>, el potencial se neutraliza; fuera de ella aparece orientación. Si <code>P_Ω(o)≠0</code>, la orientación se declara; si esa orientación se sitúa bajo centro y brazo, aparece momento; si el momento conserva traza y retorno bajo <em>append-only</em>, el giro se admite. </p><p id="nq85svnygj4">La reducción al absurdo del giro no identifica retorno simple y circulación de retorno. Primero exige el lema de retorno clausural: si una instancia realizada conserva retorno bajo frontera, traza, residual y <em>append-only</em>, el retorno no desaparece como descarga lineal sin inscripción; opera como régimen clausural de lectura. Esa condición se escribe en formalización algebraica: </p><p id="nsch635cng1"><code>LemaRetCl_SV(o,Ω)=0 ⇔ Ret_Ω(o) ∧ Fron_Ω(o) ∧ Tr_Ω(o) ∧ Res_Ω(o) ∧ AppendOnly_SV ⇒ CircRet_Ω(o)=1.</code> </p><p id="nqiv3y2zu3i">Supóngase ahora un observable realizado <code>o</code> en un dominio <code>Ω</code>, con frontera, traza, residual y retorno clausural, pero sin circulación de retorno. Si no hay circulación de retorno, el retorno no opera como régimen; si el retorno no opera como régimen, la clausura local no devuelve lectura; si la clausura local no devuelve lectura, la instancia deja de cumplir la regla de observable realizado. La hipótesis niega una condición que ella misma presupone. Por tanto: <code>Obs_real(o,Ω)=1 ∧ Ret_Ω(o) ∧ Fron_Ω(o) ∧ Tr_Ω(o) ∧ Res_Ω(o) ∧ AppendOnly_SV ⇒ CircRet_Ω(o)=1</code>. Si, además, la instancia posee intensidad positiva, potencial no nulo, centro de lectura y brazo, la circulación de retorno no permanece como neutralización abstracta; adquiere momento: <code>Obs_real(o,Ω)=1 ∧ I_Ω(o)&gt;0 ∧ P_Ω(o)≠0 ∧ Ctr_Ω(o) ∧ Brazo_Ω(o) ⇒ Mom_SV(o,Ω)=1</code>; <code>Mom_SV(o,Ω)=1 ∧ Tr_Ω(o) ∧ Res_Ω(o) ∧ Ret_Ω(o) ∧ AppendOnly_SV ⇒ Giro_SV(o,Ω)=1.</code></p><h2 id="ix-circulacin-de-retorno-del-dominio-universo-fsico-realizado"><strong>IX. Circulación de retorno del dominio-universo físico realizado</strong></h2><p id="nb24t6ltsqz">La aplicación al dominio-universo no procede por analogía visual con el átomo ni por importación de una rotación cosmológica externa. Procede por pertenencia a la regla de observable realizado. Si <code>o_U</code> comparece como observable realizado del dominio-universo <code>Ω_U</code>, con frontera sutural, contenido retornado, residual, traza, medición transducida, balance termodinámico e irreversibilidad entrópica, no queda exento de la condición general de circulación de retorno sin introducir una excepción de escala. La excepción diría: todo observable realizado exige retorno, salvo el observable de máxima escala física. Esa excepción no se deduce del Sistema Vectorial; importa privilegio externo de escala. Por reducción al absurdo, si <code>o_U</code> es observable realizado y se niega su circulación de retorno como giro, se niega que su retorno tenga régimen de circulación; si se niega esa circulación, se anula la clausura de dominio que lo hace comparecer. </p><p id="n6g03dy6a7n"><code>Obs_real(o_U,Ω_U)=1 ∧ Fron_sut(Ω_U) ∧ Tr_ΩU(o_U) ∧ Res_ΩU(o_U) ∧ Ret_ΩU(o_U) ∧ AppendOnly_SV ⇒ CircRet_ΩU(o_U)=1</code>; <code>CircRet_ΩU(o_U)=1 ∧ I_ΩU(o_U)&gt;0 ∧ Ctr_ΩU(o_U) ∧ Brazo_ΩU(o_U) ∧ AppendOnly_SV ⇒ Giro_SV(o_U,Ω_U)=1.</code> </p><p id="nrmllaqqzji">En esta aplicación formal, <code>o_U</code> nombra el observable del dominio-universo, <code>Ω_U</code> el dominio-universo físico realizado, <code>Fron_sut</code> la frontera sutural que permite distinguir dominio y exterior de lectura, <code>Tr_ΩU</code> la inscripción conservada, <code>Res_ΩU</code> el residual visible y <code>Ret_ΩU</code> el retorno de dominio. El enunciado &quot;giro&quot; se define aquí con rigor interno: el dominio-universo presenta circulación de retorno de dominio bajo <a href="https://doi.org/10.21428/39829d0b.7b41835f">frontera sutural</a>, (<strong>véase imagen de abajo</strong>), traza, residual, potencial, intensidad, centro de lectura, brazo y <em>append-only</em>. La transducción hacia rotación rígida, vorticidad métrica, anisotropía global o momento angular cosmológico exige dominio, magnitud, residual y retorno; no funda el teorema interno ni lo cancela.</p><div><hr/></div><figure id="n3t9beojtru" data-node-type="image" data-size="70" data-align="breakout" data-url="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-31780618026813.png" data-caption="" data-href="" data-alt-text="" data-hide-label="false"><img srcSet="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-31780618026813.png?width=1920&amp;fit=bounds 1x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-31780618026813.png?width=1920&amp;fit=bounds&amp;dpr=2 2x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-31780618026813.png?width=1920&amp;fit=bounds&amp;dpr=3 3x" src="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-31780618026813.png?width=1920&amp;fit=bounds" alt=""/><figcaption id="n3t9beojtru-figure-caption"><div><div></div></div></figcaption></figure><div><hr/></div><h2 id="x-tomo-formal-de-clausura"><strong>X. Átomo formal de clausura</strong></h2><p id="nm5uw0ro7cr">&quot;Átomo&quot;, en esta generalización, designa unidad formal indivisa de clausura respecto de una lectura superior (desde un observador que mira externamente a él). El átomo químico funciona como caso físico externo donde una unidad material posee centro, dominio, frontera, perfil radial, traza y retorno. Hidrógeno y helio sirven como retornos de perfil radial y clausura de dominio atómico; no como fundamento. La igualdad rectora no es &quot;universo = átomo químico&quot;, sino patrón de clausura: <code>Patron_atomico^SV(x,Ω)=1 ⇔ Dom(Ω) ∧ Ctr_Ω(x) ∧ Fron_Ω(x) ∧ I_Ω(x)&gt;0 ∧ 𝓟_min^Ω(x)&gt;0 ∧ Ret_Ω(x) ∧ Tr_Ω(x) ∧ Res_Ω(x).</code> Si una instancia clausurada conserva traza y retorno, opera como unidad formal de una lectura superior. Esa unidad no se divide desde el dominio superior sin perder la clausura que la hace comparecer. Por eso se define: <code>Atomo_formal^SV(o,Ω→Ω′)=1 ⇔ Obs_real(o,Ω)=1 ∧ Cl_Ω(o)=1 ∧ Tr_Ω(o) ∧ Res_Ω(o) ∧ Ret_{Ω→Ω′}(o) ∧ Dom(Ω′) ∧ UnidadCl_Ω′(o)=1.</code> La reducción al absurdo del átomo formal es directa. Supóngase un observable realizado <code>o</code> que se clausura bajo <code>Ω</code>, conserva traza y retorno, pero no opera como unidad formal de ningún dominio superior. Entonces su traza no retorna a lectura ulterior; si no retorna, no hay reactivación espiral; si no hay reactivación espiral, <em>append-only</em> pierde función estructural; si <em>append-only</em> pierde función, la clausura borra la inscripción que debía conservar. Contradicción. Por tanto, toda clausura realizada con traza y retorno opera como átomo formal de una lectura superior.</p><div><hr/></div><figure id="nyne03pih4g" data-node-type="image" data-size="50" data-align="full" data-url="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-41780618205293.png" data-caption="" data-href="" data-alt-text="" data-hide-label="false"><img srcSet="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-41780618205293.png?width=800&amp;fit=bounds 1x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-41780618205293.png?width=800&amp;fit=bounds&amp;dpr=2 2x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-41780618205293.png?width=800&amp;fit=bounds&amp;dpr=3 3x" src="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-41780618205293.png?width=800&amp;fit=bounds" alt=""/><figcaption id="nyne03pih4g-figure-caption"><div><div></div></div></figcaption></figure><div><hr/></div><h2 id="xi-dominio-universo-como-tomo-formal-ante-lectura-externa"><strong>XI. Dominio-universo como átomo formal ante lectura externa</strong></h2><blockquote id="n6vpjctl7mz"><p id="nn6d6cny3zq">El dominio-universo físico realizado comparece ante una lectura externa superior <strong>como átomo</strong> formal de clausura. </p></blockquote><p id="n4m4r3l3e02">Esto no significa que tenga número atómico, orbital químico, núcleo material equivalente o electrón externo. Significa que comparece como unidad de dominio clausurada respecto de una lectura que no pertenece a su interior. Desde dentro, <code>Ω_U</code> se lee como dominio físico realizado con frontera sutural, traza, residual y retorno. Desde una lectura superior <code>Ω_{U+1}</code>, <code>Ω_U</code> opera como unidad formal indivisa de clausura: <code>Atomo_formal^SV(o_U,Ω_U→Ω_{U+1})=1 ⇔ Obs_real(o_U,Ω_U)=1 ∧ Cl_ΩU(o_U)=1 ∧ Tr_ΩU(o_U) ∧ Res_ΩU(o_U) ∧ Ret_{Ω_U→Ω_{U+1}}(o_U) ∧ Dom(Ω_{U+1}) ∧ UnidadCl_{Ω_{U+1}}(o_U)=1.</code> El observador externo, si comparece como instancia de lectura superior, no ve el dominio-universo como suma interna de todos sus sucesos, sino como unidad de clausura. Esta es la relación con el átomo material: un observador externo al dominio atómico no agota la estructura interna por una imagen radial; lee un régimen clausurado con perfil, frontera, centro y retorno. Del mismo modo, la lectura externa superior del dominio-universo no agota la totalidad interna de sus sucesos; lo toma como unidad formal de clausura.</p><h2 id="xii-ascendencia-no-agotada-de-dominios-y-no-identificacin-con-todonada"><strong>XII. Ascendencia no agotada de dominios y no identificación con TODO/NADA</strong></h2><p id="n97vl2r0mdk">La ascendencia no agotada se deduce de la misma estructura. Sea una serie de dominios <code>Ω_0→Ω_1→Ω_2→...</code>, donde cada clausura admitida en <code>Ω_i</code> conserva traza, residual y retorno. La afirmación no introduce una enumeración empírica de universos observados; trabaja sobre la imposibilidad de que un observable físico realizado ocupe el lugar de TODO/NADA. Si una clausura realizada conserva inscripción y retorno, no se borra al cerrarse; permanece disponible para lectura ulterior. Si se postula un último dominio físico <code>Ω_N</code> que clausura toda ascendencia, entonces <code>Ω_N</code> ocuparía el lugar de Totalidad o de TODO/NADA. Pero el SV distingue dominio físico, dominio-universo y plano de fundamentos; ningún observable realizado ocupa la Totalidad ni clausura TODO/NADA por escala. Por tanto, la ascendencia no se agota en un último observable físico, que en su formulación algebraica lógica la podemos definir como. </p><p id="nmbahz1yd5s"><code>Clausura_realizada^SV(Ω_i)=1 ⇔ Obs_real(Ω_i)=1 ∧ Cl(Ω_i)=1 ∧ Tr(Ω_i) ∧ Res(Ω_i) ∧ Ret(Ω_i) ∧ AppendOnly_SV</code>; <code>Clausura_realizada^SV(Ω_i)=1 ⇒ Lectura_ulterior_admisible^SV(Ω_i)=1</code>; <code>Lectura_ulterior_admisible^SV(Ω_i)=1 ∧ ¬(Ω_i=TODO/NADA) ⇒ Ascendencia_no_agotada^SV(Ω_i)=1</code>; <code>Ascendencia_no_agotada^SV(Ω_i)=1 ⇒ ∃Ω_{i+1} [Dom(Ω_{i+1}) ∧ Ret_{Ω_i→Ω_{i+1}}(Ω_i) ∧ Atomo_formal^SV(Ω_i,Ω_i→Ω_{i+1})=1]</code>; <code>¬∃Ω_N físico : Ω_N=TODO/NADA</code>; <code>Asc_SV=(Ω_0,Ω_1,Ω_2,...).</code> </p><p id="nup5ag0mtxi">En esta cadena, <code>Clausura_realizada^SV</code> nombra una clausura que no destruye inscripción; <code>Lectura_ulterior_admisible^SV</code> nombra la disponibilidad de esa clausura para un dominio de lectura posterior; <code>Ascendencia_no_agotada^SV</code> expresa que la cadena no se clausura en un observable físico final. La Línea del Umbral SV conserva su función rectora en toda la cadena: sobre ella se neutraliza el predominio; fuera de ella aparece orientación; con centro y brazo comparece momento; con traza, residual y retorno aparece giro; con <em>append-only</em> el giro conserva inscripción y habilita reactivación espiral; con clausura, la instancia comparece como átomo formal de ascendencia ulterior.</p><h2 id="xiii-dipolo-electromagntico-inversin-geomagntica-y-adopcin-lateral"><strong>XIII. Dipolo electromagnético, inversión geomagnética y adopción lateral</strong></h2><p id="ntui2g5i5ai">El régimen electromagnético aporta una vía lateral ya tipada. En el caso magnético, el dipolo no debe entenderse como pareja de monopolos sustanciales separables.</p><div><hr/></div><figure id="nckahqkjzw9" data-node-type="image" data-size="50" data-align="full" data-url="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-31780619403524.png" data-caption="" data-href="" data-alt-text="" data-hide-label="false"><img srcSet="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-31780619403524.png?width=800&amp;fit=bounds 1x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-31780619403524.png?width=800&amp;fit=bounds&amp;dpr=2 2x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-31780619403524.png?width=800&amp;fit=bounds&amp;dpr=3 3x" src="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-31780619403524.png?width=800&amp;fit=bounds" alt=""/><figcaption id="nckahqkjzw9-figure-caption"><div><div></div></div></figcaption></figure><div><hr/></div><p id="nvl02qqayuu"> <a href="https://doi.org/10.17613/kep1t-57539">La ecuación Maxwell factual</a> conserva <code>Div_SV(B)=0</code>, de modo que la polaridad magnética se formula como orientación no separable de campo que retorna por circulación, corriente, variación factual, constitución magnética y frontera (Lloret Egea, 2026a). La lectura sectorial es: <code>Π_pol,EM(q)=(α_EM(q),β_EM(q))</code>; <code>P_EM(q)=α_EM(q)−β_EM(q)</code>; <code>I_EM(q)=α_EM(q)+β_EM(q)</code>; <code>𝓛_Umbral,EM^SV={q∈Ω_EM : P_EM(q)=0}.</code> El giro de campo aparece cuando la orientación polar entra en régimen de rotor y circulación: <code>Rot_SV(E)+∂_ν^SV B=0</code>; <code>Rot_SV(H)−∂_ν^SV D=J.</code> La inversión geomagnética ofrece un caso lateral de orientación mutable bajo campo y frontera. La ciencia contemporánea conserva el dato de que el campo magnético terrestre invierte su polaridad y de que lavas o sedimentos registran firmas de campos antiguos (U.S. Geological Survey, 2024). En el SV, la inversión se formula como tránsito de orientación sectorial de un campo sin monopolo, regido por rotor, corriente, constitución, frontera, traza, residual y retorno, que en su formulación lógica formal es: </p><p id="n8jnlf43qpp"><code>Inv_geoEM^SV(q)=1 ⇔ Ω_geoEM declarado ∧ Div_SV(B)=0 ∧ Rot_SV(E)+∂_ν^SV B=0 ∧ Rot_SV(H)−∂_ν^SV D=J_geo ∧ B=μ_SV(H) ∧ 𝓛_Umbral,geoEM^SV declarada ∧ transición de P_geoEM entre orientaciones opuestas ∧ I_geoEM redistribuida ∧ Fron_geoEM ∧ Tr_geoEM ∧ Res_geoEM ∧ Ret_geoEM.</code> </p><p id="nrr7wv56hva">Este caso no prueba por sí solo la circulación de retorno del dominio-universo; muestra que una instancia de campo cambia orientación sin perder dominio, traza ni retorno. Como vía lateral, adopta el enfoque con error de plano cero si declara dominio, frontera, centro de lectura, potencial, intensidad, residual, retorno y transducción, sin identificarse materialmente con el dominio-universo. </p><p id="nj986933aid">La regla general de adopción lateral es: <code>Adopcion_lateral^SV(R,Ω_R)=0 ⇔ Dom(Ω_R) ∧ Ctr_R ∧ Fron_R ∧ I_R&gt;0 ∧ P_R declarado ∧ 𝓟_min^R&gt;0 ∧ Tr_R ∧ Res_R ∧ Ret_R ∧ Trans_R→SV declarada ∧ NoIdentMat=1 ∧ NoSaltoPlano=1</code>; <code>Err_lateral^SV(R)=1 ⇔ Dom(Ω_R) omitido ∨ Fron_R ausente ∨ Res_R oculto ∨ Ret_R no declarado ∨ Trans_R→SV omitida ∨ identidad material forzada ∨ referencia_externa tratada como fuente interna.</code> </p><p id="nhocjbp6ruf">Cualquier vía lateral declarada adopta el enfoque si satisface esta regla. El enfoque no se limita a dipolos, geodinamo, hidrógeno, helio, CPS-SV o dominio-universo; esas vías son retornos ya trabajados de una estructura general.</p><h2 id="xiv-frmula-rectora-de-identificacin-de-pasos-anteriores-y-posteriores-a-lo-observado"><strong>XIV. Fórmula rectora de identificación de pasos anteriores y posteriores a lo observado</strong></h2><p id="nzf6j3zoxow">La cadena SV identifica pasos anteriores o posteriores a lo observado cuando el régimen cumple la fórmula rectora de persistencia, dominio, traza y retorno. El paso no exige empiria (experimental) previa; exige dominio, frontera, residual y conclusión formal. </p><blockquote id="nu0cd56soon"><p id="nnadaywrvfa"><strong>Esta es la lección conjunta de la génesis del hidrógeno y el CPS-SV</strong>: el hidrógeno ancla el primer caso conocido; el CPS-SV demuestra que el Sistema Vectorial (SV) extiende dominio a candidatos no empíricos, los recorre y los concluye formalmente sin borrar la diferencia entre candidato estructural y elemento descubierto. </p></blockquote><p id="ntyjxo6cyuj">La fórmula en álgebra general es: </p><p id="n96d85fong5"><code>Paso_SV(R_i→R_{i+1})=0 ⇔ Dom(R_i) ∧ Dom(R_{i+1}) ∧ 𝓟_min^{R_i}&gt;0 ∧ Cl(R_i) ∧ Tr(R_i) ∧ Res(R_i) ∧ Ret_{i→i+1}(R_i) ∧ UnidadCl_{R_{i+1}}(R_i)=1 ∧ D_{R_{i+1}} definido ∧ 𝓔★(Γ_U;τ)=0</code>. Si el paso pertenece a régimen anterior a lo observado: <code>PrePaso_SV(R_{i−1}→R_i)=0 ⇔ Ω_pre declarado ∧ persistencia parcial ∧ frontera en estabilización ∧ residual visible ∧ transición de identidad ∧ 𝓟_min^{R_i}&gt;0.</code> Si pertenece a régimen posterior a lo observado: <code>PostPaso_SV(R_i→R_{i+1})=0 ⇔ Cl(R_i) ∧ traza conservada ∧ retorno ulterior ∧ lectura superior declarada ∧ no identificación con TODO/NADA</code>. </p><p id="n7vlareqofy">Así se evita la improvisación de gradientes. No inventamos un trayecto; se sigue una cadena ya demostrada: polos, umbral, ruptura, persistencia, átomo, extensión, par, campo, observable, dominio-universo y átomo formal superior.</p><h2 id="xv-teorema-conjunto-circulacin-de-retorno-tomo-formal-y-ascendencia-no-agotada"><strong>XV. Teorema conjunto: circulación de retorno, átomo formal y ascendencia no agotada</strong></h2><p id="n9iws4x3lol"><strong>Teorema.</strong> Sea <code>Ω</code> un dominio admitido por el SV, y sea <code>o</code> una instancia realizada en <code>Ω</code>. Si <code>o</code> conserva retorno bajo frontera, traza, residual y <em>append-only</em>, entonces el retorno opera como régimen clausural y presenta circulación de retorno. Si, además, <code>o</code> conserva intensidad positiva, potencial no nulo, centro de lectura y brazo, entonces adquiere momento. Si el momento conserva traza, residual y retorno bajo <em>append-only</em>, entonces <code>o</code> presenta giro. Si <code>o</code> se clausura y conserva retorno hacia una lectura superior, entonces opera como átomo formal de esa lectura. Ningún dominio físico realizado clausura la ascendencia porque ningún observable físico se identifica con TODO/NADA. </p><p id="nxlsttzg446"><strong>Demostración.</strong> Por definición de observable realizado, <code>o</code> exige dominio, frontera, traza, residual y retorno. Sin embargo, la conclusión no descansa sólo en esa definición. Descansa en el lema de retorno clausural: <code>Ret_Ω(o) ∧ Fron_Ω(o) ∧ Tr_Ω(o) ∧ Res_Ω(o) ∧ AppendOnly_SV ⇒ CircRet_Ω(o)=1</code>. Negar la circulación de retorno bajo esas condiciones equivale a aceptar retorno con frontera, traza y residual, pero negar que ese retorno opere como régimen de lectura conservada. Si el retorno no opera como régimen, la clausura local no devuelve lectura; si la clausura local no devuelve lectura, la instancia deja de cumplir la regla de observable realizado. Luego <code>CircRet_Ω(o)=1</code>. Si <code>P_Ω(o)≠0</code>, hay orientación polar; si <code>I_Ω(o)&gt;0</code>, hay presencia polar total; si <code>Ctr_Ω(o)</code> y <code>Brazo_Ω(o)</code> sitúan la orientación, negar el momento equivaldría a aceptar orientación situada sin efecto de orientación situada. Luego <code>Mom_SV(o,Ω)=1</code>. Si el momento conserva traza, residual y retorno bajo <em>append-only</em>, no regresa como repetición idéntica sin borrar inscripción; comparece como giro de retorno. Luego <code>Giro_SV(o,Ω)=1</code>. Si, además, <code>Cl_Ω(o)=1</code> y <code>Ret_{Ω→Ω′}(o)</code> se declara para un dominio superior <code>Ω′</code>, negar que <code>o</code> opere como unidad formal de <code>Ω′</code> anularía la función de traza y reactivación espiral. Luego <code>Atomo_formal^SV(o,Ω→Ω′)=1</code>. Finalmente, una clausura realizada con traza, residual, retorno y <em>append-only</em> conserva lectura ulterior admisible; si se postula un último dominio físico que clausura toda ascendencia, ese dominio ocuparía el lugar de TODO/NADA; pero ningún observable físico realizado se identifica con TODO/NADA. Por tanto, la ascendencia no se agota en un dominio físico final. (C.Q.D.) </p><blockquote id="nf3ri1aw86m"><p id="ncxyf8k23q4"><strong>Aplicado al dominio-universo en formulación lógica formal</strong>: <code>Teo_ΩU^SV=0 ⇔ Obs_real(o_U,Ω_U)=1 ∧ Fron_sut(Ω_U) ∧ 𝓟_min^{Ω_U}&gt;0 ∧ I_ΩU(o_U)&gt;0 ∧ Ret_ΩU(o_U) ∧ Tr_ΩU(o_U) ∧ Res_ΩU(o_U) ∧ AppendOnly_SV ∧ CircRet_ΩU(o_U)=1 ∧ Ctr_ΩU(o_U) ∧ Brazo_ΩU(o_U) ∧ Giro_SV(o_U,Ω_U)=1 ∧ Atomo_formal^SV(o_U,Ω_U→Ω_{U+1})=1 ∧ Ascendencia_no_agotada^SV(Ω_U)=1 ∧ ¬(Ω_U=TODO/NADA)</code>.</p></blockquote><h2 id="xvi-corolarios"><strong>XVI. Corolarios</strong></h2><p id="n9acxie06nn"><strong>Corolario 1 --- Circulación de retorno del dominio-universo.</strong> El dominio-universo físico realizado presenta circulación de retorno bajo frontera sutural, potencial, intensidad, centro de lectura, brazo, traza, residual y <em>append-only</em>; cuando esa circulación conserva centro, brazo y momento interno de retorno, el régimen se identifica como giro. La rotación rígida, la vorticidad métrica, la anisotropía global o el momento angular cosmológico pertenecen al régimen físico externo y sólo entran mediante transducción declarada.</p><p id="ndjypq7j89c"><strong>Corolario 2 --- Patrón atómico-sutural.</strong> El patrón común entre átomo material y dominio-universo no es identidad de sustancia, escala ni composición, sino igualdad tipada de clausura: centro de lectura, frontera, intensidad, persistencia, traza, residual y retorno. Hidrógeno y helio son referencias externas de perfil radial y clausura atómica; el dominio-universo es unidad de clausura para una lectura superior.</p><p id="na5dphaq0kd"><strong>Corolario 3 --- Cadena de persistencia desde polos hasta dominios superiores.</strong> La cadena comienza en la neutralización polar de la Línea del Umbral SV, se separa por ruptura polar, adquiere orientación, momento y giro bajo retorno, desciende al régimen preatómico e hidrógeno como primer caso conocido de persistencia atómica, se extiende por Ω₄₄₃ y CPS-SV, y asciende hacia dominios superiores por átomo formal de clausura.</p><p id="ni9oe3w2yf2"><strong>Corolario 4 --- Vías laterales con error de plano cero.</strong> Cualquier vía lateral declarada ---atómica, química estructural, electromagnética, geomagnética, estelar, galáctica, biológico-formal o cosmológica--- adopta el enfoque si declara dominio, frontera, centro, potencial, intensidad, persistencia, traza, residual, retorno y transducción. El error de plano es cero sólo si no se identifica materialmente un régimen con otro y si la referencia externa no ocupa el lugar de fundamento interno.</p><p id="nh9vkvqtwu0"><strong>Corolario 5 --- Candidatos no empíricos y rigor de dominio.</strong> <a href="https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/quimica-factual-y-ciencia-de-materiales-sv/elementos-materiales-nueva-generacion/imagenes/tabla_sv_A3_horizontal_vectorial.pdf" target="_blank">Los 325 candidatos</a> estructurales del dominio extendido <code>Ω_ext={119,…,443}</code> no son elementos empíricamente descubiertos. Son candidatos estructurales SV. Su valor para este trabajo reside en mostrar que ya se dispone de un método para extender dominio, recorrerlo y concluirlo formalmente sin confundir construcción matemática con descubrimiento experimental.</p><h2 id="xvii-criterios-de-refutacin-conservacin-de-u-y-error-de-plano"><strong>XVII. Criterios de refutación, conservación de U y error de plano</strong></h2><p id="nsj7m7wtxty">La tesis se refuta dentro del SV si se demuestra un observable realizado con frontera, traza, residual, retorno y <em>append-only</em>, pero sin circulación de retorno admisible. Se refuta la lectura de giro si se demuestra orientación situada, centro de lectura, brazo, traza y retorno sin momento formal. Se refuta la lectura de átomo formal si se demuestra una clausura con traza y retorno que no opera en ninguna lectura superior sin contradicción. Se refuta la ascendencia no agotada si se demuestra un dominio físico realizado que ocupa el lugar de TODO/NADA sin dejar de ser observable físico, lo que contradice la separación de planos del SV. También se refuta cualquier formulación que trate como perfecto un tránsito con residual no declarado o no gobernado. La salida <code>U</code> no se usa como refugio favorable. Sólo procede cuando falta dominio, referencia de contraste, transducción, magnitud, residual o retorno. En esos casos, <code>U</code> conserva indeterminación honesta; no confirma la tesis ni la niega. </p><p id="n88i71xdgac">La regla lógica es: <code>U_Tesis^SV ⇔ falta dominio, frontera, residual, transducción o retorno suficiente sin contradicción</code>; <code>Err_Tesis^SV=1 ⇔ referencia_externa=fundamento_SV ∨ átomo=elemento_químico_literal ∨ giro=rotación_rígida_obligatoria ∨ Ω_U=TODO/NADA ∨ Res omitido ∨ Gov(Res) no acreditado ∨ U usada como confirmación</code></p><h2 id="conclusin"><strong>Conclusión</strong></h2><p id="ny3gkgammmw">La Línea del Umbral SV fija la neutralización polar y la ruptura; la persistencia energética estructural aporta la fórmula <code>𝓟_min=𝓕_∂−𝒬−ℛ_Γ</code>; la génesis del hidrógeno muestra el primer caso conocido de persistencia atómica discreta; el CPS-SV demuestra extensión de dominio hasta 443 candidatos estructurales y 97.903 pares evaluados formalmente; Maxwell factual y la inversión geomagnética aportan regímenes laterales de orientación, campo, frontera, traza y retorno; y la teoría de vida y clausura de observables permite llevar la regla a cuerpos, especies, estrellas, galaxias y dominio-universo. La cosmología contemporánea conserva el régimen físico externo de rotación, vorticidad, anisotropía y momento angular cosmológico; el SV conserva el régimen formal de dominio, frontera, traza, residual, retorno y conclusión formal. Este trabajo no mezcla ambos planos. En el plano SV, el dominio-universo físico realizado presenta circulación de retorno de dominio; cuando esa circulación conserva potencial, intensidad, centro de lectura, brazo, traza, residual y <em>append-only,</em> el régimen se identifica como giro. La transducción hacia magnitudes cosmológicas externas exige dominio, magnitud, residual y retorno, pero no altera el teorema interno. Lo observado no clausura la cadena: la cadena se reconoce por dominio, frontera, persistencia, traza, residual, retorno y conclusión formal.</p><h2 id="conclusin-final-del-autor"><strong>Conclusión final del autor</strong></h2><p id="nb0z7mcas4w"><strong>La conclusión final que el autor somete a reflexión no es una invitación a la simpleza</strong>, sino a la reducción rigurosa de lo complejo hasta una forma trivial suficientemente analizada, en continuidad metodológica con la descomposición analítica cartesiana (<strong>René Descartes</strong>) y con la disciplina de observación formulada por <strong>don Santiago Ramón y Cajal</strong>. En matemáticas, física e <strong>ingeniería</strong>, lo trivial no es lo pobre: es <strong>aquello qu</strong>e, <strong>después de una depuración analítica extrema</strong>, deja de esconder el problema bajo exceso de aparato y permite reconocer su estructura necesaria. La terna (<code>0,1,U</code>) expresa esa disciplina en el Sistema Vectorial: conclusión, presencia e indeterminación honesta no son licencias algebraicas, <strong>sino una forma de impedir que el lenguaje suplante al resultado</strong>. La historia de la ciencia recuerda que muchas verdades hoy elementales exigieron cálculo, geometría, conflicto conceptual y valentía - audacia formal antes de adquirir evidencia inmediata para todos: la esfericidad terrestre fue pensada y medida por la astronomía antigua mucho antes de la observación espacial (American Physical Society, 2006); el heliocentrismo reorganizó el lugar de la Tierra frente al Sol en una época de resistencia doctrinal y de transformación del aparato astronómico (Miller, 2005; Rabin, 2004); y la gravitación newtoniana mostró que una formulación matemática </p><blockquote id="nfz0twobb22"><p id="nn17pl2grap"><strong>nacida en mesa, papel y pluma</strong> </p></blockquote><p id="nt5npjgqriu">podía gobernar después trayectorias, órbitas y navegación espacial (NASA Science, 2024, 2025). Nada de ello se invoca aquí como fuente de verdad, ni como licencia histórica para declarar demostrado lo no demostrado. Se invoca como advertencia metodológica: </p><blockquote id="n8oejhippqv"><p id="nhyyc8pj9rz"><strong>No siempre se sale primero fuera del dominio para comprenderlo</strong>; </p></blockquote><p id="n3hfuvgdllr">a veces se declara el dominio, se fija la frontera, se calcula el residual, se exige retorno y sólo entonces la realidad devuelve su contraste. <strong>Este trabajo se sitúa en esa disciplina: no afirma por imagen, metáfora ni deseo que el dominio-universo sea un cuerpo visto desde fuera</strong>; formula, calcula y somete a conclusión formal que, en el plano SV, el dominio-universo físico realizado presenta circulación de retorno, y que cuando esa circulación conserva potencial, intensidad, centro de lectura, brazo, traza, residual y <em>append-only</em>, <strong>el régimen se identifica como giro</strong>. </p><p id="nqzpogoshfy">La ciencia contemporánea conserva su régimen físico externo de observación, magnitud y medida; el Sistema Vectorial (SV) conserva su régimen de dominio, frontera, transducción, residual y conclusión formal. <strong>La trivialización rigurosa no disminuye la ciencia: la obliga a mostrar, con la menor forma suficiente, qué estructura permanece cuando se han retirado la retórica, la costumbre y el exceso de explicación</strong>.</p><div><hr/></div><h2 id="anexo-a-trivializacin-todonada-e-imperfeccin-la-terna-1-0-u-la-u-honesta-y-el-corolario-de-transduccin-no-confinante"><strong>Anexo A. Trivialización, TODO/NADA e Imperfección: la terna (1-0-U), la U honesta y el corolario de transducción no confinante</strong></h2><div><hr/></div><figure id="npezhfwmtpt" data-node-type="image" data-size="70" data-align="center" data-url="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-21780607839377.png" data-caption="&lt;p id=&quot;nrqff08pysq&quot; data-reactroot=&quot;&quot;&gt;La imagen representa la instancia observable situada en dominio declarado, con frontera, identidad, soporte, traza, residual y retorno; circularidad de retorno, reactivación espiral y medición transducida convergen hacia la frontera sutural del dominio-universo, sin identificarla con TODO/NADA, Totalidad absoluta, materia oscura sustancial ni límite del espacio. &lt;strong&gt;(Es una representación contextual de la forma del Universo físico, desde el plano matemático del SV)&lt;/strong&gt;&lt;/p&gt;" data-href="" data-alt-text="" data-hide-label="false"><img srcSet="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-21780607839377.png?width=800&amp;fit=bounds 1x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-21780607839377.png?width=800&amp;fit=bounds&amp;dpr=2 2x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-21780607839377.png?width=800&amp;fit=bounds&amp;dpr=3 3x" src="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-21780607839377.png?width=800&amp;fit=bounds" alt="" aria-labelledby="npezhfwmtpt-figure-caption"/><figcaption id="npezhfwmtpt-figure-caption"><div><div><p id="nrqff08pysq" data-reactroot="">La imagen representa la instancia observable situada en dominio declarado, con frontera, identidad, soporte, traza, residual y retorno; circularidad de retorno, reactivación espiral y medición transducida convergen hacia la frontera sutural del dominio-universo, sin identificarla con TODO/NADA, Totalidad absoluta, materia oscura sustancial ni límite del espacio. <strong>(Es una representación contextual de la forma del Universo físico, desde el plano matemático del SV)</strong></p></div></div></figcaption></figure><div><hr/></div><blockquote id="n0drtqgyuz1"><p id="nqq9tbx4xhm"><strong>Nota</strong>: el anexo se realiza con la intención de que sea autónomo <em>per se</em>, por lo  tanto debe ser autocontenido. De ahí que conceptos y definiciones se reescriban o repitan de nuevo.</p><div><hr/></div></blockquote><h3 id="a0-alcance-continuidad-con-la-investigacin-desarrollada-y-paso-a-la-trivializacin"><strong>A.0. Alcance: continuidad con la investigación desarrollada y paso a la trivialización </strong></h3><blockquote id="nggnry02kyh"><p id="n9zxv9es2re"><strong>Y  continuación natural también de </strong><em><a href="https://doi.org/10.21428/39829d0b.9c15d6fe">Vida y clausura de los observables realizados: cuerpos, especies, estrellas y frontera sutural del universo observable como dominio físico realizado</a></em></p></blockquote><p id="nmaazr649c1">La trivialización la usaremos para explicitar un fundamento que ya actúa en su demostración: la trivialización rigurosa como reducción de cualquier régimen a dominio, frontera, identidad, potencial, intensidad, traza, residual, retorno, conclusión formal y conservación <em>append-only</em>. Hasta ahora sosteníamos que el dominio-<strong>universo físico realizado presenta circulación</strong> de retorno bajo dominio, frontera, potencial, intensidad, centro de lectura, brazo, traza, residual y conservación <em>append-only</em>; cuando esa circulación conserva centro, brazo y momento interno de retorno, el régimen se identifica como giro. También establecíamos que, ante una lectura externa superior, e<strong>l dominio-universo comparece como átomo formal de clausura</strong>, no como átomo químico, esfera física, globo cosmológico ni rotación rígida externa. </p><p id="no57eyew2xu">La trivialización no sustituye esa tesis; la concentra en una regla más elemental y más exigente: ninguna pregunta queda resuelta por imagen, autoridad, hábito semántico o medición aislada si no declara el dominio donde pregunta, la frontera que separa, la traza que conserva, el residual que devuelve y el retorno que permite conclusión formal. La relación con <em><a href="https://doi.org/10.21428/39829d0b.9c57c046">Imperfección preformal y espacio: ε−0, primera distinguibilidad y dominio estructural completo de separación factual recorrible</a></em> fija la base de separación. <code>ε−0</code> nombra el borde preformal de primera distinguibilidad y se distingue de <code>ε0</code>, que pertenece a otro plano, ─(obsérvese la diferencia de notación<strong>,</strong> porque es propicia a la confusión: <strong>ε−0</strong> , <strong>ε0</strong>)─,  el de la activación o suceso cero en régimen ya formulado. La secuencia <code>ε−0 ⊢ ∂ε ⊢ D_sep ⊢ Ω_esp ⊢ Ω_fis</code> impide comenzar por física constituida, magnitud externa o medición empírica como fundamento absoluto. La lectura aquí desarrollada opera después de esa distinción: no ocupa el lugar de <code>ε−0</code>, no convierte <code>U</code> en causa, no convierte la empiria en totalidad rectora y no concede al SV una excepción verbal. Formula cómo una cuestión ya situada puede retornar como <code>0</code>, como <code>1</code> o como <code>U</code>. La lectura autónoma exige fijar desde el comienzo las convenciones mínimas: <code>0</code> no equivale por sí solo a <code>NADA_SV</code>; <code>1</code> no nombra sustancia ni realización universal; y <code>U</code> designa indeterminación honesta cuando la información, la frontera, el residual o el retorno todavía no autorizan un resultado binario. Esta lectura nos remite al fundamento algebraico-semántico de la terna, donde <code>U</code> queda definido como estado de no determinación actual y no como número, infinito, probabilidad o licencia decisoria. (<strong>Véase</strong>: <em><a href="https://doi.org/10.21428/39829d0b.b0cf9a13">Fundamentos algebraico-semánticos del Sistema Vectorial SV</a></em><em>)</em>. La trivialización rigurosa se expresa por una condición general. Sea <code>Q</code> una cuestión sometida a análisis. </p><p id="n1cgpgjdgps">Entonces su formulación lógica formal: <code>Triv_SV(Q)=0 ⇔ Dom(Q) ∧ Fron(Q) ∧ Id(Q) ∧ P(Q) declarado ∧ I(Q) declarado ∧ Tr(Q) ∧ Res(Q) visible ∧ Ret(Q) ∧ d_Q∈{0,1,U} ∧ U no usada como confirmación</code>. </p><p id="nk8axoq9wbg">En esta fórmula, <code>Dom(Q)</code> declara el dominio de lectura; <code>Fron(Q)</code> fija la frontera de régimen; <code>Id(Q)</code> conserva identidad tipada; <code>P(Q)</code> nombra potencial o diferencia orientada cuando procede; <code>I(Q)</code> nombra intensidad o presencia total de régimen; <code>Tr(Q)</code> conserva traza; <code>Res(Q)</code> conserva residual visible; <code>Ret(Q)</code> exige retorno; <code>d_Q</code> designa la conclusión ternaria; y <code>U</code> sólo puede comparecer como indeterminación honesta, no como confirmación, negación, refugio favorable ni sustituto del cálculo. El error correspondiente se declara de la siguiente manera: <code>Err_Triv_SV(Q)=1 ⇔ Dom(Q) omitido ∨ Fron(Q) ausente ∨ Id(Q) confundida ∨ Res(Q) oculto ∨ Ret(Q) no acreditado ∨ U usada como confirmación ∨ referencia_externa=fundamento_SV</code>. La investigación tuvo que proteger dos afirmaciones por riesgo de lectura externa. <strong>La primera es que giro </strong>no equivale a rotación rígida cosmológica, vorticidad métrica, anisotropía global o momento angular cosmológico salvo transducción declarada. <strong>La segunda es que clausura circular</strong> no equivale a esfera física, imagen geométrica ordinaria ni átomo químico literal. La trivialización no retira esa protección; la hace más precisa. Una vez declarado el dominio de los términos, e<strong>l SV no necesita pedir permiso semántico para decir giro</strong>. Lo experimental observa, mide, registra, contrasta y devuelve magnitudes dentro de su dominio; esa función es necesaria, <strong>pero no agota la verdad completa del régimen</strong>. </p><p id="n1wguhpsb54">La medición retorna; después, el dominio decide si ese retorno basta para conclusión formal, si exige residual adicional o si devuelve <code>U</code>. <a href="https://www.itvia.online/pub/linea-del-umbral-sv-circulacion-de-retorno-del-dominio-universo-y-atomo-formal-de-ascendencia-no-agotada#a12-corolario-de-transduccin-no-confinante-resolver-en-un-dominio-no-confina-el-resultado-al-mtodo">El corolario de transducción no confinante</a> gobierna esta lectura. <strong>En matemáticas, un cambio de variable permite resolver una derivada o una integral en otro parámetro y retornar al dominio original</strong>. Si <code>y=f(u)</code> y <code>u=g(x)</code>, l<strong>a regla de la cadena</strong> conserva el paso por el dominio intermedio mediante <code>dy/dx=(dy/du)(du/dx)</code>. Si una integral se transforma por sustitución, el resultado no queda prisionero de la variable auxiliar: se retorna al dominio inicial cuando se deshace la sustitución o se transforman adecuadamente los límites. <strong>En el SV ocurre lo mismo</strong>. </p><blockquote id="nxq3tt2kt0d"><p id="n0nd23djm9l">Si una pregunta de la ciencia contemporánea se transduce a dominio SV, se resuelve con dominio, frontera, traza, residual y retorno, y después retorna al dominio interrogado, no puede decirse  <strong>que sólo vale para el SV</strong>. </p></blockquote><p id="nec70q8rj8o">Esa objeción confunde método de resolución con confinamiento de verdad. El corolario puede escribirse, de manera compacta, de esta forma: </p><p id="n6hm557ndi7"><code>Problema(D_ext) --𝔛--&gt; Resolución(D_SV) --Ret,Res--&gt; Conclusión formal(D_ext)</code>; <code>Transd_no_conf^SV=0 ⇔ Dom(D_ext) ∧ Dom(D_SV) ∧ 𝔛(D_ext↔D_SV) declarado ∧ Res visible ∧ Ret(D_SV→D_ext) ∧ Conclusión formal(D_ext)</code>; <code>Err_conf^SV=1 ⇔ 𝔛 declarado ∧ Ret(D_SV→D_ext) ∧ Conclusión formal(D_ext) ∧ objeción=&quot;sólo vale en D_SV&quot;</code>. </p><p id="nrehz25826c">Por tanto, no se añade una tesis lateral. Acredita que la trivialización SV permite responder con disciplina a preguntas de máximo alcance: qué significa que un observable realizado tenga clausura circular, qué significa que presente giro, qué significa que la espiral conserve inscripción <em>append-only</em>, qué función tiene <code>U</code> entre <code>0</code> y <code>1</code>, y <strong>por qué una transducción rigurosa no degrada el resultado al dominio auxiliar que permitió resolverlo</strong>.</p><div><hr/></div><figure id="n3rwjrv5j66" data-node-type="image" data-size="70" data-align="center" data-url="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-21780608747341.png" data-caption="&lt;p id=&quot;nnj5poyxvgb&quot; data-reactroot=&quot;&quot;&gt;Pulse sobre la imagen para verla completa&lt;/p&gt;" data-href="https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/teoria-todo-nada-sv/imagenes/Teoria_del_Todo_y_de_la_Nada_V_1_0.png" data-alt-text="" data-hide-label="false"><a href="https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/teoria-todo-nada-sv/imagenes/Teoria_del_Todo_y_de_la_Nada_V_1_0.png" target="_blank"><img srcSet="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-21780608747341.png?width=800&amp;fit=bounds 1x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-21780608747341.png?width=800&amp;fit=bounds&amp;dpr=2 2x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-21780608747341.png?width=800&amp;fit=bounds&amp;dpr=3 3x" src="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-21780608747341.png?width=800&amp;fit=bounds" alt="" aria-labelledby="n3rwjrv5j66-figure-caption"/></a><figcaption id="n3rwjrv5j66-figure-caption"><div><div><p id="nnj5poyxvgb" data-reactroot="">Pulse sobre la imagen para verla completa</p></div></div></figcaption></figure><h3 id="a1-trivializacin-rigurosa-reduccin-suficiente-de-dominio-no-empobrecimiento-del-anlisis"><strong>A.1. Trivialización rigurosa: reducción suficiente de dominio, no empobrecimiento del análisis</strong></h3><p id="nsz6a0vm9df">La trivialización rigurosa no empobrece el análisis. <strong>Retira lo accesorio</strong> hasta dejar visible la estructura necesaria de la cuestión. Una pregunta queda correctamente trivializada cuando ya no depende de imagen, prestigio externo, analogía impropia ni acumulación verbal, sino de una tupla capaz de sostener conclusión formal: <code>𝒯_Q=(D_Q,∂D_Q,Id_Q,P_Q,I_Q,Tr_Q,Res_Q,Ret_Q,d_Q)</code>. Aquí <code>D_Q</code> es dominio; <code>∂D_Q</code>, frontera; <code>Id_Q</code>, identidad tipada; <code>P_Q</code>, potencial o diferencia orientada; <code>I_Q</code>, intensidad o carga de régimen; <code>Tr_Q</code>, traza; <code>Res_Q</code>, residual; <code>Ret_Q</code>, retorno; y <code>d_Q</code>, conclusión formal en la terna <code>{0,1,U}</code>. La reducción es suficiente si conserva esos componentes. Es defectuosa si elimina residual, oculta frontera, confunde identidad, sustituye retorno por plausibilidad o usa <code>U</code> para eludir resultado formal. Esta regla ordena las vías laterales sin permitir que ninguna dirija el aparato. </p><p id="ny7hw40d9lw">Como sabemos ─ uno de los ejemplos de lateralidad que usaremos ─, en la ley de Ohm, la física externa formula V=I·R y permite escribir I=V/R, donde tensión, corriente y resistencia se relacionan en el dominio eléctrico declarado. La lectura SV no convierte la electricidad en fundamento; conserva la forma de cociente: </p><blockquote id="njfkoypln1l"><p id="nc6pigphjho">Cuando una magnitud restrictiva situada como denominador <strong>tiende a </strong><strong><code>0</code></strong> mientras el régimen activo conserva numerador, otra magnitud tiende a no quedar acotada (<strong>infinita</strong>).  En otras palabras: si la resistencia tiende a cero, la intensidad se vuelve infinita: <strong>si R → 0, entonces I = V / 0 = ∞</strong> (<strong>Advertencia lateral</strong>).</p></blockquote><p id="nisdkovtgkt">La misma advertencia lateral nos aparece, con dominio propio, en la Ley de Gravitación Universal ─ F = G * (m1 * m2) / r²  ─cuando la separación (distancia `r´) se reduce frente a masas activas. También en el cero absoluto aparece cuando el límite térmico no puede tratarse como estado ordinario disponible: en la relación entre calor reversible y temperatura cuando el denominador térmico se aproxima al límite con transferencia no nula; y en la equivalencia masa-energía cuando se despeja una magnitud por el factor de transducción correspondiente. Ninguno de esos casos prueba por sí mismo una tesis SV. <strong>Todos convergen en una misma disciplina</strong>: <strong>el cero debe tiparse</strong>. </p><p id="n4zxv50th61">El cero no opera siempre como Nada. Puede nombrar origen, límite, neutralización, ausencia, clausura de tesis, denominador restrictivo, residual nulo o frontera de no retorno. Si se ignora su posición formal, se comete error de plano. La trivialización exige preguntar de qué cero se trata y qué régimen permanece activo. La expresión general la escribiremos: <code>Cero_tipo(x)=Origen ∨ Límite ∨ Neutralización ∨ Ausencia ∨ Clausura ∨ Restricción ∨ Residual_nulo ∨ Frontera</code>; <code>Err_0^SV=1 ⇔ 0 leído como NADA_SV sin Dom ∨ 0 leído como origen cuando I&gt;0 ∨ 0 leído como residual nulo con Res no declarado ∨ 0 leído como clausura con Ret ausente</code>. La Línea del Umbral SV aporta el segundo pilar. En la formulación previa, la recta <code>μ=λ</code> fija neutralización polar; sobre ella <code>P=μ−λ=0</code>, pero la intensidad <code>I=μ+λ</code> conserva valor positivo cuando <code>μ=λ=a</code> y <code>a&gt;0</code>. Por tanto, <code>(0,0)</code> no equivale, por ejemplo, a <code>(5,5)</code> ni a <code>(64,64)</code>: todos pueden compartir neutralización polar, <strong>pero sólo (0,0) carece de intensidad</strong>. La trivialización convierte esta distinción en regla general: no basta ver <code>P=0</code> para declarar origen. La forma elemental es: <code>P(a,a)=a−a=0</code>; <code>I(a,a)=a+a=2a</code>; <code>a&gt;0 ⇒ P=0 ∧ I&gt;0</code>. Esto impide confundir igualdad polar con nulidad absoluta. También impide confundir clausura circular con quietud, giro con rotación externa, espiral con ciclo temporal y <code>U</code> con ignorancia favorable. Si hay intensidad positiva, hay presencia de régimen. Si hay traza, residual y retorno, hay inscripción conservada. Si hay centro de lectura y brazo, la circulación de retorno puede adquirir giro. Si hay conservación <em>append-only</em>, el giro no repite el origen: retorna con inscripción. </p><p id="nqzcdckcdh9">Las vías laterales quedan subordinadas a esa regla.  El <strong>Agua</strong>, por ejemplo, no se agota en <code>H₂O</code> aislado; exige identidad bajo estado, frontera de transición y retorno. El <strong>Fuego</strong> no es sustancia autónoma; es tránsito con soporte, frontera, emisión, residuo y cese cuando el régimen pierde alimentación o continuidad.  Un <strong>Volcán</strong> no es lava como imagen, sino dominio geológico con presión, frontera, emisión, depósito, traza y retorno. Una <strong>Especie</strong> no es presencia biológica muda, sino dominio vivo con traza, variación, residual y no retorno bajo <em>append-only</em>.</p><p id="n9uzgrkjal3">La <strong>Gravitación</strong>, la ley de <strong>Ohm,</strong>  la <strong>Temperatura</strong> límite y clausura circular no se identifican materialmente entre sí; se ordenan por la misma restricción de análisis: dominio declarado, residual visible, retorno exigible y conclusión ternaria. </p><p id="nj63fjt8sdt">La regla general para cualquier lectura lateral es:</p><blockquote id="n29bwez3vsv"><p id="nrjt6q9j8an"> <code>Adopcion_lateral^SV(R)=0 ⇔ Dom(R) ∧ Fron(R) ∧ Id(R) ∧ I_R&gt;0 ∧ Tr_R ∧ Res_R ∧ Ret_R ∧ Trans_R↔SV declarada ∧ NoIdentMat=1 ∧ NoSaltoPlano=1</code>; <code>U_lateral^SV(R) ⇔ Dom(R), Fron(R), Res(R), Ret(R) o Trans_R↔SV insuficientes sin contradicción</code>; <code>Err_lateral^SV(R)=1 ⇔ identidad_material_forzada ∨ referencia_externa=fundamento_SV ∨ Res oculto ∨ Ret omitido ∨ U usada como resultado favorable</code>. </p></blockquote><p id="nkk7j2hzol4">La trivialización rigurosa permite así una afirmación más fuerte y más limpia: el SV no convierte los casos externos en pruebas por analogía; los somete a dominio. Si pasan, retornan como lectura lateral. Si no pasan, devuelven <code>U</code> o error. La audacia científica no consiste en afirmar más de lo que el aparato permite; consiste en no callar cuando el dominio, la frontera, la traza, el residual y el retorno ya permiten conclusión formal.</p><h3 id="a2-la-terna-1-0-u-presencia-nulidad-e-indeterminacin-honesta"><strong>A.2. La terna (1-0-U) : presencia, nulidad e indeterminación honesta</strong></h3><blockquote id="nyxn0svdr3n"><p id="ncztd9lo4d4"><strong>Nota: </strong>(1-0-U)<strong> </strong>lo escribimos en este orden por interés o convenio que facilita la interpretación, pero no modifica en nada a la forma natural (0,1,U): ambas son la misma.</p></blockquote><p id="nyaw7xns1ex">La terna <code>Σ_SV={0,1,U}</code> se introduce como reducción mínima del resultado formal. No añade un tercer valor por comodidad ni transforma la indeterminación en licencia. <strong><code>0</code></strong><strong> y </strong><strong><code>1</code></strong><strong> no bastan para describir un dominio realizado</strong> porque el tránsito entre nulidad y presencia conserva frontera, diferencia, traza, residual y retorno. </p><blockquote id="nckz2ddn7ux"><p id="nnjf9cy5a77"><code>0</code> puede nombrar origen sin intensidad, clausura sin error de una tesis, ausencia de una propiedad, neutralización polar o límite de régimen, según el dominio declarado. </p></blockquote><blockquote id="n08y2rdziza"><p id="nq4im3o0owp"><code>1</code> puede nombrar presencia, realización, admisión de una propiedad o comparecencia de dominio. </p></blockquote><blockquote id="nbgbwbeqobs"><p id="nx1ulgqrd7p"><code>U</code> nombra la indeterminación honesta cuando la estructura todavía no permite clausura: falta dominio, frontera, residual, transducción, magnitud o retorno suficiente sin contradicción. </p></blockquote><p id="nkynhzpqkut">Ésta investigación ya fijó de inicio <strong>la regla que la trivialización toma como núcleo</strong>: <code>U</code> no opera como refugio favorable. Sólo procede cuando falta dominio, referencia de contraste, transducción, magnitud, residual o retorno; en ese caso conserva indeterminación honesta, sin confirmar ni negar la tesis. </p><p id="n5hee3ty799">La formulación (o formalización algebraica) es: <code>d_SV(x)=0 ⇔ Criterio(x) clausurado sin error</code>; <code>d_SV(x)=1 ⇔ Propiedad(x) realizada con Dom, Fron, Tr, Res y Ret suficientes</code>; <code>d_SV(x)=U ⇔ falta Dom ∨ falta Fron ∨ falta Res ∨ falta Trans ∨ falta Magnitud ∨ falta Ret, sin contradicción</code>; <code>Err_U(x)=1 ⇔ U usada como confirmación ∨ U usada como negación ∨ U usada para ocultar Res ∨ U usada para evitar Ret</code>. </p><p id="nf3mkrkeo8k">Esta distinción impide dos errores. El primero consiste en forzar <code>1</code> cuando no hay dominio completo; el segundo, en usar <code>U</code> para no concluir formalmente cuando las condiciones ya concurren. <strong>La </strong><strong><code>U</code></strong><strong> honesta no debilita el SV</strong>: impide una clausura no acreditada en régimen SV. Suspende la clausura cuando falta estructura; exige conclusión formal cuando la estructura está declarada. La terna exige separar identidad primitiva e igualdad operativa. La forma primaria de la ley de Ohm, por ejemplo, se toma aquí como identidad estructural: V <strong>≡</strong> R·I. Bajo asignación SV: <code>R → U</code>; <code>I → 1</code>; <code>V → 0</code>, la identidad resultante es: <code>0 ≡ U·1</code>. Sólo en plano derivado, operativo o proyectivo se permite escribir: 0 <strong>=</strong> U·1. La triple línea importa (<strong>≡</strong> es diferente de <strong>=</strong>) porque la identidad primitiva no pretende resolver una ecuación eléctrica dentro del SV. Fija una forma de lectura. <strong>R</strong> se traslada a <strong>U</strong> porque resistencia nombra la condición que impide paso sin límite; <strong>I</strong> se traslada a <strong>1</strong> porque intensidad nombra régimen activo; <strong>V</strong> se traslada a <strong>0</strong> porque tensión queda leída como diferencia que, bajo neutralización, comparece como clausura de relación. Si se transforma esta identidad en igualdad ordinaria desde el comienzo, se degrada la terna. Si se conserva la identidad estructural, <code>U</code> queda situada como marca honesta de no clausura entre polo <code>0</code> y el polo <code>1</code>. La <code>U</code> tampoco ocupa el lugar de <code>ε−0</code>. En <em>Imperfección preformal y espacio: ε−0, primera distinguibilidad y dominio estructural completo de separación factual recorrible</em> la imperfección preformal se formula como mínima no clausura que permite primera distinguibilidad; la secuencia <code>𝓘_pre ⇒ ∂ε</code> no depende de probabilidad, azar, fluctuación empírica ni defecto material. <strong>La U actúa aquí en otro plano</strong>: el plano de conclusión formal dentro de un régimen interrogado. No causa el dominio, no lo empuja, no lo sustituye y no lo explica como motor. Conserva el no cierre cuando entre 0 y 1 quedan frontera, predominancia relativa, diferencia de potencia, diferencia de resistencia, diferencia de intensidad, residual o retorno no completado. En el plano de la Línea del Umbral, esta función se vuelve visible. Si <code>μ=λ</code>, entonces <code>P=μ−λ=0</code>; pero si <code>μ=λ=a</code> y <code>a&gt;0</code>, entonces <code>I=μ+λ=2a&gt;0</code>. La terna nos permite distinguir: <strong>0</strong> como neutralización polar, <strong>1</strong> como presencia de régimen, <strong>U</strong> como no cierre cuando la relación entre neutralización e intensidad no ha sido completamente situada. El salto, siguiendo el ejemplo de antes, <code>(5,5) → (64,64)</code> conserva <code>P=0 </code>(es decir si se restan da cero), pero no conserva intensidad. No hay abandono de la Línea del Umbral, pero sí variación de carga de dominio. La lectura binaria no basta; la <code>U</code> impide forzar indebidamente el tránsito. Por la misma razón <strong>la clausura circular</strong> del dominio-universo no se afirmará como esfera física; se concluirá formalmente como retorno de observable realizado si hay dominio, frontera, traza, residual y retorno. <strong>El giro</strong> no se reducirá a rotación externa; se concluirá formalmente como circulación de retorno con centro, brazo, intensidad y conservación <em>append-only</em>. <strong>La espiral</strong> no se convertirá en tiempo rector; se formulará como reactivación de inscripción no borrada. Cada régimen hablará desde su dominio; el SV concluirá formalmente sólo cuando el dominio, el residual y el retorno lo permitan.</p><blockquote id="nogab04929y"><p id="nbn6bm6evzw">La ciencia experimental no será negada <strong>ni absolutizada</strong>: quedará situada en su dominio exacto, como observación, medición, registro, contraste y retorno de magnitudes. </p></blockquote><h3 id="a3-la-u-honesta-custodia-del-no-cierre-no-es-motor-no-es-probabilidad-y-no-es-refugio-favorable"><strong>A.3. La U honesta: custodia del no cierre, no es motor, no es probabilidad y no es refugio favorable</strong></h3><p id="n1tmh712mqc">La <code>U</code> <strong>honesta</strong> es la salida ternaria que conserva visible la insuficiencia de clausura cuando <code>0</code> y <code>1</code> no bastan para concluir formalmente un régimen. No introduce una causa, no inicia el dominio, no empuja la transición, no sustituye a <code>ε−0</code>, no ocupa el lugar de <code>ε0</code>, no equivale a azar, no formaliza probabilidad y no permite convertir una falta de retorno en confirmación favorable. Su función es más rigurosa: impedir que el análisis declare <code>0</code> ó <code>1</code> cuando todavía falta dominio, frontera, magnitud, traza, residual, transducción o retorno. En esta función, <code>U</code> no debilita la afirmación científica; <strong>la depura</strong>. Allí donde la estructura no alcanza conclusión formal, suspende la clausura; allí donde la estructura ya ha declarado dominio y retorno, impide refugiarse en una indeterminación artificial. </p><p id="nn4svonup0w">La formulación lógica formal elemental es: <code>U_H^SV(x)=1 ⇔ Indet_honesta(x) ∧ Res(x) visible ∧ Ret(x) insuficiente o no clausurado ∧ ¬Confirmacion(x) ∧ ¬Negacion(x) ∧ ¬Probabilidad(x) ∧ ¬Motor(x)</code>. En esta expresión, <code>Indet_honesta(x)</code> no nombra ignorancia cómoda, sino insuficiencia formal concreta; <code>Res(x)</code> exige residual visible; <code>Ret(x)</code> exige retorno suficiente; y las negaciones finales impiden convertir <code>U</code> en causa, tendencia, estadística, salvación de tesis o negación encubierta. </p><p id="n6l1o7et7dp">La <code>U</code> honesta se entiende mejor cuando se sitúa entre polos. Sea <code>Π_0(x)</code> el polo de nulidad, límite o neutralización de un régimen, y sea <code>Π_1(x)</code> el polo de presencia, realización o dominio activo. La relación entre ambos no queda agotada por una oposición binaria, porque puede conservar diferencia de potencia, resistencia de tránsito, intensidad positiva, frontera no recorrida o residual pendiente. Por eso se define una lectura relacional mínima: <code>Rel_U^SV(x)=1 ⇔ Dom(x) ∧ Π_0(x) declarado ∧ Π_1(x) declarado ∧ </code><strong><code>Fron(Π_0,Π_1)</code></strong><code> ∧ [Res(x) visible ∨ Ret(x) insuficiente ∨ P(x) no clausurado ∨ I(x) no tipada] ∧ ¬Conclusión formal_binario_suficiente</code>. El término <strong><code>Fron(Π_0,Π_1)</code></strong> no designa una pared geométrica, sino la condición que impide pasar de un polo al otro sin declarar tránsito; <code>P(x)</code> recoge la diferencia orientada cuando el régimen lo admite; <code>I(x)</code> recoge intensidad o presencia total; <code>Res(x)</code> impide borrar el resto; y <code>Ret(x)</code> decide si el resultado puede volver al dominio interrogado. Si todas esas condiciones están resueltas, <code>U</code> no procede; si alguna permanece insuficiente sin contradicción, <code>U</code> comparece como salida honesta. La diferencia entre <code>U</code> y <code>ε−0</code> debe permanecer nítida. En <em>Imperfección preformal y espacio: ε−0, primera distinguibilidad y dominio estructural completo de separación factual recorrible,</em><code>ε−0</code> designa el borde preformal de primera distinguibilidad, anterior al dominio físico constituido. La <code>U</code> tratada aquí no ocupa ese borde de fundamentos: opera como salida conclusiva dentro de un régimen ya interrogado. Tampoco equivale a <code>ε0</code>, entendido en el plano de apertura o suceso cero ya formulado. La cadena queda ordenada así: <code>ε−0</code> pertenece al borde preformal de distinguibilidad; <code>ε0</code> pertenece al régimen de activación ya formulado; <code>U</code> pertenece al conclusión formal honesto de una cuestión situada. Confundir esos planos permitiría atribuir a <code>U</code> función causal, y eso destruiría la precisión de la lectura. La forma de control es: </p><p id="noss0uv4uyw"><code>Err_plano_U^SV=1 ⇔ U=ε−0 ∨ U=ε0 ∨ U=causa ∨ U=motor ∨ U=probabilidad ∨ U=refugio_favorable</code>. </p><p id="nrdcr28ylgh">La ley de Ohm, tipada, ayuda a fijar la diferencia entre identidad primitiva e igualdad operativa sin convertir la electricidad en fundamento. La identidad <code>V ≡ R·I</code>, por ejemplo, permite la asignación <code>R→U</code>, <code>I→1</code>, <code>V→0</code>, de donde resulta <code>0 ≡ U·1</code> en plano de identidad. Sólo después, por proyección operativa, puede escribirse <code>0 = U·1</code>. La triple línea (identidad) conserva que se está leyendo una estructura y no resolviendo una igualdad ordinaria. En esa estructura, <code>R</code> se asocia a <code>U</code> porque la resistencia conserva la condición que impide el paso no acotado; <code>I</code> se asocia a <code>1</code> porque la intensidad nombra régimen activo; <code>V</code> se asocia a <code>0</code> porque la tensión queda leída como diferencia neutralizada en esa asignación. La lectura no afirma que la <code>U</code> sea resistencia eléctrica; afirma que la resistencia muestra una función formal de no paso sin coste. Si se anula indebidamente la restricción mientras el régimen activo permanece, el sistema no retorna a origen: devuelve no acotación, residual o error de dominio. La <code>U</code> honesta también mantiene la audacia del desarrollo dentro de disciplina formal. <strong>Sin </strong><strong><code>U</code></strong><strong>, la trivialización degeneraría en binarismo</strong>: o todo se declara realizado (<code>1</code>) o todo se reduce a nulidad (<code>0</code>). Con <code>U</code>, el SV puede concluir formalmente lo que el análisis permite y suspender lo que todavía no retorna. Esta disciplina es más exigente que una prudencia <em>per se</em>, porque no atenúa la conclusión formal por deferencia externa ni lo fuerza por voluntad interna. Si el dominio-universo físico realizado conserva frontera, traza, residual, retorno, centro de lectura, brazo, intensidad y conservación <em>append-only</em>, e<strong>l régimen presenta giro</strong> según el dominio declarado. Si faltan esas condiciones, no se simula una conclusión: comparece <code>U</code>. La audacia científica no consiste en exceder el aparato; consiste en no debilitar la conclusión formal cuando el aparato ya ha declarado dominio, residual y retorno.</p><h3 id="a4-lnea-del-umbral-sv-distincin-entre-origen-00-e-igualdad-polar-realizada-aa"><strong>A.4. Línea del Umbral SV: distinción entre origen </strong><strong><code>(0,0)</code></strong><strong> e igualdad polar realizada </strong><strong><code>(a,a)</code></strong></h3><div><hr/></div><figure id="ndik1932c0x" data-node-type="image" data-size="70" data-align="full" data-url="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-61780611217180.png" data-caption="" data-href="" data-alt-text="" data-hide-label="false"><img srcSet="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-61780611217180.png?width=800&amp;fit=bounds 1x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-61780611217180.png?width=800&amp;fit=bounds&amp;dpr=2 2x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-61780611217180.png?width=800&amp;fit=bounds&amp;dpr=3 3x" src="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-61780611217180.png?width=800&amp;fit=bounds" alt=""/><figcaption id="ndik1932c0x-figure-caption"><div><div></div></div></figcaption></figure><div><hr/></div><p id="njqwsqa0uac">La Línea del Umbral SV, como ya se ha explicado anteriormente, es el lugar formal de igualdad polar <code>μ=λ</code>. Su función no consiste en borrar la diferencia entre todos sus puntos, sino en distinguir la neutralización del potencial respecto de la intensidad que cada punto conserva. Sea <code>x=(μ,λ)</code> una instancia polar. </p><div><hr/></div><figure id="n9nehmfoyuf" data-node-type="image" data-size="70" data-align="full" data-url="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/Vector_directriz-31780611651065.png" data-caption="&lt;p id=&quot;nq33dc5i8jb&quot; data-reactroot=&quot;&quot;&gt;&lt;strong&gt;Vector directriz de la Línea del Umbral SV.&lt;/strong&gt; La directriz &lt;code&gt;υ_U^SV=(1,1)&lt;/code&gt; fija la orientación propia de la recta &lt;code&gt;μ=λ&lt;/code&gt;: todo desplazamiento de la forma &lt;code&gt;(a,a)&lt;/code&gt; permanece sobre el umbral y conserva potencial neutralizado, &lt;code&gt;P=μ−λ=0&lt;/code&gt;. El vector normal &lt;code&gt;n_U^SV=(1,−1)&lt;/code&gt; mide la salida polar respecto de esa línea, de modo que &lt;code&gt;P(μ,λ)=n_U^SV·(μ,λ)=μ−λ&lt;/code&gt;, mientras que la intensidad se lee sobre la propia directriz como &lt;code&gt;I(μ,λ)=υ_U^SV·(μ,λ)=μ+λ&lt;/code&gt;. La figura distingue así el origen &lt;code&gt;(0,0)&lt;/code&gt;, con &lt;code&gt;P=0&lt;/code&gt; e &lt;code&gt;I=0&lt;/code&gt;, de los puntos no nulos &lt;code&gt;(a,a)&lt;/code&gt;, donde el potencial sigue neutralizado pero la intensidad polar es positiva.&lt;/p&gt;" data-href="" data-alt-text="" data-hide-label="false"><img srcSet="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/Vector_directriz-31780611651065.png?width=800&amp;fit=bounds 1x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/Vector_directriz-31780611651065.png?width=800&amp;fit=bounds&amp;dpr=2 2x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/Vector_directriz-31780611651065.png?width=800&amp;fit=bounds&amp;dpr=3 3x" src="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/Vector_directriz-31780611651065.png?width=800&amp;fit=bounds" alt="" aria-labelledby="n9nehmfoyuf-figure-caption"/><figcaption id="n9nehmfoyuf-figure-caption"><div><div><p id="nq33dc5i8jb" data-reactroot=""><strong>Vector directriz de la Línea del Umbral SV.</strong> La directriz <code>υ_U^SV=(1,1)</code> fija la orientación propia de la recta <code>μ=λ</code>: todo desplazamiento de la forma <code>(a,a)</code> permanece sobre el umbral y conserva potencial neutralizado, <code>P=μ−λ=0</code>. El vector normal <code>n_U^SV=(1,−1)</code> mide la salida polar respecto de esa línea, de modo que <code>P(μ,λ)=n_U^SV·(μ,λ)=μ−λ</code>, mientras que la intensidad se lee sobre la propia directriz como <code>I(μ,λ)=υ_U^SV·(μ,λ)=μ+λ</code>. La figura distingue así el origen <code>(0,0)</code>, con <code>P=0</code> e <code>I=0</code>, de los puntos no nulos <code>(a,a)</code>, donde el potencial sigue neutralizado pero la intensidad polar es positiva.</p></div></div></figcaption></figure><div><hr/></div><p id="n4tqm9fhyw9">El vector directriz de la línea es <code>υ_U^SV=(1,1)</code>, porque todo desplazamiento proporcional a esa dirección conserva <code>μ=λ</code>; el <strong>vector normal</strong> polar es <code>n_U^SV=(1,−1)</code>, porque mide la separación respecto de la igualdad. De ahí se obtienen las dos magnitudes rectoras: <code>P(x)=n_U^SV·x=μ−λ</code> e <code>I(x)=υ_U^SV·x=μ+λ</code>. Sobre la Línea del Umbral, <code>P(x)=0</code>; pero esa neutralización no implica que <code>I(x)=0</code>. Sólo el origen <code>(0,0)</code> cumple simultáneamente <code>P=0</code> e <code>I=0</code>. Todo punto <code>(a,a)</code> con <code>a&gt;0</code> conserva neutralización polar y, a la vez, intensidad positiva. La distinción se expresa de forma directa algebraica: </p><p id="n3vj66cwxsn"><code>𝓛_U^SV={x=(μ,λ): μ=λ}</code>; <code>O_U=(0,0)</code>; <code>EqReal_U(a)=(a,a), a&gt;0</code>; <code>P(O_U)=0 ∧ I(O_U)=0</code>; <code>P(EqReal_U(a))=0 ∧ I(EqReal_U(a))=2a&gt;0</code>. </p><p id="nmzjpd4bch5">En consecuencia, <code>(0,0)</code> no pertenece al mismo régimen que <code>(a,a)</code> cuando <code>a&gt;0</code>, aunque ambos estén situados sobre la misma recta de neutralización polar. El origen carece de intensidad; el equilibrio realizado conserva carga de dominio. Esta diferencia impide tratar la Línea del Umbral como una línea muerta o como una repetición del origen. La igualdad polar puede mantenerse mientras la intensidad crece, se desplaza, se conserva o retorna bajo dominio. Esto ya lo hemos empleado antes, la diferencia para evitar dos confusiones mayores: identificar giro con rotación física externa, e identificar átomo formal de clausura con átomo químico o esfera física. <strong>La trivialización toma esa distinción y la hace elemental</strong>. Si <code>P=0</code> se interpreta sin <code>I</code>, se pierde el dominio; si <code>I&gt;0</code> se ignora por ver sólo la neutralización, se confunde igualdad polar con nulidad absoluta. La trivialización exige mantener ambas lecturas: potencial e intensidad. </p><p id="nxd136qjp7v">En formulación algebraica: <code>Lectura_Umbral^SV(x)=0 ⇔ x∈𝓛_U^SV ∧ P(x)=0 ∧ I(x) declarado ∧ [I(x)=0 ⇒ x=O_U] ∧ [I(x)&gt;0 ⇒ x=EqReal_U(a)]</code>. </p><p id="noj3xh27w3u">Desde esta distinción se entiende la función de <code>U</code>. La <code>U</code> no aparece porque la línea sea incompleta, sino porque una lectura binaria de la línea puede ser insuficiente. Si se pregunta sólo si hay diferencia polar, la respuesta sobre la línea es <code>0</code>: no hay diferencia de predominio. Si se pregunta si hay dominio realizado, la respuesta puede ser <code>1</code> cuando <code>I&gt;0</code> y el régimen conserva frontera, traza, residual y retorno. Si se pregunta si la transición entre dos puntos de la línea está completamente gobernada, puede comparecer <code>U</code> cuando falten dominio, vector director, residual o retorno. </p><p id="nkyt2znzu8r">En formulación lógica formal: <code>U_𝓛^SV(x_i,x_j)=1 ⇔ x_i,x_j∈𝓛_U^SV ∧ P(x_i)=P(x_j)=0 ∧ [I(x_i),I(x_j) declarados] ∧ [Tr,Res,Ret o vector de tránsito insuficientes] ∧ ¬Contradiccion</code>. </p><p id="ndapnendple">Así, <code>U</code> no contradice la neutralización polar; conserva lo que esa neutralización todavía no decide. </p><p id="nd0vpa9jovb">Esta lectura permite corregir la semántica de “redondo”, “círculo”, “giro” y “espiral”. <strong>La clausura circular</strong> de un observable realizado no equivale a esfera física ni a figura geométrica impuesta; designa retorno de dominio con frontera, identidad, traza y residual. <strong>El giro</strong> no equivale a rotación rígida externa; designa circulación de retorno con centro de lectura, brazo, intensidad y conservación <em>append-only</em>. <strong>La espiral</strong> no equivale a tiempo rector ni a repetición cíclica; designa retorno con inscripción no borrada. </p><blockquote id="n5r8u4863d6"><p id="nzh6eqgb0vh">La Línea del Umbral nos aporta la condición formal que permite formularlo sin licencia: donde hay igualdad polar con intensidad positiva, hay régimen; donde hay régimen con retorno, hay posibilidad de circulación; donde esa circulación conserva centro, brazo e intensidad, el régimen presenta giro; donde ese giro conserva inscripción, no hay repetición idéntica. </p></blockquote><p id="n0ty9477ndf">La distinción entre origen y equilibrio realizado también impide identificar TODO/NADA con un observable físico. <code>(0,0)</code> puede servir como notación de neutralización originaria sin intensidad dentro del plano correspondiente, pero ningún dominio físico realizado ocupa por escala el lugar de TODO/NADA. Si un observable conserva intensidad, traza y retorno, ya no está en origen absoluto. Si se pretende devolverlo a <code>(0,0)</code> sin residual, se viola la conservación <em>append-only</em>. El error correspondiente se declara así en su formulación lógica formal: <code>Err_origen^SV=1 ⇔ Obs_real(x)=1 ∧ I(x)&gt;0 ∧ Tr(x) ∧ Ret(x) ∧ x tratado como O_U</code>. Este error es central: buena parte de las confusiones externas nacen de mirar un <code>0</code> de potencial y convertirlo indebidamente en Nada.</p><h3 id="a5-intensidad-positiva-y-neutralizacin-polar-lectura-del-trnsito-por-ejemplo-desde-el-punto-55-a-6464"><strong>A.5. Intensidad positiva y neutralización polar: lectura del tránsito, por ejemplo, desde el punto (5,5)  a → (64,64)</strong></h3><p id="n8x4suxzhma">El tránsito <code>(5,5) → (64,64)</code> se emplea como ejemplo formal de desplazamiento dentro de la Línea del Umbral SV. No mide, <strong>de igual manera</strong>, si abordamos especies reales, edades, valores empíricos ni jerarquía biológica. <strong>Los números sólo permiten observar una estructura</strong>: ambos puntos pertenecen a <code>𝓛_U^SV</code> porque cumplen <code>μ=λ</code>; en ambos casos <code>P=μ−λ=0</code>; <strong>sin embargo, su intensidad no coincide</strong>. Para <code>x_5=(5,5)</code>, <code>I(x_5)=5+5=10</code>. Para <code>x_64=(64,64)</code>, <code>I(x_64)=64+64=128</code>. El tránsito conserva neutralización polar y modifica carga de régimen. La diferencia en <strong>un solo</strong> <strong>polo</strong> es <code>Δμ=64−5=59</code>; la diferencia de intensidad total es <code>ΔI=128−10=118</code>. La lectura correcta no es progreso, superioridad ni sustitución de una forma por otra; es variación de intensidad dentro de una igualdad polar conservada. La forma general del tránsito algebraica es: </p><p id="nlac6z8v2t4"><code>τ_U^SV((a,a),(b,b))=0 ⇔ a&gt;0 ∧ b&gt;0 ∧ a≠b ∧ P(a,a)=0 ∧ P(b,b)=0 ∧ I(a,a)=2a ∧ I(b,b)=2b ∧ ΔI=2(b−a) ∧ Dom(τ) ∧ Tr(τ) ∧ Res(τ) visible ∧ Ret(τ)</code>. </p><p id="n70il5ty72s">Si <code>b&gt;a</code>, la intensidad aumenta; si <code>b&lt;a</code>, disminuye; si <code>b=a</code>, no hay variación de intensidad aunque se conserve el punto. En ningún caso se abandona la Línea del Umbral mientras <code>μ=λ</code>. El componente que decide la admisión no es el tamaño del número, sino la declaración de dominio, traza, residual y retorno del tránsito. </p><p id="ny3zvshgrnw">Por eso se añade: <code>Err_τU^SV=1 ⇔ ΔI interpretado como superioridad ontológica ∨ P=0 interpretado como origen ∨ Res(τ) omitido ∨ Ret(τ) ausente ∨ Dom(τ) no declarado</code>. </p><p id="nle8qyel97q">El ejemplo permite separar tres niveles. El primero es el nivel de neutralización: <code>P=0</code> en ambos puntos. El segundo es el nivel de intensidad: <code>I</code> cambia de <code>10</code> a <code>128</code>. El tercero es el nivel de tránsito: sólo hay lectura admisible si la variación de intensidad se sitúa en un dominio con traza, residual y retorno. La reducción binaria no alcanza estos tres niveles. <strong>Si se mira sólo </strong><strong><code>P</code></strong><strong>, todo parece igual</strong>; si se mira sólo <code>I</code>, se pierde la neutralización; si se mira sólo el salto numérico, se introduce una escala sin dominio. <strong>La trivialización exige mantener la terna operativa</strong>: <code>0</code> para neutralización polar, <code>1</code> para presencia de régimen cuando <code>I&gt;0</code>, y <code>U</code> para todo tramo cuyo dominio, residual o retorno no esté suficientemente declarado. La relación con las especies, usada en la fase de razonamiento que exponemos, se depura perfectamente. No se afirma, usando los valores anteriores, que una especie ocupe literalmente <code>(5,5)</code> ni que otra ocupe <code>(64,64)</code>. Se afirma que cualquier régimen vivo realizado, si se somete a lectura SV, no puede quedar reducido a presencia o ausencia. Debe declarar identidad, dominio, transición, traza, residual y retorno. La evolución biológica externa trabaja con sus propias magnitudes, poblaciones, herencia, variación y adaptación; el SV no adopta esos términos como fundamento, pero conserva una enseñanza formal de los precedentes razonados: <strong>lo realizado no vuelve al origen sin inscripción</strong>. </p><blockquote id="n6uyxzzgewj"><p id="n7ndrffeby5">En lenguaje SV: <code>Vida_regimen^SV(x)=1 ⇒ Dom(x) ∧ Id(x) ∧ Tr(x) ∧ Res(x) ∧ Ret(x) ∧ AppendOnly_SV</code>. </p></blockquote><p id="nqyb52m0e37">Si falta alguno de esos componentes, no hay licencia para resultado completo; comparece <code>U</code>. El tránsito <code>(5,5) → (64,64)</code> también prepara la lectura de clausura circular, giro y espiral. La clausura circular no exige abandonar la Línea del Umbral; exige retorno de dominio. El giro no exige rotación externa; exige circulación de retorno con centro, brazo, intensidad y traza. La espiral no exige tiempo rector; exige que el retorno no borre la inscripción previa. El salto de intensidad dentro de <code>P=0</code> muestra cómo puede haber variación real sin ruptura de neutralización polar. En fórmula formal: <code>CircRet(x)=1</code> no se deduce de <code>P=0</code> por sí solo; exige <code>Dom(x) ∧ Fron(x) ∧ Tr(x) ∧ Res(x) ∧ Ret(x)</code>. <code>Giro(x)=1</code> no se deduce de intensidad aislada; exige <code>CircRet(x) ∧ Ctr(x) ∧ Brazo(x) ∧ I(x)&gt;0 ∧ AppendOnly_SV</code>. <code>Espiral_AO(x)=1</code> no se deduce de giro aislado; exige <code>Giro(x) ∧ Tr(x) ∧ Ret(x) ∧ ¬Repeticion_identica</code>. <strong>Con ello, la trivialización alcanza una formulación estable:</strong> una igualdad puede conservarse mientras cambia la intensidad; un tránsito puede producir diferencia sin abandonar la línea; un dominio puede retornar sin repetirse; y una clausura puede presentar giro sin traducirse a rotación física externa. La <code>U</code> honesta custodia los tramos no resueltos de esa cadena. Si el dominio está declarado y el retorno es suficiente, procede conclusión formal. Si falta dominio, vector, residual o retorno, no se fuerza la conclusión. Ese es el punto de la lectura <code>(5,5) → (64,64)</code>: <strong>enseñar que el cero de potencial no elimina la vida del régimen, y que la intensidad positiva impide confundir neutralización con origen</strong>.</p><h3 id="a6-el-cero-segn-su-posicin-formal-origen-lmite-restriccin-clausura-y-residual"><strong>A.6. El cero según su posición formal: origen, límite, restricción, clausura y residual</strong></h3><p id="ndv65qnanhp">El cero no puede leerse como una entidad única dentro de una pregunta ya situada. La trivialización rigurosa exige determinar qué función cumple <code>0</code> antes de usarlo como conclusión formal, límite, origen o ausencia. </p><p id="npfzc7i558i">En un régimen puede nombrar origen sin intensidad; en otro, límite no ocupable; en otro, neutralización de potencial; en otro, residual nulo; en otro, restricción que no puede anularse sin desbordamiento y en otro, clausura formal de una tesis. La confusión aparece cuando todos esos usos se reducen a Nada. El SV no autoriza esa reducción. <code>NADA_SV</code> no se obtiene por ver un símbolo <code>0</code>; exige dominio, frontera y separación de plano. </p><p id="ncerdb2aa93">La forma algebraica de control queda: </p><p id="nn3wrn0zn23"><code>Tipo_0^SV(x) ∈ {Origen, Límite, Neutralización, Ausencia, Clausura, Restricción, Residual_nulo, Frontera}</code>; <code>Lect_0^SV(x)=0 ⇔ Dom(x) ∧ Fron(x) ∧ Tipo_0^SV(x) declarado ∧ I(x) declarada ∧ Res(x) visible ∧ Ret(x)</code>; <code>Err_0^SV(x)=1 ⇔ 0=NADA_SV sin Dom(x) ∨ 0=Origen con I(x)&gt;0 ∨ 0=Residual_nulo con Res(x) no declarado ∨ 0=Clausura con Ret(x) ausente ∨ 0=Restricción anulada con régimen activo no tipado</code>. </p><p id="nou1om078rv"><strong>La distinción es obligatoria porque el mismo signo </strong><strong><code>0</code></strong><strong> puede ocupar lugares incompatibles</strong>. En la Línea del Umbral, <code>P=0</code> significa neutralización polar, no origen necesario; si <code>μ=λ=a</code> y <code>a&gt;0</code>, la intensidad <code>I=2a</code> conserva presencia de régimen. En una relación de cociente, el denominador que tiende a <code>0</code> no actúa como origen, sino como restricción que se retira mientras el régimen activo permanece. En una conclusión formal de tesis, <code>0</code> puede indicar conclusión sin error dentro del criterio declarado. En un residual, <code>Res=0</code> indica ausencia de resto dentro de una transducción concreta, no anulación de todo dominio. Por eso la pregunta correcta no es si aparece un cero, <strong>sino dónde aparece, qué sostiene, qué anula, qué conserva y qué retorno exige</strong>. </p><p id="n4ewi12r63p">La forma de cociente muestra el problema con nitidez. En la ley de Ohm, el dominio externo formula <code>V=I·R</code> y permite <code>I=V/R</code>; OpenStax recoge la relación ordinaria entre tensión, corriente y resistencia en un circuito óhmico (OpenStax, 2016d). En gravitación universal, otro ejemplo usado, la formulación newtoniana externa expresa la fuerza como proporcional al producto de masas e inversamente proporcional al cuadrado de la distancia entre sus centros (NASA Goddard Space Flight Center, 2020). En ambos casos, al reducir la magnitud restrictiva hacia <code>0</code> con numerador activo, no se obtiene origen limpio: aparece no acotación, singularización formal o error de dominio. </p><p id="nr7qke609h8">La forma abstracta es: <code>Coc_SV(Y;A,B)=0 ⇔ Y=A/B ∧ Dom(A,B,Y) ∧ B=Restricción ∧ A=Régimen_activo ∧ Ret(Y)</code>; <code>B→0 ∧ A≠0 ⇒ NoAcot(Y) ∨ U_Coc ∨ Err_Dom</code>; <code>B→0 ∧ A=0 ⇒ U_Coc</code>, salvo que el dominio declare una clausura específica. </p><p id="n7z3mtsdwd0">La advertencia no autoriza extrapolar cualquier cociente a cualquier régimen. Sólo permite tipar una función formal: cuando la magnitud que limita, separa o transduce se anula sin anular el régimen activo, el resultado no vuelve al origen. La <code>U</code> honesta comparece si falta dominio, si la magnitud restrictiva no está tipada, si el numerador no ha sido declarado o si el retorno no permite decidir entre no acotación, residual o error. La trivialización no dice que la ley de Ohm, gravitación, temperatura límite (otro ejemplo usado) y Línea del Umbral sean lo mismo; dice que todos obligan a distinguir el cero de origen, el cero de neutralización, el cero de restricción y el cero de residual. <strong>El cero absoluto</strong>  (entendido como temperatura) sirve como ejemplo externo de límite, no como fundamento SV. NIST recuerda que Lord Kelvin calculó el límite de <code>−273,15 °C</code>, equivalente a <code>0 K</code>, como extremo inferior de temperatura (NIST, 2024). Para esta lectura, el dato externo no funda la terna: sólo muestra que un cero puede operar como límite no disponible para ocupación ordinaria. </p><p id="nuh16yl9ani">La forma SV es: <code>0_Lim^SV(x)=1 ⇔ Dom(x) ∧ Límite(x)=0 ∧ Aproximación_admisible(x) ∧ Ret_límite(x) ∧ ¬Ocupación_ordinaria(x)</code>; <code>Err_Lim^SV=1 ⇔ Límite=Origen ∨ Límite=NADA_SV ∨ Aproximación=Clausura ∨ Ret_límite omitido</code>. </p><p id="n7eygiysfb8">La clausura de tesis añade un uso distinto. En esta lectura, cuando se escribe <code>Triv_SV(Q)=0</code>, el cero no significa nulidad de <code>Q</code>, sino conclusión del criterio de trivialización sin error. Cuando se escribe <code>Err_0^SV=1</code>, el uno no significa sustancia ni presencia material, sino comparecencia positiva del error. <strong>Esta convención debe mantenerse para evitar inversión semántica</strong>. El cero puede clausurar una tesis, neutralizar un potencial, anular un residual o señalar un límite; sólo bajo dominio adecuado puede ser origen. Si se confunden esos usos, convierte la trivialización en pobreza formal. Si los distingue, la trivialización recupera su fuerza: cada pregunta queda reducida a la posición exacta de sus <code>0</code>, sus <code>1</code> y sus <code>U</code>.</p><h3 id="a7-vas-laterales-de-contraste-ohm-gravitacin-cero-absoluto-agua-fuego-volcanes-y-especies"><strong>A.7. Vías laterales de contraste: Ohm, gravitación, cero absoluto, agua, fuego, volcanes y especies</strong></h3><p id="n38iso6hxv9">Las vías laterales no se incorporan como fundamentos del SV. Se incorporan como contrastes disciplinados para <strong>mostrar que la trivialización no opera por analogía libre</strong>, sino por declaración de dominio, frontera, identidad, residual y retorno. Una vía lateral sólo puede entrar si conserva su dominio externo, declara qué componente transporta, evita identificación material con el régimen SV y devuelve residual visible. </p><p id="ngiedf67gdj">La regla en formulación lógica formal es: </p><p id="nrm30n9fjej"><code>VíaLat_SV(R)=0 ⇔ Dom_ext(R) ∧ Dom_SV(R) ∧ Trans_R↔SV declarada ∧ Id(R) no confundida ∧ Función_transportada(R) declarada ∧ Res_R visible ∧ Ret_R ∧ NoIdentMat(R)=1</code>; <code>Err_VíaLat^SV(R)=1 ⇔ referencia_externa=fundamento_SV ∨ identidad_material_forzada ∨ función_transportada omitida ∨ Res_R oculto ∨ Ret_R ausente ∨ U usada como aceptación</code>; <code>U_VíaLat^SV(R) ⇔ Dom_ext, Dom_SV, Trans_R↔SV, Res_R o Ret_R insuficientes sin contradicción</code>. </p><p id="nquciznc9xv">La ley de Ohm transporta la función formal de restricción, no la electricidad como fundamento. El dominio externo declara tensión, corriente y resistencia; OpenStax formula <code>V=I·R</code> y la relación de resistencia con tensión e intensidad en un circuito óhmico (OpenStax, 2016d). En la lectura SV, la identidad primaria <code>V </code><strong><code>≡</code></strong><code> R·I</code> permite leer <code>R→U</code>, <code>I→1</code>, <code>V→0</code> en plano de identidad estructural, de donde resulta <code>0 ≡ U·1</code>; sólo después se admite la igualdad operativa <code>0</code><strong><code>=</code></strong><code>U·1</code>. La enseñanza no es eléctrica, sino formal: una restricción no puede borrarse sin coste cuando el régimen activo permanece. La función transportada algebraica es: </p><p id="nox0x8uwux0"><code>Func_Ohm^SV=Restricción_no_borrable</code>; <code>Adop_Ohm^SV=0 ⇔ Dom_elec ∧ V≡R·I ∧ R→U ∧ I→1 ∧ V→0 ∧ Dist(≡,=) ∧ Res_visible ∧ Ret_formal</code>. </p><p id="nvru8nwm6io">La gravitación universal transporta la función de separación, no una cosmología. La formulación externa <code>F=G·m₁·m₂/r²</code> expresa una relación de atracción entre masas con dependencia inversa del cuadrado de la distancia, según la exposición de NASA Goddard sobre la ley de Newton (NASA Goddard Space Flight Center, 2020). En la lectura SV, <code>G</code> puede quedar como constante externa de dominio, mientras <code>r²</code> muestra la función restrictiva de separación. Si <code>r²→0</code> con <code>m₁·m₂≠0</code>, no se obtiene origen, sino no acotación formal o error de dominio. La función transportada es: <code>Func_Grav^SV=Separación_no_borrable</code>; <code>Adop_Grav^SV=0 ⇔ Dom_grav ∧ F∝(m₁·m₂)/r² ∧ r²=Restricción_sep ∧ m₁·m₂=Régimen_activo ∧ Res_visible ∧ Ret_formal</code>. El cero absoluto transporta la función de límite. No entra como temperatura SV ni como ontología de la materia. Su utilidad reside en mostrar que un cero puede ser límite de régimen sin convertirse en estado ordinario ni en Nada. La función transportada se define: <code>Func_0K^SV=Límite_no_ocupable_como_origen</code>; <code>Adop_0K^SV=0 ⇔ Dom_term_ext ∧ 0K=Límite ∧ ¬(0K=NADA_SV) ∧ Ret_límite ∧ Res_visible</code>. </p><p id="nkj30jres24"><strong>El agua</strong>, siguiendo el ejemplo, transporta la distinción entre identidad y estado. El dominio externo identifica el agua como <code>H₂O</code>; NIST Chemistry WebBook registra el agua con fórmula <code>H₂O</code> y peso molecular <code>18,0153</code> (NIST Chemistry WebBook, s. f.). Sin embargo, la pregunta “<strong>qué es el agua</strong>” no queda agotada por la fórmula molecular si el régimen interrogado exige estado, frontera de transición y retorno. <strong>Hielo, líquido y vapor</strong> conservan identidad química bajo estados distintos; por tanto, la trivialización obliga a separar identidad material, régimen de estado y tránsito. La función transportada es: <code>Func_H2O^SV=Identidad_bajo_estado_y_tránsito</code>; <code>Agua_SV^lat=0 ⇔ Id(H₂O) ∧ Estado(H₂O) declarado ∧ Fron_estado ∧ Tr_estado ∧ Res_estado ∧ Ret_estado</code>. </p><p id="nivw2ngs7sr"><strong>El fuego</strong>, en la mima línea, transporta la función de tránsito sostenido, no una sustancia. Como vía lateral, se lee por soporte, frontera, emisión, residuo y cese del régimen cuando falta continuidad de alimentación o intercambio. El fuego enseña que no todo cero opera igual: el cero de soporte extingue el tránsito; el cero de restricción puede desbordarlo. La función transportada es: <code>Func_Fuego^SV=Tránsito_sostenido_con_cese_por_pérdida_de_soporte</code>; <code>Fuego_lat^SV=0 ⇔ Dom_comb ∧ Soporte ∧ Fron_trans ∧ Emisión ∧ Res_comb ∧ Ret_cese</code>. </p><p id="n895fa5xd1l"><strong>Un volcán</strong> transporta la función de frontera geológica bajo presión, emisión y depósito. USGS explica que, cuando el magma es viscoso y los gases no escapan fácilmente, la presión puede crecer hasta producir erupciones explosivas; también describe el ascenso del magma por flotabilidad y presión de gases (U.S. Geological Survey, s. f.-a, s. f.-c). En la lectura SV, el volcán no se usa por espectacularidad, sino porque muestra un régimen donde frontera, presión, emisión, depósito y traza no permiten retorno al origen sin resto. La función algebraica transportada es: <code>Func_Volc^SV=Frontera_activa_con_emisión_y_depósito</code>; <code>Volc_lat^SV=0 ⇔ Dom_geo ∧ Presión ∧ Fron_geo ∧ Emisión ∧ Depósito ∧ Tr_geo ∧ Res_geo ∧ Ret_geo</code>. </p><p id="nfkn7kmy0rm"><strong>Las especies</strong> transportan la función de inscripción heredada y no retorno. La biología evolutiva externa define la evolución como descendencia con modificación y cambio en la información heredable transmitida entre generaciones (University of California Museum of Paleontology, s. f.). La lectura SV no importa azar, estadística ni tiempo rector como fundamento; conserva únicamente la función formal de traza heredada y modificación no borrable. Una especie puede extinguirse, transformarse o dejar residuo, pero no vuelve a no haber ocurrido. La función transportada es: <code>Func_Esp^SV=Traza_heredada_y_no_borrado_append_only</code>; <code>Esp_lat^SV=0 ⇔ Dom_bio ∧ Id_bio ∧ Tr_heredada ∧ Variación ∧ Res_bio ∧ Ret_bio ∧ AppendOnly_SV</code>. </p><p id="ncyphzqn1wt">La conclusión que podemos extraer es estricta: las vías laterales sólo son admisibles si obedecen el aparato o sistema de trivialización. Ohm no funda <code>U</code>; gravitación no funda la Línea del Umbral; el cero absoluto no funda <code>NADA_SV</code>; el agua no funda la identidad SV; el fuego no funda el tránsito; el volcán no funda la frontera; las especies no fundan <em>append-only</em>. Cada vía devuelve una función tipada. La trivialización las subordina y las ajusta: si pasan por dominio, frontera, traza, residual y retorno, devuelven una función; si no pasan, devuelven <code>U</code> o error.</p><h3 id="a8-clausura-circular-del-observable-realizado-circularidad-sin-esfera-fsica"><strong>A.8. Clausura circular del observable realizado: circularidad sin esfera física</strong></h3><div><hr/></div><figure id="nmhrn0fp1r7" data-node-type="image" data-size="70" data-align="full" data-url="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-11780613110639.png" data-caption="" data-href="" data-alt-text="" data-hide-label="false"><img srcSet="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-11780613110639.png?width=800&amp;fit=bounds 1x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-11780613110639.png?width=800&amp;fit=bounds&amp;dpr=2 2x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-11780613110639.png?width=800&amp;fit=bounds&amp;dpr=3 3x" src="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-11780613110639.png?width=800&amp;fit=bounds" alt=""/><figcaption id="nmhrn0fp1r7-figure-caption"><div><div></div></div></figcaption></figure><div><hr/></div><p id="np14tb0po1l">La clausura circular del observable realizado no equivale a esfera física, globo cosmológico, contorno geométrico externo ni figura imaginada desde fuera. Designa un régimen de retorno de dominio. Un observable realizado presenta clausura circular cuando su identidad no se dispersa como suma de partes inconexas, sino que retorna a lectura bajo dominio, frontera, traza y residual. La circularidad, en este sentido, no describe la forma material del universo; describe la condición por la cual un dominio puede leerse como unidad retornada. La forma algebraica mínima es: </p><p id="nl8jfx5kqsy"><code>CircCl_SV(o,Ω)=1 ⇔ Obs_real(o,Ω)=1 ∧ Dom(Ω) ∧ Fron_Ω(o) ∧ Id_Ω(o) ∧ Tr_Ω(o) ∧ Res_Ω(o) ∧ Ret_Ω(o) ∧ Cl_Ω(o)=1</code>; <code>Err_CircCl^SV=1 ⇔ CircCl=esfera_física ∨ CircCl=imagen_geométrica ∨ CircCl=rotación_externa ∨ Dom(Ω) omitido ∨ Fron_Ω omitida ∨ Res_Ω oculto ∨ Ret_Ω ausente</code>; <code>U_CircCl^SV ⇔ Dom(Ω), Fron_Ω, Tr_Ω, Res_Ω o Ret_Ω insuficientes sin contradicción</code>. </p><p id="nkfnmmyuqt1">Esta definición conserva la orientación material ya fijada. Allí el dominio-universo físico realizado se formula como instancia con circulación de retorno bajo dominio, frontera, potencial, intensidad, centro de lectura, brazo, traza, residual y conservación <em>append-only</em>; además, ante lectura externa superior <strong>comparece como átomo formal de clausura</strong>, no como átomo químico literal ni esfera física. <strong>La clausura circular traduce ese núcleo a trivialización</strong>: si hay observable realizado, dominio declarado, frontera, identidad, traza, residual y retorno, <strong>puede hablarse de circularidad de clausura</strong>; si se exige que esa circularidad sea esfera física, se comete error de plano. La circularidad de clausura debe distinguirse de la representación geométrica. Un círculo externo tiene centro, radio, circunferencia y métrica gráfica. La clausura circular SV tiene centro de lectura, frontera de dominio, traza, residual y retorno. Puede adoptar recursos geométricos para ilustración, pero no depende de ellos como fundamento. La correspondencia tipada es: <code>centro_geométrico ↦ Ctr_Ω(o) como centro de lectura</code>; <code>radio ↦ Brazo_Ω(o) como separación situada respecto del centro</code>; <code>circunferencia ↦ Fron_Ω(o) como frontera de régimen</code>; <code>vuelta ↦ Ret_Ω(o) como retorno de lectura</code>; <code>área ↦ Dom(Ω) como dominio declarado</code>; <code>trazo ↦ Tr_Ω(o) como inscripción conservada</code>; <code>imperfección de clausura ↦ Res_Ω(o) como residual visible</code>. La flecha <code>↦</code> no indica identidad material. Indica traducción de función bajo dominio. Si el alguien exige que la clausura circular sea una esfera observable desde fuera, cambia de dominio sin declarar transducción. Si se permite una imagen circular sin residual, también se pierde el método y la sistemática. La clausura circular no es dibujo perfecto: es retorno de dominio con resto visible. Por eso admite residual gobernado y conserva <code>U</code> cuando falta información suficiente. La circularidad tampoco basta para afirmar giro. El giro exige una condición adicional: centro de lectura, brazo, intensidad y momento interno de retorno. Puede haber clausura circular como retorno de dominio sin que todavía se haya evaluado formalmente el régimen de giro. La transición se expresa así: <code>CircCl_SV(o,Ω)=1 ∧ I_Ω(o)&gt;0 ∧ Ctr_Ω(o) ∧ Brazo_Ω(o) ∧ MomRet_Ω(o) ∧ AppendOnly_SV ⇒ Giro(o,Ω)=1</code>; <code>CircCl_SV(o,Ω)=1 ∧ [Ctr_Ω(o) ∨ Brazo_Ω(o) ∨ MomRet_Ω(o)] insuficiente ⇒ U_Giro^SV</code>; <code>Err_Giro^SV=1 ⇔ Giro=rotación_rígida_obligatoria ∨ Giro=momento_angular_externo_sin_transducción ∨ CircCl usada como esfera física ∨ Res omitido</code>. Esta separación conserva la secuencia conceptual. El apartado A.8 fija la circularidad de clausura;  el A.9 demostrará el giro como circulación de retorno con centro, brazo, intensidad, traza, residual y <em>append-only</em>;  el A.10 formulará la espiral como retorno con inscripción no repetida. La cadena no es imagen: <code>Clausura circular → Giro → Espiral append-only</code>. La primera impide dispersión del observable; el segundo introduce orientación situada y momento de retorno; la tercera impide repetición idéntica por conservación de inscripción. Aplicado al dominio-universo físico realizado, el resultado no se formula como “el universo es una esfera”, sino como: <code>CircCl_SV(o_U,Ω_U)=1</code> si <code>o_U</code> comparece como observable realizado, <code>Ω_U</code> declara dominio, <code>Fron_sut(Ω_U)</code> fija frontera sutural, <code>Tr_ΩU(o_U)</code> conserva inscripción, <code>Res_ΩU(o_U)</code> conserva residual visible, <code>Ret_ΩU(o_U)</code> devuelve lectura de dominio y <code>Cl_ΩU(o_U)=1</code> declara clausura. Desde ahí puede avanzarse hacia giro, pero no por licencia verbal ni por imagen, sino por condiciones adicionales. La forma es: <code>CircCl_SV(o_U,Ω_U)=1 ⇔ Obs_real(o_U,Ω_U)=1 ∧ Fron_sut(Ω_U) ∧ Id_ΩU(o_U) ∧ Tr_ΩU(o_U) ∧ Res_ΩU(o_U) ∧ Ret_ΩU(o_U) ∧ Cl_ΩU(o_U)=1</code>; <code>Err_CircClΩU^SV=1 ⇔ Ω_U=esfera_física_obligatoria ∨ Ω_U=globo_cosmológico ∨ Ω_U=átomo_químico ∨ Ret_ΩU omitido ∨ Res_ΩU oculto ∨ referencia_externa=fundamento_SV</code>. La clausura circular queda así situada: no se pide permiso a la geometría externa para declarar retorno de dominio, pero tampoco se invade la geometría externa con una afirmación que no le pertenece. La ciencia empírica podrá traducir esta clausura a magnitudes de forma, curvatura, topología, observación o cosmología si declara dominio, transducción, residual y retorno. Sin esa transducción, no cancela ni confirma la resultado interno; devuelve <code>U</code> en su propio plano. El SV conserva su afirmación exacta: un observable realizado con dominio, frontera, identidad, traza, residual y retorno puede comparecer como clausura circular sin convertirse en esfera física.</p><h3 id="a9-giro-circulacin-de-retorno-con-centro-brazo-intensidad-traza-residual-y-conservacin-append-only"><strong>A.9. Giro: circulación de retorno con centro, brazo, intensidad, traza, residual y conservación </strong><em><strong>append-only</strong></em></h3><div><hr/></div><figure id="nkxtm0djr4k" data-node-type="image" data-size="70" data-align="full" data-url="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-41780613308812.png" data-caption="" data-href="" data-alt-text="" data-hide-label="false"><img srcSet="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-41780613308812.png?width=800&amp;fit=bounds 1x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-41780613308812.png?width=800&amp;fit=bounds&amp;dpr=2 2x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-41780613308812.png?width=800&amp;fit=bounds&amp;dpr=3 3x" src="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-41780613308812.png?width=800&amp;fit=bounds" alt=""/><figcaption id="nkxtm0djr4k-figure-caption"><div><div></div></div></figcaption></figure><div><hr/></div><p id="n665ayz6zkl">El giro se define en esta lectura como circulación de retorno de una instancia realizada bajo dominio declarado. No equivale por defecto a rotación rígida externa, vorticidad métrica, anisotropía cosmológica ni momento angular físico. Tampoco queda reducido a imagen circular. El término se usa en sentido estricto cuando concurren las condiciones que lo hacen admisible: observable realizado, dominio, frontera, circulación de retorno, centro de lectura, brazo, intensidad positiva, traza, residual, retorno y conservación <em>append-only</em>. Una vez fijado ese dominio, el término no necesita una reserva verbal permanente: el régimen presenta giro si el aparato lo concluye formalmente. La forma lógica formal mínima es: </p><p id="nzjqr7sqick"><code>Giro(o,Ω)=1 ⇔ Obs_real(o,Ω)=1 ∧ CircRet_Ω(o)=1 ∧ I_Ω(o)&gt;0 ∧ Ctr_Ω(o) ∧ Brazo_Ω(o) ∧ MomRet_Ω(o) ∧ Tr_Ω(o) ∧ Res_Ω(o) ∧ Ret_Ω(o) ∧ AppendOnly_SV</code>; <code>Err_Giro^SV=1 ⇔ Giro=rotación_rígida_externa ∨ Giro=vorticidad_métrica_sin_transducción ∨ Giro=momento_angular_cosmológico_sin_magnitud ∨ Ctr_Ω omitido ∨ Brazo_Ω omitido ∨ Res_Ω oculto ∨ Ret_Ω ausente</code>; <code>U_Giro^SV ⇔ CircRet_Ω, Ctr_Ω, Brazo_Ω, I_Ω, Tr_Ω, Res_Ω o Ret_Ω insuficientes sin contradicción</code>. </p><p id="n0jzmw6kd6j">La definición separa tres niveles. El primero es la clausura circular: el observable no se dispersa como suma inconexa, sino que retorna a lectura bajo dominio, frontera, traza y residual. El segundo es el momento interno de retorno: la circulación adquiere centro de lectura, brazo e intensidad positiva. El tercero es el giro: el momento de retorno conserva inscripción y residual bajo <em>append-only</em>. La cadena se expresa así: <code>CircCl_SV(o,Ω)=1 ∧ I_Ω(o)&gt;0 ∧ Ctr_Ω(o) ∧ Brazo_Ω(o) ⇒ MomRet_Ω(o)=1</code>; <code>MomRet_Ω(o)=1 ∧ Tr_Ω(o) ∧ Res_Ω(o) ∧ Ret_Ω(o) ∧ AppendOnly_SV ⇒ Giro(o,Ω)=1</code>. </p><blockquote id="n5kaa4ikqa9"><p id="nwq8pliz3hs">La diferencia entre giro y rotación externa no debilita el término; lo tipa. </p></blockquote><p id="na6bdmhwngm">La rotación rígida pertenece al dominio físico externo cuando hay magnitud cinemática o dinámica declarada. La vorticidad pertenece a su propio régimen matemático y cosmológico cuando hay campo, métrica y operador adecuados. El momento angular pertenece a un dominio mecánico definido por magnitudes y unidades. El giro, en régimen SV, pertenece al dominio declarado cuando hay circulación de retorno con centro, brazo, intensidad, traza, residual y retorno. Si se desea traducir una forma a otra, la transducción debe declararse; sin esa transducción, <strong>la ciencia empírica no confirma ni cancela el giro, sino que devuelve </strong><strong><code>U</code></strong><strong> en su dominio propio</strong>. El papel de la Línea del Umbral permanece activo. En <code>μ=λ</code>, el potencial se neutraliza: <code>P=μ−λ=0</code>. Sin embargo, si <code>μ=λ=a</code> y <code>a&gt;0</code>, la intensidad es positiva: <code>I=2a</code>. La neutralización polar no elimina el régimen. Cuando una instancia con intensidad positiva retorna bajo dominio, frontera, traza y residual, la circularidad de clausura puede adquirir momento. Si ese momento conserva inscripción y no borra el tránsito anterior, procede la conclusión formal de giro. En fórmula: <code>P(a,a)=0 ∧ I(a,a)=2a&gt;0 ∧ CircRet(a,a)=1 ∧ Ctr(a,a) ∧ Brazo(a,a) ∧ Tr(a,a) ∧ Ret(a,a) ⇒ Giro(a,a)=1</code>. Este enunciado no convierte cualquier punto de la Línea del Umbral en giro. Exige dominio y retorno. Tampoco convierte cualquier retorno en giro. Exige centro, brazo e intensidad. El criterio evita dos errores: declarar giro por mera forma circular, o negar giro </p><blockquote id="nvejcsp02e3"><p id="nieudjuv4xb"><strong>porque no se ha traducido aún a rotación física externa</strong>. </p></blockquote><p id="npk6phtd566">La trivialización conserva la pregunta en su nivel exacto: si se pregunta por rotación física, se exige magnitud física; si se pregunta por circulación de retorno de dominio, se exige el aparato SV; si se mezclan ambos sin transducción, comparece <code>U</code>. Aplicado al dominio-universo físico realizado, el resultado se formula sin imagen externa: si <code>o_U</code> comparece como observable realizado de <code>Ω_U</code>, conserva frontera sutural, traza, residual, retorno, centro de lectura, brazo, intensidad positiva y <em>append-only</em>, entonces presenta giro. La forma nos queda: <code>Giro(o_U,Ω_U)=1 ⇔ Obs_real(o_U,Ω_U)=1 ∧ Fron_sut(Ω_U) ∧ CircRet_ΩU(o_U)=1 ∧ I_ΩU(o_U)&gt;0 ∧ Ctr_ΩU(o_U) ∧ Brazo_ΩU(o_U) ∧ MomRet_ΩU(o_U) ∧ Tr_ΩU(o_U) ∧ Res_ΩU(o_U) ∧ Ret_ΩU(o_U) ∧ AppendOnly_SV</code>. </p><p id="nj7u85he60t"><strong>La ciencia externa puede devolver restricciones al traducir este resultado a rotación rígida, vorticidad, anisotropía o momento angular cosmológico. Esa traducción es necesaria cuando se pretende hablar en sus magnitudes. Pero no funda ni anula el resultado interno</strong>: pertenece al retorno externo. El giro queda, por tanto, afirmado en su dominio exacto y abierto a transducción controlada, sin confusión de planos.</p><h3 id="a10-espiral-append-only-retorno-con-inscripcin-no-repeticin-idntica"><strong>A.10. Espiral </strong><em><strong>append-only</strong></em><strong>: retorno con inscripción, no repetición idéntica</strong></h3><div><hr/></div><figure id="nbgfeyf7ygn" data-node-type="image" data-size="60" data-align="full" data-url="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-31780613494729.png" data-caption="" data-href="" data-alt-text="" data-hide-label="false"><img srcSet="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-31780613494729.png?width=800&amp;fit=bounds 1x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-31780613494729.png?width=800&amp;fit=bounds&amp;dpr=2 2x,https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-31780613494729.png?width=800&amp;fit=bounds&amp;dpr=3 3x" src="https://assets.pubpub.org/c39829d0b-6cf2-4c57-8562-04aa66068f1d/p30dfd78b-4ee2-429e-a73c-c822c800a316/u8d2bc69d-73c6-4669-a7e7-fb07fdba4171/image-31780613494729.png?width=800&amp;fit=bounds" alt=""/><figcaption id="nbgfeyf7ygn-figure-caption"><div><div></div></div></figcaption></figure><div><hr/></div><p id="n31gyq6xvk0">La espiral <em>append-only</em> nombra el retorno que conserva inscripción y, por esa razón, no repite de modo idéntico el punto anterior. No introduce tiempo rector, no impone ciclo físico externo y no convierte el giro en cronología. Designa una consecuencia formal: si una instancia retorna bajo traza, residual y conservación <em>append-only</em>, el retorno no puede borrar lo ocurrido para simular origen. La clausura circular evita dispersión; el giro introduce circulación de retorno con centro, brazo e intensidad; la espiral conserva que cada retorno lleva inscripción. </p><p id="nktmlyznqss">La forma mínima en álgebra es: <code>Espiral_AO^SV(o,Ω)=1 ⇔ Giro(o,Ω)=1 ∧ Tr_Ω(o) ∧ Res_Ω(o) ∧ Ret_Ω(o) ∧ React_Ω(o) ∧ AppendOnly_SV ∧ ¬Repeticion_identica(o)</code>; <code>Err_Espiral^SV=1 ⇔ Espiral=tiempo_rector ∨ Espiral=ciclo_idéntico ∨ Espiral=figura_geométrica_obligatoria ∨ Tr_Ω omitida ∨ Res_Ω oculto ∨ Ret_Ω ausente ∨ AppendOnly_SV negado</code>; <code>U_Espiral^SV ⇔ Giro, Tr_Ω, Res_Ω, Ret_Ω, React_Ω o AppendOnly_SV insuficientes sin contradicción</code>. </p><p id="nb0eo65b8rt">La espiral se distingue del círculo. El círculo, como imagen externa, sugiere retorno al mismo punto. La clausura circular SV no dice eso: declara retorno de dominio. La espiral añade que el retorno conserva inscripción; por tanto, la instancia retornada no es indistinguible de su estado anterior. Si se borra la inscripción, se viola <em>append-only</em>; si se conserva, la repetición idéntica deja de ser admisible. La transición se formula así: <code>CircCl_SV(o,Ω)=1 ⇒ Ret_Ω(o)</code>; <code>Giro(o,Ω)=1 ⇒ Ret_Ω(o) ∧ Ctr_Ω(o) ∧ Brazo_Ω(o) ∧ I_Ω(o)&gt;0</code>; <code>Espiral_AO^SV(o,Ω)=1 ⇒ Giro(o,Ω) ∧ Tr_Ω(o) ∧ ¬Repeticion_identica(o)</code>. La <code>U</code> honesta conserva su función dentro de esta cadena. Si hay clausura circular pero no se ha declarado centro, brazo o intensidad, la conclusión formal de giro no procede: comparece <code>U_Giro^SV</code>. Si hay giro pero no se ha declarado traza, residual, retorno o conservación <em>append-only</em>, la conclusión formal de espiral no procede: comparece <code>U_Espiral^SV</code>. Si todas las condiciones están presentes, la indeterminación artificial no debe usarse para evitar el resultado. La forma de control es: <code>NoFuga_U^SV(o,Ω)=0 ⇔ [Condiciones(Espiral_AO^SV) completas ⇒ d_SV(Espiral)=1] ∧ [Condiciones incompletas ⇒ d_SV(Espiral)=U]</code>; <code>Err_NoFuga_U^SV=1 ⇔ U usada para eludir resultado formal con condiciones completas ∨ 1 usado sin Tr,Res,Ret suficientes</code>. La espiral <em>append-only</em> permite corregir la lectura del retorno en todos los niveles de la cadena. En el agua, la identidad química puede conservarse mientras cambia el estado; no hay retorno al origen, sino tránsito con memoria de régimen si el dominio lo declara. En el fuego, la extinción no borra el tránsito producido: quedan residuo, emisión, transformación o pérdida de soporte. En el volcán, la erupción no vuelve a inexistencia: deposita, inscribe y modifica frontera. En las especies, la descendencia con modificación conserva inscripción heredada <strong>y no borra lo ocurrido</strong>. Estos casos no fundan la espiral; devuelven funciones laterales que la trivialización ordena. Aplicada al dominio-universo físico realizado, la espiral se formula como reactivación de lectura, no como tiempo absoluto. Si <code>Ω_U</code> presenta clausura circular y giro, y si esa circulación de retorno conserva traza, residual y <em>append-only</em>, entonces el retorno no es una repetición perfecta del origen. La forma es: <code>Espiral_AO^SV(o_U,Ω_U)=1 ⇔ Giro(o_U,Ω_U)=1 ∧ Tr_ΩU(o_U) ∧ Res_ΩU(o_U) ∧ Ret_ΩU(o_U) ∧ React_ΩU(o_U) ∧ AppendOnly_SV ∧ ¬Repeticion_identica(o_U)</code>. La consecuencia para TODO/NADA es inmediata. Ningún observable realizado con inscripción puede ocupar el lugar de TODO/NADA. Si hay traza, hay régimen ya inscrito; si hay residual, hay no agotamiento; si hay retorno, hay lectura de dominio; si hay <em>append-only</em>, no hay borrado del tránsito. La espiral conserva, por tanto, una tesis central: el origen <code>(0,0)</code> no se recupera por repetición de lo ya realizado. Todo retorno de un observable inscrito es retorno con diferencia conservada o con residual declarado.</p><h3 id="a11-la-empiria-experiencia-en-su-dominio-exacto-observacin-medicin-registro-contraste-y-retorno"><strong>A.11. La </strong><em><strong>empiria</strong></em><strong> (experiencia) en su dominio exacto: observación, medición, registro, contraste y retorno</strong></h3><p id="n0w7neaeb5z">La empiria no se niega <strong>ni se absolutiza</strong>. <strong>Se sitúa</strong>. Observa, mide, registra, contrasta, instrumenta y devuelve magnitudes dentro del dominio que declara. Esa función es indispensable para toda transducción externa, <strong>pero no convierte una medición aislada en fundamento total de todos los dominios</strong>. La ciencia empírica habla con autoridad cuando declara objeto, magnitud, unidad, instrumento, incertidumbre, protocolo, residual y retorno. Fuera de esa cadena, su resultado no desaparece, pero tampoco puede ocupar por sí sola el lugar de criterio rector de una pregunta que se formula en otro dominio. La forma mínima de admisión empírica es: <code>Empiria(D_ext,x)=1 ⇔ Dom_ext(x) ∧ Magnitud(x) declarada ∧ Unidad(x) ∧ Instrumento(x) ∧ Protocolo(x) ∧ Incertidumbre(x) ∧ Res_ext(x) visible ∧ Ret_ext(x)</code>; <code>Err_Emp^SV=1 ⇔ Medición=fundamento_total ∨ Magnitud sin Dom_ext ∨ Incertidumbre omitida ∨ Res_ext oculto ∨ Ret_ext usado fuera de dominio ∨ traducción externa usada para cancelar definición interna sin 𝔛</code>; <code>U_Emp^SV ⇔ Dom_ext, magnitud, unidad, instrumento, incertidumbre, residual o retorno insuficientes sin contradicción</code>. La formulación respeta el método experimental. La tradición científica moderna no se funda en autoridad desnuda, sino en contraste y prueba. </p><blockquote id="nvzv7vzj0qb"><p id="nge8bazq3li">La Royal Society resume esa exigencia <strong>en el lema </strong><em><strong>Nullius in verba</strong></em>, entendido oficialmente como determinación de resistir la dominación de la autoridad y verificar afirmaciones mediante hechos determinados por experimento. Esta referencia no se introduce como adorno histórico; sitúa una disciplina: <strong>ni autoridad institucional ni preferencia semántica sustituyen dominio,  contraste y retorno</strong>. </p></blockquote><p id="nxbjegtyjk6">La empiria vale por lo que mide y por cómo lo devuelve; <strong>no por ocupar la totalidad de la verdad posible</strong>. En el marco de esta lectura, la ciencia contemporánea conserva su dominio exacto. Si se pregunta por rotación rígida cosmológica, debe devolver magnitudes propias de cosmología física. Si se pregunta por vorticidad métrica, debe declarar campo, métrica, operador y observables. Si se pregunta por anisotropía global, debe declarar el régimen estadístico y observacional correspondiente. Si se pregunta por momento angular cosmológico, debe declarar definición, unidad, inferencia y retorno. </p><blockquote id="nipn9ytj7n6"><p id="n3qilxjhgdh">Pero si le pregunta es si un dominio realizado con frontera, traza, residual, retorno, centro de lectura, brazo e intensidad <strong>presenta giro</strong> en el dominio SV, la respuesta no se obtiene por inspección empírica directa de una rotación externa, sino por conclusión formal de dominio y posterior transducción si procede. </p></blockquote><p id="n3djf8mc7vl">La regla de relación entre empiria y SV queda así términos algebráicos: <code>Rel_Emp_SV(x)=0 ⇔ Def_SV(x) declarada ∧ Dem_SV(x) ∧ 𝔛(D_SV↔D_ext) opcional o declarada ∧ Res visible ∧ Ret(D_ext) cuando se reclame magnitud externa</code>; <code>Err_Rel_Emp_SV=1 ⇔ D_ext usado para prohibir Def_SV sin transducción ∨ D_SV usado para fingir medición externa ∨ Ret_ext omitido ∨ Res oculto ∨ U usada como aceptación</code>. </p><p id="nl1qcru2jog">Esta regla evita dos errores simétricos. El primero consiste en exigir a la definición SV que nazca ya como magnitud empírica externa. El segundo consiste en presentar una tesis SV como si fuese medición externa ya realizada. La primera exigencia confunde dominio de formulación con dominio de retorno; la segunda confunde demostración interna con registro instrumental. <strong>La transducción correcta no permite ninguna de las dos cosas</strong>. Declara el dominio de salida, el dominio de llegada, el transductor, el residual, el retorno y la conclusión formal. </p><p id="n3be9rzvy5y">Por eso el corolario de transducción no confinante prepara y modula este apartado. <strong>Resolver en un dominio no confina el resultado al método si hay retorno declarado</strong>. Del mismo modo, medir en un dominio no convierte esa medición en fundamento total de otro dominio si no hay transducción. La relación correcta es doble: <code>Resolución(D_SV) --Ret,Res--&gt; Conclusión formal(D_ext)</code> cuando la pregunta externa se ha transducido al SV y vuelve al dominio interrogado. <code>Medición(D_ext) --𝔛,Res--&gt; Retorno(D_SV)</code> cuando una magnitud externa se usa como contraste de una tesis SV. Ambas flechas exigen residual visible. Sin residual, la transducción degenera en imposición. Con residual declarado, cada dominio conserva su función. </p><blockquote id="njaivria1hd"><p id="nnitt13y73p">La empiria no manda sobre el SV; el SV no suplanta la empiria. </p></blockquote><p id="n488vlfmlj9">La primera mide; el segundo tipa, demuestra y exige retorno. Si el retorno externo falta, procede <code>U</code> en ese plano; si el retorno externo contradice una traducción concreta, se corrige la transducción; si el retorno externo no pertenece al dominio de la definición interna, no puede anularla sin cambio de dominio declarado. Aplicado al giro del dominio-universo, el criterio queda establecido. </p><p id="ndafj3mka8l">La cosmología empírica puede restringir rotación rígida, vorticidad, anisotropía o momento angular cosmológico. Esa restricción pertenece a su dominio y debe conservarse. No obstante, el giro formulado en esta lectura es circulación de retorno con centro de lectura, brazo, intensidad, traza, residual y <em>append-only</em>. La traducción de ese giro a magnitud cosmológica externa exige  <code>𝔛(D_SV↔D_cosm)</code>, magnitud, unidad, residual y retorno. Sin esa traducción, lo experimental no cancela el resultado interno; devuelve límite de traducción o <code>U</code> en el dominio externo. Con traducción suficiente, el retorno externo puede refinar, acotar o refutar una formulación transducida, pero no sustituye la definición por el solo hecho de medir otra cosa. La conclusión es sobria. Lo empírico habla de lo que observa, mide, registra y contrasta. Esa palabra es necesaria y debe respetarse. Pero no ocupa por sí sola la verdad completa del régimen cuando el problema exige dominio, frontera, transducción, residual y retorno. El SV no se refugia fuera de la ciencia empírica; la recibe como retorno exacto. Tampoco se somete a un reduccionismo de medición aislada. Cada dominio responde con sus condiciones. Donde hay medición suficiente, se incorpora. Donde hay retorno insuficiente, comparece <code>U</code>. Donde el aparato interno ya ha declarado dominio y conclusión formal, la audacia demostrativa exige sostener el resultado.</p><h3 id="a12-corolario-de-transduccin-no-confinante-resolver-en-un-dominio-no-confina-el-resultado-al-mtodo"><strong>A.12. Corolario de transducción no confinante: resolver en un dominio no confina el resultado al método</strong></h3><p id="n34e85u48px">El corolario de transducción no confinante fija una regla necesaria para impedir que el cambio de dominio se confunda con una pérdida de alcance del resultado. Si una cuestión se formula en un dominio externo, se transduce a dominio SV, se resuelve allí bajo dominio, frontera, traza, residual y retorno, y después retorna al dominio interrogado, </p><blockquote id="ntub63jmqmm"><p id="ntp1lyk11tu"><strong>el resultado no queda limitado al dominio de cálculo por el solo hecho de haber atravesado ese dominio</strong>. El método no confina la verdad que transporta; </p></blockquote><p id="nvr4s35p5eo">la somete a condiciones de admisibilidad, residual y retorno. La expresión general se representa: <code>CorTransd_no_conf^SV=0 ⇔ Problema(D_ext) ∧ Dom(D_ext) ∧ 𝔛(D_ext↔D_SV) declarado ∧ Resolución(D_SV) ∧ Res(D_SV→D_ext) visible ∧ Ret(D_SV→D_ext) ∧ Conclusión formal(D_ext)</code>; <code>Err_conf_met^SV=1 ⇔ Resolución(D_SV) ∧ Ret(D_SV→D_ext) ∧ Conclusión formal(D_ext) ∧ objeción=&quot;sólo vale en D_SV&quot;</code>; <code>U_conf_met^SV ⇔ 𝔛, Res, Ret o Conclusión formal insuficientes sin contradicción</code>. </p><blockquote id="ncbais99adz"><p id="n5n9hpr8ss4">La regla se apoya en una estructura matemática elemental. En cálculo, una sustitución permite transformar una expresión compleja en otra más tratable; la variable auxiliar no se convierte en destino exclusivo del resultado. Si <code>y=f(u)</code> y <code>u=g(x)</code>, la regla de la cadena expresa <code>dy/dx=(dy/du)(du/dx)</code>. La derivada se transporta por el dominio intermedio <code>u</code> y retorna al dominio <code>x</code>. De forma análoga, una integral puede resolverse mediante sustitución y devolverse al dominio inicial al deshacer el cambio o al transformar correctamente los límites. La forma técnica la expresamos: <code>x=φ(t)</code>; <code>dy/dt=(dy/dx)(dx/dt)</code>; <code>dx/dt≠0 ⇒ dy/dx=(dy/dt)/(dx/dt)</code>. La conclusión formal no dice que <code>t</code> sea el dominio verdadero y <code>x</code> una apariencia. Dice que el paso por <code>t</code> permitió resolver una estructura que retorna a <code>x</code>. </p></blockquote><p id="n78unftqnzz">En el SV, <code>D_SV</code> cumple una función equivalente cuando actúa como dominio de resolución y no como destino exclusivo del resultado. El transductor <code>𝔛(D_ext↔D_SV)</code> ordena la cuestión, la transforma, la somete a residual y exige retorno. Si ese retorno existe, la objeción de confinamiento pierde validez formal. La formulación SV nos: <code>D_ext --𝔛--&gt; D_SV --Res,Ret--&gt; D_ext</code>; <code>Validez_retornada^SV(Q)=1 ⇔ Q∈D_ext ∧ 𝔛(Q,D_ext,D_SV) ∧ Sol_SV(Q) ∧ Res_Q visible ∧ Ret_Q(D_SV→D_ext) ∧ Conc_Q(D_ext)</code>; <code>NoConf(Q)=1 ⇔ Validez_retornada^SV(Q)=1 ∧ ¬Confinamiento(Q,D_SV)</code>. En esta notación, <code>Q</code> nombra la cuestión interrogada; <code>D_ext</code>, el dominio externo de formulación o contraste; <code>D_SV</code>, el dominio de resolución; <code>𝔛</code>, el transductor; <code>Sol_SV(Q)</code>, la resolución interna bajo aparato SV; <code>Res_Q</code>, el residual; <code>Ret_Q</code>, el retorno; y <code>Conc_Q(D_ext)</code>, la conclusión formal devuelta al dominio interrogado. Si alguna de estas condiciones falta, no se proclama validez retornada: comparece <code>U</code> o error. Pero si todas concurren, no procede afirmar que el resultado pertenece sólo al dominio auxiliar. <strong>El corolario impide una crítica recurrente contra cualquier formalismo que opere por cambio de dominio</strong>. No basta decir que una conclusión <strong>“sólo vale para el SV”</strong> si el SV ha declarado el dominio externo, ha construido el transductor, ha conservado residual y ha devuelto conclusión formal. Esa crítica confunde plano de resolución con plano de pertenencia del resultado. </p><blockquote id="nzn1gmb0wdl"><p id="n9beqrz1ua6">Del mismo modo que una derivada resuelta mediante cambio de variable no queda reducida a la variable auxiliar, una cuestión física o formal resuelta mediante transducción SV no queda excluida del dominio que la interrogó si el retorno ha sido materialmente declarado. </p></blockquote><p id="n5y0p6yhj5d">La forma negativa debe quedar igualmente explícita. El corolario no autoriza resolver cualquier cosa en cualquier dominio. Si no hay transductor, si el dominio externo se omite, si el residual desaparece del análisis, si el retorno no se formula o si la conclusión formal no vuelve al dominio interrogado, el resultado no puede presentarse como retornado. En tal caso procede <code>U</code> o error. La condición de no confinamiento exige disciplina completa: <code>NoConf_admisible^SV(Q)=1 ⇔ Dom_ext(Q) ∧ Dom_SV(Q) ∧ 𝔛(Q) ∧ Sol_SV(Q) ∧ Res_Q visible ∧ Ret_Q ∧ Conc_Q</code>; <code>Err_NoConf^SV=1 ⇔ 𝔛 omitido ∨ Dom_ext omitido ∨ Res_Q oculto ∨ Ret_Q ausente ∨ Conc_Q no devuelto ∨ Sol_SV presentada como medición externa sin transducción</code>. </p><p id="nmc0tzaiqtl">Este corolario prepara su aplicación mayor. Si la cuestión es si el dominio-universo físico realizado presenta clausura circular y giro, el SV no necesita convertir primero esos términos en esfera física o rotación rígida externa. Define dominio, frontera, traza, residual, retorno, centro, brazo, intensidad y conservación <em>append-only</em>; concluye formalmente en su dominio; y, si se reclama traducción empírica, activa transducción hacia magnitudes externas. <strong>El resultado no queda confinado al método, pero tampoco se ofusca de medición empírica no realizada</strong>.</p><h3 id="a13-error-de-confinamiento-por-dominio-auxiliar"><strong>A.13. Error de confinamiento por dominio auxiliar</strong></h3><p id="n05q7cd48pb">El error de confinamiento por dominio auxiliar aparece cuando se declara inválido un resultado sólo porque ha sido obtenido mediante transducción a otro dominio. </p><p id="ntn9j8kkw09">Su forma general consiste en confundir el medio de resolución con el lugar exclusivo de validez. <strong>Es un error distinto de la crítica empírica legítima</strong>. La crítica experimental exige magnitud, instrumento, unidad, incertidumbre y retorno dentro de un dominio externo. El confinamiento por dominio auxiliar afirma algo más débil: que atravesar <code>D_SV</code> basta para impedir que el resultado retorne a <code>D_ext</code>. La forma mínima es: <code>Err_conf_aux^SV(Q)=1 ⇔ Q∈D_ext ∧ 𝔛(D_ext↔D_SV) declarado ∧ Sol_SV(Q) ∧ Res_Q visible ∧ Ret_Q(D_SV→D_ext) ∧ Conc_Q(D_ext) ∧ Obj_conf(Q)</code>; <code>Obj_conf(Q)=&quot;sólo vale en D_SV&quot;</code>. La objeción es inválida cuando el retorno está declarado. Si no hay retorno, la crítica procede; si hay retorno, la crítica cambia de naturaleza y debe atacar el dominio, el transductor, el residual, la conclusión formal o la coherencia interna. No basta invocar que el resultado pasó por otro dominio. La forma correcta de refutación sería una de estas: <code>Ref_dom(Q)=1 ⇔ Dom_ext(Q) mal declarado ∨ Dom_SV(Q) incompatible</code>; <code>Ref_𝔛(Q)=1 ⇔ 𝔛(D_ext↔D_SV) no preserva identidad, frontera o magnitud</code>; <code>Ref_res(Q)=1 ⇔ Res_Q oculto, no acotado o contradictorio</code>; <code>Ref_ret(Q)=1 ⇔ Ret_Q no devuelve conclusión formal al dominio interrogado</code>; <code>Ref_conc(Q)=1 ⇔ Conc_Q no se sigue de Sol_SV(Q) ∧ Res_Q ∧ Ret_Q</code>. Estas vías de refutación son legítimas porque trabajan sobre estructura. En cambio, la objeción de confinamiento por dominio auxiliar detiene el resultado por su itinerario. </p><blockquote id="nodyxufpcq3"><p id="n2ux4m6ouu2">Tal detención sería equivalente a negar una derivada por haber sido resuelta mediante una sustitución admisible. Si el cambio de variable es válido y el retorno se ejecuta, el resultado pertenece al problema. </p></blockquote><p id="n034nphxibm">Del mismo modo, si la transducción SV es válida y el retorno está declarado, la conclusión formal pertenece a la cuestión interrogada. El error tiene tres formas principales. La primera es la forma local: <code>D_SV</code> se trata como recinto sin retorno. La segunda es la forma empírica totalizante: <code>D_ext</code> se declara único tribunal posible incluso cuando la pregunta no se ha formulado en sus magnitudes. La tercera es la forma mixta: se exige retorno externo para aceptar la tesis, pero se niega la validez del transductor que permitiría producir ese retorno. En fórmulación formal: <code>Err_conf_local=1 ⇔ Sol_SV(Q) ⇒ &quot;sólo D_SV&quot;, aunque Ret_Q exista</code>; <code>Err_emp_total=1 ⇔ D_ext usado como fundamento total sin 𝔛 ni Res</code>; <code>Err_mixto=1 ⇔ se exige Ret_ext(Q) ∧ se niega por principio 𝔛(D_SV↔D_ext)</code>.</p><p id="n14g4budck9"> El SV no queda exento de control por denunciar este error. A<strong>l contrario, asume una carga más fuerte</strong>: debe declarar dominios, conservar frontera, mostrar residual, formular retorno y aceptar conclusión ternaria. Si esas condiciones faltan, no procede invocar el corolario de transducción no confinante. La forma de control interno es: <code>Control_no_conf^SV(Q)=0 ⇔ Dom_ext(Q) ∧ Dom_SV(Q) ∧ 𝔛(Q) ∧ Id_Q preservada ∧ Fron_Q preservada ∧ Tr_Q ∧ Res_Q visible ∧ Ret_Q ∧ d_Q∈{0,1,U}</code>; <code>Err_control_no_conf^SV=1 ⇔ se invoca NoConf sin 𝔛 ∨ se invoca NoConf sin Ret ∨ se invoca NoConf ocultando Res ∨ se invoca NoConf para fingir medición externa</code>. La diferencia entre audacia y arbitrariedad se decide aquí. La audacia científica formula la conclusión formal cuando las condiciones están declaradas, <strong>aunque el resultado incomode a un régimen externo</strong>. La arbitrariedad salta de dominio sin transductor, oculta residual o presenta como medición lo que sólo es definición interna. La trivialización rechaza ambas debilidades: no acepta el confinamiento injustificado del SV, pero tampoco permite que el SV use su propio lenguaje para eludir retorno. Aplicado al giro, el error de confinamiento aparece cuando se afirma que, si el giro se define mediante circulación de retorno de dominio, entonces no dice nada sobre la cuestión del dominio-universo físico realizado. Esa objeción sólo sería admisible si la transducción no devolviera el resultado al dominio interrogado. Pero el retorno sí está declarado: dominio-universo físico realizado, frontera sutural, traza, residual, retorno, centro de lectura, brazo, intensidad y conservación <em>append-only</em>. La transducción externa hacia rotación rígida, vorticidad o momento angular cosmológico puede devolver residuales propios; esos residuales pertenecen a la traducción externa, no a la cancelación automática del resultado interno. La forma final es: <code>Err_conf_giro^SV=1 ⇔ Giro(o_U,Ω_U)=1 ∧ Ret_ΩU declarado ∧ Res_ΩU visible ∧ objeción=&quot;no vale porque no es rotación externa&quot;</code>. La respuesta correcta no es imponer una rotación externa, sino distinguir dominios: giro como circulación de retorno evaluada formalmente; rotación externa como magnitud física que exige transducción específica. Si se reclama esa traducción, se formula un problema distinto. Si se niega la resultado interno por no ser ya rotación externa, se comete error de confinamiento y error de plano.</p><h3 id="a14-aplicacin-al-dominio-universo-fsico-realizado-clausura-circular-y-giro"><strong>A.14. Aplicación al dominio-universo físico realizado: clausura circular y giro</strong></h3><p id="n4v2zd83cod">La aplicación al dominio-universo físico realizado reúne y compila los resultados y el análisis anterior. La tesis no afirma esfera física, globo cosmológico, rotación rígida externa ni momento angular cosmológico sin transducción. Afirma que un observable realizado con dominio, frontera, identidad, traza, residual y retorno puede comparecer como clausura circular; y que, si esa circularidad conserva centro de lectura, brazo, intensidad, momento interno de retorno y conservación <em>append-only</em>, presenta giro. La forma completa nos queda:</p><p id="n2qfzgkmpb8"> <code>CircCl_SV(o_U,Ω_U)=1 ⇔ Obs_real(o_U,Ω_U)=1 ∧ Dom(Ω_U) ∧ Fron_sut(Ω_U) ∧ Id_ΩU(o_U) ∧ Tr_ΩU(o_U) ∧ Res_ΩU(o_U) ∧ Ret_ΩU(o_U) ∧ Cl_ΩU(o_U)=1</code>; <code>Giro(o_U,Ω_U)=1 ⇔ CircCl_SV(o_U,Ω_U)=1 ∧ I_ΩU(o_U)&gt;0 ∧ Ctr_ΩU(o_U) ∧ Brazo_ΩU(o_U) ∧ MomRet_ΩU(o_U) ∧ Tr_ΩU(o_U) ∧ Res_ΩU(o_U) ∧ Ret_ΩU(o_U) ∧ AppendOnly_SV</code>; <code>Espiral_AO^SV(o_U,Ω_U)=1 ⇔ Giro(o_U,Ω_U)=1 ∧ Tr_ΩU(o_U) ∧ Res_ΩU(o_U) ∧ Ret_ΩU(o_U) ∧ React_ΩU(o_U) ∧ ¬Repeticion_identica(o_U)</code>. </p><p id="ngb0byngjmy">El primer resultado dice que el dominio-universo no se dispersa como suma inconexa cuando comparece bajo frontera sutural, traza, residual y retorno. El segundo dice que la clausura circular adquiere giro cuando posee centro de lectura, brazo, intensidad y momento interno de retorno. El tercero dice que el giro, bajo conservación <em>append-only</em>, no repite idénticamente el origen, sino que conserva inscripción. Ninguna de esas fórmulas exige traducir de inmediato el resultado a rotación rígida externa; todas exigen dominio, residual y retorno. </p><blockquote id="nym0wo3zvrb"><p id="nc3exqtilk4"><strong>El término “presenta giro” queda aquí autorizado por definición y demostración</strong>. </p></blockquote><p id="n3tsgwl5wj5">No se añade una reserva permanente porque el dominio del término ya ha sido declarado. Si se hablara de rotación física externa, harían falta magnitudes cosmológicas, modelo, observación, unidad, incertidumbre y residual externo. Si se habla de giro en esta lectura, se habla de circulación de retorno con centro, brazo, intensidad, traza, residual y conservación <em>append-only</em>. </p><p id="n93xh8qem77">La diferencia no es retirada verbal, sino precisión de dominio: <code>Giro(o_U,Ω_U)=1</code> no equivale a <code>Rot_ext(o_U)=1</code>; <code>Rot_ext(o_U)=1 ⇒ Dom_cosm ∧ Magnitud_rot ∧ Unidad ∧ Instrumento/Modelo ∧ Incertidumbre ∧ Res_ext ∧ Ret_ext</code>; <code>Giro(o_U,Ω_U)=1 ⇒ Dom_SV ∧ CircRet ∧ Ctr ∧ Brazo ∧ I&gt;0 ∧ Tr ∧ Res ∧ Ret ∧ AppendOnly_SV</code>. </p><p id="ntavc9402t9">Si se reclama traducción entre ambas formas, se activa el transductor: <code>𝔛(Giro↔Rot_ext) declarado ⇒ Res(Giro→Rot_ext) visible ∧ Ret_ext</code>. Sin esa transducción, la rotación externa no confirma ni cancela el giro. Devuelve <code>U</code> o residual en su dominio. De igual modo, el giro no debe presentarse como rotación expererimental ya medida. Cada régimen conserva su sitio: el SV concluye formalmente circulación de retorno; la ciencia experimental devuelve magnitudes cuando el problema se formula en su dominio. La clausura circular del dominio-universo tampoco se traduce como esfera física. La forma correcta es: <code>CircCl_SV(o_U,Ω_U)=1</code>, y no: <code>Esfera_ext(o_U)=1</code>. La traducción a forma, curvatura, topología u observación cosmológica exigiría dominio externo. </p><p id="nl6sd6qmtys">La ciencia empírica puede interrogar el resultado mediante sus propios criterios; esa interrogación es legítima cuando declara magnitud, instrumento, modelo e incertidumbre. Pero no puede cancelar la clausura circular por exigir que sea esfera material desde fuera, porque esa exigencia cambia el dominio del término. La objeción correcta debería atacar <code>Dom(Ω_U)</code>, <code>Fron_sut</code>, <code>Tr</code>, <code>Res</code>, <code>Ret</code> o <code>Cl_ΩU</code>; no la ausencia de esfera. </p><p id="n5lkv9u7rga">La reducción al absurdo se formula así. Supóngase que <code>o_U</code> es observable realizado de <code>Ω_U</code>, conserva frontera sutural, traza, residual y retorno, pero se niega toda clausura circular. Si no hay clausura circular, el retorno no puede operar como unidad de lectura; si el retorno no opera como unidad, el observable queda disperso; si queda disperso, no comparece como dominio-universo realizado bajo frontera y traza. La hipótesis niega la condición que presupone. Por tanto: <code>Obs_real(o_U,Ω_U)=1 ∧ Fron_sut(Ω_U) ∧ Tr_ΩU(o_U) ∧ Res_ΩU(o_U) ∧ Ret_ΩU(o_U) ⇒ CircCl_SV(o_U,Ω_U)=1</code>. Supóngase ahora que hay clausura circular, intensidad positiva, centro de lectura, brazo y momento interno de retorno, pero se niega el giro. Si no hay giro, el momento de retorno queda sin régimen; si el momento queda sin régimen, centro y brazo se vuelven accesorios no operativos; si centro y brazo no operan, la circulación de retorno queda desactivada como orientación situada. La hipótesis conserva las condiciones y niega su resultado. Por tanto: <code>CircCl_SV(o_U,Ω_U)=1 ∧ I_ΩU(o_U)&gt;0 ∧ Ctr_ΩU(o_U) ∧ Brazo_ΩU(o_U) ∧ MomRet_ΩU(o_U) ∧ Tr_ΩU(o_U) ∧ Res_ΩU(o_U) ∧ Ret_ΩU(o_U) ∧ AppendOnly_SV ⇒ Giro(o_U,Ω_U)=1</code>. La <code>U</code> honesta permanece como control. Si falta frontera sutural, si la traza no está declarada, si el residual se oculta, si el retorno no se formula, si el centro de lectura o el brazo son insuficientes, no procede conclusión formal positiva. Comparece <code>U</code>. Pero si todas las condiciones están presentes, usar <code>U</code> para evitar el resultado sería un error de cautela artificial: <code>U_ΩU^SV=1 ⇔ Fron_sut, Tr_ΩU, Res_ΩU, Ret_ΩU, Ctr_ΩU, Brazo_ΩU o MomRet_ΩU insuficientes sin contradicción</code>; <code>Err_U_ΩU^SV=1 ⇔ U usada para no declarar CircCl_SV o Giro con condiciones completas</code>.  La aplicación queda situada en su dominio exacto. </p><blockquote id="nqldqx3qmw8"><p id="ndfmyagfnts">El dominio-universo físico realizado comparece como clausura circular de observable realizado y presenta giro cuando concurren circulación de retorno, centro de lectura, brazo, intensidad, traza, residual, retorno y conservación <em>append-only</em>. </p></blockquote><p id="ncbz3k35j59">La transducción empírica hacia rotación, vorticidad, anisotropía, momento angular, forma o curvatura pertenece a otro tramo de retorno. La trivialización no la niega; la exige cuando se reclame en su propio lenguaje. Tampoco deja que esa traducción externa anule por anticipado el resultado interno. Cada dominio responde con sus magnitudes; la trivialización impide confundir método, retorno y verdad de dominio.</p><h3 id="a15-conclusin-ternaria-cundo-procede-0-cundo-procede-1-y-cundo-comparece-u"><strong>A.15. Conclusión ternaria: cuándo procede </strong><strong><code>0</code></strong><strong>, cuándo procede </strong><strong><code>1</code></strong><strong> y cuándo comparece </strong><strong><code>U</code></strong></h3><p id="nyqeg0i9u6f">La conclusión ternaria ordena la trivialización y evita que una pregunta quede reducida a una oposición binaria insuficiente. El valor <code>0</code> procede cuando el criterio declarado queda clausurado sin error, cuando una propiedad no comparece en el dominio interrogado o cuando una neutralización ha sido tipada como tal. El valor <code>1</code> procede cuando la propiedad positiva se realiza con dominio, frontera, identidad, traza, residual y retorno suficientes. El valor <code>U</code> comparece cuando no hay contradicción, pero falta alguna condición material para concluir formalmente: dominio, frontera, magnitud, transducción, residual, traza o retorno. La expresión general adopta la forma: <code>d_SV(Q)=0 ⇔ Criterio_Q resuelto ∧ Dom(Q) ∧ Fron(Q) ∧ Ret(Q) ∧ ¬Error(Q)</code>; <code>d_SV(Q)=1 ⇔ Propiedad_Q realizada ∧ Dom(Q) ∧ Fron(Q) ∧ Id(Q) ∧ Tr(Q) ∧ Res(Q) visible ∧ Ret(Q)</code>; <code>d_SV(Q)=U ⇔ Insuf(Dom,Fron,Id,Tr,Res,Ret,𝔛,Magnitud) ∧ ¬Contradiccion(Q)</code>; <code>Err_d^SV(Q)=1 ⇔ d=1 sin Dom ∨ d=0 como NADA_SV sin separación de plano ∨ d=U como confirmación ∨ d=U como negación ∨ Ret no acreditado ∨ Res oculto</code>. </p><blockquote id="nynz6gdwlxl"><p id="ni3toy20988">La conclusión formal no se decide por el prestigio del lenguaje usado para formular la pregunta, sino por la estructura que permite responderla.</p></blockquote><p id="nx9ogdacqv4"> Una pregunta empírica exige magnitud empírica si pretende respuesta empírica; una pregunta formal exige dominio formal si pretende conclusión formal formal; una pregunta transducida exige transductor, residual y retorno. La trivialización no elimina esos niveles. Los separa. Por eso <code>0</code>, <code>1</code> y <code>U</code> no son etiquetas psicológicas, sino salidas de régimen. La pregunta por la rotación física externa del universo no recibe el mismo conclusión formal que la pregunta por el giro como circulación de retorno de dominio. Confundirlas genera error de plano; relacionarlas exige transducción declarada. La regla de decisión se expresa mediante una secuencia de admisión. Primero se declara el dominio: <code>Dom(Q)</code>. Después se fija la frontera: <code>Fron(Q)</code>. A continuación se preserva identidad: <code>Id(Q)</code>. Si el régimen admite magnitudes internas, se declaran potencial e intensidad: <code>P(Q)</code> e <code>I(Q)</code>. Luego se exige traza, residual y retorno: <code>Tr(Q)</code>, <code>Res(Q)</code>, <code>Ret(Q)</code>. Sólo entonces procede conclusión formal. En forma compacta: <code>Adm_Q^SV=0 ⇔ Dom(Q) ∧ Fron(Q) ∧ Id(Q) ∧ [P(Q),I(Q) si proceden] ∧ Tr(Q) ∧ Res(Q) visible ∧ Ret(Q)</code>; <code>Adm_Q^SV=0 ∧ Propiedad_Q realizada ⇒ d_SV(Q)=1</code>; <code>Adm_Q^SV=0 ∧ Propiedad_Q no realizada bajo criterio ⇒ d_SV(Q)=0</code>; <code>Adm_Q^SV≠0 ∧ ¬Contradiccion(Q) ⇒ d_SV(Q)=U</code>. </p><p id="nelzdxqjpur">Este orden impide usar <code>U</code> como refugio favorable. Si el dominio está completo y la propiedad comparece, <code>U</code> no procede. Si el dominio está incompleto y no hay contradicción, <code>1</code> tampoco procede. La <code>U</code> honesta conserva el lugar donde la estructura todavía no alcanza conclusión formal, pero no bloquea la conclusión formal cuando la estructura ya lo permite. En el caso del dominio-universo físico realizado, si concurren frontera sutural, traza, residual, retorno, centro de lectura, brazo, intensidad, momento interno de retorno y conservación <em>append-only</em>, la conclusión formal positiva de giro procede en el dominio declarado. Si se reclama rotación externa, se formula otro dominio de pregunta y se exige transducción. La lectura ternaria también regula las vías laterales. En Ohm, gravitación, cero absoluto, agua, fuego, volcanes y especies, el SV no toma la imagen externa como fundamento. Cada vía devuelve una función tipada: restricción, separación, límite, identidad bajo estado, tránsito sostenido, frontera activa o inscripción heredada. Si la función está declarada y retorna, puede operar como contraste. Si falta dominio, residual o retorno, comparece <code>U</code>. Si se fuerza identidad material entre la vía lateral y el régimen SV, comparece error. La forma de control es: <code>Lat_Q^SV=1 ⇔ Función_transportada(Q) ∧ Dom_ext(Q) ∧ Dom_SV(Q) ∧ 𝔛(Q) ∧ Res(Q) ∧ Ret(Q)</code>; <code>d_SV(Lat_Q)=U ⇔ Lat_Q incompleto sin contradicción</code>; <code>Err_Lat_Q=1 ⇔ analogía libre ∨ identidad material forzada ∨ referencia externa como fundamento interno</code>. La conclusión ternaria, por tanto, es el instrumento que mantiene la audacia dentro de disciplina formal. Ésta consiste en concluir formalmente cuando el dominio, la frontera, la traza, el residual y el retorno lo permiten. La disciplina consiste en devolver <code>U</code> cuando esas condiciones no están presentes. La trivialización no intensifica la tesis mediante retórica; la reduce a sus condiciones suficientes. Allí donde se cumplan, la conclusión formal no debe debilitarse por deferencia externa. Allí donde falten, no debe simularse completitud.</p><h3 id="a16-corolario-mayor-de-trivializacin-rigurosa"><strong>A.16. Corolario mayor de trivialización rigurosa</strong></h3><p id="nzoi1a5orhw">Todo observable realizado que conserva dominio, frontera, identidad, traza, residual, retorno y conservación <em>append-only</em> no puede ser tratado como suma dispersa, presencia muda ni repetición del origen. </p><p id="nw5ci0a2xky">La trivialización rigurosa exige determinar si comparece clausura circular, si esa clausura adquiere giro y si el retorno conserva inscripción como espiral <em>append-only</em>. La expresión general la representamos como: <code>Obs_real(o,Ω)=1 ∧ Dom(Ω) ∧ Fron_Ω(o) ∧ Id_Ω(o) ∧ Tr_Ω(o) ∧ Res_Ω(o) ∧ Ret_Ω(o) ∧ AppendOnly_SV ⇒ CircCl_SV(o,Ω)=1 ∨ U_CircCl^SV</code>; <code>CircCl_SV(o,Ω)=1 ∧ I_Ω(o)&gt;0 ∧ Ctr_Ω(o) ∧ Brazo_Ω(o) ∧ MomRet_Ω(o) ∧ Tr_Ω(o) ∧ Res_Ω(o) ∧ Ret_Ω(o) ⇒ Giro(o,Ω)=1</code>; <code>Giro(o,Ω)=1 ∧ Tr_Ω(o) ∧ Res_Ω(o) ∧ Ret_Ω(o) ∧ React_Ω(o) ∧ AppendOnly_SV ⇒ Espiral_AO^SV(o,Ω)=1</code>. El primer tramo reconoce que un observable realizado con retorno no se agota como agregado. El segundo reconoce que la clausura circular, cuando conserva centro, brazo, intensidad y momento interno de retorno, presenta giro. El tercero reconoce que el giro, si conserva inscripción bajo <em>append-only</em>, no repite idénticamente el origen. </p><p id="nluiexpvcpc">El corolario no afirma esfera física, rotación rígida externa ni ciclo temporal. Afirma dominio, clausura circular, giro y espiral en sus condiciones propias. Si una lectura externa quiere traducir esos resultados a curvatura, topología, rotación, vorticidad, anisotropía o momento angular, debe declarar dominio externo, magnitudes, instrumentos, incertidumbre, residual y retorno. El enunciado aplicado al dominio-universo físico realizado nos queda formalmente así: </p><p id="nxebgo2ob44"><code>Obs_real(o_U,Ω_U)=1 ∧ Fron_sut(Ω_U) ∧ Id_ΩU(o_U) ∧ Tr_ΩU(o_U) ∧ Res_ΩU(o_U) ∧ Ret_ΩU(o_U) ⇒ CircCl_SV(o_U,Ω_U)=1</code>; <code>CircCl_SV(o_U,Ω_U)=1 ∧ I_ΩU(o_U)&gt;0 ∧ Ctr_ΩU(o_U) ∧ Brazo_ΩU(o_U) ∧ MomRet_ΩU(o_U) ∧ AppendOnly_SV ⇒ Giro(o_U,Ω_U)=1</code>; <code>Giro(o_U,Ω_U)=1 ∧ Tr_ΩU(o_U) ∧ Res_ΩU(o_U) ∧ Ret_ΩU(o_U) ∧ React_ΩU(o_U) ⇒ Espiral_AO^SV(o_U,Ω_U)=1</code>. </p><p id="n0pjd2kcjv4">Este corolario resuelve dos cautelas. La clausura circular no se reduce a esfera física; el giro no se reduce a rotación rígida externa. La trivialización permite decir lo que corresponde: el dominio-universo físico realizado comparece como clausura circular de observable realizado y presenta giro cuando concurren circulación de retorno, centro de lectura, brazo, intensidad, traza, residual, retorno y conservación <em>append-only</em>. La ciencia experimental conserva su papel exacto: puede medir, contrastar y traducir en su dominio; no puede cancelar una conclusión formal de dominio por sustituir la pregunta formal por otra pregunta empírica sin transducción. El corolario mayor incorpora también la transducción no confinante. </p><blockquote id="nzj4qihqu7q"><p id="nmwvx6f0q2g">Si una cuestión de la ciencia contemporánea se lleva al SV mediante transductor declarado, se resuelve bajo dominio, frontera, traza, residual y retorno, y se devuelve al dominio interrogado, <strong>el resultado no queda confinado al dominio de resolución</strong>. </p></blockquote><blockquote id="niu7xfepz4r"><p id="neyfldx3nu9">Esta regla no exime al SV de control; lo obliga a declarar la cadena completa. Pero, cuando la cadena está completa, <strong>la objeción “sólo vale dentro del SV” deja de ser refutación estructural</strong>. </p></blockquote><p id="nrogwrljxvy">La forma formal la representamos: <code>Q∈D_ext ∧ 𝔛(D_ext↔D_SV) ∧ Sol_SV(Q) ∧ Res_Q visible ∧ Ret_Q(D_SV→D_ext) ∧ Conc_Q(D_ext) ⇒ NoConf(Q)=1</code>; <code>NoConf(Q)=1 ∧ objeción=&quot;sólo vale en D_SV&quot; ⇒ Err_conf_aux^SV=1</code>. </p><p id="n82byozchzm">El corolario no sustituye la ciencia contemporánea. La obliga a conservar su propio rigor cuando reclama intervención sobre un resultado SV: dominio, magnitud, unidad, instrumento, incertidumbre, residual y retorno. Del mismo modo, obliga al SV a no presentar definición interna como medición empírica ya realizada. La relación queda equilibrada por transducción. Donde hay medición, se exige dominio empírico. Donde hay conclusión formal formal, se exige dominio SV. Donde hay paso entre ambos, se exige transductor y retorno. Donde falta cualquiera de esas condiciones, comparece <code>U</code>. Así formulado, el corolario mayor devuelve a la trivialización su sentido fuerte. La reducción a <code>1-0-U</code> no empobrece la ciencia: impide que el análisis confunda origen con neutralización, límite con Nada, restricción con ausencia, retorno con repetición, giro con rotación externa o transducción con confinamiento. La <code>U</code> honesta conserva lo no resuelto; el <code>1</code> concluye formalmente lo realizado; el <code>0</code> clausura o niega según criterio declarado. Ninguno de los tres valores opera sin dominio.</p><h3 id="a17-resultado-final-audacia-demostrativa-dominio-declarado-residual-visible-y-retorno-exigible"><strong>A.17. Resultado final: audacia demostrativa, dominio declarado, residual visible y retorno exigible</strong></h3><p id="noz8ba078nx">La cadena culmina en una regla de conducta formal: </p><blockquote id="n9taerifre9"><p id="nu0038lge35"><strong>La ciencia no se protege debilitando la conclusión formal cuando las condiciones están declaradas, ni se fortalece sustituyendo demostración por afirmación verbal</strong>. </p></blockquote><p id="noigb2ee34u">La trivialización rigurosa exige audacia demostrativa. Audacia no significa exceso; significa aceptar el resultado que se sigue de dominio, frontera, traza, residual, retorno y conclusión formal. Cuando esas condiciones faltan, procede <code>U</code>. Cuando concurren, la conclusión no debe quedar suspendida por cautela artificial ni por deferencia semántica hacia otro dominio. La línea completa puede resumirse de esta manera: <code>0</code> nombra origen, límite, neutralización, ausencia, residual nulo o clausura sólo cuando su posición formal está declarada. <code>1</code> nombra realización, presencia o conclusión formal positiva sólo cuando el dominio, la frontera, la traza, el residual y el retorno son suficientes. <code>U</code> nombra indeterminación honesta cuando falta alguna condición de conclusión formal sin contradicción; no es motor, probabilidad, causa, refugio favorable ni negación encubierta. <code>CircCl_SV</code> nombra clausura circular de observable realizado, no esfera física. <code>Giro</code> nombra circulación de retorno con centro, brazo, intensidad, traza, residual y conservación <em>append-only</em>, no rotación externa sin transducción. <code>Espiral_AO^SV</code> nombra retorno con inscripción no repetida, no ciclo temporal rector. <code>𝔛(D_ext↔D_SV)</code> nombra transducción controlada; si hay residual visible y retorno, el resultado no queda confinado al dominio de resolución. </p><p id="nvihyy28ybx">La consecuencia final para el dominio-universo físico realizado es precisa. Si comparece como observable realizado bajo frontera sutural, identidad, traza, residual y retorno, <strong>puede concluir formalmente clausura circular</strong>. Si esa clausura circular conserva intensidad, centro de lectura, brazo y momento interno de retorno, <strong>presenta giro</strong>. Si ese giro conserva inscripción bajo <em>append-only</em>, el retorno no es repetición idéntica, <strong>sino espiral</strong> de inscripción no borrada. </p><p id="nyznfmc6twm">La forma condensada en formulación lógica formal es: <code>Obs_real(o_U,Ω_U) ∧ Fron_sut ∧ Tr ∧ Res ∧ Ret ⇒ CircCl_SV(o_U,Ω_U)=1</code>; <code>CircCl_SV(o_U,Ω_U) ∧ I&gt;0 ∧ Ctr ∧ Brazo ∧ MomRet ∧ AppendOnly_SV ⇒ Giro(o_U,Ω_U)=1</code>; <code>Giro(o_U,Ω_U) ∧ Tr ∧ Res ∧ Ret ∧ React ∧ AppendOnly_SV ⇒ Espiral_AO^SV(o_U,Ω_U)=1</code>. </p><p id="nittrra58n8">La ciencia empírica conserva íntegra su autoridad dentro del dominio que declara. Observa, mide, registra, contrasta, corrige y devuelve magnitudes. Pero no ocupa el lugar de totalidad rectora de toda pregunta. Cuando se le reclama rotación externa, vorticidad, anisotropía, momento angular, curvatura o topología, debe responder con sus magnitudes y sus incertidumbres. Cuando la pregunta se formula en el SV como circulación de retorno de dominio, la conclusión formal se decide por dominio SV y sólo se traduce externamente mediante transducción declarada. <strong>Esa separación no enfrenta dominios; impide que uno usurpe el lugar del otro</strong>. El desarrollo culmina con el corolario de transducción no confinante. Resolver en un dominio no confina el resultado al método cuando hay retorno admisible. Medir en un dominio tampoco convierte esa medición en fundamento total de otro dominio si no hay transducción. La verdad de dominio se conserva por declaración, residual y retorno; no por autoridad, etiqueta o hábito semántico. </p><blockquote id="ni6ghcnibwh"><p id="n4n5n4gsz2u"><strong>Por eso el SV puede decir con voz propia que el dominio-universo físico realizado comparece como clausura circular y presenta giro </strong>en el dominio en que esos términos han sido definidos, demostrados y evaluados formalmente. </p></blockquote><p id="ns3x67sk6ow">Si se reclama traducción empírica, se activa la transducción correspondiente. Si falta dominio, residual o retorno, comparece la <code>U</code> honesta. El resultado final no es una licencia, sino una restricción más severa: ningún <code>0</code>, ningún <code>1</code> y ninguna <code>U</code> pueden pronunciarse sin dominio. Ninguna vía lateral puede adoptarse sin función transportada. Ninguna medición externa puede absolutizarse sin declarar su propio alcance. Ninguna transducción puede invocarse sin residual y retorno. Bajo esas condiciones, la trivialización no reduce la ciencia a simpleza: la devuelve a su forma más exigente, donde cada pregunta queda obligada a mostrar qué dominio declara, qué frontera respeta, qué traza conserva, qué residual devuelve y qué retorno permite.</p><h2 id="bibliografa"><strong>Bibliografía</strong></h2><p id="njbgfz1fox6">American Physical Society. (2006, junio 1). <em>Eratosthenes measures Earth</em>. <em>APS News</em>. <a href="https://www.aps.org/apsnews/2006/06/eratosthenes-measures-earth">https://www.aps.org/apsnews/2006/06/eratosthenes-measures-earth</a></p><p id="noj73l0r9wg">British Geological Survey. (s. f.). <em>Reversals: Magnetic flip</em>. <a href="https://geomag.bgs.ac.uk/education/reversals.html">https://geomag.bgs.ac.uk/education/reversals.html</a></p><p id="ntaotyxqimq">Encyclopaedia Britannica. (2026, mayo 25). <em>Galileo | Biography, discoveries, inventions, &amp; facts</em>. <a href="https://www.britannica.com/biography/Galileo-Galilei">https://www.britannica.com/biography/Galileo-Galilei</a></p><p id="ndnode8lxif">Feldman, J., Rechnitzer, A., &amp; Yeager, E. (2022). <em>1.3: Equations of lines in 2d</em>. Mathematics LibreTexts. <a href="https://math.libretexts.org/Bookshelves/Calculus/CLP-3_Multivariable_Calculus_%28Feldman_Rechnitzer_and_Yeager%29/01%3A_Vectors_and_Geometry_in_Two_and_Three_Dimensions/1.03%3A_Equations_of_Lines_in_2d">https://math.libretexts.org/Bookshelves/Calculus/CLP-3_Multivariable_Calculus_%28Feldman_Rechnitzer_and_Yeager%29/01%3A_Vectors_and_Geometry_in_Two_and_Three_Dimensions/1.03%3A_Equations_of_Lines_in_2d</a></p><p id="n9tapytrfrw">IUPAC. (2016, noviembre 30). <em>IUPAC announces the names of the elements 113, 115, 117, and 118</em>. <a href="https://iupac.org/iupac-announces-the-names-of-the-elements-113-115-117-and-118/">https://iupac.org/iupac-announces-the-names-of-the-elements-113-115-117-and-118/</a></p><p id="n65ledgnfc5">Kramida, A., Ralchenko, Y., Reader, J., &amp; NIST ASD Team. (s. f.). <em>Atomic data for helium (He)</em>. National Institute of Standards and Technology. <a href="https://physics.nist.gov/PhysRefData/Handbook/Tables/heliumtable1.htm">https://physics.nist.gov/PhysRefData/Handbook/Tables/heliumtable1.htm</a></p><p id="n4g6tdojomr">Lawrence Berkeley National Laboratory. (2024, julio 23). <em>A new way to make element 116 opens the door to heavier atoms</em>. <a href="https://newscenter.lbl.gov/2024/07/23/a-new-way-to-make-element-116-opens-the-door-to-heavier-atoms/">https://newscenter.lbl.gov/2024/07/23/a-new-way-to-make-element-116-opens-the-door-to-heavier-atoms/</a></p><p id="nukp8oy78u9">LibreTexts. (2026). <em>6.5: s-orbitals are spherically symmetric</em>. Chemistry LibreTexts. <a href="https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Physical_Chemistry_%28LibreTexts%29/06%3A_The_Hydrogen_Atom/6.05%3A_s-orbitals_are_Spherically_Symmetric">https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Physical_Chemistry_%28LibreTexts%29/06%3A_The_Hydrogen_Atom/6.05%3A_s-orbitals_are_Spherically_Symmetric</a></p><p id="n4ztbejq36v">Lloret Egea, J. A. (2026a). <em>Reducción estructural absoluta de Maxwell en el Sistema Vectorial SV y ecuación única de la física factual electromagnética --- con desarrollo algebraico del operador maestro absoluto 𝔼_SV</em>. IA eñ™ --- La Biblia de la IA™. <a href="https://doi.org/10.17613/kep1t-57539">https://doi.org/10.17613/kep1t-57539</a></p><p id="nybt15xthrk">Lloret Egea, J. A. (2026b). <em>Vida y clausura de los observables realizados: cuerpos, especies, estrellas y frontera sutural del universo observable como dominio físico realizado</em>. IA eñ™ --- La Biblia de la IA™. <a href="https://doi.org/10.21428/39829d0b.9c15d6fe">https://doi.org/10.21428/39829d0b.9c15d6fe</a></p><p id="n6idw07327o">Lloret Egea, J. A. (2026c). <em>Vida y clausura de los universos y sus observables: Humanos, especies, estrellas y dominios recursivos bajo circularidad no agotada y lectura armónica por Fourier</em>. IA eñ™ --- La Biblia de la IA™. <a href="https://doi.org/10.21428/39829d0b.b53ebe0a">https://doi.org/10.21428/39829d0b.b53ebe0a</a></p><p id="nouayhjx6rg">Lloret Egea, J. A. (2026d). <em>Génesis del hidrógeno y teoría de la persistencia energética estructural: Masa, frontera, residual e identidad física bajo compatibilidad operatoria universal</em>. IA eñ™ --- La Biblia de la IA™. <a href="https://doi.org/10.17613/qq4q9-sd847">https://doi.org/10.17613/qq4q9-sd847</a></p><p id="ni0mbdwmgoj">Lloret Egea, J. A. (2026e). <em>Catálogo de Pares Estructurales SV (CPS-SV): enlace, aleación y compatibilidad posicional desde los 118 elementos base hasta los 443 candidatos del dominio extendido</em>. IA eñ™ --- La Biblia de la IA™. <a href="https://doi.org/10.21428/39829d0b.a56b9cd7">https://doi.org/10.21428/39829d0b.a56b9cd7</a></p><p id="n4qud14wv0e">Lloret Egea, J. A. (2026f). <em>El origen material ordinario del Universo observable y la relación entre física contemporánea y el SV en el tránsito por dominios: errores de plano, contraste entre aparatos y continuidad hidrógeno-helio de la materia ordinaria</em>. IA eñ™ --- La Biblia de la IA™. <a href="https://doi.org/10.21428/39829d0b.90fce13d">https://doi.org/10.21428/39829d0b.90fce13d</a></p><p id="nbu45nmb5e1">Lloret Egea, J. A. (2026g). <em>Imperfección preformal y espacio: ε−0, primera distinguibilidad y dominio estructural completo de separación factual recorrible</em>. IA eñ™ --- La Biblia de la IA™. <a href="https://doi.org/10.21428/39829d0b.9c57c046">https://doi.org/10.21428/39829d0b.9c57c046</a></p><p id="n1e2kzlwk7l">Lloret Egea, J. A., &amp; Instituto tecnológico virtual IAeñ™. (2026h). <em>Fundamentos algebraico-semánticos del Sistema Vectorial SV: Célula exacta, representación polar, indeterminación epistémica y composición tipada</em>. IA eñ™ --- La Biblia de la IA™. <a href="https://doi.org/10.21428/39829d0b.b0cf9a13">https://doi.org/10.21428/39829d0b.b0cf9a13</a></p><p id="nwrcb6sry36">Miller, D. M. (2005). <em>Galileo Galilei</em>. En E. N. Zalta (Ed.), <em>The Stanford Encyclopedia of Philosophy</em>. Stanford University. <a href="https://plato.stanford.edu/entries/galileo/">https://plato.stanford.edu/entries/galileo/</a></p><p id="n16nb1tpjts">NASA Goddard Space Flight Center. (2020). <em>Newton&#x27;s law of universal gravitation</em>. Imagine the Universe! <a href="https://imagine.gsfc.nasa.gov/features/yba/CygX1_mass/gravity/more.html">https://imagine.gsfc.nasa.gov/features/yba/CygX1_mass/gravity/more.html</a></p><p id="nlc1ong7nym">NASA Science. (2024, noviembre 4). <em>Chapter 13: Navigation</em>. National Aeronautics and Space Administration. <a href="https://science.nasa.gov/learn/basics-of-space-flight/chapter13-1/">https://science.nasa.gov/learn/basics-of-space-flight/chapter13-1/</a></p><p id="n0k4sdqp304">NASA Science. (2025, enero 16). <em>Chapter 3: Gravity &amp; mechanics</em>. National Aeronautics and Space Administration. <a href="https://science.nasa.gov/learn/basics-of-space-flight/chapter3-2/">https://science.nasa.gov/learn/basics-of-space-flight/chapter3-2/</a></p><p id="noi9t07ygii">NIST ASD Team. (s. f.). <em>Atomic Spectra Database</em>. National Institute of Standards and Technology. <a href="https://www.nist.gov/pml/atomic-spectra-database">https://www.nist.gov/pml/atomic-spectra-database</a></p><p id="n49i2pfmzyk">NIST Chemistry WebBook. (s. f.). <em>Water</em>. National Institute of Standards and Technology. <a href="https://webbook.nist.gov/cgi/cbook.cgi?ID=C7732185">https://webbook.nist.gov/cgi/cbook.cgi?ID=C7732185</a></p><p id="nsatxe7gz05">NIST. (2024, junio 26). <em>How low can temperature go? Lord Kelvin and the science of absolute zero</em>. <a href="https://www.nist.gov/blogs/taking-measure/how-low-can-temperature-go-lord-kelvin-and-science-absolute-zero">https://www.nist.gov/blogs/taking-measure/how-low-can-temperature-go-lord-kelvin-and-science-absolute-zero</a></p><p id="n5p7v8mayk7">NOAA National Centers for Environmental Information. (s. f.). <em>Geomagnetism frequently asked questions</em>. <a href="https://www.ncei.noaa.gov/products/geomagnetism-frequently-asked-questions">https://www.ncei.noaa.gov/products/geomagnetism-frequently-asked-questions</a></p><p id="nwsc5px07lt">OpenStax. (2016a). <em>2.5 Equations of lines and planes in space</em>. En <em>Calculus Volume 3</em>. Rice University. <a href="https://openstax.org/books/calculus-volume-3/pages/2-5-equations-of-lines-and-planes-in-space">https://openstax.org/books/calculus-volume-3/pages/2-5-equations-of-lines-and-planes-in-space</a></p><p id="ntrr5oahffk">OpenStax. (2016b). <em>3.6 The chain rule</em>. En <em>Calculus Volume 1</em>. Rice University. <a href="https://openstax.org/books/calculus-volume-1/pages/3-6-the-chain-rule">https://openstax.org/books/calculus-volume-1/pages/3-6-the-chain-rule</a></p><p id="nyrajw89lkj">OpenStax. (2016c). <em>5.5 Substitution</em>. En <em>Calculus Volume 1</em>. Rice University. <a href="https://openstax.org/books/calculus-volume-1/pages/5-5-substitution">https://openstax.org/books/calculus-volume-1/pages/5-5-substitution</a></p><p id="n5q4t7i9eo5">OpenStax. (2016d). <em>9.4 Ohm&#x27;s law</em>. En <em>University Physics Volume 2</em>. Rice University. <a href="https://openstax.org/books/university-physics-volume-2/pages/9-4-ohms-law">https://openstax.org/books/university-physics-volume-2/pages/9-4-ohms-law</a></p><p id="nn74z5ynmis">OpenStax. (2016e). <em>11.5 Force and torque on a current loop</em>. En <em>University Physics Volume 2</em>. Rice University. <a href="https://openstax.org/books/university-physics-volume-2/pages/11-5-force-and-torque-on-a-current-loop">https://openstax.org/books/university-physics-volume-2/pages/11-5-force-and-torque-on-a-current-loop</a></p><p id="nnf6scs1ycf">OpenStax. (2016f). <em>16.1 Maxwell&#x27;s equations and electromagnetic waves</em>. En <em>University Physics Volume 2</em>. Rice University. <a href="https://openstax.org/books/university-physics-volume-2/pages/16-1-maxwells-equations-and-electromagnetic-waves">https://openstax.org/books/university-physics-volume-2/pages/16-1-maxwells-equations-and-electromagnetic-waves</a></p><p id="n0q7euehdme">Planck Collaboration, Aghanim, N., Akrami, Y., Ashdown, M., Aumont, J., Baccigalupi, C., Ballardini, M., Banday, A. J., Barreiro, R. B., Bartolo, N., Basak, S., Battye, R., Benabed, K., Bernard, J.-P., Bersanelli, M., Bielewicz, P., Bock, J. J., Bond, J. R., Borrill, J., ... Zonca, A. (2020). Planck 2018 results. VI. Cosmological parameters. <em>Astronomy &amp; Astrophysics, 641</em>, A6. <a href="https://doi.org/10.1051/0004-6361/201833910">https://doi.org/10.1051/0004-6361/201833910</a></p><p id="nmv33bsumq5">Planck Collaboration, Akrami, Y., Ashdown, M., Aumont, J., Baccigalupi, C., Ballardini, M., Banday, A. J., Barreiro, R. B., Bartolo, N., Basak, S., Benabed, K., Bersanelli, M., Bielewicz, P., Bock, J. J., Bond, J. R., Borrill, J., Bouchet, F. R., Boulanger, F., Bucher, M., ... Zonca, A. (2020). Planck 2018 results. VII. Isotropy and statistics of the CMB. <em>Astronomy &amp; Astrophysics, 641</em>, A7. <a href="https://doi.org/10.1051/0004-6361/201935201">https://doi.org/10.1051/0004-6361/201935201</a></p><p id="nqt20jjee14">Pyykkö, P. (2011). A suggested periodic table up to Z ≤ 172, based on Dirac--Fock calculations on atoms and ions. <em>Physical Chemistry Chemical Physics, 13</em>(1), 161--168. <a href="https://doi.org/10.1039/C0CP01575J">https://doi.org/10.1039/C0CP01575J</a></p><p id="n6zf4jovpq9">Rabin, S. (2004). <em>Nicolaus Copernicus</em>. En E. N. Zalta (Ed.), <em>The Stanford Encyclopedia of Philosophy</em>. Stanford University. <a href="https://plato.stanford.edu/entries/copernicus/">https://plato.stanford.edu/entries/copernicus/</a></p><p id="n52bczwxu5g">Royal Society. (s. f.). <em>History of the Royal Society</em>. <a href="https://royalsociety.org/about-us/who-we-are/history/">https://royalsociety.org/about-us/who-we-are/history/</a></p><p id="nzad4dwvczb">Saadeh, D., Feeney, S. M., Pontzen, A., Peiris, H. V., &amp; McEwen, J. D. (2016). How isotropic is the Universe? <em>Physical Review Letters, 117</em>(13), 131302. <a href="https://doi.org/10.1103/PhysRevLett.117.131302">https://doi.org/10.1103/PhysRevLett.117.131302</a></p><p id="njw1flxhlz2">U.S. Geological Survey. (2024, mayo 2). <em>Is it true that Earth&#x27;s magnetic field occasionally reverses its polarity?</em> <a href="https://www.usgs.gov/faqs/it-true-earths-magnetic-field-occasionally-reverses-its-polarity">https://www.usgs.gov/faqs/it-true-earths-magnetic-field-occasionally-reverses-its-polarity</a></p><p id="nb8dugpfxlq">U.S. Geological Survey. (s. f.-a). <em>About volcanoes</em>. <a href="https://www.usgs.gov/programs/VHP/about-volcanoes">https://www.usgs.gov/programs/VHP/about-volcanoes</a></p><p id="nyye2jhmyc4">U.S. Geological Survey. (s. f.-b). <em>Geomagnetism FAQs</em>. <a href="https://www.usgs.gov/programs/geomagnetism/science/faqs">https://www.usgs.gov/programs/geomagnetism/science/faqs</a></p><p id="njszhnpk1ip">U.S. Geological Survey. (s. f.-c). <em>How do volcanoes erupt?</em> <a href="https://www.usgs.gov/faqs/how-do-volcanoes-erupt">https://www.usgs.gov/faqs/how-do-volcanoes-erupt</a></p><p id="ns0r5q8fasi">University of California Museum of Paleontology. (s. f.). <em>Descent with modification</em>. Understanding Evolution. <a href="https://evolution.berkeley.edu/evolution-101/mechanisms-the-processes-of-evolution/descent-with-modification/">https://evolution.berkeley.edu/evolution-101/mechanisms-the-processes-of-evolution/descent-with-modification/</a></p><div><hr/></div><p id="n31lo5hivy9"><strong>Advertencia</strong>: Esta publicación está protegida por <strong><a href="https://www.cedro.org/english?lng=en">CEDRO</a></strong> y su aplicación en el campo de la Física, así como cualquier forma de explotación, reproducción o uso por parte de empresas, queda sujeta al copyright del autor y a los términos de la licencia indicada; la reproducción, distribución, comunicación pública o transformación de esta obra solo puede ser realizada con la autorización de sus titulares, salvo excepción prevista por la ley, y cualquier uso comercial sin autorización expresa queda prohibido y supeditado estrictamente al licenciamiento permitido.</p><p id="nnlo7ys59cr"><em><strong>Warning</strong></em><em>: This publication is protected by </em><em><strong><a href="https://www.cedro.org/english?lng=en">CEDRO</a></strong></em><em>. Its application in the field of Physics, as well as any form of exploitation, reproduction, or use by corporate entities, is strictly subject to the author&#x27;s copyright and the terms of the license indicated; any reproduction, distribution, public communication, or transformation of this work requires authorization from the rightsholders, except as provided by law, and any commercial use without express written consent is prohibited and strictly subject to permitted licensing.</em></p><p id="nm1l74oskow"><strong>URL canónica:</strong>*<a href="https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/biologia-molecular-y-medicina/linea_umbral_sv_giro_universo_atomo_formal_cadena_global/linea_umbral_sv_giro_universo_atomo_formal_cadena_global.md">https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/biologia-molecular-y-medicina/linea_umbral_sv_giro_universo_atomo_formal_cadena_global/linea_umbral_sv_giro_universo_atomo_formal_cadena_global.md</a></p><div class="pub-notes"></div></div></div></body></html>
