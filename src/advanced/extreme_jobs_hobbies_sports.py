"""Extreme Jobs, Hobbies and Sports — Advanced (B2+/C1) TOEFL lesson.
Why do some people crave adventure and risk?

Builds:
  advanced/Extreme_Jobs_Hobbies_Sports_Student_Pack.pdf
  advanced/Extreme_Jobs_Hobbies_Sports_Teacher_Guide.pdf

Run from the repo root:  python3 src/advanced/extreme_jobs_hobbies_sports.py
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
from lesson_kit import (header, sec, part, L, kcard, nlist, stage, build,
                        ws, ex, wordbox, tbl, note, kgrid, pair)

LEVEL, TOPIC, PILL = "Advanced", "Extreme Jobs, Hobbies &amp; Sports", "B2+ / C1"
FOOT_TOPIC = "Extreme Jobs, Hobbies & Sports"
SLUG = "Extreme_Jobs_Hobbies_Sports"

# ═════════════════════════════ STUDENT PACK ═════════════════════════════════

# 1 — Interview warm-up
interview_qs = [
    "What is the most adventurous thing you have ever done? How did you feel before, during and after it?",
    "Would you ever try bungee jumping or skydiving? Why or why not?",
    "Some people say that people in dangerous jobs, like firefighters, should earn much more than other "
    "workers. Do you agree? Why?",
    "Running a marathon is painful and exhausting. Why do you think so many people choose to do it?",
    "Do you think people are born risk-takers, or do they learn to enjoy risk? Give an example.",
]
ws1 = ws(
    header(TOPIC, "Student Pack", PILL,
           "Advanced TOEFL lesson — why do some people crave adventure and risk?", fields=True),
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
    ("adrenaline", "e"), ("endurance", "b"), ("daredevil", "d"), ("reckless", "a"),
    ("calculated risk", "f"), ("thrive on (something)", "h"), ("push your limits", "i"),
    ("hazardous", "c"), ("exhilarating", "g"), ("overcome (a fear)", "j"),
]
DEFS = {
    "a": "not thinking about the possible danger of your actions",
    "b": "the ability to keep doing something difficult or tiring for a long time",
    "c": "dangerous, especially to people's health or safety",
    "d": "a person who enjoys doing dangerous things",
    "e": "a hormone your body releases when you are frightened or excited",
    "f": "a danger you accept after thinking carefully about it",
    "g": "very exciting and enjoyable",
    "h": "to enjoy and do well in a situation other people find difficult",
    "i": "to try to do more than you thought you could",
    "j": "to succeed in controlling a feeling or problem",
}
BOX = ["adrenaline", "endurance", "daredevil", "reckless", "calculated risk",
       "thrive on", "push your limits", "hazardous", "exhilarating", "overcome"]
PARA_KEY = ["thrive on", "daredevil", "exhilarating", "endurance", "push your limits",
            "hazardous", "reckless", "calculated risk", "overcome"]
G = '<b>{}.</b> _____________'
para = (
    "Some people seem to {1} danger: the more frightening a situation is, the happier they feel. A typical "
    "{2} will jump off a bridge attached to a rope and describe the experience as {3}. Others prefer tests "
    "of {4}, such as a 100-kilometer race through the mountains, where the goal is to {5} and keep going "
    "long after your body wants to stop. Firefighters, on the other hand, work in {6} conditions because "
    "it is their job, not their hobby. Experts point out that most of these people are not {7}: before every "
    "climb, jump or rescue, they plan carefully and take only a {8}. For many beginners, the hardest part is "
    "simply learning to {9} their fear of heights."
)
for i in range(1, 10):
    para = para.replace("{%d}" % i, G.format(i))

ws2 = ws(
    sec(2, "Topic vocabulary", "Vocabulary · Reading"),
    part("A", "Match each word (1–10) to its definition (a–j). Number 0 is an example."),
    ex("Example: 0. thrill → <b>k</b> (a sudden feeling of excitement and pleasure)"),
    pair(tbl(["#", "Word", "Answer"], [[f"{i}.", w, ""] for i, (w, _) in enumerate(VOCAB, 1)],
             cls="tall", widths=["14%", "62%", "24%"], numcol=True),
         tbl(["", "Definition"], [[k, v] for k, v in DEFS.items()]
             + [[("k", "ex"), ("a sudden feeling of excitement and pleasure", "ex")]],
             cls="tall", widths=["12%", "88%"], numcol=True)),
    part("B", "Complete the paragraph with the words from Part A."),
    wordbox(BOX, struck={"adrenaline"}),
    ex("Example: When you jump, your body releases <b>adrenaline</b>, so your heart beats faster."),
    f'<p style="text-align:justify;line-height:2.35">{para}</p>',
)

# 3 — Academic lecture (notes) + questions
frame_rows = [["Who seeks sensation most", "", ""], ["Reason 1: the brain", "", ""],
              ["Reason 2: risk perception", "", ""], ["Reason 3: flow", "", ""],
              ["Example 1: bungee jumping", "", ""], ["Example 2: marathons", "", ""],
              ["Example 3: firefighters", "", ""], ["Professor's conclusion", "", ""]]
ex_row = [("Example:<br>Definition", "ex"), ("need for new, varied, intense experiences", "ex"),
          ("Zuckerman (US psych.), 1960s; high scorers → bored easily", "ex")]
ws3 = ws(
    sec(3, "Academic lecture", "Listening · Note-taking"),
    part("A", "Before you listen. Why do you think some people enjoy danger? Write two ideas."),
    nlist([L(1), L(1)]),
    part("B", "First listening. Write the main idea of the lecture in one sentence."),
    L(2),
    part("C", "Second listening. Complete the note frame."),
    note("How to take notes", [
        "The lecture follows the order of the rows below: first a definition, then who seeks sensation most, "
        "three reasons, three examples and the conclusion.",
        "In <b>Claim</b>, write the professor's main point for that section in 2–5 words.",
        "In <b>Evidence / example</b>, write one fact, name, date or example he gives to support it.",
        "Write notes, not sentences. Abbreviations and symbols (↑, ↓, →, =, ~) are fine.",
    ]),
    tbl(["Section", "Claim", "Evidence / example"], [ex_row] + frame_rows,
        cls="tall frame", widths=["22%", "31%", "47%"]),
)

QS = [
    ("What is the lecture mainly about?",
     ["How to reduce injuries in extreme sports",
      "Why some people are drawn to risk, and how their motives differ",
      "The history of bungee jumping",
      "Why firefighters should earn higher salaries"]),
    ("According to the professor, what is sensation seeking?",
     ["A fear of new or intense experiences",
      "A medical condition that makes people reckless",
      "The need for new, varied and intense experiences",
      "The ability to stay calm in an emergency"]),
    ("When does sensation seeking tend to be highest?",
     ["In early childhood", "In the late teens and early twenties", "In middle age",
      "It stays the same throughout life."]),
    ("What is the professor's view of the research on dopamine?",
     ["It proves that dopamine causes all risk-taking.",
      "It has been rejected by most psychologists.",
      "It applies only to professional athletes.",
      "It is promising, but the evidence is still mixed."]),
    ("Why does the professor mention two friends on a roller coaster?",
     ["To show that the same activity can feel very different to different people",
      "To warn that roller coasters are more dangerous than they look",
      "To compare amusement parks with extreme sports",
      "To explain how the body produces adrenaline"]),
    ("According to the lecture, what is flow?",
     ["A rush of fear just before a dangerous jump",
      "The speed at which a runner finishes a marathon",
      "A state of total concentration when the challenge of a task matches your skill",
      "A training method used by firefighters"]),
    ("What does the professor say about the first modern bungee jumps?",
     ["They took place in New Zealand in the 1990s.",
      "They were part of a scientific experiment.",
      "They were made by professional stunt performers.",
      "They were made in England in 1979 by members of a university club."]),
    ("According to more recent studies, what may play a bigger role in the \"runner's high\"?",
     ["Chemicals called endocannabinoids", "Endorphins", "Dehydration during the race",
      "The cheering of the crowd"]),
    ("What can be inferred about why many firefighters stay in the job for decades?",
     ["Their pay increases every year.",
      "They depend on the adrenaline of emergencies.",
      "Their motivation comes mainly from purpose, not from the thrill.",
      "They have few other career options."]),
    ("What is the professor's main conclusion?",
     ["Extreme sports should be more strictly regulated.",
      "Risk-takers have different motives, and most of them plan carefully.",
      "Sensation seeking is mainly genetic.",
      "Bungee jumpers and firefighters have the same personality."]),
]
KEY_3D = ["b", "c", "b", "d", "a", "c", "d", "a", "c", "b"]


def mc(q, opts):
    o = "<br>".join(f"{l}. {t}" for l, t in zip("abcd", opts))
    return f'{q}<div class="opts">{o}</div>'


ws3q = ws(
    sec(3, "Academic lecture — questions", "Listening"),
    part("D", "Use your notes only. Circle the best answer (a, b, c or d)."),
    nlist([mc(q, o) for q, o in QS], cls="two"),
)

# 4 — Town council debate: who pays for mountain rescues?
CARDS = [
    ("Advocate", "Rescue team chief: keep rescues free",
     "people who are afraid of a bill wait too long to call for help, and late rescues are slower, more "
     "dangerous for the team and more expensive.",
     "local taxpayers keep paying for other people's risky choices, and calls keep rising."),
    ("Advocate", "Tourism board: free rescues + safety campaign",
     "climbers, skiers and hikers bring millions to local hotels and shops; better trail signs and free "
     "safety courses would cut accidents without scaring visitors away.",
     "campaigns are slow, their results are hard to measure, and taxpayers still pay for every rescue."),
    ("Advocate", "Extreme athlete: charge only reckless people",
     "most adventurers plan carefully; only people who ignore closed trails or storm warnings should pay, "
     "which is fair and encourages responsible behavior.",
     "who decides what is reckless? Every bill could become an argument, and people may still delay calling."),
    ("Advocate", "Insurance company: required rescue insurance",
     "a small fee with every climbing, skiing or trail permit covers the full cost of rescues, so nobody gets "
     "a huge bill and taxpayers pay nothing.",
     "it is hard to check every day hiker, it adds paperwork, and local residents may resent paying a fee."),
    ("Advocate", "Local taxpayer: everyone pays their own bill",
     "if you choose a hazardous hobby, you should pay for your own rescue, just as you pay for your own "
     "equipment and lift tickets.",
     "a rescue can cost thousands of dollars; poorer visitors may not call for help, and the town could get "
     "bad publicity."),
]
cards_html = "".join(
    f'<div class="card"><div class="role">{r.upper()}</div><div class="cn">{n}</div>'
    f"<p><b>Your strengths:</b> {s}</p><p><b>Expect criticism:</b> {c}</p></div>"
    for r, n, s, c in CARDS
) + ('<div class="card solid"><div class="role">CHAIR</div><div class="cn">Council Chair</div>'
     "<p><b>Your job:</b> give each advocate 1 minute, then ask hard questions: Will people still call for "
     "help early? Is it fair to local residents? How will we enforce it?</p>"
     "<p>At the end, choose ONE policy and explain your decision in 30 seconds.</p></div>")
ws4 = ws(
    sec(4, "Town council debate", "Speaking · Groups"),
    part("A", "60-second summary."),
    "<p>Plan for 1 minute using your notes, then summarize the lecture to your partner. Cover: what "
    "sensation seeking is, two reasons some people seek risk, one of the three examples, and the "
    "professor's conclusion.</p>",
    part("B", "Role cards."),
    note("How the debate works", [
        "Read the situation below. Your teacher gives you ONE card.",
        "<b>Advocates:</b> read your card and plan a 1-minute pitch (4 min). <b>Chair:</b> plan your questions.",
        "Each advocate pitches for 1 minute. Use your strengths and answer the criticism before anyone else says it.",
        "Open discussion: the Chair asks hard questions and advocates respond to each other.",
        "The Chair chooses ONE policy and explains the decision in 30 seconds.",
    ]),
    ex("Example pitch opening: The main reason rescues must stay free is that <b>people who fear a bill wait "
       "too long to call</b>. While it's true that <b>taxpayers cover the cost</b>, in the long run late "
       "rescues cost far more."),
    '<div class="bar"><b>The situation.</b> Rescue calls in your mountain town have tripled in ten years, '
    "mostly for climbers, skiers and hikers. Rescues are free and paid for by local taxes. The council must "
    "choose ONE policy today.</div>",
    '<p class="muted small">✂ Cut along the dashed lines. One card per student.</p>',
    f'<div class="cards">{cards_html}</div>',
    '<div class="note" style="margin-top:8pt"><div class="nt small" style="letter-spacing:2pt">USEFUL LANGUAGE</div>'
    '<span class="serif" style="font-style:italic">The main reason is that… / While it\'s true that…, … / '
    "I'd argue that… / That's a fair point, but… / In the long run…</span></div>",
)

# 5 — Speculating about causes and motives
DISCOVERY = [
    "That might explain why some people get bored so easily in a routine job.",
    "Part of the answer may lie in the brain.",
    "Their interest in danger seems to stem from a stronger response to novelty.",
    "The first jumpers must have felt terrified as they stepped off the bridge.",
    "They can't have known exactly how the ropes would behave.",
    "For most firefighters, the job is driven by a desire to help, which explains why many stay in it for decades.",
]
REWRITE = [
    "Leo has run 30 marathons in five years.",
    "Mia screamed all the way down on her first bungee jump.",
    "The climber didn't check the weather forecast before he set off into a storm.",
    "Thousands of people apply to become firefighters every year, even though the job is dangerous.",
    "Sensation seeking is usually highest in people under 25.",
    "My grandfather went skydiving on his 80th birthday.",
]
BUILD = [
    "must / felt / she / have / terrified",
    "their work / driven by / is / a desire to help",
    "can't / known / have / the danger / they",
    "stem from / may / their love of risk / childhood experiences",
    "that's / why / they / under pressure / stay calm",
]
ws5 = ws(
    sec(5, "Speculating about causes and motives", "Grammar"),
    part("A", "Discovery. Underline the words that show how sure the speaker is, or that explain a cause or motive."),
    ex("Example: Boredom <b>could be</b> part of the reason."),
    nlist(DISCOVERY, cls="tight"),
    tbl(["Deduction (how sure?)", "Cause and motive"], [
        ["must / must have + past participle (almost sure: yes)", "stem from / result from + noun"],
        ["might / may / could (have) + past participle (possible)", "be driven by / be motivated by + noun"],
        ["can't / couldn't (have) + past participle (almost sure: no)", "which explains why / that's why + clause"],
        ["seem to / appear to + verb", "the cause lies in + noun"],
        ["probably / is likely to + verb", "due to / because of + noun"],
    ], cls="compact", widths=["52%", "48%"]),
    part("B", "Speculate about each situation in one sentence. Use a different structure from the box each time."),
    ex("Example: Ana quit her bank job to become a mountain guide. → She <b>must have been</b> bored in the office."),
    nlist([c + L(1, short=True) for c in REWRITE]),
    part("C", "Build a Sentence. Put the chunks in the correct order. Add punctuation."),
    note("How to build a sentence", [
        "Use every chunk once. Add no new words.",
        "Find the subject and main verb first, then place the other chunks.",
        "Start with a capital letter and end with a period.",
    ], inline=True),
    ex("Example: have / they / must / trained hard → <b>They must have trained hard.</b>"),
    nlist([b + L(1, short=True) for b in BUILD]),
)

# 6 — Academic Discussion post
CHECKS_L = ["States a clear position early", "Adds a new idea, not a repeat of Sofia or Daniel",
            "Supports it with a reason and a specific example", "Uses at least two structures from Worksheet 5 (underline them)"]
CHECKS_R = ["Uses at least one concession (although / while it's true that…)",
            "Uses at least two words from Worksheet 2", "100 words or more"]
ws6 = ws(
    sec(6, "Academic Discussion post", "Writing · 10 min"),
    "<p><b>Time: 10 minutes. Minimum: 100 words.</b> Use at least two structures from Worksheet 5 and one "
    "concession.</p>",
    '<div class="bar"><b>Professor Okafor:</b> Many schools organize adventure trips, such as rock climbing, '
    "white-water rafting or long mountain hikes, to help teenagers build confidence and resilience. Other "
    "schools have stopped these trips because of the risk of injury and the cost of insurance. Should schools "
    "offer risky activities like these? Why or why not?</div>",
    '<div class="bar soft"><b>Sofia:</b> Yes, they should. On my school climbing trip I was terrified at first, '
    "but with good instructors I reached the top. Facing a real challenge taught me to overcome fear in a way "
    "no classroom could.</div>",
    '<div class="bar soft"><b>Daniel:</b> I disagree. One accident can change a student\'s life forever, and '
    "the school is responsible for every child. Families who want their children to try extreme activities can "
    "do that on weekends, outside school.</div>",
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
    '<div class="bar">You signed up for the City Charity Marathon next month, but you injured your knee '
    "during training. Write an email to the race organizer, Ms. Carter. In your email:"
    '<ul style="margin:2pt 0 0;padding-left:14pt">'
    "<li>explain what happened</li>"
    "<li>ask to switch to the 10K race or move your entry to next year</li>"
    "<li>explain why the charity is important to you</li></ul></div>",
    "<p>Use a polite, formal register, at least one structure from Worksheet 5 and two words from Worksheet 2.</p>",
    '<p style="margin-top:6pt"><b>To:</b> <span class="inline-line">Ms. Carter, Race Organizer</span>'
    '&nbsp;&nbsp;&nbsp;&nbsp;<b>Subject:</b> <span class="inline-line" style="min-width:170pt">&nbsp;</span></p>',
    L(22),
)

STUDENT = [ws1, ws2, ws3, ws3q, ws4, ws5, ws6, ws7]

# ═════════════════════════════ TEACHER'S GUIDE ══════════════════════════════

overview = ws(
    header(TOPIC, "Guide", "Teacher",  # full "Teacher's Guide" overflows the line with this title
           "Lesson plan, answer keys and scripts for the Advanced TOEFL lesson pack.", outline=True),
    sec("i", "Lesson overview", "2h15"),
    tbl(["Item", "Detail"], [
        ["Level", "B2+ / C1"],
        ["Total time", "75 min + 15 min break + 60 min"],
        ["Topic", "Extreme jobs, hobbies and sports: why do some people crave adventure and risk?"],
        ["Skills", "Speaking, vocabulary, listening, grammar, writing"],
        ["Grammar focus", "Speculating about causes and motives: modals of deduction (present and past) and "
                          "cause language (<i>stem from, be driven by, which explains why</i>)"],
        ["TOEFL tasks practiced", "Take an Interview, Complete the Words, academic lecture listening, Build a "
         "Sentence, Academic Discussion, Listen and Repeat, Write an Email (homework)"],
    ], widths=["24%", "76%"]),
    "<p><b>Aims.</b> By the end of the lesson, students can take structured notes on a 4-minute psychology "
    "lecture, summarize it in 60 seconds, use 10 topic words with correct collocations, speculate about "
    "people's feelings and motives with present and past modals, and write a 100+ word academic discussion "
    "post in 10 minutes.</p>",
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
        ["4", "Summary + town council debate", "25 min", "Speaking", "Individual, then groups of 4–6", "Worksheet 4"],
        ["—", "Break", "15 min", "—", "—", "—"],
        ["5", "Speculating about causes and motives", "20 min", "Grammar", "Pairs", "Worksheet 5"],
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
        "With a short class, use questions 1, 2 and 5 only.",
        "After each answer, the speaker jots down a few key words in the space; the listener notes one strong "
        "phrase and one moment of hesitation.",
        "Feedback (2 min): ask two or three students for the strongest phrase they heard. Board useful language "
        "for later.",
    ]),
    stage("Stage 2 — Topic vocabulary (15 min)", [
        "Students match the 10 words to their definitions alone (5 min). Item 0 (<i>thrill</i> — k) is the example.",
        "Pairs compare. Check answers, drill pronunciation of <i>adrenaline</i> /əˈdrɛnəlɪn/, <i>exhilarating</i> "
        "/ɪɡˈzɪləreɪtɪŋ/, <i>hazardous</i> /ˈhæzərdəs/, <i>endurance</i> /ɪnˈdʊrəns/ (3 min).",
        "Students complete the Part B paragraph with the words from Part A, alone (5 min). <i>Adrenaline</i> is "
        "used in the example.",
        "Quick check (2 min). Point out the clues that decide each gap: <i>A typical ___ will jump</i> needs a "
        "noun (daredevil); <i>most of these people are not ___</i> needs an adjective (reckless).",
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
    stage("Stage 4 — Summary + town council debate (25 min)", [
        "60-second summary (8 min): 1 minute to plan from notes, then students summarize the lecture to a "
        "partner, timed, and swap. If phones are allowed, they record themselves.",
        'Debate set-up (3 min): groups of up to six. Read the five "How the debate works" steps and the example '
        "pitch opening aloud. Hand out the role cards: five advocates (Rescue team chief, Tourism board, Extreme "
        "athlete, Insurance company, Local taxpayer) and one Council Chair. With smaller groups, leave out the "
        "Insurance company first, then the Tourism board.",
        "Prep (4 min): advocates read their card and prepare a 1-minute pitch. The Chair prepares questions.",
        "Debate (8 min): each advocate pitches (1 min), then open discussion. The Chair must pick one policy and "
        "justify the decision in 30 seconds.",
        "Feedback (2 min): each Chair announces the decision and the deciding reason.",
    ]),
    '<div class="block" style="margin-top:10pt">Break (15 min) · Block 2 (60 min)</div>',
    stage("Stage 5 — Speculating about causes and motives (20 min)", [
        "Discovery (5 min): students underline the deduction and cause language in the six lecture extracts "
        "in Part A.",
        "Concept check (3 min): draw a line from 0% to 100% on the board and place <i>can't have known</i>, "
        "<i>might have felt</i> and <i>must have felt</i> on it. Ask \"Was the professor there in 1979? So how "
        "can he say <i>must</i>?\" (He is deducing from evidence.) Then board the cause phrases and their "
        "patterns: <i>stem from + noun</i>, <i>be driven by + noun</i>, <i>which explains why + clause</i>.",
        "Controlled practice (7 min): pairs write one speculative sentence for each of the six situations in "
        "Part B, using a different structure each time.",
        'Build a Sentence (5 min): go through the three "How to build a sentence" steps and the example, then '
        "students reorder the five scrambled sentences in Part C, a direct copy of the TOEFL task format. "
        "Fastest pair writes answers on the board.",
    ]),
    stage("Stage 6 — Academic Discussion post (30 min)", [
        "Task intro (3 min): read the prompt aloud. Remind students that the TOEFL rewards a new idea, not a "
        "repeat of Sofia's or Daniel's post.",
        "Timed writing (10 min): strict timer. Minimum 100 words, at least two Worksheet 5 structures and one "
        "concession.",
        "Peer review (7 min): swap papers. Partners use the checklist and underline every Worksheet 5 structure "
        "they find.",
        "Class upgrade (10 min): copy two or three anonymous sentences onto the board and improve them together. "
        "Then show the model answer from the key.",
    ]),
    stage("Stage 7 — Listen and Repeat + homework set-up (10 min)", [
        "Read the seven sentences in Script C aloud, one at a time (or play them). Students repeat exactly, "
        "chorally first, then two or three individuals per sentence (6 min). Sentences get longer, so watch for "
        "dropped words and the weak form of <i>have</i> in <i>must have</i> /ˈmʌstəv/.",
        "Homework set-up (4 min): go through the email task on Worksheet 7. Elicit polite request language "
        "(<i>I was wondering if it would be possible to…</i>) and one reason a charity might matter to someone.",
    ]),
    "<p><b>Homework.</b> Worksheet 7, Write an Email (about 120 words).</p>",
)

# ── Answer Key ──
key_2a = nlist([f"{w.split(' (')[0]} — {k}" for w, k in VOCAB])
key_2b = nlist(PARA_KEY) + ('<div class="why">2 vs 7: "A typical ___ will jump" needs a noun (<i>daredevil</i>); '
                            '"are not ___" needs an adjective (<i>reckless</i>). 1 vs 5: "seem to ___ danger" '
                            'takes an object (<i>thrive on</i>).</div>')
frame_key = tbl(["Section", "Claim", "Evidence / example"], [
    ["Definition <i>(example)</i>", "Need for new, varied, intense experiences",
     "Zuckerman, US psychologist, 1960s; high scorers bored easily in routine"],
    ["Who seeks sensation most", "Peaks in late teens / early 20s", "Declines slowly with age; may explain higher "
     "car insurance for young drivers"],
    ["Reason 1: the brain", "More dopamine in response to novelty", "Some studies; evidence still mixed but promising"],
    ["Reason 2: risk perception", "High seekers judge risk as lower", "Roller coaster: one friend terrified, one "
     "almost bored; less anxiety"],
    ["Reason 3: flow", "Total concentration; challenge = skill", "Csikszentmihalyi; time disappears; climbers, "
     "surfers, runners"],
    ["Example 1: bungee jumping", "Close to a pure thrill", "1979, Oxford Univ. club, Clifton Suspension Bridge, "
     "England"],
    ["Example 2: marathons", "Little danger; test of endurance", "Runner's high; endocannabinoids may matter more "
     "than endorphins"],
    ["Example 3: firefighters", "Real risk, but part of a job; purpose", "Slightly above-average sensation seeking; "
     "help + team; years of training → calculated risk"],
    ["Conclusion", "Risk-taking is not one single trait", "Motives differ; most are careful planners, not reckless"],
], widths=["20%", "30%", "50%"])
WHY_3D = [
    ("Main idea", "a and d are never discussed; c is only one small part of the lecture."),
    ("Detail", "He defines it as the need for new, varied and intense experiences; a is the opposite; b and d are "
               "not mentioned."),
    ("Detail", "It tends to peak in the late teens and early twenties, then declines slowly, so c and d are wrong."),
    ("Attitude", 'He says "the evidence here is still mixed, but it\'s a promising line of research", so a is too '
                 "strong; b and c are not stated."),
    ("Purpose", "The ride is identical but the experience is not; he is not warning about danger (b) or explaining "
                "adrenaline (d)."),
    ("Detail", "Csikszentmihalyi's flow is total concentration when challenge matches skill; a describes fear, "
               "not flow."),
    ("Detail", "Members of an Oxford University club jumped from the Clifton Suspension Bridge in 1979; New Zealand (a) "
               "is not mentioned."),
    ("Detail", "Researchers used to credit endorphins (b), but recent studies suggest endocannabinoids may play a "
               "bigger role."),
    ("Inference", "The job is driven by a desire to help, which explains why many stay for decades; pay (a) and "
                  "options (d) are not mentioned, and b contradicts the lecture."),
    ("Main idea", "Motives differ, and most people who do extreme activities are careful planners, not reckless "
                  "thrill-seekers. c and d contradict the lecture; a is not discussed."),
]
key_3d = tbl(["#", "Ans.", "Type", "Why the distractors are wrong"],
             [[str(i), f"<b>{a}</b>", t, w] for i, (a, (t, w)) in enumerate(zip(KEY_3D, WHY_3D), 1)],
             widths=["5%", "7%", "13%", "75%"])
key_5a = nlist(["<i>might</i>; <i>explain why</i> (cause)", "<i>may</i>; <i>lie in</i> (cause)",
                "<i>seems to</i>; <i>stem from</i> (cause)", "<i>must have felt</i> (almost sure: yes)",
                "<i>can't have known</i> (almost sure: no)",
                "<i>is driven by</i>; <i>which explains why</i> (cause)"])
key_5c = nlist([
    "She must have felt terrified.",
    "Their work is driven by a desire to help.",
    "They can't have known the danger.",
    "Their love of risk may stem from childhood experiences.",
    "That's why they stay calm under pressure.",
])
key_5b = nlist([
    "Leo must love pushing his limits. / His hobby is probably driven by a need for challenge.",
    "Mia must have been terrified. / She can't have enjoyed the first jump very much.",
    "He can't have known that a storm was coming. / He might have underestimated the danger.",
    "Their choice is often driven by a desire to help others, which explains why so many apply.",
    "This may stem from the way the brain responds to novelty at that age.",
    "He might have wanted to prove that age is just a number.",
])
model_post = (
    '<p class="serif">Both Sofia and Daniel make reasonable points, but I think they are missing one group of '
    "students: those whose families could never pay for climbing or rafting. For these teenagers, a school trip "
    "may be their only chance to push their limits in a safe, supervised setting. Daniel's concern probably "
    "comes from cases where trips were badly organized, and that risk is real. However, accidents usually stem "
    "from poor planning rather than from the activity itself. If schools hire certified instructors and teach "
    "students how to judge a calculated risk, the danger becomes much smaller. In my view, cancelling these trips "
    "would not make students safer; it would simply mean that only wealthier teenagers get the chance to "
    "overcome their fears and discover what they are capable of.</p>"
    '<div class="why">Why it scores well: a new idea (fair access) instead of simply choosing Sofia or Daniel; '
    "four Worksheet 5 structures (<i>may be, probably comes from, stem from, would</i>); one concession "
    "(<i>…and that risk is real. However,</i>); three lesson terms (<i>push their limits, calculated risk, "
    "overcome</i>).</div>"
)
answer_key = ws(
    header(TOPIC, "Answer Key", "Answer Key",
           "Answers for Worksheets 2, 3, 5 and 6. Worksheets 1, 4 and 7 are open tasks with no fixed answers.",
           outline=True),
    kgrid(kcard("2A", "Vocabulary — matching", key_2a), kcard("2B", "Vocabulary — paragraph", key_2b)),
    kcard("3B", "Listening — main idea (sample)",
          "<p style='margin:0'>Some people crave risk because of sensation seeking, which may be linked to the "
          "brain, to how they perceive danger and to the experience of flow; but motives differ, and most "
          "risk-takers plan carefully.</p>"),
    kcard("3C", "Listening — note frame (sample)", frame_key),
    kcard("3D", "Listening — questions", key_3d),
    kgrid(kcard("5A", "Speculating — discovery", key_5a), kcard("5C", "Build a Sentence", key_5c)),
    kcard("5B", "Speculating — sample answers (accept any accurate structure)", key_5b),
    kcard("6", "Model Academic Discussion post (about 135 words)", model_post),
)

# ── Scripts ──
LECTURE = [
    "Okay, let's begin. Picture this: you're standing on a bridge, there's a rope tied around your ankles, and "
    "you're about to jump. Some of you are probably thinking, \"Never.\" Others are thinking, \"When can I go?\" "
    "So today's question is: why are some people drawn to danger while others avoid it?",
    "Psychologists call this trait sensation seeking. The idea comes from Marvin Zuckerman, an American "
    "psychologist who began studying it in the 1960s. Simply put, sensation seeking is the need for experiences "
    "that are new, varied and intense, and the willingness to take risks to get them. Zuckerman found that high "
    "scorers on his scale also feel restless in predictable situations. That might explain why some people get "
    "bored so easily in a routine job.",
    "Sensation seeking isn't spread evenly across the population. On average, it tends to peak in the late "
    "teens and early twenties, and then it declines slowly with age. That may be one reason car insurance costs "
    "more for young drivers.",
    "So where does it come from? Part of the answer may lie in the brain. Dopamine is a chemical linked to "
    "reward and motivation. Some studies suggest that in high sensation seekers, the brain releases more dopamine "
    "in response to something new or exciting. In other words, their interest in danger seems to stem from a "
    "stronger response to novelty. I should say the evidence here is still mixed, but it's a promising line of "
    "research.",
    "The second piece is how people perceive risk. Imagine two friends on the same roller coaster. One is "
    "screaming in terror; the other is almost bored. The ride is identical, but their experience is not. Research "
    "shows that high sensation seekers tend to judge risky activities as less dangerous, and they feel less "
    "anxiety while doing them.",
    "The third piece is something called flow. The psychologist Mihaly Csikszentmihalyi used this word for a "
    "state of total concentration, when the challenge of a task matches your skill. Time seems to disappear. "
    "Climbers, surfers and long-distance runners often describe exactly this feeling, and for many of them it's "
    "the real reward, not the danger itself.",
    "Let's apply this to three examples. Bungee jumping is close to a pure thrill. The first modern jumps were "
    "made in 1979, when members of an Oxford University club leapt from the Clifton Suspension Bridge in England. "
    "The first jumpers must have felt terrified as they stepped off the bridge. They can't have known exactly how "
    "the ropes would behave.",
    "Marathons are different. The danger is small; the challenge is endurance. Runners often talk about a "
    "\"runner's high,\" a feeling of calm and happiness during a long run. Researchers used to credit endorphins, "
    "but more recent studies suggest that other chemicals, called endocannabinoids, may play a bigger role.",
    "And firefighters? Here the risk is real, but it's part of a job. Some studies have found that firefighters "
    "score slightly above average for sensation seeking. Yet when you ask them, most talk about helping people "
    "and about the team. For most firefighters, the job is driven by a desire to help, which explains why many "
    "stay in it for decades. And they don't ignore danger: they train for years so that every risk they take is "
    "a calculated one.",
    "So, what's the takeaway? Risk-taking is not one single trait. A bungee jumper, a marathon runner and a "
    "firefighter may look similar from the outside, but their motives are very different. And, perhaps "
    "surprisingly, most people who do extreme activities are careful planners, not reckless thrill-seekers.",
    "For next class, think about the riskiest thing you've ever done. What was really driving you? We'll start "
    "there next time.",
]
REPEAT = [
    "Some people love danger.",
    "Her heart was racing at the top.",
    "Firefighters take calculated risks every day.",
    "Sensation seeking tends to peak in our early twenties.",
    "The first jumpers must have felt terrified on the bridge.",
    "For most firefighters, the job is driven by a desire to help others.",
    "Most people who do extreme sports are careful planners, not reckless thrill-seekers.",
]
scripts = ws(
    header(TOPIC, "Scripts", "Teacher",
           "Teacher-read scripts. If the audio fails, read Script A aloud at a natural pace; it runs about 4 minutes.",
           outline=True),
    sec("A", 'Lecture: "Why We Crave Risk"', "About 620 words"),
    '<p class="serif muted" style="font-style:italic">Professor (male), introductory psychology class.</p>',
    "".join(f'<p class="serif">{p}</p>' for p in LECTURE),
    '<div style="page-break-inside:avoid">',
    sec("B", "Model 60-second summary", "About 120 words"),
    '<p class="serif">The lecture was about why some people are drawn to risk. The professor explained '
    "sensation seeking, Marvin Zuckerman's term for the need for new, varied and intense experiences. It tends to "
    "peak in the late teens and early twenties. He gave three possible reasons for it: the brain may release more "
    "dopamine in response to novelty, high sensation seekers perceive less risk, and many people enjoy the "
    "feeling of flow, when the challenge matches their skill. He then compared bungee jumping, which is close to "
    "a pure thrill, marathons, which test endurance, and firefighting, which is driven by a desire to help. He "
    "concluded that motives differ, and that most risk-takers plan carefully.</p></div>",
    sec("C", "Listen and Repeat", "7 sentences"),
    "<p>Read each sentence once at natural speed. Students repeat it exactly.</p>",
    nlist(REPEAT, cls="tight"),
    sec("♪", "Audio", "Browser text-to-speech"),
    "<p>Play Script A and Script C through the browser's built-in text-to-speech, or read them live.</p>",
    tbl(["Track", "Where it starts", "Length"], [
        ["Script A, full lecture", '"Okay, let\'s begin."', "About 4 min"],
        ['Script A, second half (the three examples)', '"Let\'s apply this to three examples."', "About 1.5 min"],
        ["Script C, Listen and Repeat", "Sentence 1", "About 1.5 min with gaps"],
    ], widths=["46%", "34%", "20%"]),
    "<p><b>Settings.</b> Speed 0.95× suits advanced learners and is close to TOEFL lecture pace; raise it to "
    "1.05× for a challenge. Repeat gap 5 seconds; use 7–8 seconds for sentences 6 and 7.</p>",
    '<p><b>Best voices.</b> In Edge, pick a "Microsoft … Online (Natural)" US English voice. In Chrome, pick '
    '"Google US English". Test the voice on the classroom speakers before the lesson.</p>',
    "<p><b>In class.</b> Do not pause during the first two listenings in Stage 3, to match test conditions. "
    "Backup: in Edge, select Script A and right-click → Read aloud selection, or read it live.</p>",
)

TEACHER = [overview, steps, answer_key, scripts]

if __name__ == "__main__":
    out = ROOT / "advanced"
    build(STUDENT, out / f"{SLUG}_Student_Pack.pdf", LEVEL, FOOT_TOPIC)
    build(TEACHER, out / f"{SLUG}_Teacher_Guide.pdf", LEVEL, FOOT_TOPIC)
    print("built", out)
