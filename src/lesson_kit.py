"""lesson_kit — shared look and helpers for every Lesson Hub lesson.

Visual identity follows the Review Hub PDFs (arschul/reviews): A4, WeasyPrint,
DejaVu Sans body, DejaVu Serif titles and examples, thick black top rule,
letter-spaced school label, level pill, black number badges, outlined part
badges, gray serif-italic examples, gray rounded word boxes, bordered key cards.

Lessons import this module and only call its helpers. Do not restyle a lesson
locally; change the kit (on request) and rebuild every lesson.

Core helpers: header, sec, part, L, kcard, nlist, stage, build.
Extras used by lessons: ex, wordbox, tbl, note, kgrid, cols, pagebreak, esc.
"""
from html import escape as _esc
from pathlib import Path

SCHOOL = "Phil Young's English School"

CSS = r"""
@page {
  size: A4;
  margin: 20mm 17mm 18mm 17mm;
  @bottom-left  { content: string(foot); font: 6.6pt 'DejaVu Sans'; color: #9a9a9a; }
  @bottom-right { content: counter(page) " / " counter(pages); font: 6.6pt 'DejaVu Sans'; color: #9a9a9a; }
}
html { string-set: foot attr(data-foot); }
* { box-sizing: border-box; }
body { font-family: 'DejaVu Sans', sans-serif; font-size: 8.7pt; line-height: 1.42;
       color: #111; margin: 0; }
p { margin: 0 0 5pt; }
b, strong { font-weight: bold; }

/* ── page header ── */
.hdr { border-top: 3.2pt solid #000; padding-top: 9pt; margin-bottom: 10pt; }
.hdr .school { font-size: 6.4pt; font-weight: bold; letter-spacing: 2.6pt;
               text-transform: uppercase; color: #8a8a8a; margin-bottom: 3pt; }
.hdr .row { display: flex; align-items: center; }
.hdr h1 { font-family: 'DejaVu Serif', serif; font-weight: bold; font-size: 15.6pt;
          margin: 0; letter-spacing: -0.1pt; flex: 1; white-space: nowrap; }
.pill { font-size: 6.4pt; font-weight: bold; letter-spacing: 2pt; text-transform: uppercase;
        padding: 3pt 13pt; border-radius: 20pt; background: #000; color: #fff;
        border: 1.6pt solid #000; white-space: nowrap; }
.pill.outline { background: #fff; color: #000; border-width: 2.2pt; }
.hdr .lede { color: #7a7a7a; font-size: 8.2pt; margin: 6pt 0 0; }
.fields { display: flex; gap: 9pt; margin-top: 11pt; }
.fields div { border-bottom: 0.8pt solid #9a9a9a; height: 26pt; font-size: 6pt;
              font-weight: bold; letter-spacing: 2pt; color: #7a7a7a; }
.fields .f-name { flex: 2.75; } .fields .f-date, .fields .f-group { flex: 1; }

/* ── worksheet / section heading ── */
.ws { page-break-before: always; }
.ws.first { page-break-before: auto; }
.sec { display: flex; align-items: center; border-bottom: 0.7pt solid #c8c8c8;
       padding-bottom: 5pt; margin: 4pt 0 9pt; page-break-after: avoid; }
.sec .num { display: inline-block; min-width: 12.5pt; height: 12.5pt; line-height: 12.5pt;
            background: #000; color: #fff; font-weight: bold; font-size: 7.6pt;
            text-align: center; border-radius: 2pt; margin-right: 6pt; padding: 0 2pt; }
.sec .ttl { font-weight: bold; font-size: 9.6pt; }
.sec .tag { margin-left: auto; font-size: 5.8pt; font-weight: bold; letter-spacing: 2pt;
            text-transform: uppercase; color: #8a8a8a; }
.sub { font-weight: bold; font-size: 9pt; margin: 10pt 0 5pt; page-break-after: avoid; }

/* ── parts ── */
.part { font-weight: bold; font-size: 8.6pt; margin: 10pt 0 6pt; page-break-after: avoid; }
.part .pb { display: inline-block; min-width: 10.5pt; height: 10.5pt; line-height: 9.2pt;
            border: 1.1pt solid #000; border-radius: 2.4pt; font-size: 6.6pt; text-align: center;
            margin-right: 4pt; vertical-align: 1pt; padding: 0 1pt; }
.part .plain { font-weight: normal; }

/* ── examples, word boxes, notes ── */
.ex { font-family: 'DejaVu Serif', serif; font-style: italic; color: #8a8a8a;
      border-left: 2.6pt solid #cfcfcf; padding: 1pt 0 1pt 8pt; margin: 6pt 0 8pt; }
.ex b { color: #000; }
.wordbox { background: #f0f0f0; border: 0.7pt solid #cfcfcf; border-radius: 5pt;
           padding: 6pt 10pt; text-align: center; font-weight: bold; letter-spacing: 1.8pt;
           text-transform: uppercase; font-size: 7.6pt; line-height: 1.6; margin: 6pt 0 8pt; }
.wordbox s { color: #9a9a9a; font-weight: bold; }
.note { background: #f3f3f3; border: 0.7pt solid #dcdcdc; border-radius: 5pt;
        padding: 6pt 9pt; margin: 5pt 0 8pt; }
.note .nt { font-weight: bold; margin-bottom: 2pt; }
.note ol { margin: 0; padding-left: 13pt; }
.bar { border-left: 2.6pt solid #000; padding: 1pt 0 1pt 8pt; margin: 6pt 0 8pt; }
.bar.soft { border-left-color: #cfcfcf; }
.muted { color: #8a8a8a; }
.small { font-size: 6.6pt; }
.serif { font-family: 'DejaVu Serif', serif; }

/* ── numbered lists ── */
.nl { margin: 4pt 0 6pt; padding: 0; list-style: none; }
.nl > li { display: flex; margin: 0 0 3pt; page-break-inside: avoid; }
.nl .n { flex: 0 0 15pt; color: #8a8a8a; font-weight: bold; }
.nl .b { flex: 1; }
.nl.tight > li { margin-bottom: 1.5pt; }
.nl.two { column-count: 2; column-gap: 14pt; }
.nl.two > li { break-inside: avoid; }
.opts { margin-top: 1pt; }

/* ── answer lines ── */
.lines { margin: 1pt 0 4pt; }
.lines div { border-bottom: 0.7pt solid #8a8a8a; height: 15pt; }
.lines.tall div { height: 17pt; }
.lines.short { margin: 0 0 2pt; }
.lines.short div { height: 11.5pt; }
.inline-line { display: inline-block; border-bottom: 0.7pt solid #8a8a8a; min-width: 140pt; }

/* ── tables ── */
table.t { width: 100%; border-collapse: collapse; margin: 5pt 0 8pt; font-size: 7.6pt; }
table.t th { background: #f0f0f0; text-align: left; font-size: 5.8pt; font-weight: bold;
             letter-spacing: 1.6pt; text-transform: uppercase; padding: 4pt 6pt;
             border: 0.6pt solid #c8c8c8; }
table.t td { border: 0.6pt solid #c8c8c8; padding: 4pt 6pt; vertical-align: top; }
table.t td.n { color: #8a8a8a; font-weight: bold; }
table.t td.ex { font-family: 'DejaVu Serif', serif; font-style: italic; color: #8a8a8a;
                border-left: 0.6pt solid #c8c8c8; padding: 4pt 6pt; margin: 0; }
table.t.tall td { height: 28pt; }
table.pair { width: 100%; border-collapse: collapse; }
table.pair > tbody > tr > td { vertical-align: top; padding: 0; }
table.pair > tbody > tr > td.gap { width: 10pt; }

/* ── key cards ── */
.kgrid { display: flex; gap: 8pt; align-items: flex-start; margin-bottom: 8pt; }
.kgrid > .kcard { flex: 1; margin-bottom: 0; }
.kcard { border: 0.8pt solid #c8c8c8; border-radius: 5pt; padding: 7pt 10pt 6pt;
         margin-bottom: 8pt; page-break-inside: avoid; }
.kcard .kh { font-size: 5.8pt; font-weight: bold; letter-spacing: 2pt; text-transform: uppercase;
             color: #8a8a8a; margin-bottom: 4pt; }
.kcard .kh .kb { display: inline-block; background: #000; color: #fff; letter-spacing: 0;
                 border-radius: 2pt; padding: 0 2.5pt; margin-right: 4pt; font-size: 6.4pt; }
.kcard .nl { margin: 0; }
.kcard .nl > li { margin-bottom: 1.5pt; }
.kcard .why { color: #8a8a8a; font-size: 6.8pt; margin-top: 4pt; }
.kcard table.t { margin: 2pt 0 2pt; }

/* ── role cards ── */
.cards { display: flex; flex-wrap: wrap; gap: 6pt; }
.card { width: calc(50% - 3pt); border: 0.8pt dashed #8a8a8a; border-radius: 3pt;
        padding: 6pt 8pt; page-break-inside: avoid; font-size: 7.4pt; }
.card.solid { border: 1.2pt solid #000; }
.card .role { font-size: 5.6pt; font-weight: bold; letter-spacing: 2pt; color: #8a8a8a; }
.card .cn { font-family: 'DejaVu Serif', serif; font-weight: bold; font-size: 8.6pt; margin: 1pt 0 3pt; }
.card p { margin: 0 0 2pt; }

/* ── teacher's guide ── */
.stage { margin: 8pt 0 6pt; page-break-inside: avoid; }
.stage .sh { font-weight: bold; font-size: 8.6pt; margin-bottom: 3pt; }
.stage ol { margin: 0; padding-left: 13pt; }
.stage li { margin-bottom: 2pt; }
.block { font-weight: bold; font-size: 9.6pt; margin: 4pt 0 6pt; }
.checks { display: flex; gap: 20pt; }
.checks div { flex: 1; }
.cols2 { column-count: 2; column-gap: 14pt; }
"""


def esc(s):
    return _esc(str(s), quote=False)


# ── core helpers ──────────────────────────────────────────────────────────────

def header(topic, kind, pill, lede, outline=False, fields=False):
    """Page header. kind = 'Student Pack', "Teacher's Guide", 'Answer Key', 'Scripts'.
    Student Pack uses a black pill; teacher documents use outline=True."""
    f = ""
    if fields:
        f = ('<div class="fields"><div class="f-name">NAME</div>'
             '<div class="f-date">DATE</div><div class="f-group">GROUP</div></div>')
    return (f'<div class="hdr"><div class="school">{esc(SCHOOL)}</div>'
            f'<div class="row"><h1>{topic} · {kind}</h1>'
            f'<span class="pill{" outline" if outline else ""}">{pill}</span></div>'
            f'<p class="lede">{lede}</p>{f}</div>')


def sec(num, title, tag=""):
    """Worksheet or section heading: black badge, bold title, letter-spaced tag right."""
    return (f'<div class="sec"><span class="num">{num}</span>'
            f'<span class="ttl">{title}</span><span class="tag">{tag}</span></div>')


def part(letter, text):
    """Part heading with an outlined letter badge."""
    return f'<div class="part"><span class="pb">{letter}</span>{text}</div>'


def L(n=2, tall=False, short=False):
    """n answer lines. short=True: one tight line right under a list item (rewrites, Build a Sentence)."""
    c = " tall" if tall else (" short" if short else "")
    return f'<div class="lines{c}">' + "<div></div>" * n + "</div>"


def nlist(items, start=1, cls="", fmt="{}."):
    """Numbered list with gray bold numbers. items: html strings (may contain L())."""
    out = [f'<ol class="nl {cls}">']
    for i, it in enumerate(items, start):
        out.append(f'<li><span class="n">{fmt.format(i)}</span><span class="b">{it}</span></li>')
    out.append("</ol>")
    return "".join(out)


def kcard(tag, title, body, cls=""):
    """Bordered answer-key card: black tag badge + letter-spaced gray title."""
    return (f'<div class="kcard {cls}"><div class="kh"><span class="kb">{tag}</span>{title}</div>'
            f'{body}</div>')


def stage(title, steps):
    """Teacher's Guide stage: bold title + numbered steps."""
    lis = "".join(f"<li>{s}</li>" for s in steps)
    return f'<div class="stage"><div class="sh">{title}</div><ol>{lis}</ol></div>'


def build(body_parts, out, level, topic):
    """Render a list of html parts (or a single string) to a PDF at `out`."""
    from weasyprint import HTML
    body = body_parts if isinstance(body_parts, str) else "".join(body_parts)
    foot = esc(f"{SCHOOL} · {level} · {topic}")
    html = (f'<!doctype html><html data-foot="{foot}"><head><meta charset="utf-8">'
            f'<style>{CSS}</style></head><body>{body}</body></html>')
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    HTML(string=html).write_pdf(out)
    return out


# ── extras ───────────────────────────────────────────────────────────────────

def ws(*parts, first=False):
    """Wrap a worksheet so it starts on a new page."""
    return f'<div class="ws{" first" if first else ""}">' + "".join(parts) + "</div>"


def ex(text):
    """Example line: gray serif italic, left bar. Put the answer in <b>."""
    return f'<div class="ex">{text}</div>'


def wordbox(words, struck=()):
    """Gray rounded word box; words in `struck` are struck through (used in the example)."""
    w = [f"<s>{esc(x)}</s>" if x in struck else esc(x) for x in words]
    return '<div class="wordbox">' + " · ".join(w) + "</div>"


def tbl(head, rows, cls="", widths=None, numcol=False):
    """Simple bordered table. rows: lists of html cells. numcol grays the first column."""
    cg = ""
    if widths:
        cg = "<colgroup>" + "".join(f'<col style="width:{w}">' for w in widths) + "</colgroup>"
    th = "".join(f"<th>{h}</th>" for h in head)
    trs = []
    for r in rows:
        tds = []
        for j, c in enumerate(r):
            k = ' class="n"' if numcol and j == 0 else ""
            if isinstance(c, tuple):
                c, k = c[0], f' class="{c[1]}"'
            tds.append(f"<td{k}>{c}</td>")
        trs.append("<tr>" + "".join(tds) + "</tr>")
    return f'<table class="t {cls}">{cg}<thead><tr>{th}</tr></thead><tbody>{"".join(trs)}</tbody></table>'


def note(title, steps):
    """Gray instruction box with numbered steps."""
    lis = "".join(f"<li>{s}</li>" for s in steps)
    return f'<div class="note"><div class="nt">{title}</div><ol>{lis}</ol></div>'


def kgrid(*cards):
    """Place key cards side by side."""
    return '<div class="kgrid">' + "".join(cards) + "</div>"


def pair(left, right, split=("44%", "56%")):
    """Two blocks side by side (e.g. word table + definition table)."""
    return (f'<table class="pair"><tr><td style="width:{split[0]}">{left}</td><td class="gap"></td>'
            f'<td style="width:{split[1]}">{right}</td></tr></table>')


def pagebreak():
    return '<div style="page-break-before:always"></div>'
