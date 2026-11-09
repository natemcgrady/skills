#!/usr/bin/env python3
"""Check an .excalidraw file against the house style. Prints findings, or `ok`.

The allowed colors are every hex value in references/geist-palette.md.
"""
import json
import re
import sys
from pathlib import Path

PALETTE = Path(__file__).resolve().parent.parent / "references" / "geist-palette.md"
COLORS = set(re.findall(r"`(#[0-9a-f]{6})`", PALETTE.read_text())) | {"transparent"}
ALPHA_OPACITIES = {6, 9, 13, 14, 24, 51, 54, 47, 61, 92}
FONT_FAMILIES = {3, 5, 6}
FONT_SIZES = {14, 16, 18, 20, 22, 40}
SHAPES = {"rectangle", "ellipse", "diamond"}
LINEAR = {"arrow", "line"}


def on_grid(value):
    return round(value, 3) % 4 == 0


def check(path):
    data = json.loads(Path(path).read_text())
    app = data.get("appState", {})
    findings = []
    if app.get("viewBackgroundColor") != "#0a0a0a":
        findings.append(f"appState.viewBackgroundColor is {app.get('viewBackgroundColor')!r}, want '#0a0a0a'")
    if app.get("gridStep") != 4:
        findings.append(f"appState.gridStep is {app.get('gridStep')!r}, want 4")

    for e in data["elements"]:
        if e.get("isDeleted"):
            continue
        say = lambda msg: findings.append(f"{e['type']} {e['id']}: {msg}")
        for key in ("strokeColor", "backgroundColor"):
            if e[key] not in COLORS:
                say(f"{key} {e[key]!r} is not in the Geist palette")
        if e["roughness"] != 0:
            say(f"roughness {e['roughness']}, want 0")
        if e["fillStyle"] != "solid":
            say(f"fillStyle {e['fillStyle']!r}, want 'solid'")
        if e["type"] not in LINEAR and e.get("roundness") is not None:
            say("roundness set, want null (sharp edges)")
        is_alpha = "#ffffff" in (e["strokeColor"], e["backgroundColor"])
        if e["opacity"] != 100 and not (is_alpha and e["opacity"] in ALPHA_OPACITIES):
            say(f"opacity {e['opacity']}, want 100 (or a gray-alpha step on #ffffff)")

        if e["type"] == "text":
            if e["fontFamily"] not in FONT_FAMILIES:
                say(f"fontFamily {e['fontFamily']}, want 5, 6, or 3")
            if e["fontSize"] not in FONT_SIZES:
                say(f"fontSize {e['fontSize']}, want one of {sorted(FONT_SIZES)}")
            if not e.get("containerId") and not (on_grid(e["x"]) and on_grid(e["y"])):
                say(f"position ({e['x']}, {e['y']}) is off the 4 px grid")
            continue

        if e["strokeWidth"] not in (1, 2):
            say(f"strokeWidth {e['strokeWidth']}, want 1 or 2")
        if e["type"] in SHAPES:
            box = (e["x"], e["y"], e["width"], e["height"])
            if not all(map(on_grid, box)):
                say(f"box {box} is off the 4 px grid")
        if e["type"] in LINEAR and not (e.get("startBinding") or e.get("endBinding")):
            if not (on_grid(e["x"]) and on_grid(e["y"])):
                say(f"start ({e['x']}, {e['y']}) is off the 4 px grid")
    return findings


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: check_style.py <file.excalidraw>")
    findings = check(sys.argv[1])
    print("\n".join(findings) or "ok")
    sys.exit(1 if findings else 0)
