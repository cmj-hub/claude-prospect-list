#!/usr/bin/env python3
"""score.py prints a list score from a signal or refuses a title-only list."""

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CELL = "super-secret-cell"


def run(args, stdin=None):
    return subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "score.py"), *args],
        input=stdin,
        capture_output=True,
        text=True,
    )


class ScoreList(unittest.TestCase):
    def test_good_draft_prints_score(self):
        result = run(["--file", str(ROOT / "examples" / "list-good.json")])
        self.assertEqual(result.returncode, 0)
        self.assertIn("a list score from a signal", result.stdout)
        self.assertIn("signal: Posted a role for an outbound lead this week.", result.stdout)
        self.assertNotIn("a title-only list", result.stdout)

    def test_title_only_exits_1(self):
        result = run(["--file", str(ROOT / "examples" / "list-title.json")])
        self.assertEqual(result.returncode, 1)
        self.assertIn("a title-only list", result.stdout)
        self.assertNotIn("a list score from a signal", result.stdout)

    def test_bad_json_hides_input(self):
        bad = run(["--stdin"], stdin='{"title": "' + CELL)
        self.assertNotEqual(bad.returncode, 0)
        self.assertNotIn(CELL, bad.stdout + bad.stderr)
        self.assertIn("invalid JSON", bad.stderr)
        array = run(["--stdin"], stdin='["' + CELL + '"]')
        self.assertNotEqual(array.returncode, 0)
        self.assertNotIn(CELL, array.stdout + array.stderr)
        self.assertIn("JSON must be an object", array.stderr)


if __name__ == "__main__":
    unittest.main()
