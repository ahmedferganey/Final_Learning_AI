from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.db_schemes import Asset
from models.db_schemes.minirag.schemes import AssetORM


class AssetRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    def _to_schema(self, record: AssetORM) -> Asset:
        return Asset.model_construct(
            id=record.id,
            project_uuid=record.project_uuid,
            asset_name=record.asset_name,
            asset_type=record.asset_type,
            asset_size=record.asset_size,
            asset_pushed_at=record.asset_pushed_at,
            asset_config=record.asset_config or {},
        )

    async def create_asset(
        self,
        project_uuid: UUID,
        asset_name: str,
        asset_type: str,
        asset_size: Optional[int] = None,
        asset_config: Optional[dict] = None,
        asset_pushed_at: Optional[datetime] = None,
    ) -> Asset:
        record = AssetORM(
            project_uuid=project_uuid,
            asset_name=asset_name,
            asset_type=asset_type,
            asset_size=asset_size,
            asset_config=asset_config or {},
            asset_pushed_at=asset_pushed_at or datetime.utcnow(),
        )
        self.session.add(record)
        await self.session.flush()
        await self.session.refresh(record)
        return self._to_schema(record)

    async def get_all_project_assets(self, project_uuid: UUID, asset_type: str = None):
        statement = select(AssetORM.id, AssetORM.asset_name).where(AssetORM.project_uuid == project_uuid)
        if asset_type is not None:
            statement = statement.where(AssetORM.asset_type == asset_type)

        rows = (await self.session.execute(statement)).all()
        return {row.id: row.asset_name for row in rows}

    async def get_project_asset_by_name(
        self,
        project_uuid: UUID,
        asset_name: str,
        asset_type: str = None,
    ):
        statement = (
            select(AssetORM.id, AssetORM.asset_name)
            .where(
                AssetORM.project_uuid == project_uuid,
                AssetORM.asset_name == asset_name,
            )
            .limit(1)
        )
        if asset_type is not None:
            statement = statement.where(AssetORM.asset_type == asset_type)

        row = (await self.session.execute(statement)).first()
        if row is None:
            return {}
        return {row.id: row.asset_name}
