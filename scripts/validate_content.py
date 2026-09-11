#!/usr/bin/env python3
"""Validate the active tutorial inventory without rendering publishing artifacts."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_STATUS_FIELDS = {
    "name",
    "description",
    "domain",
    "status",
    "entry",
    "has_repo",
    "updated",
}


def read_frontmatter(path: Path) -> dict[str, str] | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end < 0:
        return None
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def validate() -> list[str]:
    errors: list[str] = []

    status_path = ROOT / "STATUS.md"
    status = read_frontmatter(status_path)
    if status is None:
        errors.append("STATUS.md has no readable frontmatter")
    else:
        missing = sorted(REQUIRED_STATUS_FIELDS - status.keys())
        errors.extend(f"STATUS.md missing `{field}`" for field in missing)
        if status.get("name") != "tutorials":
            errors.append("STATUS.md name must be tutorials")
        if status.get("domain") != "brand":
            errors.append("STATUS.md domain must be brand")
        if status.get("status") not in {"active", "incubating", "dormant", "archived"}:
            errors.append("STATUS.md status is invalid")

    deck_paths = sorted((ROOT / "AI AGENTS LEVELS").glob("*.md"))
    deck_paths += sorted((ROOT / "PROMPT ENGINEERING").glob("carousel.md"))
    deck_paths += [ROOT / "PI-CODING-AGENT" / "pi-agent.md"]
    for path in deck_paths:
        frontmatter = read_frontmatter(path)
        relative = path.relative_to(ROOT)
        if frontmatter is None:
            errors.append(f"{relative} has no readable Marp frontmatter")
        elif frontmatter.get("marp") != "true":
            errors.append(f"{relative} must declare `marp: true`")

    tracks = {
        "Single Agent": 4,
        "Pipeline Agent": 4,
        "Multi-Agent": 4,
        "Agent Teams": 4,
    }
    level_dir = ROOT / "AI AGENTS LEVELS"
    for track, expected_count in tracks.items():
        actual_count = len(list(level_dir.glob(f"{track} p*.md")))
        if actual_count != expected_count:
            errors.append(f"{track} has {actual_count} parts; expected {expected_count}")

    for required in [
        ROOT / "_templates" / "MARP_STYLING_TEMPLATE.md",
        ROOT / "PI-CODING-AGENT" / "README.md",
        ROOT / "PI-CODING-AGENT" / "build-pdf.sh",
    ]:
        if not required.exists():
            errors.append(f"missing required file: {required.relative_to(ROOT)}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Tutorial validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Tutorial inventory and Marp source validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
