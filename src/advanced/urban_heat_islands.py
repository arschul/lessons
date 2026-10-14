"""Urban Heat Islands — Advanced (B2+/C1) TOEFL lesson.

Builds:
  advanced/Urban_Heat_Islands_Student_Pack.pdf
  advanced/Urban_Heat_Islands_Teacher_Guide.pdf

Run from the repo root:  python3 src/advanced/urban_heat_islands.py
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
from lesson_kit import (header, sec, part, L, kcard, nlist, stage, build,
                        ws, ex, wordbox, tbl, note, kgrid, pair)

LEVEL, TOPIC, PILL = "Advanced", "Urban Heat Islands", "B2+ / C1"
SLUG = "Urban_Heat_Islands"

# ═════════════════════════════ STUDENT PACK ═════════════════════════════════

# 1 — Interview warm-up
interview_qs = [
    "Describe the hottest place you have ever lived or visited. How did people cope with the heat?",
    "Some people say cities should use public space for parks; others say it should be used for housing. "
    "Which do you think is more important, and why?",
    "How has your neighborhood changed in the last ten years? Has it become more or less pleasant to live in?",
    "Do you think your city does enough to protect people during heat waves? What could it do better?",
    "If you could change one thing about the streets or buildings in your city to make summer more "
    "comfortable, what would it be? Why?",
]
ws1 = ws(
    header(TOPIC, "Student Pack", PILL,
           "Advanced TOEFL lesson — speaking, vocabulary, listening, grammar and writing.", fields=True),
    sec(1, "Interview warm-up", "Speaking · Pairs"),
    "<p>Answer each question for about 45 seconds. No preparation time. After speaking, write a few key "
    "words or a short answer in the space.</p>",
    nlist([q + L(3) for q in interview_qs]),
    '<p style="margin-top:8pt"><b>While your partner speaks, write:</b></p>',
    "<p>One strong phrase they used:</p>", L(1),
    "<p>One moment they hesitated or repeated themselves:</p>", L(1),
    first=True,
)

# 2 — Topic vocabulary
VOCAB = [  # (word as shown, definition letter)
    ("absorb (heat)", "e"), ("impervious (surface)", "b"), ("canopy cover", "j"), ("mitigate", "h"),
    ("disproportionately", "g"), ("albedo", "f"), ("retrofit", "d"), ("exacerbate", "a"),
    ("vulnerable (populations)", "i"), ("cost-effective", "c"),
]
DEFS = {
    "a": "to make a problem worse",
    "b": "not allowing water to pass through",
    "c": "giving good results for the money spent",
    "d": "to add new parts or technology to an existing building",
    "e": "to take in and hold energy or liquid",
    "f": "how much light a surface reflects",
    "g": "to an unfairly or unusually large degree",
    "h": "to reduce how serious or harmful something is",
    "i": "easily harmed or affected",
    "j": "the area of ground shaded by tree leaves and branches",
}
BOX = ["absorb", "impervious", "canopy cover", "mitigate", "disproportionately",
       "albedo", "retrofit", "exacerbate", "vulnerable", "cost-effective"]
PARA_KEY = ["impervious", "absorb", "canopy cover", "exacerbate", "disproportionately",
            "vulnerable", "mitigate", "cost-effective", "retrofit"]
G = '<b>{}.</b> _____________'
para = (
    "In many cities, summer heat is becoming a serious problem. Asphalt and concrete are {1} surfaces, "
    "so rain cannot soak into them, and they {2} heat from the sun all day long. Neighborhoods with "
    "little {3} get almost no shade from trees. Waste heat from air conditioners can {4} the problem, "
    "making hot streets even hotter. Unfortunately, heat does not affect everyone equally: it affects "
    "the elderly and outdoor workers {5}, because these groups are especially {6}. So how can cities "
    "{7} the effect? Painting roofs white is a {8} solution, because it is cheap and quick. Green roofs "
    "also work well, but it can be expensive to {9} older buildings so that they can carry the extra weight."
)
for i in range(1, 10):
    para = para.replace("{%d}" % i, G.format(i))

ws2 = ws(
    sec(2, "Topic vocabulary", "Vocabulary · Reading"),
    part("A", "Match each word (1–10) to its definition (a–j)."),
    pair(tbl(["#", "Word", "Answer"], [[f"{i}.", w, ""] for i, (w, _) in enumerate(VOCAB, 1)],
             cls="tall", widths=["14%", "62%", "24%"], numcol=True),
         tbl(["", "Definition"], [[k, v] for k, v in DEFS.items()],
             cls="tall", widths=["12%", "88%"], numcol=True)),
    part("B", "Complete the paragraph with the words from Part A."),
    wordbox(BOX, struck={"albedo"}),
    ex("Example: Dark roofs have a low <b>albedo</b>, so they reflect very little sunlight."),
    f'<p style="text-align:justify;line-height:2.35">{para}</p>',
)

# 3 — Academic lecture (notes) + questions
frame_rows = [["Cause 1", "", ""], ["Cause 2", "", ""], ["Cause 3", "", ""], ["Who is affected", "", ""],
              ["Solution 1", "", ""], ["Solution 2", "", ""], ["Solution 3", "", ""],
              ["Professor's conclusion", "", ""]]
ex_row = [("Example:<br>Definition", "ex"), ("city ↑ warmer than countryside around it", "ex"),
          ("few °C on avg.; up to ~10 °C on calm, clear nights", "ex")]
ws3 = ws(
    sec(3, "Academic lecture", "Listening · Note-taking"),
    part("A", "Before you listen. What do you think makes cities hotter than the countryside? Write two ideas."),
    nlist([L(1), L(1)]),
    part("B", "First listening. Write the main idea of the lecture in one sentence."),
    L(2),
    part("C", "Second listening. Complete the note frame."),
    note("How to take notes", [
        "The lecture follows the order of the rows below: first a definition, then three causes, who is "
        "affected, three solutions and the conclusion.",
        "In <b>Claim</b>, write the professor's main point for that section in 2–5 words.",
        "In <b>Evidence / example</b>, write one fact, number or example she gives to support it.",
        "Write notes, not sentences. Abbreviations and symbols (↑, ↓, →, =, ~) are fine.",
    ]),
    tbl(["Section", "Claim", "Evidence / example"], [ex_row] + frame_rows,
        cls="tall frame", widths=["20%", "32%", "48%"]),
)

QS = [
    ("What is the lecture mainly about?",
     ["Why rural areas are cooling faster than cities",
      "The causes and effects of urban heat islands and ways to reduce them",
      "The history of air conditioning in large cities",
      "Why green roofs are the best solution to urban heat"]),
    ("According to the professor, when is the temperature difference between cities and the countryside "
     "often largest?", ["In the early afternoon", "On windy days", "At night", "In the winter"]),
    ("What does the professor say impervious surfaces are?",
     ["Surfaces that reflect most sunlight", "Surfaces that water cannot soak into",
      "Surfaces covered with plants", "Surfaces that cool down quickly"]),
    ("According to the professor, why do cities often stay warm after sunset?",
     ["Air conditioners are used more at night.", "Trees release warm water vapor at night.",
      "Wind carries warm air in from the countryside.",
      "Dark surfaces slowly release heat they absorbed during the day."]),
    ("Why does the professor mention sweating?",
     ["To explain how plants cool the air through evaporation",
      "To describe the health effects of heat on outdoor workers",
      "To recommend that people drink more water in summer",
      "To show that humans adapt to heat better than plants"]),
    ('Why does the professor describe an "ironic loop"?',
     ["Factories produce goods that make cities hotter.",
      "Hotter cities lead to more air conditioning, which makes them hotter still.",
      "Trees need water, but cities have less rain.",
      "Cool roofs reflect heat back onto the roofs themselves."]),
    ("Which group does the professor NOT mention as especially affected by urban heat?",
     ["The elderly", "Outdoor workers", "People without air conditioning", "Young children"]),
    ("What can be inferred about lower-income neighborhoods?",
     ["They use more air conditioning than wealthier areas.",
      "Their surfaces have a higher albedo than other areas.",
      "Planting more trees there could reduce heat-related health risks.",
      "They are usually located far from the city center."]),
    ("What drawback of green roofs does the professor mention?",
     ["They can reflect heat onto pedestrians.", "They take years to grow.",
      "Older buildings may need to be retrofitted to support them.", "They increase the risk of flooding."]),
    ("What is the professor's attitude toward the three strategies?",
     ["She is confident that cool roofs alone can solve the problem.",
      "She thinks each has limitations and that cities need a combination.",
      "She doubts that any of them reduces temperatures.",
      "She prefers green roofs, whatever the cost."]),
]
KEY_3D = ["b", "c", "b", "d", "a", "b", "d", "c", "c", "b"]


def mc(q, opts):
    o = "<br>".join(f"{l}. {t}" for l, t in zip("abcd", opts))
    return f'{q}<div class="opts">{o}</div>'


ws3q = ws(
    sec(3, "Academic lecture — questions", "Listening"),
    part("D", "Use your notes only. Circle the best answer (a, b, c or d)."),
    nlist([mc(q, o) for q, o in QS], cls="two"),
)

# 4 — City council debate
CARDS = [
    ("Advocate", "Trees and parks",
     "trees cool the street where people walk, provide shade, clean the air, and are very popular with voters.",
     "trees take many years to grow, need space in crowded streets, and need water during droughts."),
    ("Advocate", "Cool roofs",
     "painting roofs white or using reflective materials is cheap and fast, and helps people in buildings "
     "without air conditioning.",
     "reflective surfaces can bounce heat and glare onto pedestrians, and the benefit is less visible to voters."),
    ("Advocate", "Green roofs",
     "they cool buildings, absorb rainwater, reduce flooding, and support wildlife.",
     "they are expensive to install and maintain, and older buildings may need to be retrofitted to support "
     "the weight."),
    ("Advocate", "Cool pavements",
     "light-colored or water-permeable coatings on roads, sidewalks and parking lots cool the ground right "
     "where people walk, and can be added during normal road repairs.",
     "coatings wear off under heavy traffic and must be reapplied, they can cause glare for drivers, and "
     "there is less research on them than on trees."),
    ("Advocate", "Cooling centers and heat alerts",
     "air-conditioned public spaces (libraries, community centers) and text-message warnings protect "
     "vulnerable people immediately, and they use buildings the city already has.",
     "they treat the symptoms, not the cause; people must travel to reach them; and they do not make the "
     "city any cooler."),
]
cards_html = "".join(
    f'<div class="card"><div class="role">{r.upper()}</div><div class="cn">{n}</div>'
    f"<p><b>Your strengths:</b> {s}</p><p><b>Expect criticism:</b> {c}</p></div>"
    for r, n, s, c in CARDS
) + ('<div class="card solid"><div class="role">CHAIR</div><div class="cn">Council Chair</div>'
     "<p><b>Your job:</b> give each advocate 1 minute, then ask hard questions: How quickly will we see "
     "results? Who benefits most? What happens if it fails?</p>"
     "<p>At the end, choose ONE option and explain your decision in 30 seconds.</p></div>")
ws4 = ws(
    sec(4, "City council debate", "Speaking · Groups"),
    part("A", "60-second summary."),
    "<p>Plan for 1 minute using your notes, then summarize the lecture to your partner. Cover: what an "
    "urban heat island is, two causes, who is most affected, and the professor's conclusion.</p>",
    part("B", "Role cards."),
    '<div class="bar"><b>The situation.</b> Your city has budget for ONE heat-reduction program in the '
    "next five years. The council meets today.</div>",
    '<p class="muted small">✂ Cut along the dashed lines. One card per student.</p>',
    f'<div class="cards">{cards_html}</div>',
    '<div class="note" style="margin-top:8pt"><div class="nt small" style="letter-spacing:2pt">USEFUL LANGUAGE</div>'
    '<span class="serif" style="font-style:italic">The main advantage is that… / While it\'s true that…, … / '
    "I'd argue that… / That's a fair point, but… / In the long run…</span></div>",
)

# 5 — Hedging and concession
DISCOVERY = [
    "That's largely why cities stay warm after sunset.",
    "Lower-income neighborhoods tend to be hotter than wealthier ones.",
    "Increasing canopy cover is probably the most popular approach. The downside is that trees take years to grow.",
    "Some studies suggest cool roofs can noticeably reduce indoor temperatures.",
    "Although green roofs cool buildings and absorb rainwater, they're more expensive to install.",
    "Reflective surfaces can sometimes bounce heat onto pedestrians.",
]
REWRITE = [
    "Trees solve the urban heat problem.",
    "Cool roofs always reduce temperatures.",
    "Poor neighborhoods are hotter than rich ones.",
    "Green roofs are too expensive for any city.",
    "Air conditioning causes urban heat islands.",
    "Cities will be 10 degrees hotter by 2050.",
]
BUILD = [
    "tend to / neighborhoods / hotter / lower-income / be",
    "suggest / some studies / that / cool roofs / reduce / can / indoor temperatures",
    "although / expensive / green roofs / are / they absorb rainwater",
    "is / probably / tree planting / the most popular / approach",
    "that / the downside / is / trees / take years / to grow",
]
ws5 = ws(
    sec(5, "Hedging and concession", "Grammar"),
    part("A", "Discovery. Underline the words that make each statement less absolute or that admit a weakness."),
    ex("Example: On average, the difference <b>may be</b> just a few degrees."),
    nlist(DISCOVERY, cls="tight"),
    tbl(["Hedges (less certain)", "Concession (admitting the other side)"], [
        ["tend to, probably, likely", "although / even though + clause"],
        ["may, might, could, can sometimes", "while it's true that…"],
        ["some studies suggest / research indicates", "admittedly, …"],
        ["largely, to some extent, in many cases", "the downside is that…"],
        ["it could be argued that…", "despite + noun / -ing"],
    ], widths=["50%", "50%"]),
    part("B", "Rewrite these overconfident claims in academic style. Use a different hedge each time."),
    ex("Example: Trees always cool the street. → Trees <b>can often</b> cool the street."),
    nlist([c + L(1, short=True) for c in REWRITE]),
    part("C", "Build a Sentence. Put the chunks in the correct order. Add punctuation."),
    ex("Example: stay / cities / tend to / warm at night → <b>Cities tend to stay warm at night.</b>"),
    nlist([b + L(1, short=True) for b in BUILD]),
)

# 6 — Academic Discussion post
CHECKS_L = ["States a clear position early", "Adds a new idea, not a repeat of Maya or Lucas",
            "Supports it with a reason and a specific example", "Uses at least two hedges (underline them)"]
CHECKS_R = ["Uses at least one concession", "Uses at least two words from Worksheet 2", "100 words or more"]
ws6 = ws(
    sec(6, "Academic Discussion post", "Writing · 10 min"),
    "<p><b>Time: 10 minutes. Minimum: 100 words.</b> Use at least two hedges and one concession.</p>",
    '<div class="bar"><b>Professor Alvarez:</b> Many cities are considering laws that would require cool '
    "roofs or green roofs on all new buildings. Supporters say this is the most effective way to fight urban "
    "heat. Critics say the money would be better spent elsewhere, for example on planting street trees. What "
    "do you think? Why?</div>",
    '<div class="bar soft"><b>Maya:</b> I support the roof requirement. New buildings are the cheapest place '
    "to add these features, because you don't have to retrofit anything. Over time, every new rooftop adds "
    "up, and the whole city benefits.</div>",
    '<div class="bar soft"><b>Lucas:</b> I disagree. Roofs mainly help the people inside the building. Heat '
    "is most dangerous at street level, for people waiting for buses or working outside. Street trees "
    "protect those people directly, so I think they are a better investment.</div>",
    '<p style="margin-top:8pt"><b>Your response:</b></p>', L(13),
    part("✓", "Peer review checklist. Tick each box for your partner's post."),
    '<div class="checks"><div>' + "<br>".join("☐ " + c for c in CHECKS_L) + "</div><div>"
    + "<br>".join("☐ " + c for c in CHECKS_R) + "</div></div>",
    '<p style="margin-top:8pt">One thing your partner did well:</p>', L(1),
    "<p>One thing to improve:</p>", L(1),
)

# 7 — Homework
ws7 = ws(
    sec(7, "Homework — Write an Email", "About 120 words"),
    '<div class="bar">Your city council is asking residents for ideas to reduce summer heat. Write an email '
    "to Councilor Ribeiro. In your email:"
    '<ul style="margin:2pt 0 0;padding-left:14pt">'
    "<li>describe a place in your neighborhood that gets uncomfortably hot</li>"
    "<li>propose ONE solution from today's lesson</li>"
    "<li>explain why it would be cost-effective for that location</li></ul></div>",
    "<p>Use a polite, formal register, at least one hedge and two words from Worksheet 2.</p>",
    '<p style="margin-top:6pt"><b>To:</b> <span class="inline-line">councilor.ribeiro@city.gov</span>'
    '&nbsp;&nbsp;&nbsp;&nbsp;<b>Subject:</b> <span class="inline-line" style="min-width:170pt">&nbsp;</span></p>',
    L(22),
)

STUDENT = [ws1, ws2, ws3, ws3q, ws4, ws5, ws6, ws7]

# ═════════════════════════════ TEACHER'S GUIDE ══════════════════════════════

overview = ws(
    header(TOPIC, "Teacher's Guide", "Teacher",
           "Lesson plan, answer keys and scripts for the Advanced TOEFL lesson pack.", outline=True),
    sec("i", "Lesson overview", "2h15"),
    tbl(["Item", "Detail"], [
        ["Level", "B2+ / C1"],
        ["Total time", "75 min + 15 min break + 60 min"],
        ["Topic", "Urban heat islands: why cities are hotter than the countryside, and what to do about it"],
        ["Skills", "Speaking, vocabulary, listening, grammar, writing"],
        ["Grammar focus", "Hedging and concession in academic English"],
        ["TOEFL tasks practiced", "Take an Interview, Complete the Words, academic lecture listening, Build a "
         "Sentence, Academic Discussion, Listen and Repeat, Write an Email (homework)"],
    ], widths=["24%", "76%"]),
    "<p><b>Aims.</b> By the end of the lesson, students can take structured notes on a 4-minute lecture, "
    "summarize it in 60 seconds, use 10 topic words with correct collocations, and write a hedged, 100+ word "
    "academic discussion post in 10 minutes.</p>",
    "<p><b>Materials.</b> One student pack per student, the lecture audio (see Audio) or Script A to read "
    "aloud, a timer, and phones for optional self-recording.</p>",
    "<p><b>Prep (10 min).</b> Print one student pack per student, cut up the debate role cards (Worksheet 4), "
    "and test the audio on the classroom speakers.</p>",
    sec("ii", "Teacher plan", "7 stages"),
    "<p>Seven stages: four before the break (75 min) and three after (60 min). Every stage reuses the lecture "
    "content, so vocabulary and ideas recycle across all skills.</p>",
    tbl(["#", "Stage", "Time", "Skill", "Interaction", "Material"], [
        ["1", "Interview warm-up", "10 min", "Speaking", "Pairs", "Worksheet 1"],
        ["2", "Topic vocabulary", "15 min", "Vocabulary, reading", "Individual, then pairs", "Worksheet 2"],
        ["3", "Academic lecture", "25 min", "Listening, note-taking", "Individual, then pairs", "Worksheet 3, audio"],
        ["4", "Summary + city council debate", "25 min", "Speaking", "Individual, then groups of 4–6", "Worksheet 4"],
        ["—", "Break", "15 min", "—", "—", "—"],
        ["5", "Hedging and concession", "20 min", "Grammar", "Pairs", "Worksheet 5"],
        ["6", "Academic Discussion post", "30 min", "Writing", "Individual, pairs, whole class", "Worksheet 6"],
        ["7", "Listen and Repeat + homework set-up", "10 min", "Pronunciation, writing", "Whole class",
         "Script C, Worksheet 7"],
    ], widths=["5%", "27%", "10%", "17%", "23%", "18%"]),
    first=True,
)

steps = ws(
    '<div class="block">Block 1 (75 min)</div>',
    stage("Stage 1 — Interview warm-up (10 min)", [
        'Put students in pairs, A and B. Tell them this mirrors the TOEFL "Take an Interview" task: no '
        "preparation time, about 45 seconds per answer.",
        'A asks B questions 1–5 on Worksheet 1, then they swap. Keep time and call "switch" every 45 seconds. '
        "With a short class, use questions 1–3 only.",
        "After each answer, the speaker jots down a few key words in the space; the listener notes one strong "
        "phrase and one moment of hesitation.",
        "Feedback (2 min): ask two or three students for the strongest phrase they heard. Board useful language "
        "for later.",
    ]),
    stage("Stage 2 — Topic vocabulary (15 min)", [
        "Students match the 10 words to their definitions alone (5 min).",
        "Pairs compare. Check answers, drill pronunciation of <i>albedo</i> /ælˈbiːdoʊ/, <i>impervious</i> "
        "/ɪmˈpɜːrviəs/, <i>exacerbate</i> /ɪɡˈzæsərbeɪt/ (3 min).",
        "Students complete the Part B paragraph with the words from Part A, alone (5 min). <i>Albedo</i> is used "
        "in the example.",
        "Quick check (2 min). Point out the clues that decide each gap: <i>can ___ the problem, making hot "
        "streets even hotter</i> (exacerbate, not mitigate).",
    ]),
    stage("Stage 3 — Academic lecture (25 min)", [
        "Pre-listening (2 min): students write two ideas in Part A. Collect two or three guesses.",
        "First listening, gist (4 min): play the audio once. Students write the main idea in one sentence (Part B).",
        'Note-frame set-up (1 min): read the four "How to take notes" steps aloud and point to the example row '
        "so students see the length of a note.",
        "Second listening, notes (6 min): play again. Students complete the note frame (Part C).",
        "Questions (7 min): students answer the 10 questions in Part D from their notes only. No third listening.",
        "Pair check (5 min): partners compare notes and find one point one of them missed. Go through answers "
        "with the key, focusing on <i>why</i> distractors are wrong.",
    ]),
    stage("Stage 4 — Summary + city council debate (25 min)", [
        "60-second summary (8 min): 1 minute to plan from notes, then students summarize the lecture to a "
        "partner, timed, and swap. If phones are allowed, they record themselves.",
        "Debate set-up (3 min): groups of up to six. Hand out the role cards: five advocates (Trees, Cool roofs, "
        "Green roofs, Cool pavements, Cooling centers) and one Council Chair. With smaller groups, leave out "
        "Cool pavements first, then Cooling centers.",
        "Prep (4 min): advocates read their card and prepare a 1-minute pitch. The Chair prepares questions.",
        "Debate (8 min): each advocate pitches (1 min), then open discussion. The Chair must pick one option and "
        "justify the decision in 30 seconds.",
        "Feedback (2 min): each Chair announces the decision and the deciding reason.",
    ]),
    '<div class="block" style="margin-top:10pt">Break (15 min) · Block 2 (60 min)</div>',
    stage("Stage 5 — Hedging and concession (20 min)", [
        "Discovery (5 min): students underline the hedging and concession language in the six lecture extracts "
        "in Part A.",
        "Concept check (3 min): ask \"Is the professor sure? Why might a scientist avoid saying 'always'?\" Board "
        "the two categories: hedges (<i>tend to, probably, some studies suggest, can sometimes, largely</i>) and "
        "concession (<i>although, the downside is that, while it's true that</i>).",
        "Controlled practice (7 min): pairs rewrite the six overconfident claims in Part B.",
        "Build a Sentence (5 min): students reorder the five scrambled sentences in Part C, a direct copy of the "
        "TOEFL task format. Fastest pair writes answers on the board.",
    ]),
    stage("Stage 6 — Academic Discussion post (30 min)", [
        "Task intro (3 min): read the prompt aloud. Remind students that the TOEFL rewards a new idea, not a "
        "repeat of Maya's or Lucas's post.",
        "Timed writing (10 min): strict timer. Minimum 100 words, at least two hedges and one concession.",
        "Peer review (7 min): swap papers. Partners use the checklist and underline every hedge they find.",
        "Class upgrade (10 min): copy two or three anonymous sentences onto the board and improve them together. "
        "Then show the model answer from the key.",
    ]),
    stage("Stage 7 — Listen and Repeat + homework set-up (10 min)", [
        "Read the seven sentences in Script C aloud, one at a time (or play them). Students repeat exactly, "
        "chorally first, then two or three individuals per sentence (6 min). Sentences get longer, so watch for "
        "dropped words and stress.",
        "Homework set-up (4 min): go through the email task on Worksheet 7. Elicit one hot place in the "
        "students' own neighborhoods and which solution would suit it.",
    ]),
    "<p><b>Homework.</b> Worksheet 7, Write an Email (about 120 words).</p>",
)

# ── Answer Key ──
key_2a = nlist([f"{w.split(' (')[0]} — {k}" for w, k in VOCAB])
key_2b = nlist(PARA_KEY) + ('<div class="why">4 vs 7: "making hot streets even hotter" signals <i>exacerbate</i>; '
                            '"how can cities ___ the effect?" signals <i>mitigate</i>.</div>')
frame_key = tbl(["Section", "Claim", "Evidence / example"], [
    ["Definition <i>(example)</i>", "City warmer than the countryside around it",
     "A few °C on average; up to ~10 °C on calm, clear nights"],
    ["Cause 1", "Surfaces", "Asphalt, concrete, dark roofs; impervious, low albedo; absorb by day, release at night"],
    ["Cause 2", "Lack of vegetation", "Evapotranspiration cools air, like sweating; trees give shade"],
    ["Cause 3", "Human activity", "Waste heat from cars, AC, factories; AC feedback loop"],
    ["Who is affected", "Vulnerable populations",
     "Lower-income areas hotter, fewer trees; elderly, outdoor workers, people without AC"],
    ["Solution 1", "Trees and parks", "Popular, cleaner air; slow to grow, need space and water"],
    ["Solution 2", "Cool roofs", "Cheap and quick; may reduce indoor temps; can reflect heat onto pedestrians"],
    ["Solution 3", "Green roofs", "Cool buildings, absorb rain; expensive, may need retrofitting"],
    ["Conclusion", "Combination needed", "Adapted to local conditions"],
], widths=["17%", "26%", "57%"])
WHY_3D = [
    ("Main idea", "a and c are never discussed; d is too narrow and contradicts her conclusion."),
    ("Detail", "She says the gap is often largest at night, especially on calm, clear nights."),
    ("Detail", 'She defines impervious as "water can\'t soak into them"; low reflection (a) is albedo.'),
    ("Detail", "AC heat (a) is a separate cause, not the night-time reason; b and c are not mentioned."),
    ("Purpose", "Sweating is an analogy for evaporative cooling; workers (b) come later, in another section."),
    ("Detail", "Hotter city → more AC → more waste heat → hotter city. The other options are not described as a loop."),
    ("Detail (NOT)", "She names the elderly, outdoor workers and people without AC; children are not mentioned."),
    ("Inference", "Lower-income areas are hotter partly because of fewer trees, so more trees could reduce risk. "
                  "a, b and d are not stated."),
    ("Detail", "a is a drawback of reflective surfaces; b is trees; green roofs absorb rain, so d is wrong."),
    ("Attitude", "She says none is perfect on its own and most researchers argue for a combination."),
]
key_3d = tbl(["#", "Ans.", "Type", "Why the distractors are wrong"],
             [[str(i), f"<b>{a}</b>", t, w] for i, (a, (t, w)) in enumerate(zip(KEY_3D, WHY_3D), 1)],
             widths=["5%", "7%", "13%", "75%"])
key_5a = nlist(["<i>largely</i>", "<i>tend to</i>", "<i>probably</i>; <i>The downside is that</i> (concession)",
                "<i>Some studies suggest</i>; <i>can</i>", "<i>Although</i> (concession)", "<i>can sometimes</i>"])
key_5c = nlist([
    "Lower-income neighborhoods tend to be hotter.",
    "Some studies suggest that cool roofs can reduce indoor temperatures.",
    "Although green roofs are expensive, they absorb rainwater. (Also accept: Although they absorb rainwater, "
    "green roofs are expensive.)",
    "Tree planting is probably the most popular approach.",
    "The downside is that trees take years to grow.",
])
key_5b = nlist([
    "Planting trees can significantly reduce urban heat, although it is unlikely to solve the problem on its own.",
    "Cool roofs tend to reduce indoor temperatures, particularly in buildings without air conditioning.",
    "Lower-income neighborhoods are often hotter than wealthier ones, partly because they tend to have fewer trees.",
    "Green roofs may be too expensive for some cities, especially where older buildings would need to be retrofitted.",
    "Waste heat from air conditioning is likely to exacerbate urban heat islands, but it is only one of several causes.",
    "Some projections suggest that cities could become considerably hotter by 2050.",
])
model_post = (
    '<p class="serif">I think both Maya and Lucas make valid points, but I would argue that the real question is '
    "not only which strategy to choose, but where to use it. Research suggests that lower-income neighborhoods "
    "tend to be hotter, partly because they have less canopy cover. A citywide roof law would mostly affect new "
    "buildings, which are probably being built in wealthier areas. Admittedly, a roof requirement costs the city "
    "very little, since developers pay for it. However, if the goal is to protect vulnerable populations, it "
    "could be more cost-effective to plant trees and install cool roofs on existing homes in the hottest "
    "neighborhoods first. In my view, a targeted approach is likely to save more lives than a general rule that "
    "mainly benefits areas that are already relatively comfortable.</p>"
    '<div class="why">Why it scores well: a new idea (location and equity) instead of simply choosing Maya or '
    "Lucas; six hedges (<i>would argue, suggests, tend to, probably, could be, is likely to</i>); one concession "
    "(<i>Admittedly… However</i>); three lesson terms (<i>canopy cover, vulnerable populations, "
    "cost-effective</i>).</div>"
)
answer_key = ws(
    header(TOPIC, "Answer Key", "Answer Key",
           "Answers for Worksheets 2, 3, 5 and 6. Worksheets 1, 4 and 7 are open tasks with no fixed answers.",
           outline=True),
    kgrid(kcard("2A", "Vocabulary — matching", key_2a), kcard("2B", "Vocabulary — paragraph", key_2b)),
    kcard("3B", "Listening — main idea (sample)",
          "<p style='margin:0'>Cities are warmer than surrounding rural areas because of dark surfaces, lack of "
          "vegetation and waste heat; this harms vulnerable people most, and no single solution is enough.</p>"),
    kcard("3C", "Listening — note frame (sample)", frame_key),
    kcard("3D", "Listening — questions", key_3d),
    kgrid(kcard("5A", "Hedging — discovery", key_5a), kcard("5C", "Build a Sentence", key_5c)),
    kcard("5B", "Hedging — rewrites (sample answers; accept any accurate hedge)", key_5b),
    kcard("6", "Model Academic Discussion post (about 130 words)", model_post),
)

# ── Scripts ──
LECTURE = [
    "Okay, let's get started. Today I want to talk about something many of you have probably felt without "
    "knowing its name: the urban heat island effect.",
    "So, what is it? Simply put, an urban heat island is a city area that is significantly warmer than the rural "
    "areas around it. On average, the difference may be just a few degrees. But here's the surprising part: the "
    "gap is often largest at night. On calm, clear nights, some cities have been measured at up to around ten "
    "degrees Celsius warmer than the nearby countryside.",
    "Why does this happen? There are three main causes. The first is surfaces. Cities are covered in asphalt, "
    "concrete, and dark roofs. These are what we call impervious surfaces, meaning water can't soak into them. "
    "Dark materials also have a low albedo, which means they reflect very little sunlight. Instead, they absorb "
    "heat during the day and release it slowly at night. That's largely why cities stay warm after sunset.",
    "The second cause is the lack of vegetation. In the countryside, plants cool the air through a process "
    "called evapotranspiration. Basically, they release water vapor, and that evaporation removes heat from the "
    "air, a bit like sweating does for us. Trees also provide shade. When you replace fields and forests with "
    "buildings, you lose both effects.",
    "The third cause is human activity itself. Cars, air conditioners, factories: they all release waste heat. "
    "And there's an ironic loop here. As cities get hotter, people use more air conditioning, which pumps more "
    "heat outside, which makes the city hotter still.",
    "Now, why should we care? Well, heat isn't just uncomfortable. In the United States, it's the leading "
    "weather-related cause of death. And it doesn't affect everyone equally. Studies in several cities have "
    "found that lower-income neighborhoods tend to be hotter than wealthier ones, partly because they have "
    "fewer trees. So urban heat disproportionately affects vulnerable populations: the elderly, outdoor workers, "
    "and people without air conditioning.",
    "So what can cities do? Let me mention three strategies. First, trees and parks. Increasing canopy cover is "
    "probably the most popular approach, and it brings other benefits too, like cleaner air. The downside is "
    "that trees take years to grow, and they need space and water.",
    "Second, cool roofs. That means painting roofs white or using reflective materials. This is relatively "
    "cheap and quick. Some studies suggest cool roofs can noticeably reduce indoor temperatures, especially in "
    "buildings without air conditioning.",
    "Third, green roofs: roofs covered with plants. Although green roofs cool buildings and absorb rainwater, "
    "they're more expensive to install and maintain. And older buildings may need to be retrofitted to support "
    "the extra weight.",
    "Now, I want to be careful here. None of these is a perfect solution on its own. Reflective surfaces can "
    "sometimes bounce heat onto pedestrians at street level, for example. So most researchers argue that cities "
    "need a combination of strategies, adapted to local conditions.",
    "For next class, I'd like you to think about your own city. Which of these strategies would be most "
    "cost-effective there, and why? We'll start with that discussion next time.",
]
REPEAT = [
    "Cities are getting hotter.",
    "Dark roofs absorb a lot of heat.",
    "Trees cool the air and provide shade.",
    "Lower-income neighborhoods tend to be hotter.",
    "Some studies suggest that cool roofs are cost-effective.",
    "Although green roofs are expensive, they help absorb rainwater.",
    "Most researchers argue that cities need a combination of strategies adapted to local conditions.",
]
scripts = ws(
    header(TOPIC, "Scripts", "Teacher",
           "Teacher-read scripts. If the audio fails, read Script A aloud at a natural pace; it runs about 4 minutes.",
           outline=True),
    sec("A", 'Lecture: "Urban Heat Islands"', "About 560 words"),
    '<p class="serif muted" style="font-style:italic">Professor (female), environmental science class.</p>',
    "".join(f'<p class="serif">{p}</p>' for p in LECTURE),
    '<div style="page-break-inside:avoid">',
    sec("B", "Model 60-second summary", "About 120 words"),
    '<p class="serif">The lecture was about urban heat islands, which are city areas that are warmer than the '
    "countryside around them, especially at night. The professor gave three causes. First, dark, impervious "
    "surfaces like asphalt absorb heat during the day and release it at night. Second, cities have fewer plants, "
    "so they lose the cooling effect of evapotranspiration and shade. Third, cars and air conditioners release "
    "waste heat. She explained that heat disproportionately affects vulnerable people, and that poorer "
    "neighborhoods tend to be hotter. Finally, she described three solutions: trees, cool roofs and green roofs. "
    "Each has advantages and drawbacks, so she concluded that cities probably need a combination of "
    "strategies.</p></div>",
    sec("C", "Listen and Repeat", "7 sentences"),
    "<p>Read each sentence once at natural speed. Students repeat it exactly.</p>",
    nlist(REPEAT, cls="tight"),
    sec("♪", "Audio", "Browser text-to-speech"),
    "<p>All audio plays through the browser's built-in text-to-speech, using the TTS player in the Claude chat "
    "where this pack was made.</p>",
    tbl(["Track", "Player button", "Length"], [
        ["Script A, full lecture", "Play from start", "About 4 min"],
        ['Script A, second half ("Now, why should we care?")', "Start at part 2", "About 2 min"],
        ["Script C, Listen and Repeat", "Play drill", "About 1.5 min with gaps"],
        ["Script C, one sentence again", "Repeat last sentence", "A few seconds"],
    ], widths=["52%", "24%", "24%"]),
    "<p><b>Settings.</b> Speed 0.95× suits advanced learners and is close to TOEFL lecture pace; raise it to "
    "1.05× for a challenge. Repeat gap 5 seconds; use 7–8 seconds for sentences 6 and 7.</p>",
    '<p><b>Best voices.</b> In Edge, pick a "Microsoft … Online (Natural)" US English voice. In Chrome, pick '
    '"Google US English". Test the voice on the classroom speakers before the lesson.</p>',
    "<p><b>In class.</b> Do not pause during the first two listenings in Stage 3, to match test conditions. "
    "Backup: in Edge, select Script A in the doc and right-click → Read aloud selection, or read it live.</p>",
)

TEACHER = [overview, steps, answer_key, scripts]

if __name__ == "__main__":
    out = ROOT / "advanced"
    build(STUDENT, out / f"{SLUG}_Student_Pack.pdf", LEVEL, TOPIC)
    build(TEACHER, out / f"{SLUG}_Teacher_Guide.pdf", LEVEL, TOPIC)
    print("built", out)
