# Lesson Hub — Standards

A **lesson** is a complete, ready-to-teach class built on one topic. Every lesson ships as two A4 print PDFs, a **Student Pack** and a **Teacher's Guide**, built from one Python source with `src/lesson_kit.py`, and gets two cards on `index.html`.

Model lesson: `src/advanced/urban_heat_islands.py` (Advanced, B2+/C1, TOEFL iBT task types). Match its structure, tone and finish.

## Files

| What | Path |
|---|---|
| Student Pack | `<level>/<Topic_Words>_Student_Pack.pdf` |
| Teacher's Guide | `<level>/<Topic_Words>_Teacher_Guide.pdf` |
| Source | `src/<level>/<topic_words>.py` |
| Shared kit | `src/lesson_kit.py` |

Level slugs: `teens`, `basic-1`…`basic-4`, `inter-1`…`inter-4`, `advanced`, `adults` (private tutoring).

Build a lesson from the repo root: `python3 src/<level>/<topic_words>.py` (needs WeasyPrint and the DejaVu fonts).

## The kit

Lessons import `lesson_kit` and never restyle locally. The kit changes only on request, and then every lesson is rebuilt.

| Helper | Use |
|---|---|
| `header(topic, kind, pill, lede, outline=False, fields=False)` | Page header. Student Pack: black pill, `fields=True` for NAME / DATE / GROUP. Teacher's Guide, Answer Key, Scripts: `outline=True`. |
| `sec(num, title, tag)` | Worksheet / section heading with a black number badge and a letter-spaced tag. |
| `part(letter, text)` | Part heading with an outlined A/B/C badge. |
| `L(n, tall=False, short=False)` | Answer lines. `short=True` for a single tight line under a list item. |
| `nlist(items, cls="")` | Numbered list with gray bold numbers. `cls="two"` for two columns, `"tight"` for close spacing. |
| `kcard(tag, title, body)` | Bordered answer-key card. |
| `stage(title, steps)` | Teacher's Guide stage with numbered steps. |
| `build(parts, out, level, topic)` | Renders the PDF with the footer "Phil Young's English School · Level · Topic" and "n / N". |
| `ws(*parts, first=False)` | Wraps a worksheet so it starts on a new page. |
| `ex(text)` | Example line (gray serif italic, left bar); put the answer in `<b>`. |
| `wordbox(words, struck=())` | Gray rounded word box; the example word is struck through. |
| `tbl(head, rows, …)`, `pair(left, right)`, `note(title, steps)`, `kgrid(*cards)` | Tables, side-by-side blocks, numbered instruction box, side-by-side key cards. |

## Visual identity

Taken from the Review Hub PDFs (`arschul/reviews`, e.g. `inter-1/Inter_1_Test_1_Review.pdf` and its key).

- A4, WeasyPrint. DejaVu Sans for body text, DejaVu Serif for titles and examples.
- Header: thick black top rule, letter-spaced gray "PHIL YOUNG'S ENGLISH SCHOOL", serif title "Topic · Student Pack" with a level pill, gray lede line.
- Black number badges for worksheets, outlined badges for parts.
- Examples: gray serif italic, left bar, answer in bold.
- Word boxes: gray, rounded, uppercase letter-spaced words.
- Item numbers: gray and bold.
- Footer: "Phil Young's English School · Level · Topic" left, "n / N" right.

## Student Pack

- Header with NAME / DATE / GROUP, then one worksheet per stage.
- Each worksheet starts on a new page and fits on one page when possible. No worksheet spills a line or two onto a new page.
- Answer lines under every open question.
- Homework, if any, is the last worksheet.
- No answers and no scripts.

## Teacher's Guide

1. **Overview**: table of level, time, topic, skills, grammar focus and task types; then aims, materials and prep.
2. **Plan**: plan table, then numbered steps for each stage with timings.
3. **Answer Key**: bordered cards; for comprehension items, explain why the distractors are wrong.
4. **Scripts**: teacher-read texts and audio notes.

## Content rules

- American English, in spelling and word choice.
- An example (item 0) for every exercise where one fits. In choose-from-the-box exercises, add one extra word for the example and strike it through.
- Reword any ambiguous item so only one answer works. Never footnote ambiguity.
- Activities that could confuse students (note frames, debate cards, Build a Sentence) get numbered instructions and a filled example.
- Listening scripts are teacher-read and live in the Teacher's Guide, never in the Student Pack.

## Before sending a draft

- Page count of both PDFs.
- Render every page and look at it.
- No worksheet spilling onto a new page.
- Keys match the items.

## Publishing

1. PDFs and source at the paths above.
2. `index.html`: each level is a `class-section` (badge, title, file count). Each lesson gets a violet **Student Pack** card and a gold `key-card` **Teacher's Guide** card, each with a one-line meta and Open / ↓ buttons. New levels go before `<!-- LEVELS:end -->`. Edit with Python string replacement, assert each anchor is unique (`src.count(old) == 1`), then check that the HTML tags are balanced.
3. Push. Verify by comparing blob SHAs through the GitHub API.
