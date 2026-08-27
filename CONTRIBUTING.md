# Adding a practice

Three ways in. Pick whichever one fits how you work.

---

## 1. Just email it (easiest)

Hit **"Send me a practice"** on the site and send whatever you've got:

- a typed workout
- a photo of your notebook page
- a PDF or a screenshot
- a Google Doc link

Handwritten is fine. Messy is fine. If it works on deck, it works here. It'll get formatted, tagged, and go in with your name on it.

Helpful but not required: course (SCY/SCM/LCM), the group or ability level it was written for, and total distance.

**New coaches:** questions count too. If you want to know why a set is built a certain way, or whether something is appropriate for your group, ask. That's what this is for.

---

## 2. Open an issue

[Submit a workout](../../issues/new?template=submit-workout.yml) — fill in the form, hit submit, done. No git required.

---

## 3. Open a pull request

If you're comfortable with git:

1. Fork the repo.
2. Add your entry to `data/workouts.json`.
3. Run `python3 tools/build-data.py` from the repo root. This renumbers ids and regenerates `data/workouts.js`.
4. Commit both files and open a PR.

Entry format:

```json
{
  "id": 474,
  "title": "Thursday LCM — Race Pace",
  "type": "Race Pace / Broken",
  "tags": ["Sprint / Speed-Power"],
  "course": "LCM",
  "dist": "2900 Meters",
  "dur": "60 min",
  "stress": "85",
  "interval": "2:00 per 100",
  "source": "coaches_shared",
  "blocks": [
    ["h", "WARM UP"],
    ["l", "400 Smooth — 3 UWs off every wall"],
    ["h", "MAIN"],
    ["l", "8×100 @ 2:00 — Descend 1-4, hold 5-8"]
  ]
}
```

**Field notes:**

- `type` — pick exactly one from the list in the README. It drives the card color and the filter pills.
- `tags` — any other types that also apply. Can be an empty list.
- `course` — `SCY`, `SCM`, or `LCM`.
- `blocks` — `["h", "..."]` is a section header, `["l", "..."]` is a line under it.
- `id` — put anything; the build script renumbers on every run.
- Interval columns, if you use them, run A / B / C — fast, mid, slower.

---

## What gets accepted

Pretty much everything. Two things that'll get sent back for a tweak:

- **LCM sets that don't work in a 50m pool.** No 75s, no mid-pool stops unless swimmers can genuinely stop at the 25m mark. Intervals need to reflect long course pacing.
- **Missing course.** SCY intervals in an LCM practice will get someone hurt.

---

## Credit

Every practice keeps the coach it came from. If you'd rather stay anonymous, say so and it goes in unattributed.
