"""Check a day's solution against the test cases in its JSON file.

    python check_solution.py 2026-09-26 novice
    python check_solution.py 2026-09-26          # every tier in tests.json

Loads <date>/<tier>.py, calls the function named under that tier in
<date>/tests.json with each case's args, and compares the result to the case's
expected value. Each date has one tests.json holding every tier solved that day:

    {
      "novice": {
        "function": "cross_off",
        "cases": [
          {"args": [["Bran", "Cass"], "Dov"], "expected": ["Bran", "Cass"]}
        ]
      },
      "apprentice": {...}
    }
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
    func = getattr(load_solution(solution_path), tests["function"])
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


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("date", help="puzzle date, YYYY-MM-DD")
    parser.add_argument("tier", nargs="?", choices=TIERS,
                        help="tier to check; omit to check every tier in tests.json")
    args = parser.parse_args()

    tests_path = ROOT / args.date / "tests.json"
    if not tests_path.exists():
        sys.exit(f"Not found: {tests_path.relative_to(ROOT)}")
    all_tests = json.loads(tests_path.read_text())

    if args.tier:
        if args.tier not in all_tests:
            sys.exit(f"No {args.tier!r} entry in {tests_path.relative_to(ROOT)}")
        tiers = [args.tier]
    else:
        tiers = [tier for tier in TIERS if tier in all_tests]

    all_passed = True
    for n, tier in enumerate(tiers):
        solution_path = ROOT / args.date / f"{tier}.py"
        if len(tiers) > 1:
            print(f"{'\n' if n else ''}== {tier}")
        if not solution_path.exists():
            print(f"Not found: {solution_path.relative_to(ROOT)}")
            all_passed = False
            continue
        passed, total = run_tier(solution_path, all_tests[tier])
        print(f"\n{passed}/{total} passed")
        all_passed = all_passed and passed == total

    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
