#!/usr/bin/env python3
"""
Rebuild data/workouts.js from data/workouts.json.

workouts.json is the source of truth — it's the file you (or a contributor)
edit. workouts.js is what the web page actually loads, because a plain
JSON fetch() is blocked when you open index.html straight off your desktop.

Run it from the repo root:

    python3 tools/build-data.py
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "workouts.json"
OUT = ROOT / "data" / "workouts.js"

data = json.loads(SRC.read_text(encoding="utf-8"))

# renumber ids so they always run 1..N with no gaps
for i, w in enumerate(data["workouts"], 1):
    w["id"] = i

data.setdefault("meta", {})
data["meta"]["count"] = len(data["workouts"])
data["meta"]["sources"] = sorted({w.get("source", "unknown") for w in data["workouts"]})

SRC.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")

with OUT.open("w", encoding="utf-8") as f:
    f.write("/* Coach Cody's Workout Library - data file.\n")
    f.write("   Generated from workouts.json by tools/build-data.py. Do not edit by hand. */\n")
    f.write("window.WORKOUT_DATA = ")
    json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
    f.write(";\n")

print(f"Wrote {len(data['workouts'])} practices to {OUT.relative_to(ROOT)}")
