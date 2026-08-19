# Polymath Tutorials

Educational slide-based tutorials by **[Julius Darang](https://github.com/julius-darang)**, focused on AI agents, coding workflows, and practical developer foundations.

This repository is the source workspace for tutorial Markdown, Marp decks, product documentation, and generated publishing artifacts. The canonical GitHub repository is [`julius-darang/TUTORIALS`](https://github.com/julius-darang/TUTORIALS).

## Current inventory

After the cleanup, 32 Markdown files remain outside the ignored local archive. The active repository is intentionally small and focused:

| Area | Location | Current state |
|---|---|---|
| **AI Agents Levels** | `AI AGENTS LEVELS/` | 4 agent architectures × 4 parts: single, pipeline, multi-agent, and agent teams |
| **Pi Coding Agent** | `PI-CODING-AGENT/` | Active two-output package: `pi-agent.md` and `pi-agent.pdf` |
| **Prompt Engineering** | `PROMPT ENGINEERING/` | Developing curriculum, carousel, and long-form source |
| **CLI reference** | `MASTERING CLI.md` | Early curriculum outline |
| **Power-systems reference** | `pandapower.md` | Standalone engineering tutorial/reference |

Supporting material lives in:

- `_templates/` — shared Marp styling and cover templates
- `_product/` — brand structure and product definitions
- `STATUS.md` — project metadata used by the workspace `/doctor` extension

## AI Agents Levels

`AI AGENTS LEVELS/` contains four architecture tracks, each divided into four parts:

- **Single Agent** — one agent with tools and memory
- **Pipeline Agent** — staged work across specialized steps
- **Multi-Agent** — multiple agents coordinating a task
- **Agent Teams** — agents collaborating as a team

Each track is a standalone Marp Markdown deck sequence and can be exported independently.

## Pi Coding Agent package

`PI-CODING-AGENT/` publishes exactly two outputs:

1. `pi-agent.md` — a 24-page progressive Marp tutorial source
2. `pi-agent.pdf` — the rendered PDF export

Render the PDF with:

```bash
cd PI-CODING-AGENT
marp --pdf pi-agent.md --output pi-agent.pdf
```

The package README documents its supporting source and maintenance files. The removed expanded Pi deck is not part of the current publishing output.

## Prompt Engineering

`PROMPT ENGINEERING/` currently contains:

- `PROMPT ENGINEERING 101.md` — long-form curriculum source
- `carousel.md` — social derivative
- `docx.md` — document-oriented derivative

## Archive and cleanup

`archive/` is an ignored local holding area for retired material. It currently contains the former:

- Zero to AI Builder curriculum and associated product/export files
- Vibe Coding 101 files
- Carousel exports and source files

The previous `CLAUDE CODE/` collection was deleted rather than moved into the archive. Archived files are not part of the published repository and are not discovered by the workspace `/doctor` scan.

## How tutorials are built

Tutorial sources use single-file Marp Markdown decks with embedded HTML/CSS components. The shared design system is `_templates/MARP_STYLING_TEMPLATE.md`; reuse it rather than creating a separate visual system.

### Marp file format

```markdown
---
marp: true
paginate: true
html: true
size: 4:3
style: |
  /* CSS variables + component styles */
---

<!-- _class: cover -->

# Title Slide

Content with HTML grid/card components...
```

### Design conventions

- **Typography:** DM Sans for headings/body and DM Mono for code/vocabulary
- **Blue theme:** `#2563eb` for selected educational decks
- **Amber theme:** `#d97706` for AI Agents Levels
- **Dark themes:** used by Pi and selected technical decks
- **Components:** cards, stat cards, comparison grids, process flows, timelines, code comparisons, checklists, and diagrams

## Export workflow

### Install Marp

```bash
npm install -g @marp-team/marp-cli
```

### Preview a deck

```bash
npx @marp-team/marp-cli --preview "path/to/file.md"
```

### Export one deck

```bash
npx @marp-team/marp-cli --pdf "AI AGENTS LEVELS/Single Agent p1.md"
```

### Export the Pi package

```bash
cd PI-CODING-AGENT
marp --pdf pi-agent.md --output pi-agent.pdf
```

PDF files are generated publishing artifacts and are ignored by Git. Treat Markdown as the source of truth and rebuild exports before distribution.

## Product and distribution

Product definitions and brand strategy are kept under `_product/`:

- `_product/PRODUCT_AI_AGENTS_LEVELS.md`
- `_product/PRODUCT_ZERO_TO_AI_BUILDER.md`
- `_product/juliusdarang_BRAND_STRUCTURE.md`

Tutorial products are distributed through **[Gumroad](https://gumroad.com/)** and related free content channels. The archived Zero to AI Builder files remain available locally for reference but are not active publishing sources in this cleaned repository.

## Repository structure

```text
tutorials/
├── _product/           # Brand docs and product definitions
├── _templates/         # Shared Marp styling and cover templates
├── PI-CODING-AGENT/    # Pi tutorial: pi-agent.md + pi-agent.pdf
├── AI AGENTS LEVELS/   # 4 agent architectures × 4 parts
├── PROMPT ENGINEERING/ # Prompting curriculum and derivatives
├── MASTERING CLI.md    # CLI curriculum outline
├── pandapower.md       # Standalone engineering reference
├── archive/            # Ignored local archive of retired material
├── README.md           # Repository guide
└── STATUS.md           # Workspace metadata entry point
```

## Quick start

```bash
# From the repository root: preview a deck
npx @marp-team/marp-cli --preview "path/to/file.md"

# Export a deck
npx @marp-team/marp-cli --pdf "path/to/file.md"

# Render the Pi tutorial PDF
cd PI-CODING-AGENT && marp --pdf pi-agent.md --output pi-agent.pdf
```

## License

All content © Julius Darang. All rights reserved.
