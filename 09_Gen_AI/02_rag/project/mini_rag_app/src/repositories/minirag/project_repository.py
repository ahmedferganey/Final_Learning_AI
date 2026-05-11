from __future__ import annotations

from math import ceil
from typing import Optional
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from models.db_schemes import Project
from models.db_schemes.minirag.schemes import ProjectORM


class ProjectRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    def _to_schema(self, record: ProjectORM) -> Project:
        return Project.model_construct(
            id=record.id,
            project_id=record.project_id,
        )

    async def create_project(self, project_id: str) -> Project:
        if not project_id.isalnum():
            raise ValueError("project_id must be alphanumeric")

        record = ProjectORM(project_id=project_id)
        self.session.add(record)
        await self.session.flush()
        await self.session.refresh(record)
        return self._to_schema(record)

    async def get_project_or_create(self, project_id: str) -> Project:
        existing = await self.get_project_by_project_id(project_id)
        if existing is not None:
            return existing
        return await self.create_project(project_id=project_id)

    async def get_project_by_project_id(self, project_id: str) -> Optional[Project]:
        statement = select(ProjectORM).where(ProjectORM.project_id == project_id)
        record = await self.session.scalar(statement)
        if record is None:
            return None
        return self._to_schema(record)

    async def get_all_projects(self, page: int = 1, page_size: int = 10):
        total_documents = await self.session.scalar(select(func.count()).select_from(ProjectORM))
        total_documents = int(total_documents or 0)
        total_pages = ceil(total_documents / page_size) if page_size else 0

        statement = (
            select(ProjectORM)
            .offset((page - 1) * page_size)
            .limit(page_size)
        )
        records = (await self.session.scalars(statement)).all()
        projects = [self._to_schema(record) for record in records]
        return projects, total_pages

    async def get_project_uuid(self, project_id: str) -> Optional[UUID]:
        statement = (
            select(ProjectORM.id)
            .where(ProjectORM.project_id == project_id)
            .limit(1)
        )
        return await self.session.scalar(statement)
