"""baseline

Revision ID: 0001
Revises:
Create Date: 2026-04-09
"""

revision: str = "0001"
down_revision: str | None = None
branch_labels: str | None = None
depends_on: str | None = None


def upgrade() -> None:
    pass  # Baseline migration — no tables defined yet


def downgrade() -> None:
    pass
