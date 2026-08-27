# Coach Cody's Workout Library

473 swim practices in one searchable page. SCY, SCM, and LCM. Filter by energy system, filter by course, or search any set, drill, or distance.

**Live site:** https://YOUR-USERNAME.github.io/coach-cody-workout-library/

---

## Why this exists

I started this for the newer coaches getting their feet wet.

If you've ever stood on deck at 5:15 in the morning staring at an empty whiteboard, wondering what a good practice actually looks like — this is for you. Nobody should have to invent 473 workouts to figure out how a week is built, or how a season stacks up, or what a race-pace set is supposed to feel like.

So take them. Run them. Change the intervals to fit your group. Look at how a Tuesday differs from a Thursday. That's the whole point.

We'll adjust from here as it grows.

---

## Got a practice? Send it.

The library gets better when coaches add to it. Two ways in:

1. **Email it.** Hit "Send me a practice" on the site. Typed, handwritten and photographed, a PDF, a screenshot off your phone — doesn't matter. It gets formatted, tagged, and added.
2. **Open an issue.** [Submit a workout](../../issues/new?template=submit-workout.yml) right here on GitHub.

Questions about *why* a set is built the way it is are welcome too. That's how you learn this.

Coaches comfortable with git can open a pull request against `data/workouts.json`. See [CONTRIBUTING.md](CONTRIBUTING.md).

Every practice keeps credit to whoever wrote it.

---

## What's in here

| File | What it does |
|---|---|
| `index.html` | The whole app. One file, no build step, no dependencies. |
| `config.js` | Your name, your email, your repo URL. **The only file you have to edit.** |
| `data/workouts.json` | The source of truth. 473 practices. Edit this to add or fix one. |
| `data/workouts.js` | Generated from the JSON — this is what the page loads. |
| `tools/build-data.py` | Regenerates `workouts.js` after you edit the JSON. |

---

## Setting it up

**1. Fill in `config.js`**

```js
window.WORKOUT_CONFIG = {
  coachName: "Coach Cody",
  coachEmail: "you@example.com",
  repoUrl: "https://github.com/YOUR-USERNAME/coach-cody-workout-library"
};
```

**2. Push it to GitHub**

Make a new repo on github.com (public, no README — this folder already has one), then from inside this folder:

```bash
git init
git add .
git commit -m "Coach Cody's Workout Library"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/coach-cody-workout-library.git
git push -u origin main
```

**3. Turn on GitHub Pages**

**Settings → Pages → Source: Deploy from a branch → Branch `main`, folder `/ (root)` → Save.**

The site goes live at `https://YOUR-USERNAME.github.io/coach-cody-workout-library/`. That's the link you share.

---

## Adding a practice

Edit `data/workouts.json`, add an entry, then run:

```bash
python3 tools/build-data.py
git add . && git commit -m "Add practice" && git push
```

Entry format:

```json
{
  "id": 474,
  "title": "Thursday LCM — Race Pace",
  "type": "Race Pace / Broken",
  "tags": ["Sprint / Speed-Power", "Kick"],
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

`"h"` is a section header, `"l"` is a line under it. `id` gets renumbered automatically when you run the build script, so don't sweat it.

Valid `type` values (pick one — this drives the color bar and the filter pills):

`Aerobic / Base` · `Threshold / Endurance` · `VO2 Max` · `Sprint / Speed-Power` · `Race Pace / Broken` · `IM` · `Kick` · `Pull / Recovery` · `Underwater / Skills` · `Distance / Test` · `Stroke-Specific` · `Themed / Holiday`

`tags` is a list of any other types that also apply.

---

## Notes for newer coaches

A few things that will save you a bad practice:

- **LCM practices are built for a 50m pool.** No 75s, nothing that asks a swimmer to stop mid-pool. Intervals reflect long course pacing, not short course — a 100 in a 50m pool takes noticeably longer than in a 25-yard pool, and the interval has to account for that.
- **Interval columns run A / B / C.** A is your fast lane, B is mid, C is slower. Some practices list all three, some only two. Adjust to your group — nobody's numbers are your numbers.
- **Time estimates are coach-facing guides.** They help you plan a 60-minute window. They are not a promise, and swimmers don't need to see them.
- **Practice structure** in most of these runs warm-up → kick → skill/pre-set → main → pull → blocks/cool down. That skeleton works. Start there.
- Practices came from nine batches — handwritten notebooks, typed sheets, shared sets from other coaches. Source is tagged on every entry.

---

## Using these

If you post a set publicly, credit the coach it's tagged to. Otherwise, take what works and go coach.
