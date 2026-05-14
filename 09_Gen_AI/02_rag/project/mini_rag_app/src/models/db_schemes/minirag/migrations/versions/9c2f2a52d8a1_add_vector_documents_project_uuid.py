"""Add project_uuid to vector_documents.

Revision ID: 9c2f2a52d8a1
Revises: 7b7f0b2e9c2f
Create Date: 2026-05-11
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = "9c2f2a52d8a1"
down_revision = "7b7f0b2e9c2f"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "vector_documents",
        sa.Column("project_uuid", postgresql.UUID(as_uuid=True), nullable=True),
    )
    op.create_index("ix_vector_documents_project_uuid", "vector_documents", ["project_uuid"], unique=False)
    op.create_foreign_key(
        "fk_vector_documents_project_uuid_projects",
        "vector_documents",
        "projects",
        ["project_uuid"],
        ["id"],
        ondelete="CASCADE",
    )

    # Best-effort backfill for existing rows, if any:
    # index_name is "project_{project_id}_collection".
    op.execute(
        """
        UPDATE vector_documents vd
        SET project_uuid = p.id
        FROM projects p
        WHERE vd.project_uuid IS NULL
          AND vd.index_name = 'project_' || p.project_id || '_collection'
        """
    )


def downgrade() -> None:
    op.drop_constraint("fk_vector_documents_project_uuid_projects", "vector_documents", type_="foreignkey")
    op.drop_index("ix_vector_documents_project_uuid", table_name="vector_documents")
    op.drop_column("vector_documents", "project_uuid")

