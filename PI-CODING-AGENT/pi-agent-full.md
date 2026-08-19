---
marp: true
paginate: true
html: true
size: 4:3
style: |
  @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,400;0,500;0,600;1,400&family=STIX+Two+Text:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap');

  :root {
    --body: 'STIX Two Text', 'Latin Modern Roman', Georgia, serif;
    --mono: 'JetBrains Mono', 'IBM Plex Mono', ui-monospace, monospace;
    --white:       #e8e7e3;
    --off-white:   #c9c8c3;
    --subtle:      #a7a6a1;
    --muted:       #85847f;
    --faint:       #4e4e4a;
    --bg:          #121313;
    --card-border: #2a2a28;
  }

  section {
    font-family: var(--body);
    background: var(--bg);
    color: var(--white);
    padding: 64px 88px 72px;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    position: relative;
  }

  h1 {
    font-size: 40px;
    font-weight: 600;
    line-height: 1.12;
    margin: 0 0 16px 0;
    color: var(--white);
    letter-spacing: 0;
  }
  h2 {
    font-size: 28px;
    font-weight: 600;
    line-height: 1.15;
    margin: 0 0 18px 0;
    color: var(--white);
    letter-spacing: 0;
    border: none;
  }
  p {
    font-size: 17px;
    line-height: 1.65;
    color: var(--subtle);
    margin: 0 0 14px 0;
  }
  strong { color: var(--white); font-weight: 600; }
  em     { color: var(--muted); font-style: italic; }
  code {
    font-family: var(--mono);
    background: transparent;
    border: none;
    color: var(--white);
    padding: 0;
    border-radius: 0;
    font-size: 0.9em;
  }
  .header-row {
    display: flex;
    justify-content: flex-start;
    align-items: baseline;
    gap: 20px;
    margin-bottom: 28px;
  }
  .header-row h2 {
    margin: 0;
    font-size: 30px;
  }
  .page-num {
    font-family: var(--mono);
    font-size: 30px;
    line-height: 1.15;
    color: var(--muted);
    letter-spacing: 0;
    flex-shrink: 0;
  }
  .cards-col {
    display: flex;
    flex-direction: column;
    gap: 10px;
    width: 100%;
    max-width: 720px;
    margin: 0 auto 16px;
  }
  .card-row {
    background: transparent;
    border: none;
    border-left: 1px solid var(--card-border);
    border-radius: 0;
    padding: 0 0 0 18px;
    display: flex;
    align-items: flex-start;
    gap: 14px;
  }
  .card-row-letter {
    font-family: var(--mono);
    font-size: 12px;
    color: var(--muted);
    flex-shrink: 0;
    margin-top: 1px;
    min-width: 16px;
  }
  .card-row-body h3 {
    font-size: 16px;
    font-weight: 600;
    color: var(--white);
    margin: 0 0 3px;
  }
  .card-row-body p {
    font-size: 15px;
    color: var(--subtle);
    margin: 0;
    line-height: 1.45;
  }

  .list {
    display: flex;
    flex-direction: column;
    gap: 9px;
    width: 100%;
    max-width: 720px;
    margin: 0 auto 16px;
  }
  .list-item {
    display: flex;
    align-items: flex-start;
    gap: 16px;
    background: transparent;
    border: none;
    border-radius: 0;
    padding: 0;
  }
  .list-num {
    font-family: var(--mono);
    font-size: 12px;
    color: var(--muted);
    flex-shrink: 0;
    margin-top: 1px;
    min-width: 18px;
  }
  .list-text { font-size: 16px; color: var(--subtle); line-height: 1.45; }
  .list-text strong { color: var(--white); }

  section.cover {
    justify-content: center;
    text-align: center;
    padding-bottom: 72px;
    background: #0f1010;
  }
  .cover-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    max-width: 720px;
  }
  .cover-kicker,
  .cta-kicker {
    font-family: var(--mono);
    font-size: 12px;
    color: var(--muted);
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 24px;
  }
  section.cover h1 {
    font-size: 58px;
    line-height: 1.05;
    margin-bottom: 18px;
  }
  section.cover p {
    max-width: 620px;
    font-size: 20px;
    color: var(--subtle);
    margin-bottom: 20px;
  }
  .cover-meta {
    display: flex;
    flex-direction: column;
    gap: 6px;
    font-family: var(--mono);
    font-size: 12px;
    color: var(--muted);
    letter-spacing: 2px;
    text-transform: uppercase;
  }

  section.divider {
    justify-content: center;
    border-left: 5px solid var(--off-white);
    background: #171817;
  }
  section.divider h1 { font-size: 42px; color: var(--white); margin-bottom: 10px; }
  section.divider p  { font-size: 15px; color: var(--muted); }

  section.cta {
    justify-content: center;
    align-items: center;
    text-align: center;
    background: #e9e9e5;
  }
  section.cover::after,
  section.cta::after {
    display: none !important;
  }
  .cta-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    max-width: 720px;
  }
  section.cta h1 {
    color: #171716;
    font-size: 44px;
    line-height: 1.1;
    letter-spacing: 0;
    margin-bottom: 24px;
  }
  .cta-line {
    font-family: var(--mono);
    font-size: 13px;
    color: #65645f;
    letter-spacing: 1px;
    margin-bottom: 4px;
  }
  section.cta .handle {
    font-family: var(--mono);
    font-size: 13px;
    color: #555550;
    margin-top: 22px;
    letter-spacing: 2px;
    text-transform: uppercase;
  }

  section > .header-row,
  section > h2 {
    width: 100%;
    max-width: 720px;
  }

  section::after {
    font-family: var(--mono);
    font-size: 9px;
    color: var(--muted);
    letter-spacing: 1px;
    content: 'PI CODING AGENT · ' attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);
    position: absolute;
    bottom: 20px;
    right: 40px;
  }

  .code-block {
    width: 100%;
    max-width: 720px;
    box-sizing: border-box;
    margin: 8px auto 14px;
    padding: 14px 18px;
    border-left: 1px solid var(--card-border);
    color: var(--off-white);
    font-family: var(--mono);
    font-size: 14px;
    line-height: 1.45;
    white-space: pre-wrap;
  }
  .code-block .comment { color: var(--muted); }
  .note {
    width: 100%;
    max-width: 720px;
    box-sizing: border-box;
    margin: 14px auto 0;
    padding-left: 18px;
    border-left: 1px solid var(--card-border);
    color: var(--muted);
    font-size: 14px;
    line-height: 1.45;
  }
  .two-col {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 28px;
    width: 100%;
    max-width: 720px;
    margin: 0 auto;
  }
  .two-col > div { min-width: 0; }
  .two-col h3 {
    margin: 0 0 8px;
    color: var(--white);
    font-size: 16px;
  }
  .small { font-size: 14px; line-height: 1.45; }

  /* Simple explanatory visuals */
  .visual {
    width: 100%;
    max-width: 720px;
    margin: 0 auto 18px;
  }
  .diagram-node {
    border: 1px solid var(--card-border);
    padding: 12px 14px;
    color: var(--subtle);
    font-size: 13px;
    line-height: 1.35;
    box-sizing: border-box;
  }
  .diagram-node strong {
    display: block;
    color: var(--white);
    font-family: var(--mono);
    font-size: 12px;
    letter-spacing: .4px;
    margin-bottom: 4px;
  }
  .diagram-node small {
    color: var(--muted);
    font-size: 12px;
  }
  .mental-hub {
    display: grid;
    grid-template-columns: 1fr auto 1fr auto 1fr auto 1fr;
    gap: 8px;
    align-items: stretch;
  }
  .mental-hub .core {
    border-color: var(--off-white);
    text-align: center;
  }
  .hub-arrow {
    display: flex;
    align-items: center;
    color: var(--muted);
    font-family: var(--mono);
    font-size: 16px;
  }
  .mental-hub .resources {
    grid-column: 3;
    position: relative;
    margin-top: 18px;
    text-align: center;
  }
  .mental-hub .resources::before {
    content: '↑';
    position: absolute;
    top: -23px;
    left: 0;
    right: 0;
    color: var(--muted);
    font-family: var(--mono);
    font-size: 15px;
  }

  .mental-grid {
    display: grid;
    grid-template-columns: 1fr 1.15fr 1fr;
    grid-template-areas: "project . model" ". core ." "tools . resources";
    gap: 12px;
    align-items: center;
  }
  .mental-grid .project { grid-area: project; }
  .mental-grid .model { grid-area: model; }
  .mental-grid .core {
    grid-area: core;
    text-align: center;
    border-color: var(--off-white);
    padding: 18px 14px;
  }
  .mental-grid .tools { grid-area: tools; }
  .mental-grid .resources { grid-area: resources; }
  .session-tree {
    display: grid;
    grid-template-columns: 1.1fr auto 1fr;
    grid-template-rows: 1fr 1fr auto;
    grid-template-areas: "root branch-a fork" "root branch-b clone" "recover recover recover";
    gap: 10px;
    align-items: center;
  }
  .session-tree .root { grid-area: root; }
  .session-tree .branch-a { grid-area: branch-a; color: var(--muted); font-family: var(--mono); }
  .session-tree .branch-b { grid-area: branch-b; color: var(--muted); font-family: var(--mono); }
  .session-tree .fork { grid-area: fork; }
  .session-tree .clone { grid-area: clone; }
  .session-tree .recover {
    grid-area: recover;
    text-align: center;
    border-top: 1px solid var(--card-border);
    padding-top: 10px;
  }
  .flow-row {
    display: grid;
    grid-template-columns: 1fr auto 1fr auto 1fr auto 1fr;
    gap: 8px;
    align-items: stretch;
  }
  .flow-step {
    border-left: 1px solid var(--off-white);
    padding: 10px 10px 10px 12px;
    color: var(--subtle);
    font-size: 13px;
    line-height: 1.35;
  }
  .flow-step strong {
    display: block;
    color: var(--white);
    font-family: var(--mono);
    font-size: 11px;
    margin-bottom: 4px;
  }
  .flow-step.human-gate {
    border: 1px solid var(--off-white);
    padding: 10px 12px;
  }
  .flow-step.human-gate::before {
    content: 'HUMAN-OWNED GATE';
    display: block;
    color: var(--off-white);
    font-family: var(--mono);
    font-size: 9px;
    letter-spacing: .5px;
    margin-bottom: 7px;
  }
  .flow-arrow {
    display: flex;
    align-items: center;
    color: var(--muted);
    font-family: var(--mono);
  }
  .session-loop .loop-return {
    grid-column: 1 / -1;
    border-top: 1px solid var(--card-border);
    padding-top: 7px;
    text-align: right;
    color: var(--muted);
    font-family: var(--mono);
    font-size: 11px;
  }
  .tool-map {
    display: grid;
    grid-template-columns: 1fr 1.1fr 1fr;
    grid-template-rows: auto auto auto;
    grid-template-areas: ". model ." "read core write" "edit . bash";
    gap: 10px;
    align-items: center;
  }
  .tool-map .model { grid-area: model; text-align: center; }
  .tool-map .model::after {
    content: '↓';
    display: block;
    color: var(--muted);
    font-family: var(--mono);
    margin-top: 6px;
  }
  .tool-map .core { grid-area: core; text-align: center; border-color: var(--off-white); }
  .tool-map .read { grid-area: read; }
  .tool-map .write { grid-area: write; }
  .tool-map .edit { grid-area: edit; }
  .tool-map .bash { grid-area: bash; }
  .lane-diagram {
    display: grid;
    grid-template-columns: 150px 1fr;
    gap: 0;
    border-top: 1px solid var(--card-border);
  }
  .lane-diagram > div {
    padding: 12px 14px;
    border-bottom: 1px solid var(--card-border);
  }
  .lane-label {
    color: var(--white);
    font-family: var(--mono);
    font-size: 11px;
  }
  .lane-text { color: var(--subtle); font-size: 14px; line-height: 1.4; }
  .trust-contrast {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
  }
  .trust-panel {
    border: 1px solid var(--card-border);
    padding: 14px;
  }
  .trust-panel strong {
    display: block;
    color: var(--white);
    font-family: var(--mono);
    font-size: 11px;
    margin-bottom: 10px;
  }
  .trust-flow {
    display: flex;
    align-items: center;
    gap: 8px;
    color: var(--subtle);
    font-size: 13px;
    line-height: 1.35;
  }
  .trust-flow .arrow { color: var(--muted); font-family: var(--mono); }
  .timeline {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 20px;
  }
  .timeline-step {
    position: relative;
    border-top: 1px solid var(--off-white);
    padding-top: 10px;
    color: var(--subtle);
    font-size: 13px;
    line-height: 1.35;
  }
  .timeline-step.change {
    border-left: 2px solid var(--off-white);
    padding-left: 14px;
  }
  .timeline-step.change::before {
    content: 'SCOPE BOUNDARY';
    position: absolute;
    top: -25px;
    left: 14px;
    color: var(--off-white);
    font-family: var(--mono);
    font-size: 9px;
    letter-spacing: .5px;
  }
  .timeline-step strong {
    display: block;
    color: var(--white);
    font-family: var(--mono);
    font-size: 11px;
    margin-bottom: 4px;
  }
  .timeline-step:not(:last-child)::after {
    content: '→';
    position: absolute;
    top: -9px;
    right: -15px;
    color: var(--muted);
    font-family: var(--mono);
  }
  .context-diagram {
    display: grid;
    grid-template-columns: 1fr auto 1fr;
    gap: 14px;
    align-items: center;
  }
  .context-window {
    border: 1px solid var(--card-border);
    padding: 14px;
    min-height: 118px;
    box-sizing: border-box;
  }
  .context-window h3 {
    margin: 0 0 10px;
    color: var(--white);
    font-size: 15px;
  }
  .context-window p { font-size: 13px; margin: 0 0 8px; }
  .context-window.durable {
    grid-column: 1 / -1;
    border-color: var(--off-white);
    min-height: 0;
  }
  .context-arrow { text-align: center; color: var(--muted); font-family: var(--mono); }
  .output-modes { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; }
  .output-mode {
    border-top: 1px solid var(--off-white);
    padding-top: 10px;
    min-height: 115px;
  }
  .output-mode h3 { margin: 0 0 8px; color: var(--white); font-size: 15px; }
  .output-mode p { font-size: 13px; line-height: 1.4; margin: 0; }
  .stack-diagram { display: flex; flex-direction: column; gap: 7px; max-width: 520px; margin: 0 auto; }
  .stack-layer {
    border: 1px solid var(--card-border);
    padding: 9px 14px;
    color: var(--subtle);
    font-size: 13px;
  }
  .stack-layer strong { color: var(--white); font-family: var(--mono); font-size: 11px; margin-right: 10px; }
  .gate-flow { display: grid; grid-template-columns: 1fr auto 1fr auto 1fr; gap: 10px; align-items: center; }
  .gate { border: 1px solid var(--card-border); padding: 13px; text-align: center; color: var(--subtle); font-size: 13px; }
  .gate strong { display: block; color: var(--white); font-family: var(--mono); font-size: 11px; margin-bottom: 4px; }
  .gate.blocked { border-color: var(--off-white); }
  .integration-diagram { display: grid; grid-template-columns: 1fr auto 1fr auto 1fr; gap: 10px; align-items: center; }
  .integration-node { border: 1px solid var(--card-border); padding: 14px; text-align: center; color: var(--subtle); font-size: 13px; }
  .integration-node strong { display: block; color: var(--white); font-family: var(--mono); font-size: 11px; margin-bottom: 4px; }
  .integration-node.safe,
  .integration-node.json-stream { border-color: var(--off-white); }
  .integration-arrow { color: var(--muted); font-family: var(--mono); }

---
<!-- SLIDE 1 · COVER -->
<!-- _class: cover -->

<div class="cover-content">
  <div class="cover-kicker">PI CODING AGENT · FULL TUTORIAL</div>
  <h1>Build your workflow around Pi</h1>
  <p>A practical guide to installing, using, extending, and safely integrating a minimal terminal coding agent.</p>
  <div class="cover-meta">
    <span>Terminal first</span>
    <span>Four core tools</span>
    <span>Shape the workflow</span>
  </div>
</div>

---

<!-- SLIDE 2 · ROADMAP -->

<div class="header-row">
  <span class="page-num">I.</span>
  <h2>What you will build</h2>
</div>

<div class="cards-col">
  <div class="card-row"><span class="card-row-letter">01</span><div class="card-row-body"><h3>A working local agent</h3><p>Install Pi, authenticate a provider, and complete a real repository task.</p></div></div>
  <div class="card-row"><span class="card-row-letter">02</span><div class="card-row-body"><h3>A project-aware workflow</h3><p>Use context files, Git checkpoints, sessions, and focused prompts.</p></div></div>
  <div class="card-row"><span class="card-row-letter">03</span><div class="card-row-body"><h3>Your first customization</h3><p>Add a skill, prompt template, or safety extension.</p></div></div>
  <div class="card-row"><span class="card-row-letter">04</span><div class="card-row-body"><h3>A path to integration</h3><p>Understand print, JSON, RPC, SDK, packages, and sandboxing.</p></div></div>
</div>

<div class="note">Start with the interactive workflow. Advanced modes make more sense after you have completed one small task with Pi.</div>

---

<!-- SLIDE 3 · DEFINITION -->

<div class="header-row">
  <span class="page-num">II.</span>
  <h2>What Pi is</h2>
</div>

<div class="list">
  <div class="list-item"><span class="list-num">01</span><span class="list-text"><strong>A terminal coding harness</strong> — a model connected to a local project and a small set of tools.</span></div>
  <div class="list-item"><span class="list-num">02</span><span class="list-text"><strong>Provider-agnostic</strong> — authenticate through a subscription or API key, then select a compatible model.</span></div>
  <div class="list-item"><span class="list-num">03</span><span class="list-text"><strong>Extensible</strong> — add skills, prompts, extensions, themes, and packages without forking the core.</span></div>
  <div class="list-item"><span class="list-num">04</span><span class="list-text"><strong>Deliberately small</strong> — workflow features can be added when you actually need them.</span></div>
</div>

---

<!-- SLIDE 4 · MENTAL MODEL -->

<div class="header-row">
  <span class="page-num">III.</span>
  <h2>The mental model</h2>
</div>

<div class="visual mental-hub">
  <div class="diagram-node"><strong>MODEL</strong>Provider · reasoning<br><small>what thinks</small></div>
  <div class="hub-arrow">→</div>
  <div class="diagram-node core"><strong>PI</strong>minimal generic core<br><small>connects the workflow</small></div>
  <div class="hub-arrow">→</div>
  <div class="diagram-node"><strong>TOOLS</strong>read · write · edit · bash<br><small>what can act</small></div>
  <div class="hub-arrow">→</div>
  <div class="diagram-node"><strong>PROJECT</strong>Files · Git · tests<br><small>where Pi runs</small></div>
  <div class="diagram-node resources"><strong>RESOURCES</strong>Rules · skills · prompts<br><small>shape how Pi works</small></div>
</div>

<div class="note"><strong>Core principle:</strong> keep Pi generic; put your team's rules and automation in the project or in a reusable package.</div>

---

<!-- SLIDE 5 · REQUIREMENTS -->

<div class="header-row">
  <span class="page-num">IV.</span>
  <h2>Before you install</h2>
</div>

<div class="list">
  <div class="list-item"><span class="list-num">01</span><span class="list-text"><strong>Node.js and npm</strong> — Pi is distributed as an npm package.</span></div>
  <div class="list-item"><span class="list-num">02</span><span class="list-text"><strong>A model route</strong> — a supported subscription or provider API key.</span></div>
  <div class="list-item"><span class="list-num">03</span><span class="list-text"><strong>A real project</strong> — start in a repository with a clear task.</span></div>
  <div class="list-item"><span class="list-num">04</span><span class="list-text"><strong>A rollback path</strong> — Git, a branch, or a disposable copy.</span></div>
</div>

<div class="note">Pi runs with your user permissions. Installation and project trust are not security sandboxes.</div>

---

<!-- SLIDE 6 · INSTALL -->

<div class="header-row">
  <span class="page-num">V.</span>
  <h2>Install Pi</h2>
</div>

<div class="code-block">npm install -g --ignore-scripts @earendil-works/pi-coding-agent

# Verify the command
pi --version</div>

<div class="list">
  <div class="list-item"><span class="list-num">01</span><span class="list-text"><code>--ignore-scripts</code> disables dependency lifecycle scripts during installation.</span></div>
  <div class="list-item"><span class="list-num">02</span><span class="list-text">On macOS and Linux, the official alternative is <code>curl -fsSL https://pi.dev/install.sh | sh</code>.</span></div>
  <div class="list-item"><span class="list-num">03</span><span class="list-text">Run Pi from the directory you want it to work on.</span></div>
</div>

---

<!-- SLIDE 7 · AUTH -->

<div class="header-row">
  <span class="page-num">VI.</span>
  <h2>Authenticate once</h2>
</div>

<div class="two-col">
  <div><h3>Subscription</h3><div class="code-block">pi
/login</div><p class="small">Choose a supported subscription provider and complete its login flow.</p></div>
  <div><h3>API key</h3><div class="code-block">export ANTHROPIC_API_KEY=sk-ant-...
pi</div><p class="small">Or use <code>/login</code> to store a key in Pi's auth file.</p></div>
</div>

<div class="note">Credentials are stored under <code>~/.pi/agent/auth.json</code>. Never commit this file or place keys in a repository.</div>

---

<!-- SLIDE 8 · FIRST SESSION -->

<div class="header-row">
  <span class="page-num">VII.</span>
  <h2>Run your first session</h2>
</div>

<div class="visual flow-row session-loop">
  <div class="flow-step"><strong>01 · PROJECT</strong><code>cd /your/repo</code><br>Start in the right directory.</div>
  <div class="flow-arrow">→</div>
  <div class="flow-step"><strong>02 · INSPECT</strong>Ask for a summary and the checks.</div>
  <div class="flow-arrow">→</div>
  <div class="flow-step"><strong>03 · ACT</strong>Give one bounded next action.</div>
  <div class="flow-arrow">→</div>
  <div class="flow-step"><strong>04 · VERIFY</strong>Read the response, tools, and result.</div>
  <div class="loop-return">↺ next bounded task</div>
</div>

<div class="note"><code>cd /path/to/your/project</code> → <code>pi</code>. Start with understanding before asking for edits.</div>

---

<!-- SLIDE 9 · FOUR TOOLS -->

<div class="header-row">
  <span class="page-num">VIII.</span>
  <h2>The four default tools</h2>
</div>

<div class="visual tool-map">
  <div class="diagram-node model"><strong>MODEL</strong>decides what to request</div>
  <div class="diagram-node core"><strong>PI</strong>routes explicit actions<br><small>four focused capabilities</small></div>
  <div class="diagram-node read"><strong>read</strong>inspect files and images</div>
  <div class="diagram-node write"><strong>write</strong>create or replace deliberately</div>
  <div class="diagram-node bash"><strong>bash</strong>run checks and commands</div>
  <div class="diagram-node edit"><strong>edit</strong>apply the smallest precise patch</div>
</div>

<div class="note">The additional tools <code>grep</code>, <code>find</code>, and <code>ls</code> can be included in an explicit tool allowlist.</div>

---

<!-- SLIDE 10 · INSPECT -->

<div class="header-row">
  <span class="page-num">IX.</span>
  <h2>Inspect before you edit</h2>
</div>

<div class="visual timeline">
  <div class="timeline-step"><strong>01 · LOCATE</strong>Find files and entry points.</div>
  <div class="timeline-step"><strong>02 · UNDERSTAND</strong>Explain behavior and constraints.</div>
  <div class="timeline-step"><strong>03 · PLAN</strong>Bound the work before editing.</div>
  <div class="timeline-step change"><strong>04 · CHANGE</strong>Make the smallest useful patch.</div>
  <div class="timeline-step"><strong>05 · VERIFY</strong>Run checks and inspect the diff.</div>
</div>

<div class="note">A coding agent is most reliable when discovery is visibly separated from modification.</div>

---

<!-- SLIDE 11 · PROMPTS -->

<div class="header-row">
  <span class="page-num">X.</span>
  <h2>Prompt for a result</h2>
</div>

<div class="code-block">Goal: add CSV validation for the import command.

Constraints:
- preserve the public function signature
- do not add a runtime dependency
- report every invalid row with its line number

Workflow:
1. inspect the importer and existing tests
2. propose the smallest implementation
3. implement it
4. run the focused tests
5. summarize the diff and remaining risks</div>

<div class="note">Name the goal, constraints, workflow, verification command, and stopping point. Do not outsource judgment just because Pi can write code.</div>

---

<!-- SLIDE 12 · CONTEXT -->

<div class="header-row">
  <span class="page-num">XI.</span>
  <h2>Bring context into the prompt</h2>
</div>

<div class="two-col">
  <div><h3>Reference files with <code>@</code></h3><div class="code-block">pi @README.md @src/app.ts \
  "Review these together"</div><p class="small">In interactive mode, type <code>@</code> for fuzzy file search.</p></div>
  <div><h3>Run commands with <code>!</code></h3><div class="code-block">!npm test
!!git status --short</div><p class="small"><code>!</code> sends output to the model; <code>!!</code> does not.</p></div>
</div>

---

<!-- SLIDE 13 · AGENTS -->

<div class="header-row">
  <span class="page-num">XII.</span>
  <h2>Teach the project its rules</h2>
</div>

<div class="code-block"># AGENTS.md

## Project instructions
- Run `npm run check` after code changes.
- Do not edit generated files directly.
- Preserve the public API.
- Never commit secrets.
- Report uncertainty.</div>

<div class="list">
  <div class="list-item"><span class="list-num">01</span><span class="list-text">Pi loads global, parent, and current-directory <code>AGENTS.md</code> or <code>CLAUDE.md</code> files.</span></div>
  <div class="list-item"><span class="list-num">02</span><span class="list-text"><code>AGENTS.override.md</code> replaces that directory's instruction file; other directories still contribute context.</span></div>
  <div class="list-item"><span class="list-num">03</span><span class="list-text">Run <code>/reload</code> after changing context files.</span></div>
</div>

---

<!-- SLIDE 14 · TRUST -->

<div class="header-row">
  <span class="page-num">XIII.</span>
  <h2>Trust is not a sandbox</h2>
</div>

<div class="visual trust-contrast">
  <div class="trust-panel">
    <strong>PROJECT TRUST</strong>
    <div class="trust-flow"><span>trust decision</span><span class="arrow">→</span><span>resources loaded</span></div>
  </div>
  <div class="trust-panel">
    <strong>USER PERMISSIONS</strong>
    <div class="trust-flow"><span>account access</span><span class="arrow">→</span><span>tools can execute</span></div>
  </div>
</div>

<div class="note">Trust is a loading decision, not a security sandbox. Narrow the task, protect credentials, keep a rollback path, and verify consequential changes.</div>

---

<!-- SLIDE 15 · GIT -->

<div class="header-row">
  <span class="page-num">XIV.</span>
  <h2>Use Git as your checkpoint</h2>
</div>

<div class="visual flow-row">
  <div class="flow-step"><strong>01 · CHECKPOINT</strong><code>git switch -c ...</code><br>Start from a reversible branch.</div>
  <div class="flow-arrow">→</div>
  <div class="flow-step"><strong>02 · PI WORKS</strong>Bound the task and let Pi change files.</div>
  <div class="flow-arrow">→</div>
  <div class="flow-step"><strong>03 · EVIDENCE</strong><code>git diff</code> · tests · checks</div>
  <div class="flow-arrow">→</div>
  <div class="flow-step human-gate"><strong>04 · HUMAN DECISION</strong>Review, then commit only what you understand.</div>
</div>

<div class="note"><code>git status --short</code> · <code>git diff --check</code> · <code>npm test</code>. The agent can make changes; the diff, tests, and commit decision remain yours.</div>

---

<!-- SLIDE 16 · COMMANDS -->

<div class="header-row">
  <span class="page-num">XV.</span>
  <h2>The command desk</h2>
</div>

<div class="list">
  <div class="list-item"><span class="list-num">/login</span><span class="list-text">Manage provider authentication.</span></div>
  <div class="list-item"><span class="list-num">/model</span><span class="list-text">Switch models.</span></div>
  <div class="list-item"><span class="list-num">/settings</span><span class="list-text">Change model, UI, terminal, retry, and compaction settings.</span></div>
  <div class="list-item"><span class="list-num">/session</span><span class="list-text">Inspect the current session, tokens, cost, and context usage.</span></div>
  <div class="list-item"><span class="list-num">/trust</span><span class="list-text">Save the project trust decision for future sessions.</span></div>
  <div class="list-item"><span class="list-num">/reload</span><span class="list-text">Reload skills, prompts, themes, extensions, and context files.</span></div>
</div>

---

<!-- SLIDE 17 · KEYBOARD -->

<div class="header-row">
  <span class="page-num">XVI.</span>
  <h2>Control the terminal loop</h2>
</div>

<div class="two-col">
  <div><h3>Write and stop</h3><p class="small"><strong>Shift+Enter</strong> inserts a line. <strong>Escape</strong> aborts. <strong>Ctrl+C</strong> clears; press twice to quit.</p></div>
  <div><h3>Queue deliberately</h3><p class="small"><strong>Enter</strong> queues steering input. <strong>Alt+Enter</strong> queues a follow-up.</p></div>
  <div><h3>Change reasoning</h3><p class="small"><strong>Shift+Tab</strong> cycles thinking levels. <strong>Ctrl+L</strong> opens model selection.</p></div>
  <div><h3>Inspect history</h3><p class="small"><strong>Escape twice</strong> opens the session tree. <strong>Ctrl+O</strong> expands tool output.</p></div>
</div>

<div class="note">Inside tmux 3.5+, configure <code>set -g extended-keys on</code> and <code>set -g extended-keys-format csi-u</code>.</div>

---

<!-- SLIDE 18 · SESSIONS -->

<div class="header-row">
  <span class="page-num">XVII.</span>
  <h2>Sessions are recoverable work</h2>
</div>

<div class="code-block">pi --name "release-audit"
pi -c                 # continue the latest session
pi -r                 # browse previous sessions
pi --no-session       # ephemeral session

# Inside Pi
/resume   /new   /tree   /fork   /clone   /export</div>

<div class="visual session-tree">
  <div class="diagram-node root"><strong>SESSION</strong><code>release-audit</code><br><small>original path preserved</small></div>
  <div class="branch-a">↗</div>
  <div class="diagram-node fork"><strong>/fork</strong>branch A<br><small>start from an earlier message</small></div>
  <div class="branch-b">↘</div>
  <div class="diagram-node clone"><strong>/clone</strong>branch B<br><small>duplicate before a risky direction</small></div>
  <div class="diagram-node recover"><strong>RECOVER</strong><code>/resume</code> · <code>/new</code> · <code>/tree</code> · <code>/export</code></div>
</div>

<div class="note"><code>pi -c</code> continues the latest session; <code>pi -r</code> browses previous sessions; <code>pi --no-session</code> stays ephemeral.</div>

---

<!-- SLIDE 19 · COMPACTION -->

<div class="header-row">
  <span class="page-num">XVIII.</span>
  <h2>Manage a long context</h2>
</div>

<div class="visual context-diagram">
  <div class="context-window">
    <h3>Active context</h3>
    <p>Recent conversation, tool output, decisions, and open work fill the context window.</p>
    <p><code>/compact</code> starts a new phase.</p>
  </div>
  <div class="context-arrow">→<br><small>/compact</small></div>
  <div class="context-window">
    <h3>Lossy summary</h3>
    <p>Older conversation is compressed into what still matters.</p>
    <p>Useful, but not the full history.</p>
  </div>
  <div class="context-window durable">
    <h3>Durable memory outside the context</h3>
    <p><strong>Decisions belong in files, issues, or commits.</strong> They survive compaction and remain available to the next phase.</p>
  </div>
</div>

<div class="note">Focus compaction when needed: <code>/compact Focus on decisions, modified files, and remaining tests</code>.</div>

---

<!-- SLIDE 20 · MODELS -->

<div class="header-row">
  <span class="page-num">XIX.</span>
  <h2>Choose the right model</h2>
</div>

<div class="code-block">pi --list-models
pi --provider openai --model gpt-4o "Review the tests"
pi --model anthropic/claude-sonnet-4 "Implement the fix"
pi --thinking high "Trace this difficult failure"</div>

<div class="list">
  <div class="list-item"><span class="list-num">01</span><span class="list-text">Use a faster model for navigation and mechanical edits.</span></div>
  <div class="list-item"><span class="list-num">02</span><span class="list-text">Use stronger reasoning for architecture and ambiguous debugging.</span></div>
  <div class="list-item"><span class="list-num">03</span><span class="list-text">Levels are <code>off</code>, <code>minimal</code>, <code>low</code>, <code>medium</code>, <code>high</code>, <code>xhigh</code>, and <code>max</code>, depending on the model.</span></div>
</div>

---

<!-- SLIDE 21 · PRINT -->

<div class="header-row">
  <span class="page-num">XX.</span>
  <h2>Use Pi non-interactively</h2>
</div>

<div class="visual integration-diagram">
  <div class="integration-node"><strong>PROMPT</strong>one-shot request<br><small>no interactive UI</small></div>
  <div class="integration-arrow">→</div>
  <div class="integration-node safe"><strong>PI</strong>read-only allowlist<br><small><code>read,grep,find,ls</code></small></div>
  <div class="integration-arrow">→</div>
  <div class="integration-node"><strong>OUTPUT</strong>plain text<br><small>review before action</small></div>
</div>

<div class="code-block">pi -p "Summarize this codebase"
cat README.md | pi -p "Suggest three documentation improvements"
pi --tools read,grep,find,ls -p "Review risky patterns"</div>

<div class="note">The read-only example excludes <code>bash</code>, <code>edit</code>, and <code>write</code>. Validate model output before automation acts on it.</div>

---

<!-- SLIDE 22 · JSON -->

<div class="header-row">
  <span class="page-num">XXI.</span>
  <h2>Consume structured events</h2>
</div>

<div class="visual integration-diagram">
  <div class="integration-node"><strong>PI</strong>emits streaming events</div>
  <div class="integration-arrow">→</div>
  <div class="integration-node json-stream"><strong>JSON STREAM</strong>deltas by content index<br><small><code>message_end</code> is final authority</small></div>
  <div class="integration-arrow">→</div>
  <div class="integration-node"><strong>JQ / APP</strong>assemble and consume<br><small>filter or observe</small></div>
</div>

<div class="code-block">pi --mode json "List the files in this project" 2&gt;/dev/null \
  | jq -c 'select(.type == "message_end")'</div>

<div class="note">JSON lines include session, agent, message, tool, queue, compaction, and retry events. Streaming updates are deltas; the final <code>message_end</code> event is authoritative.</div>

---

<!-- SLIDE 23 · RPC -->

<div class="header-row">
  <span class="page-num">XXII.</span>
  <h2>Integrate through RPC</h2>
</div>

<div class="visual integration-diagram">
  <div class="integration-node"><strong>YOUR APP</strong>language-agnostic controller</div>
  <div class="integration-arrow">⇄</div>
  <div class="integration-node"><strong>PI RPC PROCESS</strong><code>stdin</code> / <code>stdout</code><br><small>one JSON object per line</small></div>
  <div class="integration-arrow">⇄</div>
  <div class="integration-node"><strong>PROJECT</strong>tools and session state</div>
</div>

<div class="code-block">pi --mode rpc --no-session
{"id":"req-1","type":"prompt","message":"Summarize this repository"}</div>

<div class="note">Use <code>prompt</code>, <code>steer</code>, <code>follow_up</code>, and <code>abort</code>. Frame records with LF only; do not split on Unicode line separators.</div>

---

<!-- SLIDE 24 · CUSTOMIZATION -->

<div class="header-row">
  <span class="page-num">XXIII.</span>
  <h2>Shape the workflow</h2>
</div>

<div class="visual stack-diagram">
  <div class="stack-layer"><strong>PACKAGES</strong>share resources through npm, Git, or a local path</div>
  <div class="stack-layer"><strong>EXTENSIONS</strong>add tools, commands, events, UI, and gates</div>
  <div class="stack-layer"><strong>PROMPT TEMPLATES</strong>turn repeatable prompts into slash commands</div>
  <div class="stack-layer"><strong>SKILLS</strong>load on-demand instructions for a capability</div>
  <div class="stack-layer"><strong>CONTEXT FILES</strong>keep project rules always present</div>
  <div class="stack-layer"><strong>PI CORE</strong>small, generic, and reusable</div>
</div>

---

<!-- SLIDE 25 · SKILLS -->

<div class="header-row">
  <span class="page-num">XXIV.</span>
  <h2>Build a skill</h2>
</div>

<div class="code-block">.pi/skills/release-check/SKILL.md

<span class="comment">[frontmatter]</span>
name: release-check
description: Checks a repository before a release. Use for release audits.
<span class="comment">[instructions]</span>
# Release check
1. Read the changelog and package version.
2. Run tests and the build.
3. Inspect the staged diff.
4. Report blockers; do not publish.</div>

<div class="list">
  <div class="list-item"><span class="list-num">01</span><span class="list-text">Use lowercase letters, numbers, and hyphens for the skill name.</span></div>
  <div class="list-item"><span class="list-num">02</span><span class="list-text">Make the description specific; it affects discovery.</span></div>
  <div class="list-item"><span class="list-num">03</span><span class="list-text">Invoke it as <code>/skill:release-check</code>.</span></div>
</div>

---

<!-- SLIDE 26 · PROMPTS -->

<div class="header-row">
  <span class="page-num">XXV.</span>
  <h2>Turn prompts into commands</h2>
</div>

<div class="code-block">.pi/prompts/review.md

<span class="comment">[frontmatter]</span>
description: Review staged changes
argument-hint: "[focus]"
<span class="comment">[prompt body]</span>
Review the staged git changes.
Focus on: $@.
Report bugs, security issues, and missing tests.</div>

<div class="list">
  <div class="list-item"><span class="list-num">01</span><span class="list-text"><code>review.md</code> becomes <code>/review</code>.</span></div>
  <div class="list-item"><span class="list-num">02</span><span class="list-text">Use <code>$1</code>, <code>$2</code>, or <code>$@</code> for arguments.</span></div>
  <div class="list-item"><span class="list-num">03</span><span class="list-text">Capture a repeatable outcome, not a giant personality prompt.</span></div>
</div>

---

<!-- SLIDE 27 · EXTENSIONS -->

<div class="header-row">
  <span class="page-num">XXVI.</span>
  <h2>Use extensions for behavior</h2>
</div>

<div class="code-block">import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";

export default function (pi: ExtensionAPI) {
  pi.registerCommand("hello", {
    description: "Show a custom command",
    handler: async (_args, ctx) =&gt; {
      ctx.ui.notify("Hello from an extension", "info");
    },
  });
}</div>

<div class="list">
  <div class="list-item"><span class="list-num">01</span><span class="list-text">Extensions can register tools, commands, events, keyboard shortcuts, and UI.</span></div>
  <div class="list-item"><span class="list-num">02</span><span class="list-text">They can add safety gates, Git checkpoints, and external integrations.</span></div>
  <div class="list-item"><span class="list-num">03</span><span class="list-text">Load one temporarily with <code>pi -e ./my-extension.ts</code>.</span></div>
</div>

---

<!-- SLIDE 28 · SAFETY -->

<div class="header-row">
  <span class="page-num">XXVII.</span>
  <h2>Put a gate before danger</h2>
</div>

<div class="visual gate-flow">
  <div class="gate"><strong>TOOL CALL</strong><code>bash</code><br>command requested</div>
  <div class="flow-arrow">→</div>
  <div class="gate"><strong>GATE</strong>inspect command<br>ask for confirmation</div>
  <div class="flow-arrow">→</div>
  <div class="gate blocked"><strong>ALLOW / BLOCK</strong>continue or stop<br>with a reason</div>
</div>

<div class="code-block">pi.on("tool_call", async (event, ctx) =&gt; {
  if (event.toolName !== "bash") return;

  const command = event.input.command ?? "";
  if (command.includes("rm -rf") || command.includes("sudo")) {
    const allowed = await ctx.ui.confirm("Dangerous command", command);
    if (!allowed) return { block: true, reason: "Blocked by user" };
  }
});</div>

<div class="note">This pattern is not a complete security policy. Test gates against the commands and paths your projects actually use.</div>

---

<!-- SLIDE 29 · PACKAGES -->

<div class="header-row">
  <span class="page-num">XXVIII.</span>
  <h2>Share a Pi package</h2>
</div>

<div class="code-block">pi install npm:@your-org/pi-tools
pi install git:github.com/your-org/pi-tools@v1
pi list
pi update --all

# Project-local install
pi install -l npm:@your-org/pi-tools</div>

<div class="list">
  <div class="list-item"><span class="list-num">01</span><span class="list-text">Review package source first; extensions run with your permissions.</span></div>
  <div class="list-item"><span class="list-num">02</span><span class="list-text">Pin versions or Git refs when reproducibility matters.</span></div>
  <div class="list-item"><span class="list-num">03</span><span class="list-text">Declare resources under the <code>pi</code> key in <code>package.json</code>.</span></div>
</div>

---

<!-- SLIDE 30 · CUSTOM MODELS -->

<div class="header-row">
  <span class="page-num">XXIX.</span>
  <h2>Connect a local model</h2>
</div>

<div class="visual integration-diagram">
  <div class="integration-node"><strong>PI</strong><code>/model</code><br><small>same agent workflow</small></div>
  <div class="integration-arrow">→</div>
  <div class="integration-node"><strong>OPENAI-COMPATIBLE API</strong><code>localhost:11434/v1</code><br><small>provider route</small></div>
  <div class="integration-arrow">→</div>
  <div class="integration-node"><strong>OLLAMA</strong><code>qwen2.5-coder:7b</code><br><small>model runs locally</small></div>
</div>

<div class="code-block">~/.pi/agent/models.json

{
  "providers": {
    "ollama": {
      "baseUrl": "http://localhost:11434/v1",
      "api": "openai-completions",
      "apiKey": "ollama",
      "models": [{ "id": "qwen2.5-coder:7b" }]
    }
  }
}</div>

<div class="note">Supported API styles include OpenAI Completions, Responses, Anthropic Messages, and Google Generative AI. Edit <code>models.json</code>, then open <code>/model</code>.</div>

---

<!-- SLIDE 31 · SDK -->

<div class="header-row">
  <span class="page-num">XXX.</span>
  <h2>Embed Pi with the SDK</h2>
</div>

<div class="visual integration-diagram">
  <div class="integration-node"><strong>APPLICATION</strong>Node / TypeScript<br><small>your product boundary</small></div>
  <div class="integration-arrow">→</div>
  <div class="integration-node"><strong>SDK SESSION</strong>state · events · prompts<br><small><code>createAgentSession</code></small></div>
  <div class="integration-arrow">→</div>
  <div class="integration-node"><strong>PI WORKFLOW</strong>model · tools · project<br><small>direct integration</small></div>
</div>

<div class="code-block">npm install @earendil-works/pi-coding-agent

import {
  createAgentSession,
  ModelRuntime,
  SessionManager,
} from "@earendil-works/pi-coding-agent";

const modelRuntime = await ModelRuntime.create();
const { session } = await createAgentSession({
  modelRuntime,
  sessionManager: SessionManager.inMemory(),
});

await session.prompt("What files are in this project?");</div>

<div class="note">Use the SDK when a Node or TypeScript application needs direct session state, events, tools, or resource loading. Use RPC for a language-agnostic process boundary.</div>

---

<!-- SLIDE 32 · SANDBOX -->

<div class="header-row">
  <span class="page-num">XXXI.</span>
  <h2>Sandbox untrusted work</h2>
</div>

<div class="visual lane-diagram">
  <div class="lane-label">HOST</div>
  <div class="lane-text">Your project and credentials remain outside the container boundary.</div>
  <div class="lane-label">CONTAINER</div>
  <div class="lane-text"><code>pi-sandbox</code> runs with only the workspace, credentials, and network access you pass in.</div>
  <div class="lane-label">LIMIT</div>
  <div class="lane-text"><strong>A mounted workspace can still write through to the host.</strong> Use a VM or stronger policy-controlled sandbox when needed.</div>
</div>

<div class="code-block">docker build -t pi-sandbox -f Dockerfile.pi .

docker run --rm -it \
  -e ANTHROPIC_API_KEY \
  -v "$PWD:/workspace" \
  -v pi-agent-home:/root/.pi/agent \
  pi-sandbox</div>

<div class="note">Pass only the credentials and network access the task requires. A container is a boundary, not automatically complete isolation.</div>

---

<!-- SLIDE 33 · CAPSTONE -->

<div class="header-row">
  <span class="page-num">XXXII.</span>
  <h2>Capstone: ship a small fix</h2>
</div>

<div class="code-block">1. Create a branch.
2. Write acceptance criteria in the prompt.
3. Ask Pi to inspect the relevant files first.
4. Implement the smallest change.
5. Run focused tests.
6. Ask Pi to review the diff.
7. Read the diff yourself.
8. Commit only what you understand.</div>

<div class="note">A successful task ends with evidence: test output, a reviewed diff, and a clear explanation of what changed.</div>

---

<!-- SLIDE 34 · TROUBLESHOOTING -->

<div class="header-row">
  <span class="page-num">XXXIII.</span>
  <h2>When something goes wrong</h2>
</div>

<div class="list">
  <div class="list-item"><span class="list-num">01</span><span class="list-text"><strong>No model</strong> — run <code>/login</code>, then <code>/model</code> or <code>pi --list-models</code>.</span></div>
  <div class="list-item"><span class="list-num">02</span><span class="list-text"><strong>Rules ignored</strong> — check the filename, location, startup header, and run <code>/reload</code>.</span></div>
  <div class="list-item"><span class="list-num">03</span><span class="list-text"><strong>Keys fail in tmux</strong> — configure extended keys and restart the tmux server.</span></div>
  <div class="list-item"><span class="list-num">04</span><span class="list-text"><strong>Context is bloated</strong> — compact, start a focused session, and write durable notes.</span></div>
  <div class="list-item"><span class="list-num">05</span><span class="list-text"><strong>Wrong change</strong> — stop, inspect the diff, revert deliberately, and tighten the prompt.</span></div>
</div>

---

<!-- SLIDE 35 · CHECKLIST -->

<div class="header-row">
  <span class="page-num">XXXIV.</span>
  <h2>Your operating checklist</h2>
</div>

<div class="list">
  <div class="list-item"><span class="list-num">01</span><span class="list-text">Start Pi in the correct project directory.</span></div>
  <div class="list-item"><span class="list-num">02</span><span class="list-text">Give it project instructions and a bounded goal.</span></div>
  <div class="list-item"><span class="list-num">03</span><span class="list-text">Inspect before editing; preserve a Git checkpoint.</span></div>
  <div class="list-item"><span class="list-num">04</span><span class="list-text">Use the smallest useful tool and model.</span></div>
  <div class="list-item"><span class="list-num">05</span><span class="list-text">Test, inspect the diff, and record important decisions.</span></div>
  <div class="list-item"><span class="list-num">06</span><span class="list-text">Customize only after the repeated workflow is understood.</span></div>
</div>

<div class="note"><strong>Remember:</strong> the agent is a force multiplier for clear engineering judgment, not a replacement for it.</div>

---

<!-- SLIDE 36 · REFERENCES -->

<div class="header-row">
  <span class="page-num">XXXV.</span>
  <h2>Keep learning</h2>
</div>

<div class="list">
  <div class="list-item"><span class="list-num">01</span><span class="list-text"><strong>Documentation</strong> — <code>https://pi.dev</code></span></div>
  <div class="list-item"><span class="list-num">02</span><span class="list-text"><strong>Source and examples</strong> — <code>github.com/earendil-works/pi-mono</code></span></div>
  <div class="list-item"><span class="list-num">03</span><span class="list-text"><strong>First customization</strong> — build a skill for a task you repeat every week.</span></div>
  <div class="list-item"><span class="list-num">04</span><span class="list-text"><strong>Next level</strong> — write an extension that protects a path, gates a command, or exposes a domain-specific tool.</span></div>
</div>

---

<!-- SLIDE 37 · CTA -->
<!-- _class: cta -->

<div class="cta-content">
  <div class="cta-kicker">PI CODING AGENT</div>
  <h1>Start small.<br>Keep the boundary yours.</h1>
  <div class="cta-line">Inspect. Shape. Verify.</div>
  <div class="handle">juliusdarang · polymath tutorials</div>
</div>
