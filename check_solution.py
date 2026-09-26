"""Check a day's solution against the test cases in its JSON file.

    python check_solution.py 2026-09-26 novice
    python check_solution.py 2026-09-26          # every tier in tests.json
    python check_solution.py                     # every date with a tests.json

Loads <date>/<tier>.py, calls the function named under that tier in
<date>/tests.json with each case's args, and compares the result to the case's
expected value. Each date has one tests.json with a block for every tier; tiers
not attempted that day are left as {}:

    {
      "novice": {
        "function": "cross_off",
        "cases": [
          {"args": [["Bran", "Cass"], "Dov"], "expected": ["Bran", "Cass"]}
        ]
      },
      "apprentice": {},
      ...
    }

With no tier given, a tier is skipped if it has neither a .py file nor any cases.
"""

import argparse
import contextlib
import copy
import importlib.util
import io
import json
import sys
from pathlib import Path

TIERS = ["novice", "apprentice", "adept", "master", "boss"]
ROOT = Path(__file__).parent

# Don't leave __pycache__ folders in the date directories when loading solutions.
sys.dont_write_bytecode = True


def load_solution(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    # Keep any stray prints in a solution file out of the results.
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


def run_tier(solution_path, tests):
    """Run one tier's cases, printing each result. Returns (passed, total)."""
    try:
        func = getattr(load_solution(solution_path), tests["function"])
    except Exception as e:
        print(f"ERROR loading {solution_path.relative_to(ROOT)}\n    {type(e).__name__}: {e}")
        return 0, len(tests["cases"])
    passed = 0
    for i, case in enumerate(tests["cases"], 1):
        call = f"{tests['function']}({', '.join(map(repr, case['args']))})"
        try:
            actual = func(*copy.deepcopy(case["args"]))
        except Exception as e:
            print(f"ERROR {i}: {call}\n    raised {type(e).__name__}: {e}")
            continue
        if actual == case["expected"]:
            passed += 1
            print(f"PASS  {i}: {call}")
        else:
            print(f"FAIL  {i}: {call}\n    expected {case['expected']!r}\n    got      {actual!r}")
    return passed, len(tests["cases"])


def check_date(date, tier=None):
    """Check one date's tiers (or just `tier`), printing results. Returns True if all passed."""
    tests_path = ROOT / date / "tests.json"
    if not tests_path.exists():
        print(f"Not found: {tests_path.relative_to(ROOT)}")
        return False
    all_tests = json.loads(tests_path.read_text())

    if tier:
        if tier not in all_tests:
            print(f"No {tier!r} entry in {tests_path.relative_to(ROOT)}")
            return False
        tiers = [tier]
    else:
        tiers = [t for t in TIERS if t in all_tests
                 and (all_tests[t] or (ROOT / date / f"{t}.py").exists())]
        if not tiers:
            print(f"No tiers to check in {tests_path.relative_to(ROOT)}")
            return False

    all_passed = True
    for n, tier in enumerate(tiers):
        solution_path = ROOT / date / f"{tier}.py"
        if len(tiers) > 1:
            print(f"{'\n' if n else ''}== {tier}")
        if not solution_path.exists():
            print(f"Not found: {solution_path.relative_to(ROOT)}")
            all_passed = False
            continue
        if not all_tests[tier].get("cases"):
            print(f"No {tier} cases in {tests_path.relative_to(ROOT)} yet")
            all_passed = False
            continue
        passed, total = run_tier(solution_path, all_tests[tier])
        print(f"\n{passed}/{total} passed")
        all_passed = all_passed and passed == total
    return all_passed


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("date", nargs="?",
                        help="puzzle date, YYYY-MM-DD; omit to check every date")
    parser.add_argument("tier", nargs="?", choices=TIERS,
                        help="tier to check; omit to check every tier in tests.json")
    args = parser.parse_args()

    if args.date:
        sys.exit(0 if check_date(args.date, args.tier) else 1)

    dates = sorted(p.parent.name for p in ROOT.glob("????-??-??/tests.json"))
    failed = []
    for n, date in enumerate(dates):
        print(f"{'\n' if n else ''}######## {date}")
        if not check_date(date):
            failed.append(date)

    print(f"\n{len(dates) - len(failed)}/{len(dates)} dates passed")
    if failed:
        print(f"Failed: {', '.join(failed)}")
    sys.exit(0 if not failed else 1)


if __name__ == "__main__":
    main()
