# Pi Coding Agent tutorial

This directory is the main home for the Pi Coding Agent tutorial. It contains the same material in three publishing formats:

1. A progressive Marp presentation for social, live, and introductory use.
2. An expanded Marp presentation for a visual walkthrough.
3. A long-form Markdown source rendered as a vertical, book-like PDF tutorial.

The long-form Markdown file is the canonical source for the complete written tutorial. The presentations are separate editorial formats, not intermediate build steps for the PDF.

## Directory contents

```text
PI-CODING-AGENT/
├── README.md
├── pi-agent.md
├── pi-agent-full.md
├── pi-agent-contents.md
├── pi-agent.pdf              # generated; ignored by Git
├── pi-agent-full.pdf          # generated; ignored by Git
├── build-pdf.sh
├── _pdf-header.tex
└── _pdf-parts.json
```

### `pi-agent-contents.md`

The canonical long-form Markdown tutorial. This is the file to edit when changing the complete written tutorial.

It contains the detailed explanations, commands, examples, safety guidance, troubleshooting, capstone workflow, checklist, and references. It is also suitable as a source for:

- The vertical PDF
- YouTube narration or lesson scripts
- Blog or newsletter publishing
- Captions and shorter derivative content

Do not manually edit the generated PDF. Make content changes here and rebuild it.

### `pi-agent.md`

The progressive Marp presentation. Repeated slide states reveal the cards and list items one at a time while preserving the fixed-page Marp workflow. It contains 24 static pages and is useful for LinkedIn and Instagram carousels, live presenting, progressive PDFs, and screen recordings. It does not depend on CSS animation or JavaScript.

Render it as a Marp PDF with:

```bash
marp --pdf pi-agent.md
```

### `pi-agent-full.md`

The expanded Marp presentation. It covers more of the tutorial, including sessions, automation modes, skills, extensions, packages, models, SDK integration, and sandboxing. It is a fixed-page slide deck, not the source used to generate the vertical PDF.

Render it with:

```bash
marp --pdf pi-agent-full.md
```

### `pi-agent-full.pdf`

The generated vertical A4 PDF. It is a complete tutorial rather than a presentation deck. It includes:

- A designed cover page
- A table of contents with part entries
- Four full-page part dividers
- Flowing body text
- Code blocks with syntax highlighting
- Chapter headings
- Page headers and page numbers
- Official references

The repository ignores `*.pdf`, so this output is available locally after building but is not shown as an untracked Git file by default.

### `_pdf-parts.json`

PDF-only editorial metadata for the four tutorial parts. It maps each part's number, title, description, and insertion point to a canonical Markdown heading:

```text
I    Foundations                  before About this tutorial
II   Operating Workflow           before chapter 10
III  Automation and Customization before chapter 15
IV   Integration and Shipping     before chapter 23
```

The part structure is injected only into the temporary PDF input. The canonical Markdown and Marp decks do not receive raw LaTeX part markers.

### `build-pdf.sh`

The reproducible PDF build script. It resolves paths relative to its own directory, checks for required tools, prepares a temporary Markdown input, injects the four part dividers from `_pdf-parts.json`, invokes Pandoc, and writes `pi-agent-full.pdf`.

It accepts an optional output path:

```bash
./build-pdf.sh /tmp/pi-agent-preview.pdf
```

### `_pdf-header.tex`

The XeLaTeX styling header used by Pandoc. It defines the PDF's layout and visual system:

- A4 page dimensions and margins
- PT Sans body typography
- Andale Mono code typography
- Dark cover page
- Orange `#D77600` accent
- Section and subsection styles
- Code-block colors and wrapping
- Blockquote callouts
- Table-of-contents depth
- Headers, footers, and page numbers
- PDF metadata and link colors

Change this file when adjusting the PDF's visual design. Do not put tutorial content in it.

## PDF build process

The vertical PDF is **not converted from either Marp file**. The pipeline is:

```text
pi-agent-contents.md
        │
        ▼
Temporary cleaned Markdown input
        │
        ▼
Pandoc
        │
        ▼
XeLaTeX + _pdf-header.tex
        │
        ▼
pi-agent-full.pdf
```

### Step 1: install the required tools

The current build requires:

- Pandoc
- XeLaTeX

On this machine, Pandoc was installed with Homebrew and XeLaTeX was already available:

```bash
brew install pandoc
command -v pandoc
command -v xelatex
```

The project does not currently require Quarto or Typst for this build.

### Step 2: run the build

From this directory:

```bash
cd brand/tutorials/PI-CODING-AGENT
./build-pdf.sh
```

The script performs the following operations:

1. Resolves the directory containing the script so it works from any current directory.
2. Verifies that `pandoc` and `xelatex` are available.
3. Creates a temporary Markdown file.
4. Removes the first four lines of `pi-agent-contents.md`, which contain the written title and subtitle used for the cover treatment.
5. Adds an `About this tutorial` heading before the introductory prose so it appears in the table of contents.
6. Reads `_pdf-parts.json` and injects a raw LaTeX `\partpage{...}` marker before each configured chapter anchor.
7. Replaces the Unicode right-arrow with `->` in the temporary copy for compatibility with the installed PDF font.
8. Runs Pandoc with Markdown plus raw LaTeX support, pipe tables, syntax highlighting, and a two-level table of contents.
9. Includes `_pdf-header.tex` to apply the A4 layout, visual styling, bookmarks, and part pages.
10. Writes `pi-agent-full.pdf`.
11. Removes the temporary Markdown file using the script's cleanup trap.

The core Pandoc options are:

```bash
pandoc INPUT.md \
  --from=markdown+raw_tex+pipe_tables+autolink_bare_uris+strikeout+task_lists+gfm_auto_identifiers \
  --to=pdf \
  --pdf-engine=xelatex \
  --include-in-header=_pdf-header.tex \
  --toc \
  --toc-depth=2 \
  --syntax-highlighting=pygments \
  --output=pi-agent-full.pdf
```

### Step 3: verify the output

Check the PDF metadata and page dimensions:

```bash
pdfinfo pi-agent-full.pdf | grep -E 'Pages|Page size|Title|Author'
```

Extract text to confirm that the output contains expected sections:

```bash
pdftotext pi-agent-full.pdf - | less
```

For a visual preview, convert selected pages to PNG if `pdftoppm` is available:

```bash
mkdir -p /tmp/pi-agent-preview
pdftoppm -png -f 1 -singlefile -r 120 \
  pi-agent-full.pdf /tmp/pi-agent-preview/cover
pdftoppm -png -f 3 -singlefile -r 100 \
  pi-agent-full.pdf /tmp/pi-agent-preview/body
```

## Editing and publishing workflow

Use the format that matches the change:

### Content change

1. Edit `pi-agent-contents.md`.
2. Check commands, links, and factual claims.
3. Rebuild the PDF:

   ```bash
   ./build-pdf.sh
   ```

4. Render or review the Marp decks separately if the content change affects them.
5. Inspect the PDF text and selected page images.

### PDF design change

1. Edit `_pdf-header.tex`.
2. Rebuild with `./build-pdf.sh`.
3. Review the cover, table of contents, code blocks, headings, and page furniture.
4. Keep the change limited to PDF presentation; do not add tutorial prose to the header file.

### Marp design or slide change

1. Edit the relevant Marp file.
2. Render it with `marp --pdf <file>.md`.
3. Review the fixed-size slide output independently of the vertical PDF.

## Security and generated files

The build process does not access Pi credentials or project secrets. It only reads the tutorial Markdown and styling header, then invokes local rendering tools.

The build creates no credentials, `.env` files, API keys, or private-key files. Its only temporary artifact is the cleaned Markdown file created by `mktemp`; it is deleted when the script exits.

The PDF is generated output and is ignored by the repository's existing rule:

```gitignore
*.pdf
```

If a release copy needs to be distributed, export or upload the generated PDF separately rather than changing the source Markdown to embed binary output.

## Troubleshooting

### `pandoc: command not found`

Install Pandoc:

```bash
brew install pandoc
```

### `xelatex: command not found`

Install a TeX distribution that includes XeLaTeX, then confirm:

```bash
command -v xelatex
```

### The PDF has stale content

The PDF is generated from `pi-agent-contents.md`, not `pi-agent-full.md`. Edit the contents file and run:

```bash
./build-pdf.sh
```

### A code block overflows

The PDF header enables line wrapping for highlighted code. If a particular example remains too wide, shorten the example or split it into two code blocks in `pi-agent-contents.md`.

### The table of contents is wrong

The build currently includes headings through level two. Check that chapter headings use `##` and subheadings use `###` in `pi-agent-contents.md`, then rebuild from a clean output path.
