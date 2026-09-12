"""Visual theme for InterviewForge AI — an ironworks / forge motif.

Palette:
  iron-900  #1B1815   warm near-black background
  iron-800  #26221D   panel background
  iron-700  #362D23   card borders / chips
  ash-100   #F3EEE4   primary text / cream
  ash-300   #CDC3B3   secondary text
  ember     #E8622C   primary accent (hot metal)
  gold      #E8A93A   secondary accent (spark / highlight)
  slate     #9AA3A0   muted steel for labels
  good/warn/bad        semantic colors used ONLY for score bands, so a
                       reading is never conveyed by color alone (a text
                       label always sits next to it too)
Typography: Space Grotesk for headings (geometric, industrial),
IBM Plex Sans for body copy — a deliberate pairing, not the default
Streamlit sans-serif.
"""

# Icon shown next to each pipeline stage — sidebar stepper + page headers.
STEP_ICONS = [
    "🗂️",  # Setup
    "🪪",  # Candidate & Job Profiles
    "🔍",  # Information Check
    "🎯",  # Job Match Analysis
    "🧯",  # Interview Risk Engine
    "❓",  # Question Engine
    "📶",  # Question Priority
    "🧭",  # Answer Blueprint
    "🥊",  # Tough Question Coach
    "🛡️",  # Battle Plan & Forge Score
    "🔁",  # Practice & Refine Loop
]

FORGE_CSS = """
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">

<style>
:root {
  --iron-900: #1B1815;
  --iron-800: #262019;
  --iron-700: #362D23;
  --ash-100: #F3EEE4;
  --ash-300: #CDC3B3;
  --ember: #E8622C;
  --ember-dim: #B84A1E;
  --gold: #E8A93A;
  --slate: #9AA3A0;
  --good: #7CB68A;
  --warn: #E8A93A;
  --bad: #DD6B5B;
}

html, body, [class*="css"]  {
  font-family: 'IBM Plex Sans', sans-serif;
  font-size: 16px;
}

.stApp {
  background:
    radial-gradient(ellipse 900px 500px at 15% -10%, rgba(232,98,44,0.12), transparent 60%),
    radial-gradient(ellipse 700px 500px at 100% 0%, rgba(232,169,58,0.07), transparent 55%),
    var(--iron-900);
  color: var(--ash-100);
}

h1, h2, h3, h4 {
  font-family: 'Space Grotesk', sans-serif !important;
  color: var(--ash-100) !important;
  letter-spacing: -0.01em;
}
h3 { display: flex; align-items: center; gap: 10px; }

p, li, span, label, div { line-height: 1.55; }

/* ---------------------------------------------------------------- */
/* Hero title bar                                                    */
/* ---------------------------------------------------------------- */
.forge-hero {
  display: flex;
  align-items: center;
  gap: 16px;
  border-bottom: 1px solid var(--iron-700);
  padding-bottom: 18px;
  margin-bottom: 4px;
}
.forge-hero .anvil {
  font-size: 2.3rem;
  line-height: 1;
  filter: drop-shadow(0 0 10px rgba(232,98,44,0.45));
}
.forge-hero h1 {
  font-size: 2.1rem !important;
  margin: 0 !important;
  background: linear-gradient(90deg, var(--ash-100) 25%, var(--ember) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.forge-tagline {
  color: var(--slate);
  font-size: 0.97rem;
  margin-top: -6px;
  margin-bottom: 14px;
}

/* Progress readout under the hero */
.forge-progress-label {
  display: flex;
  justify-content: space-between;
  font-size: 0.82rem;
  color: var(--slate);
  margin-bottom: 4px;
}
.forge-progress-label b { color: var(--gold); font-family: 'Space Grotesk', sans-serif; }
div[data-testid="stProgress"] > div > div {
  background-color: var(--iron-700) !important;
}
div[data-testid="stProgress"] > div > div > div {
  background-image: linear-gradient(90deg, var(--ember), var(--gold)) !important;
}

/* ---------------------------------------------------------------- */
/* Stage stepper (sidebar)                                           */
/* ---------------------------------------------------------------- */
.stage-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 10px;
  border-radius: 9px;
  margin-bottom: 3px;
  font-size: 0.9rem;
  transition: background 0.15s ease;
}
.stage-item .icon { font-size: 1.0rem; width: 20px; text-align: center; flex-shrink: 0; }
.stage-item .num {
  width: 20px; height: 20px;
  border-radius: 5px;
  display: flex; align-items: center; justify-content: center;
  font-size: 0.7rem;
  font-family: 'Space Grotesk', sans-serif;
  flex-shrink: 0;
}
.stage-current { background: rgba(232,98,44,0.16); border: 1px solid rgba(232,98,44,0.35); }
.stage-current .num { background: var(--ember); color: #1B1815; font-weight: 700; }
.stage-current span.label { color: var(--ash-100); font-weight: 600; }
.stage-done .num { background: var(--iron-700); color: var(--gold); border: 1px solid var(--gold); }
.stage-done span.label { color: var(--ash-300); }
.stage-todo .num { background: var(--iron-700); color: var(--slate); }
.stage-todo span.label { color: var(--slate); }

/* ---------------------------------------------------------------- */
/* Cards                                                             */
/* ---------------------------------------------------------------- */
.forge-card {
  background: linear-gradient(180deg, var(--iron-800), var(--iron-800) 96%);
  border: 1px solid var(--iron-700);
  border-left: 4px solid var(--ember);
  border-radius: 12px;
  padding: 16px 20px;
  margin-bottom: 14px;
  transition: transform 0.15s ease, box-shadow 0.15s ease;
}
.forge-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 22px rgba(0,0,0,0.28);
}
.forge-card h4 {
  margin-top: 0 !important;
  font-size: 1.05rem !important;
  display: flex; align-items: center; flex-wrap: wrap; gap: 6px;
}
.forge-card p, .forge-card li { color: var(--ash-100); }
.forge-card b, .forge-card strong { color: var(--gold); font-weight: 600; }
.forge-card em { color: var(--ash-300); }
.forge-card ul { margin: 4px 0 10px 0; padding-left: 20px; }
.forge-card.gold { border-left-color: var(--gold); }
.forge-card.slate { border-left-color: var(--slate); }
.forge-card.good { border-left-color: var(--good); }
.forge-card.bad { border-left-color: var(--bad); }

/* ---------------------------------------------------------------- */
/* Priority chips                                                    */
/* ---------------------------------------------------------------- */
.chip {
  display: inline-block;
  font-size: 0.72rem;
  font-family: 'Space Grotesk', sans-serif;
  padding: 2px 10px;
  border-radius: 20px;
  font-weight: 600;
  margin-left: 8px;
  vertical-align: middle;
}
.chip-high { background: rgba(232,98,44,0.20); color: var(--ember); border: 1px solid var(--ember-dim); }
.chip-medium { background: rgba(232,169,58,0.20); color: var(--gold); border: 1px solid var(--gold); }
.chip-low { background: rgba(154,163,160,0.20); color: var(--slate); border: 1px solid var(--slate); }

/* ---------------------------------------------------------------- */
/* Score blocks                                                      */
/* ---------------------------------------------------------------- */
.score-block {
  text-align: center;
  background: var(--iron-800);
  border: 1px solid var(--iron-700);
  border-top: 4px solid var(--slate);
  border-radius: 14px;
  padding: 20px 10px 16px;
  transition: transform 0.15s ease;
}
.score-block:hover { transform: translateY(-2px); }
.score-block .num {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 2.3rem;
  font-weight: 700;
}
.score-block .band {
  font-size: 0.72rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-top: 2px;
}
.score-block .label {
  font-size: 0.8rem;
  color: var(--slate);
  text-transform: uppercase;
  letter-spacing: 0.04em;
  margin-top: 6px;
}

/* ---------------------------------------------------------------- */
/* Buttons                                                           */
/* ---------------------------------------------------------------- */
div.stButton > button, div.stDownloadButton > button {
  background: var(--ember);
  color: #1B1815;
  border: none;
  font-family: 'Space Grotesk', sans-serif;
  font-weight: 600;
  border-radius: 22px;
  padding: 0.55em 1.3em;
  box-shadow: 0 2px 10px rgba(232,98,44,0.25);
  transition: transform 0.12s ease, background 0.12s ease;
}
div.stButton > button:hover, div.stDownloadButton > button:hover {
  background: var(--gold);
  color: #1B1815;
  transform: translateY(-1px);
}
div.stButton > button:disabled {
  background: var(--iron-700);
  color: var(--slate);
  box-shadow: none;
}

/* ---------------------------------------------------------------- */
/* Tabs, expanders, inputs                                           */
/* ---------------------------------------------------------------- */
button[data-baseweb="tab"] {
  font-family: 'Space Grotesk', sans-serif;
  color: var(--slate) !important;
}
button[data-baseweb="tab"][aria-selected="true"] {
  color: var(--ember) !important;
  border-bottom-color: var(--ember) !important;
}
div[data-testid="stExpander"] {
  border: 1px solid var(--iron-700) !important;
  border-radius: 10px !important;
  background: var(--iron-800);
}
input, textarea {
  background-color: var(--iron-800) !important;
  color: var(--ash-100) !important;
  border-color: var(--iron-700) !important;
}

section[data-testid="stSidebar"] {
  background: var(--iron-800);
  border-right: 1px solid var(--iron-700);
}

hr { border-color: var(--iron-700) !important; }

/* Small helper text under section headers */
.forge-caption { color: var(--slate); font-size: 0.88rem; margin-top: -8px; }
</style>
"""


def hero_html(title="InterviewForge AI", tagline="Forge a sharper interview, one stage at a time."):
    return f"""
<div class="forge-hero">
  <div class="anvil">🔥</div>
  <h1>{title}</h1>
</div>
<div class="forge-tagline">{tagline}</div>
"""


def progress_label_html(step_index, total, step_name):
    pct = int(round((step_index) / (total - 1) * 100)) if total > 1 else 0
    return (
        f'<div class="forge-progress-label">'
        f'<span>Stage <b>{step_index + 1}</b> of {total} &middot; {step_name}</span>'
        f'<span>{pct}% through the pipeline</span></div>'
    )


def stage_sidebar_html(steps, icons, current_index):
    rows = []
    for i, name in enumerate(steps):
        icon = icons[i] if i < len(icons) else "•"
        if i < current_index:
            cls, mark = "stage-done", "✓"
        elif i == current_index:
            cls, mark = "stage-current", str(i + 1)
        else:
            cls, mark = "stage-todo", str(i + 1)
        rows.append(
            f'<div class="stage-item {cls}"><div class="num">{mark}</div>'
            f'<div class="icon">{icon}</div>'
            f'<span class="label">{name}</span></div>'
        )
    return "<div>" + "".join(rows) + "</div>"


def chip(priority):
    p = (priority or "").lower()
    cls = "chip-high" if p == "high" else "chip-medium" if p == "medium" else "chip-low"
    return f'<span class="chip {cls}">{priority}</span>'


def score_band(value):
    """Return (band_label, color) for a 0-100 score."""
    try:
        v = float(value)
    except (TypeError, ValueError):
        return "—", "var(--slate)"
    if v >= 75:
        return "Strong", "var(--good)"
    if v >= 50:
        return "Developing", "var(--warn)"
    return "Needs work", "var(--bad)"


def score_block_html(value, label):
    band, color = score_band(value)
    display_val = value if value is not None else "—"
    return (
        f'<div class="score-block" style="border-top-color:{color}">'
        f'<div class="num" style="color:{color}">{display_val}</div>'
        f'<div class="band" style="color:{color}">{band}</div>'
        f'<div class="label">{label}</div></div>'
    )
