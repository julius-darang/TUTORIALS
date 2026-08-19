#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE="$ROOT/pi-agent-contents.md"
PARTS="$ROOT/_pdf-parts.json"
HEADER="$ROOT/_pdf-header.tex"
OUTPUT="${1:-$ROOT/pi-agent-full.pdf}"
SCRIPT="$ROOT/$(basename "${BASH_SOURCE[0]}")"

if ! command -v pandoc >/dev/null 2>&1; then
  echo "pandoc is required: brew install pandoc" >&2
  exit 1
fi
if ! command -v xelatex >/dev/null 2>&1; then
  echo "xelatex is required" >&2
  exit 1
fi

for required_file in "$SOURCE" "$PARTS" "$HEADER"; do
  if [[ ! -f "$required_file" ]]; then
    echo "Required file not found: $required_file" >&2
    exit 1
  fi
done

file_mtime() {
  if [[ "$(uname -s)" == "Darwin" ]]; then
    stat -f %m "$1"
  else
    stat -c %Y "$1"
  fi
}

# Avoid paying for Pandoc/XeLaTeX when none of the build inputs changed.
# Set FORCE=1 for an explicit rebuild (for example after changing installed fonts).
if [[ -f "$OUTPUT" && "${FORCE:-}" != "1" ]]; then
  newest_input=0
  for input_file in "$SOURCE" "$PARTS" "$HEADER" "$SCRIPT"; do
    input_mtime="$(file_mtime "$input_file")"
    (( input_mtime > newest_input )) && newest_input="$input_mtime"
  done
  if (( $(file_mtime "$OUTPUT") >= newest_input )); then
    echo "Up to date: $OUTPUT"
    exit 0
  fi
fi

TMP="$(mktemp -t pi-agent-contents.XXXXXX.md)"
cleanup() { rm -f "$TMP"; }
trap cleanup EXIT

# Prepare a PDF-only input. The first heading and subtitle become the cover,
# while part dividers are injected without changing the canonical Markdown.
python3 - "$SOURCE" "$PARTS" "$TMP" <<'PY'
import json
import sys
from pathlib import Path

source_path, parts_path, output_path = map(Path, sys.argv[1:])
source_lines = source_path.read_text().splitlines()
parts = json.loads(parts_path.read_text())

# pi-agent-contents.md reserves its first four lines for the title/subtitle.
body = source_lines[4:]
by_heading = {part["before"]: part for part in parts}
found = set()
output = []

for line in ["## About this tutorial", "", *body]:
    if line in by_heading:
        part = by_heading[line]
        output.append(
            f'\\partpage{{{part["number"]}}}{{{part["title"]}}}{{{part["description"]}}}'
        )
        output.append("")
        found.add(line)

    # PT Sans lacks the arrow glyph, so normalize it only in this temporary
    # PDF input. The canonical Markdown remains unchanged.
    output.append(line.replace("→", "->"))

missing = set(by_heading) - found
if missing:
    raise SystemExit(f"Missing PDF part anchors: {', '.join(sorted(missing))}")

output_path.write_text("\n".join(output) + "\n")
PY

pandoc "$TMP" \
  --from=markdown+raw_tex+pipe_tables+autolink_bare_uris+strikeout+task_lists+gfm_auto_identifiers \
  --to=pdf \
  --pdf-engine=xelatex \
  --pdf-engine-opt=-interaction=nonstopmode \
  --pdf-engine-opt=-halt-on-error \
  --include-in-header="$HEADER" \
  --metadata title="Pi Coding Agent" \
  --metadata author="Julius Darang" \
  --toc \
  --toc-depth=2 \
  --syntax-highlighting=pygments \
  --resource-path="$ROOT" \
  --output="$OUTPUT"

echo "Wrote $OUTPUT"
