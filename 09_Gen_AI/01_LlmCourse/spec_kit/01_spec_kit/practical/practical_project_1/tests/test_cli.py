from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


class ExpenseTrackerCliTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.db_path = Path(self.temp_dir.name) / "expenses.db"

    def run_cli(self, *args: str) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env["EXPENSE_TRACKER_DB_PATH"] = str(self.db_path)
        env["PYTHONPATH"] = str(PROJECT_ROOT)
        return subprocess.run(
            [sys.executable, "-m", "expense_tracker", *args],
            cwd=PROJECT_ROOT,
            env=env,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_add_and_list_default_month(self) -> None:
        added = self.run_cli("add", "42.50", "food", "Lunch at cafe")
        listed = self.run_cli("list")

        self.assertEqual(added.returncode, 0, added.stderr)
        self.assertIn("Added expense #1: $42.50 for food", added.stdout)
        self.assertEqual(listed.returncode, 0, listed.stderr)
        self.assertIn("Lunch at cafe", listed.stdout)
        self.assertIn("$42.50", listed.stdout)

    def test_category_and_date_filters(self) -> None:
        self.run_cli("add", "12.00", "coffee", "Espresso", "--date", "2026-04-05")
        self.run_cli("add", "18.00", "food", "Brunch", "--date", "2026-04-06")

        filtered = self.run_cli(
            "list",
            "--category",
            "coffee",
            "--start-date",
            "2026-04-01",
            "--end-date",
            "2026-04-30",
        )

        self.assertEqual(filtered.returncode, 0, filtered.stderr)
        self.assertIn("Espresso", filtered.stdout)
        self.assertNotIn("Brunch", filtered.stdout)

    def test_summary_groups_by_category(self) -> None:
        self.run_cli("add", "10.00", "food", "Breakfast", "--date", "2026-04-01")
        self.run_cli("add", "15.00", "food", "Lunch", "--date", "2026-04-02")
        self.run_cli("add", "7.50", "coffee", "Latte", "--date", "2026-04-03")

        summary = self.run_cli(
            "summary",
            "--start-date",
            "2026-04-01",
            "--end-date",
            "2026-04-30",
        )

        self.assertEqual(summary.returncode, 0, summary.stderr)
        self.assertIn("food", summary.stdout)
        self.assertIn("$25.00", summary.stdout)
        self.assertIn("coffee", summary.stdout)
        self.assertIn("$7.50", summary.stdout)

    def test_delete_missing_id_is_a_clear_error(self) -> None:
        deleted = self.run_cli("delete", "999")

        self.assertEqual(deleted.returncode, 1)
        self.assertIn("Expense with ID 999 does not exist.", deleted.stdout)

    def test_invalid_amount_is_rejected(self) -> None:
        result = self.run_cli("add", "-5.00", "food", "Negative lunch")

        self.assertEqual(result.returncode, 2)
        self.assertIn("Amount must be zero or greater.", result.stdout)


if __name__ == "__main__":
    unittest.main()
