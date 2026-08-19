---
name: tutorials
description: Curated Marp tutorial workspace focused on AI agents, Pi Coding Agent workflows, and practical developer education
domain: brand
status: active
stack: Marp (.md → .pdf) · shared styling templates
entry: README.md · PI-CODING-AGENT/README.md · _templates/MARP_STYLING_TEMPLATE.md
has_repo: true
updated: 2026-08-19
---

# tutorials

## State

The repository has been cleaned down to its active tutorial work:

- **AI Agents Levels** — four agent architectures, each organized into four parts.
- **Pi Coding Agent** — two-output package with `pi-agent.md` and `pi-agent.pdf`.
- **Prompt Engineering** — developing curriculum with carousel and document derivatives.
- **CLI and power-systems references** — `MASTERING CLI.md` and `pandapower.md`.

Retired Zero to AI Builder, Vibe Coding 101, and carousel material is held in the ignored local `archive/` directory. The former `CLAUDE CODE/` collection was deleted rather than archived. Archived material is not part of the active repository source of truth.

## Next action

Maintain the Pi Coding Agent package as the current publishing output, then complete the highest-value gaps in AI Agents Levels and Prompt Engineering before reopening archived curricula.

## Conventions

- Use the global `marp-output` skill for deck authoring, rendering, and visual QA.
- Reuse `_templates/MARP_STYLING_TEMPLATE.md`; do not recreate the shared styling system.
- Keep active tutorial content in Markdown. Treat generated PDFs as build artifacts.
- For Pi Coding Agent changes, read `PI-CODING-AGENT/README.md`; update `pi-agent.md` and render `pi-agent.pdf` with Marp.
- Keep archive cleanup local and intentional; `archive/` is ignored and is not an active publishing source.
- Keep the public Three Pillars brand framework in `_product/juliusdarang_BRAND_STRUCTURE.md` distinct from the Conquer Self Four-Layer Stack.

## Pointers

- Repository guide: `README.md`
- Templates: `_templates/`
- Product and brand definitions: `_product/`
- Active flagship: `PI-CODING-AGENT/`
- AI curriculum: `AI AGENTS LEVELS/`
- Canonical remote: `github.com/julius-darang/TUTORIALS`
