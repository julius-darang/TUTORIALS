---
name: tutorials
description: Gumroad course business — paid Marp slide decks across multiple learning tracks
domain: brand
status: active
stack: Marp (.md → .pdf) · shared styling templates
entry: marp <deck>.md --pdf  (per _templates/MARP_STYLING_TEMPLATE.md)
has_repo: true
updated: 2026-07-31
---

# tutorials

## State
Five tracks: ZERO TO AI BUILDER (~45), AI AGENTS LEVELS (4 topics × 4 parts),
CLAUDE CODE (~18 single-page guides), PROMPT ENGINEERING (stub), VIBE CODING 101 (stub).
Plus CAROUSELS/ for social derivatives. Tracks ZERO TO AI BUILDER + CLAUDE CODE are solid;
PROMPT ENGINEERING + VIBE CODING 101 are stubs.

## Next action
Monetize: publish free tutorials, ship the Gumroad PDF, open the Substack tier.
Then fill the two stub tracks.

## Conventions
- Global `marp-output` skill — authoring, structure, template selection, rendering, and QA; use `.pi/skills/visual-style/` for the Polymath tutorial template and design contract.
- Styling source: `_templates/MARP_STYLING_TEMPLATE.md` — reuse, don't recreate.
- Brand structure: `_product/juliusdarang_BRAND_STRUCTURE.md` + product defs.

## Pointers
- Templates: `_templates/` · product defs: `_product/`.
- Own `.git` (origin `github.com/Murasakiao/TUTORIALS`).