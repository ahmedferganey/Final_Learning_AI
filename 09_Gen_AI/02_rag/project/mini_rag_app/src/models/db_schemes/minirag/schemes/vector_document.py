import uuid
from datetime import datetime

from pgvector.sqlalchemy import Vector
from sqlalchemy import DateTime, Index, String, Text, func, text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column

from database.base import Base


class VectorDocumentORM(Base):
    __tablename__ = "vector_documents"
    __table_args__ = (
        Index("ix_vector_documents_index_name", "index_name"),
        Index("ix_vector_documents_index_name_id", "index_name", "id"),
    )

    # Use deterministic UUIDs when callers provide them (to match Qdrant record ids).
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    index_name: Mapped[str] = mapped_column(String(500), nullable=False)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    metadata: Mapped[dict] = mapped_column(
        JSONB,
        nullable=False,
        default=dict,
        server_default=text("'{}'::jsonb"),
    )
    # Keep the initial dimension aligned with current embedding model size (384).
    # Changing embedding models requires a migration.
    embedding: Mapped[list[float]] = mapped_column(Vector(384), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=True,
    )

