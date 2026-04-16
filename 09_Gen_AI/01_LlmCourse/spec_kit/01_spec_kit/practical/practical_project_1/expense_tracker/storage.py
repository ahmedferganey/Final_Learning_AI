from __future__ import annotations

import os
import sqlite3
from dataclasses import dataclass
from datetime import date
from pathlib import Path


DEFAULT_DB_PATH = Path.home() / ".expense-tracker" / "expenses.db"


@dataclass(slots=True)
class Expense:
    id: int
    amount_cents: int
    category: str
    description: str
    expense_date: str


class ExpenseStore:
    def __init__(self, db_path: Path | None = None) -> None:
        configured_path = os.environ.get("EXPENSE_TRACKER_DB_PATH")
        self.db_path = Path(configured_path) if configured_path else (db_path or DEFAULT_DB_PATH)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._initialize()

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.db_path)
        connection.row_factory = sqlite3.Row
        return connection

    def _initialize(self) -> None:
        with self._connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    amount_cents INTEGER NOT NULL CHECK(amount_cents >= 0),
                    category TEXT NOT NULL,
                    description TEXT NOT NULL,
                    expense_date TEXT NOT NULL
                )
                """
            )

    def add_expense(
        self,
        *,
        amount_cents: int,
        category: str,
        description: str,
        expense_date: str,
    ) -> Expense:
        with self._connect() as connection:
            cursor = connection.execute(
                """
                INSERT INTO expenses (amount_cents, category, description, expense_date)
                VALUES (?, ?, ?, ?)
                """,
                (amount_cents, category.strip(), description.strip(), expense_date),
            )
            expense_id = int(cursor.lastrowid)
        return Expense(expense_id, amount_cents, category.strip(), description.strip(), expense_date)

    def list_expenses(
        self,
        *,
        category: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
    ) -> list[Expense]:
        clauses: list[str] = []
        params: list[str] = []
        if category:
            clauses.append("category = ?")
            params.append(category)
        if start_date:
            clauses.append("expense_date >= ?")
            params.append(start_date)
        if end_date:
            clauses.append("expense_date <= ?")
            params.append(end_date)

        where = f"WHERE {' AND '.join(clauses)}" if clauses else ""
        with self._connect() as connection:
            rows = connection.execute(
                f"""
                SELECT id, amount_cents, category, description, expense_date
                FROM expenses
                {where}
                ORDER BY expense_date DESC, id DESC
                """,
                params,
            ).fetchall()

        return [
            Expense(
                id=int(row["id"]),
                amount_cents=int(row["amount_cents"]),
                category=str(row["category"]),
                description=str(row["description"]),
                expense_date=str(row["expense_date"]),
            )
            for row in rows
        ]

    def delete_expense(self, expense_id: int) -> bool:
        with self._connect() as connection:
            cursor = connection.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
            return cursor.rowcount > 0

    def summary_by_category(
        self,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
    ) -> list[tuple[str, int]]:
        clauses: list[str] = []
        params: list[str] = []
        if start_date:
            clauses.append("expense_date >= ?")
            params.append(start_date)
        if end_date:
            clauses.append("expense_date <= ?")
            params.append(end_date)

        where = f"WHERE {' AND '.join(clauses)}" if clauses else ""
        with self._connect() as connection:
            rows = connection.execute(
                f"""
                SELECT category, SUM(amount_cents) AS total_cents
                FROM expenses
                {where}
                GROUP BY category
                ORDER BY total_cents DESC, category ASC
                """,
                params,
            ).fetchall()

        return [(str(row["category"]), int(row["total_cents"])) for row in rows]


def current_month_bounds(today: date | None = None) -> tuple[str, str]:
    resolved_today = today or date.today()
    month_start = resolved_today.replace(day=1)
    if resolved_today.month == 12:
        next_month = resolved_today.replace(year=resolved_today.year + 1, month=1, day=1)
    else:
        next_month = resolved_today.replace(month=resolved_today.month + 1, day=1)
    month_end = next_month.fromordinal(next_month.toordinal() - 1)
    return month_start.isoformat(), month_end.isoformat()

