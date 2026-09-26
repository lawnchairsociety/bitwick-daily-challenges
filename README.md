# bitwick-daily-challenges

Daily programming puzzles from [bitwick.dev](https://bitwick.dev), solved in Python. Each day
has up to four, one per difficulty tier, and once a week there's a fifth, boss-tier puzzle.

Each directory is named for the date of the puzzle (`YYYY-MM-DD`) and holds one file per
difficulty level solved that day — `novice.py`, `apprentice.py`, `adept.py`, `master.py`
or `boss.py` — plus a `tests.json` with the puzzle's worked examples for each tier. Each
`.py` file has the puzzle statement as a comment block at the top and the solution below
it.

## Checking a solution

`check_solution.py` runs a day's solutions against the worked examples in its
`tests.json`:

```sh
python check_solution.py 2026-09-26 novice   # one tier
python check_solution.py 2026-09-26          # every tier in that date's tests.json
python check_solution.py                     # every date, with a pass/fail summary
```

It loads `<date>/<tier>.py` and reads the cases from `<date>/tests.json`, one file per
date with a block for every tier. Tiers not attempted that day are left empty:

```json
{
  "novice": {
    "function": "cross_off",
    "cases": [
      {"args": [["Bran", "Cass"], "Dov"], "expected": ["Bran", "Cass"]}
    ]
  },
  "apprentice": {},
  "adept": {},
  "master": {},
  "boss": {}
}
```

When checking every tier, an empty tier with no `.py` file is skipped. A tier with a
`.py` file but no cases yet is reported and counts as not passing.

`args` is the list of positional arguments for the call and `expected` is the return
value. Each case prints `PASS`, `FAIL` (with expected and actual values) or `ERROR` (if
the function raised), and the script exits non-zero if any case doesn't pass.
