from __future__ import annotations

from typing import Optional
from uuid import UUID

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from models.db_schemes import DataChunk
from models.db_schemes.minirag.schemes import DataChunkORM


class ChunkRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    def _to_schema(self, record: DataChunkORM) -> DataChunk:
        return DataChunk.model_construct(
            id=record.id,
            chunk_text=record.chunk_text,
            chunk_metadata=record.chunk_metadata or {},
            chunk_order=record.chunk_order,
            project_uuid=record.project_uuid,
            asset_uuid=record.asset_uuid,
        )

    async def create_chunk(
        self,
        chunk_text: str,
        chunk_metadata: dict,
        chunk_order: int,
        project_uuid: UUID,
        asset_uuid: UUID,
    ) -> DataChunk:
        record = DataChunkORM(
            chunk_text=chunk_text,
            chunk_metadata=chunk_metadata,
            chunk_order=chunk_order,
            project_uuid=project_uuid,
            asset_uuid=asset_uuid,
        )
        self.session.add(record)
        await self.session.flush()
        await self.session.refresh(record)
        return self._to_schema(record)

    async def insert_many_chunks(self, chunks: list, batch_size: int = 100) -> int:
        inserted = 0
        for index in range(0, len(chunks), batch_size):
            batch = chunks[index:index + batch_size]
            records = [
                DataChunkORM(
                    chunk_text=chunk["chunk_text"],
                    chunk_metadata=chunk["chunk_metadata"],
                    chunk_order=chunk["chunk_order"],
                    project_uuid=chunk["project_uuid"],
                    asset_uuid=chunk["asset_uuid"],
                )
                for chunk in batch
            ]
            self.session.add_all(records)
            await self.session.flush()
            inserted += len(records)
        return inserted

    async def delete_chunks_by_project_uuid(self, project_uuid: UUID) -> int:
        statement = delete(DataChunkORM).where(DataChunkORM.project_uuid == project_uuid)
        result = await self.session.execute(statement)
        return result.rowcount or 0

    async def get_chunk(self, chunk_uuid: UUID) -> Optional[DataChunk]:
        statement = select(DataChunkORM).where(DataChunkORM.id == chunk_uuid).limit(1)
        record = await self.session.scalar(statement)
        if record is None:
            return None
        return self._to_schema(record)

    async def get_project_chunks(self, project_uuid: UUID, page_no: int = 1, page_size: int = 50):
        statement = (
            select(DataChunkORM)
            .where(DataChunkORM.project_uuid == project_uuid)
            .offset((page_no - 1) * page_size)
            .limit(page_size)
        )
        records = (await self.session.scalars(statement)).all()
        return [self._to_schema(record) for record in records]
