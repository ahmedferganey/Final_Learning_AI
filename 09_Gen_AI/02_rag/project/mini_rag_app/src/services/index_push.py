"""
Vector index push from persisted chunks — shared by sync route and Celery worker.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from controllers import NLPController
from models import ResponseSignal
from repositories.minirag import ChunkRepository, ProjectRepository
from sqlalchemy.ext.asyncio import AsyncSession
from stores.llm.templates import TemplateParser
from stores.vectordb.VectorStoreInterface import VectorStoreInterface


@dataclass(frozen=True)
class IndexPushJobResult:
    """HTTP mapping for the API route; Celery uses ``body`` as the task return value."""

    status_code: int
    body: dict[str, Any]


async def run_index_push_job(
    db_session: AsyncSession,
    *,
    project_id: str,
    do_reset: int,
    vector_store: VectorStoreInterface,
    generation_client: object,
    embedding_client: object,
    template_parser: TemplateParser | None,
) -> IndexPushJobResult:
    project_repository = ProjectRepository(db_session)
    chunk_repository = ChunkRepository(db_session)

    project = await project_repository.get_project_or_create(project_id=project_id)

    if not project:
        await db_session.rollback()
        return IndexPushJobResult(
            status_code=404,
            body={
                "signal": ResponseSignal.PROJECT_CREATION_FAILED.value,
                "message": f"Project with id {project_id} not found and failed to create one.",
            },
        )

    nlp_controller = NLPController(
        vector_store=vector_store,
        generation_client=generation_client,
        embedding_client=embedding_client,
        template_parser=template_parser,
    )

    has_records = True
    page_no = 1
    inserted_items_count = 0
    reset_flag = do_reset

    while has_records:
        page_chunks = await chunk_repository.get_project_chunks(
            project_uuid=project.id,
            page_no=page_no,
        )
        if len(page_chunks):
            page_no += 1

        if not page_chunks or len(page_chunks) == 0:
            has_records = False
            break

        is_inserted = await nlp_controller.index_into_vector_db(
            project=project,
            chunks=page_chunks,
            do_reset=reset_flag,
        )
        reset_flag = 0

        if not is_inserted:
            await db_session.rollback()
            return IndexPushJobResult(
                status_code=400,
                body={"signal": ResponseSignal.INSERT_INTO_VECTORDB_ERROR.value},
            )

        inserted_items_count += len(page_chunks)

    await db_session.commit()
    return IndexPushJobResult(
        status_code=200,
        body={
            "signal": ResponseSignal.INSERT_INTO_VECTORDB_SUCESS.value,
            "inserted_items_count": inserted_items_count,
        },
    )
