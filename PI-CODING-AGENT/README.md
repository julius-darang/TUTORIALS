# Pi Coding Agent tutorial

This directory publishes two outputs:

1. `pi-agent.md` — the progressive Marp tutorial source.
2. `pi-agent.pdf` — the rendered PDF export.

These are the only published outputs for this package. The previous expanded `pi-agent-full.md` deck and `pi-agent-full.pdf` export have been removed.

## Published outputs

### `pi-agent.md`

The 24-page progressive Marp deck for social, live, and introductory use. Repeated slide states reveal the cards and list items one at a time while preserving a fixed-page workflow. It does not depend on CSS animation or JavaScript.

Render it with:

```bash
marp --pdf pi-agent.md --output pi-agent.pdf
```

### `pi-agent.pdf`

The PDF export of `pi-agent.md`. It is a generated artifact and is ignored by Git. Rebuild it whenever the Markdown source changes.

Verify the generated file with:

```bash
pdfinfo pi-agent.pdf | grep -E 'Pages|Page size|Title|Author'
```

## Supporting source files

The directory also contains implementation files used to maintain the tutorial package:

- `pi-agent-contents.md` — long-form source material retained for reference and future editorial work
- `build-pdf.sh` — legacy Pandoc/XeLaTeX build script retained for the long-form source
- `_pdf-header.tex` — PDF styling header
- `_pdf-parts.json` — PDF part metadata

These files are not additional published outputs. The current publishing target is only `pi-agent.md` and `pi-agent.pdf`.

## Editing workflow

1. Edit `pi-agent.md` for changes to the published tutorial.
2. Render the PDF:

   ```bash
   marp --pdf pi-agent.md --output pi-agent.pdf
   ```

3. Review the Markdown and PDF output before distribution.
4. Keep generated PDFs out of Git; the repository's `*.pdf` ignore rule handles this.

## Design conventions

- Reuse the shared Marp styling system from `../_templates/MARP_STYLING_TEMPLATE.md`.
- Keep the progressive slide states as complete static pages.
- Use the existing visual language and component patterns rather than introducing a separate design system.
- Do not recreate the removed full-deck files unless the publishing target changes again.
