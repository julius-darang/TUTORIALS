# Pi Agent — Instagram carousel

Eight slides, each **1080 × 1440 px (3:4)**. This is an editable SVG companion to `../pi-agent-full.pdf`.

## Edit in Figma

1. Install **STIX Two Text** and **JetBrains Mono** on your machine. In Figma's browser app, enable its local font helper; the desktop app can use installed fonts.
2. Unzip `pi-agent-carousel-svg.zip` and drag the eight numbered SVG files onto a Figma canvas in order.
3. Each SVG uses native text, paths, rectangles, and lines. Important elements have named groups, including the cube grid, terminal examples, and footer. Ungroup where needed to edit individual elements.
4. Check font matching after import. The SVG source keeps text live rather than converting it into paths; import behavior depends on Figma's importer. The full copy is also in `slide-copy.md` if a text layer needs rebuilding.
5. Export each finished frame as PNG for Instagram. The supplied `previews/` PNGs are also 1080 × 1440.

Fonts: [STIX Two Text](https://github.com/stipub/stixfonts) and [JetBrains Mono](https://www.jetbrains.com/lp/mono/).

## Design

- Pi editorial theme: near-black `#131414`, warm white `#e8e7e3`, orange `#d77600`.
- Serif headlines, monospace commands, 88 px side margins, thin rules, and wireframe cubes.
- A warm light final slide introduces the complete guide and the CTA: **DM me “PI” for the guide.**
- No raster images, external asset references, filters, HTML, or embedded scripts in the SVGs.

## Files

- `01-*.svg` through `08-*.svg`: editable masters, in posting order.
- `pi-agent-carousel-svg.zip`: eight SVGs plus the import notes and slide copy.
- `previews/`: rendered PNGs for review and posting.
- `carousel-overview.png`: overview of all eight slides.
- `slide-copy.md`: complete editable copy and a suggested Instagram caption.
- `build-carousel.py`: optional standard-library Python generator. Running it rewrites the SVG masters; it does not render PNGs or update the ZIP.

## Content sources

Adapted from `../pi-agent-contents.md`. Setup commands, default tools, and project customization were checked against the [official Pi documentation](https://github.com/earendil-works/pi/tree/main/packages/coding-agent) on 2026-09-06. The guide promotion refers to the existing 28-lesson long-form tutorial.

This package creates assets only; it does not post to Instagram or send DMs. A Figma import has not been performed in this workspace.
