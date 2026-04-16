from __future__ import annotations

import argparse
from datetime import date, datetime
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

from .storage import Expense, ExpenseStore, current_month_bounds


def parse_amount_to_cents(raw_amount: str) -> int:
    try:
        decimal_amount = Decimal(raw_amount).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    except InvalidOperation as exc:
        raise ValueError(f"Invalid amount: {raw_amount}") from exc
    if decimal_amount < 0:
        raise ValueError("Amount must be zero or greater.")
    return int(decimal_amount * 100)


def parse_iso_date(raw_date: str) -> str:
    try:
        return datetime.strptime(raw_date, "%Y-%m-%d").date().isoformat()
    except ValueError as exc:
        raise ValueError(f"Invalid date: {raw_date}. Use YYYY-MM-DD.") from exc


def format_currency(amount_cents: int) -> str:
    return f"${amount_cents / 100:.2f}"


def format_expenses_table(expenses: list[Expense]) -> str:
    if not expenses:
        return "No expenses found for the selected filters."

    headers = ("ID", "Date", "Category", "Amount", "Description")
    rows = [
        (
            str(expense.id),
            expense.expense_date,
            expense.category,
            format_currency(expense.amount_cents),
            expense.description,
        )
        for expense in expenses
    ]
    widths = [
        max(len(header), *(len(row[index]) for row in rows))
        for index, header in enumerate(headers)
    ]

    def render_row(row: tuple[str, ...]) -> str:
        return "  ".join(cell.ljust(widths[index]) for index, cell in enumerate(row))

    separator = "  ".join("-" * width for width in widths)
    return "\n".join([render_row(headers), separator, *(render_row(row) for row in rows)])


def format_summary_chart(summary_rows: list[tuple[str, int]]) -> str:
    if not summary_rows:
        return "No expenses found for the selected period."

    max_total = max(total for _, total in summary_rows)
    max_category_len = max(len(category) for category, _ in summary_rows)
    lines = ["Spending by category"]
    for category, total in summary_rows:
        bar_length = max(1, round((total / max_total) * 30))
        lines.append(
            f"{category.ljust(max_category_len)}  {'#' * bar_length}  {format_currency(total)}"
        )
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="expense", description="Track personal expenses.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new expense.")
    add_parser.add_argument("amount", help="Amount in dollars, e.g. 42.50")
    add_parser.add_argument("category", help="Free-form category name.")
    add_parser.add_argument("description", help="Expense description.")
    add_parser.add_argument("--date", dest="expense_date", help="Expense date as YYYY-MM-DD.")

    list_parser = subparsers.add_parser("list", help="List expenses.")
    list_parser.add_argument("--category", help="Filter by category.")
    list_parser.add_argument("--start-date", help="Filter from date YYYY-MM-DD.")
    list_parser.add_argument("--end-date", help="Filter to date YYYY-MM-DD.")
    list_parser.add_argument(
        "--all",
        action="store_true",
        help="List all expenses instead of defaulting to the current month.",
    )

    delete_parser = subparsers.add_parser("delete", help="Delete an expense by ID.")
    delete_parser.add_argument("expense_id", type=int)

    summary_parser = subparsers.add_parser("summary", help="Summarize spending by category.")
    summary_parser.add_argument("--start-date", help="Filter from date YYYY-MM-DD.")
    summary_parser.add_argument("--end-date", help="Filter to date YYYY-MM-DD.")
    summary_parser.add_argument(
        "--all",
        action="store_true",
        help="Summarize across all expenses instead of defaulting to the current month.",
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    store = ExpenseStore()

    try:
        if args.command == "add":
            expense_date = parse_iso_date(args.expense_date) if args.expense_date else date.today().isoformat()
            expense = store.add_expense(
                amount_cents=parse_amount_to_cents(args.amount),
                category=args.category,
                description=args.description,
                expense_date=expense_date,
            )
            print(
                f"Added expense #{expense.id}: {format_currency(expense.amount_cents)} "
                f"for {expense.category} on {expense.expense_date}."
            )
            return 0

        if args.command == "list":
            start_date = args.start_date
            end_date = args.end_date
            if not args.all and not start_date and not end_date:
                start_date, end_date = current_month_bounds()
            if start_date:
                start_date = parse_iso_date(start_date)
            if end_date:
                end_date = parse_iso_date(end_date)
            expenses = store.list_expenses(
                category=args.category,
                start_date=start_date,
                end_date=end_date,
            )
            print(format_expenses_table(expenses))
            return 0

        if args.command == "delete":
            deleted = store.delete_expense(args.expense_id)
            if not deleted:
                print(f"Expense with ID {args.expense_id} does not exist.")
                return 1
            print(f"Deleted expense #{args.expense_id}.")
            return 0

        if args.command == "summary":
            start_date = args.start_date
            end_date = args.end_date
            if not args.all and not start_date and not end_date:
                start_date, end_date = current_month_bounds()
            if start_date:
                start_date = parse_iso_date(start_date)
            if end_date:
                end_date = parse_iso_date(end_date)
            summary_rows = store.summary_by_category(start_date=start_date, end_date=end_date)
            print(format_summary_chart(summary_rows))
            return 0
    except ValueError as error:
        print(str(error))
        return 2

    parser.print_help()
    return 1

