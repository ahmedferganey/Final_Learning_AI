"""Add vector_documents table for PGVector.

Revision ID: 7b7f0b2e9c2f
Revises: abc25a35ca49
Create Date: 2026-05-11
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from pgvector.sqlalchemy import Vector


# revision identifiers, used by Alembic.
revision = "7b7f0b2e9c2f"
down_revision = "abc25a35ca49"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Ensure pgvector extension exists.
    op.execute("CREATE EXTENSION IF NOT EXISTS vector")

    op.create_table(
        "vector_documents",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("index_name", sa.String(length=500), nullable=False),
        sa.Column("text", sa.Text(), nullable=False),
        sa.Column("metadata", postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'{}'::jsonb"), nullable=False),
        sa.Column("embedding", Vector(384), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True),
    )

    op.create_index("ix_vector_documents_index_name", "vector_documents", ["index_name"], unique=False)
    op.create_index("ix_vector_documents_index_name_id", "vector_documents", ["index_name", "id"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_vector_documents_index_name_id", table_name="vector_documents")
    op.drop_index("ix_vector_documents_index_name", table_name="vector_documents")
    op.drop_table("vector_documents")
