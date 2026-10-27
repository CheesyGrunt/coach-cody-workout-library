# Coach Cody's Workout Library

473 swim practices in one searchable page. SCY, SCM, and LCM. Filter by energy system, filter by course, or search any set, drill, or distance.

**Live site:** https://coach-cody-workout-library.onrender.com

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
| `config.js` | Your name, your email, and the Start Here picks. **The only file you have to edit.** |
| `data/workouts.json` | The source of truth. 473 practices. Edit this to add or fix one. |
| `data/workouts.js` | Generated from the JSON — this is what the page loads. |
| `tools/build-data.py` | Regenerates `workouts.js` after you edit the JSON. |
| `coaches.html` | **New Coaches** — welcome, glossary, how a practice is built. |
| `submit.html` | **Send a Practice** — any format, credited to the coach. |
| `style.css` | Shared styles across all pages, including the lane rope. |
| `og-image.png` | Social preview card. Regenerate it if the practice count changes a lot. |
| `favicon.svg` / `.png` | Browser tab and phone home-screen icon. |
| `robots.txt` / `sitemap.xml` | Lets search engines in, keeps Deck Pass out. |
| `admin.html` | **Deck Pass** — the tool for turning raw practices into library entries. |
| `render.yaml` | Tells Render how to serve the site. You shouldn't need to touch it. |

---

## Setting it up

**1. Fill in `config.js`**

```js
window.WORKOUT_CONFIG = {
  coachName: "Coach Cody",
  coachEmail: "cody.a.mackall@gmail.com",
  adminPassphrase: "your-passphrase"
};
```

**2. Push it to GitHub**

Render pulls from a Git repo, so the code still lives on GitHub — Render just serves it.

Make a new repo on github.com (public, no README — this folder already has one), then from inside this folder:

```bash
git init
git add .
git commit -m "Coach Cody's Workout Library"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/coach-cody-workout-library.git
git push -u origin main
```

**3. Deploy on Render**

Sign in at [dashboard.render.com](https://dashboard.render.com), then **New + → Static Site**. Connect your GitHub account, pick this repo, and Render reads `render.yaml` for the rest:

| Setting | Value |
|---|---|
| Branch | `main` |
| Root Directory | *(leave blank)* |
| Build Command | *(leave blank — there is no build step)* |
| Publish Directory | `.` |

Click **Create Static Site**. First deploy takes about a minute.

Your URL shows at the top of the service page: `https://coach-cody-workout-library.onrender.com`. That's the link you share.

Every push to `main` from here on redeploys automatically.

---

## Start here (the curated six)

The top of the library shows a short "Start here" row: a handful of practices you want a brand-new coach to run first.

**These ship as placeholders.** They were picked mechanically for clean structure and a good spread across a week, not by you. Swapping them for your own picks is the single highest-value edit on the site, because it turns a pile of 473 into a door someone can walk through.

Edit `starterPicks` in `config.js`:

```js
starterPicks: [
  { id: 276, why: "A clean threshold day. This is the workout you will run more often than any other." },
  ...
]
```

To find an id, open a practice on the site and look at the link: it ends in `#p=276`. Set `starterPicks: []` to hide the row entirely.

---

## Look and feel

The site uses your Tier 1 Open Water palette: Deep Teal `#004E64` as primary, Persian Indigo `#27187E` as the attention accent, Ink on Ghost. Type is Oswald for caps and headings, Montserrat for body. JetBrains Mono is kept for intervals and distances, where a monospace column matters more than brand fidelity.

**Light is the default on purpose.** A coach reads this on a deck in daylight, and the print sheet is black on white, so what you see matches what comes out of the printer. A dark toggle sits in the nav on every page, it remembers the choice, and it follows the operating system until someone sets it themselves.

**All colour lives in `style.css`.** Two blocks of tokens, `:root` for light and `:root[data-theme="dark"]` for dark, including the twelve focus-area colours (`--t-aerobic`, `--t-sprint`, and so on). Change a value once and it moves everywhere. No page has hardcoded hex any more.

---

## Using the library

**Three filter rows,** stacked so you narrow the same way you'd think about it:

- **Pool** - SCY, SCM, LCM
- **Length** - Under 2k, 2k-3k, 3k-4k, 4k+. This is the "I have an hour" filter.
- **Focus** - the twelve energy systems

Plus search across every set line, and a sort (shortest first, longest first, A-Z). Filters stack, and **Clear filters** resets everything.

**Click any practice** to open the full sheet. From there:

- **Print this practice** - prints just that practice on clean white paper, nothing else on the page. Take it on deck.
- **Copy as text** - plain text for a group chat or an email.
- **Copy link** - a direct link to that one practice (`#p=142`). Send a coach exactly the set you meant.
- **Arrow keys** step through the filtered list. **Esc** closes.

**Pick one for me** opens a random practice from whatever is currently filtered.

The grid loads 24 at a time and pulls more as you scroll, so it stays quick on a phone.

---

## Known data to clean up

A few records came through the original import with distances that aren't real practice distances. The site handles them gracefully (they show as `--` and sort to the end), but they're worth fixing in Deck Pass when you get a chance:

**Placeholder distances** - ids 96, 65, 88, 291, 297, 19, 24 (values of 0, 5, 40, 395).

**Too big for a single practice** - id 282 reads 150,325; ids 332, 287, 283, 288, 284, 289 land between 11,875 and 21,350. These look like full-day or full-week totals rather than one session.

---

## Deck Pass — adding practices without touching JSON

`admin.html` on the live site (or open it locally). Passphrase is set in `config.js`.

1. **Paste or drop** a practice — plain text, markdown, or a `.json` file. For PDFs and photos, copy the text out and paste it.
2. **Read it.** The parser splits headers from set lines, guesses the type from the language, reads the course, and adds up the distance from every `4x50` and `400 swim` it finds.
3. **Fix the guesses.** Green "guessed" labels mark anything the parser decided on its own. There's a live card preview so you see exactly what lands in the library.
4. **Add to the stack.** Queue as many as you want — the stack survives closing the tab.
5. **Export.** Downloads `workouts.json` and `workouts.js`. Drop both into `data/`, then commit and push.

**On the passphrase:** it's a doorknob, not a deadbolt. Anyone can read `config.js`. That's fine, and here's why — Deck Pass has no server behind it. It reads files on *your* computer and writes files to *your* downloads folder. Someone who finds the page and guesses the passphrase can generate a JSON file for themselves. They cannot touch your library. The only thing that changes what's live is a push from you.

---

## Locking down the repo

The library should be yours to edit and everyone else's to read. Public repo, but nobody pushes but you.

That's already how GitHub works — outside collaborators can't push to a repo they're not on. But a few settings make it airtight:

- **Settings → Collaborators** — should list only you.
- **Settings → General → Features** — leave **Issues** on (that's the submission form) and turn **Wikis**, **Projects**, and **Discussions** off if you don't want them.
- **Settings → General → Pull Requests** — you can't disable forks on a public repo, and you don't need to. Anyone can fork and open a PR; nothing merges without you clicking merge.
- **Settings → Branches → Add branch ruleset** on `main` — optional, but it blocks force-pushes and accidental deletion. Useful insurance against your own bad Tuesday.

---

## Adding a practice

Edit `data/workouts.json`, add an entry, then run:

```bash
python3 tools/build-data.py
git add . && git commit -m "Add practice" && git push
```

Render picks up the push and redeploys on its own. No dashboard visit needed.

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
