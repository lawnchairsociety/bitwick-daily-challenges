# daily-challenges

One small programming puzzle a day from [bitwick.dev](https://bitwick.dev), solved in Python.

Each directory is named for the date of the puzzle (`YYYY-MM-DD`) and holds one file per
difficulty level solved that day — `novice.py`, `apprentice.py`, `adept.py`, `master.py`
or `boss.py` — plus a `tests.json` with the puzzle's worked examples for each of those
tiers. Each `.py` file has the puzzle statement as a comment block at the top and the
solution below it.

```
2026-09-12/novice.py       The Tap-Room Slate
2026-09-16/apprentice.py   The Beacon-Keeper's Oil Ledger
2026-09-17/apprentice.py   The Tollhouse at Mirebridge
2026-09-18/adept.py        The Lanterns of Dusk Lane
2026-09-19/novice.py       The Ferryman's Tally Board
2026-09-20/apprentice.py   The Cistern-Keeper's Tally at Tidewell
2026-09-21/apprentice.py   The Tollhouse Permit Desk
2026-09-21/novice.py       The Miller's Tally Stick
2026-09-22/novice.py       The Cooper's Tally at the Brimming Barrel
2026-09-23/novice.py       The Cellar Ledger of the Sleeping Badger
2026-09-24/novice.py       The Miller's Whole-Stone Tally
2026-09-25/apprentice.py   The Ferryman's Rafts
2026-09-25/novice.py       The Chalkboard of the Hearth and Hammer
2026-09-26/novice.py       The Roster of the Night Watch
```

## Checking a solution

`check_solution.py` runs a day's solutions against the worked examples in its
`tests.json`:

```sh
python check_solution.py 2026-09-26 novice   # one tier
python check_solution.py 2026-09-26          # every tier in that date's tests.json
```

It loads `<date>/<tier>.py` and reads the cases from `<date>/tests.json`, one file per
date with an entry for each tier solved that day:

```json
{
  "novice": {
    "function": "cross_off",
    "cases": [
      {"args": [["Bran", "Cass"], "Dov"], "expected": ["Bran", "Cass"]}
    ]
  }
}
```

`args` is the list of positional arguments for the call and `expected` is the return
value. Each case prints `PASS`, `FAIL` (with expected and actual values) or `ERROR` (if
the function raised), and the script exits non-zero if any case doesn't pass.
