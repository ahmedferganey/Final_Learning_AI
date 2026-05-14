"""
Tasks for POST /api/v1/data/process/{project_id} — chunk files and persist DataChunk rows.
"""

from __future__ import annotations

import asyncio
import logging
from typing import Any, Optional

from celery_app import celery_app
from controllers import ProcessController
from models import ResponseSignal
from models.enums.AssetTypeEnum import AssetTypeEnum
from repositories.minirag import AssetRepository, ChunkRepository, ProjectRepository
from tasks.worker_context import worker_bundle

logger = logging.getLogger(__name__)


@celery_app.task(name="tasks.process_workflow.process_project")
def process_project_task(
    project_id: str,
    file_id: Optional[str] = None,
    chunk_size: int = 100,
    overlap_size: int = 20,
    do_reset: int = 0,
) -> dict[str, Any]:
    return asyncio.run(
        _process_project_async(
            project_id=project_id,
            file_id=file_id,
            chunk_size=chunk_size,
            overlap_size=overlap_size,
            do_reset=do_reset,
        )
    )


async def _process_project_async(
    project_id: str,
    file_id: Optional[str],
    chunk_size: int,
    overlap_size: int,
    do_reset: int,
) -> dict[str, Any]:
    async with worker_bundle() as bundle:
        async with bundle.session_factory() as db_session:
            try:
                return await _process_project_with_session(
                    db_session,
                    project_id,
                    file_id,
                    chunk_size,
                    overlap_size,
                    do_reset,
                )
            except Exception:
                await db_session.rollback()
                logger.exception("Unexpected database processing error for project_id=%s", project_id)
                return {
                    "signal": ResponseSignal.PROCESSING_FAILED.value,
                    "project_id": project_id,
                }


async def _process_project_with_session(
    db_session,
    project_id: str,
    file_id: Optional[str],
    chunk_size: int,
    overlap_size: int,
    do_reset: int,
) -> dict[str, Any]:
    project_repository = ProjectRepository(db_session)
    asset_repository = AssetRepository(db_session)
    chunk_repository = ChunkRepository(db_session)

    project = await project_repository.get_project_or_create(project_id=project_id)
    project_uuid = project.id or await project_repository.get_project_uuid(project_id=project_id)

    if project_uuid is None:
        await db_session.rollback()
        return {
            "signal": ResponseSignal.PROCESSING_FAILED.value,
            "project_id": project_id,
        }

    if file_id is not None:
        project_files_ids = await asset_repository.get_project_asset_by_name(
            project_uuid=project_uuid,
            asset_name=file_id,
            asset_type=AssetTypeEnum.File.value,
        )
        if len(project_files_ids) == 0:
            await db_session.rollback()
            return {
                "signal": ResponseSignal.FILE_ID_ERORR.value,
                "project_id": project_id,
                "file_id": file_id,
            }
    else:
        project_files_ids = await asset_repository.get_all_project_assets(
            project_uuid=project_uuid,
            asset_type=AssetTypeEnum.File.value,
        )

    if len(project_files_ids) == 0:
        await db_session.rollback()
        return {
            "signal": ResponseSignal.FILE_NOT_FOUND.value,
            "project_id": project_id,
        }

    process_controller = ProcessController(project_id=project_id)
    if do_reset == 1:
        await chunk_repository.delete_chunks_by_project_uuid(project_uuid=project_uuid)

    inserted_chunks = 0
    processed_files: list[str] = []
    failed_files: list[dict[str, str]] = []

    for asset_uuid, current_file_id in project_files_ids.items():
        try:
            file_content = process_controller.get_file_content(file_id=current_file_id)
            file_chunks = process_controller.process_file_content(
                file_content=file_content,
                file_id=current_file_id,
                chunk_size=chunk_size,
                overlap_size=overlap_size,
            )
        except FileNotFoundError as exc:
            logger.error("File not found while processing: %s", exc)
            failed_files.append(
                {"file_id": current_file_id, "signal": ResponseSignal.FILE_NOT_FOUND.value}
            )
            continue
        except ValueError as exc:
            logger.error("Invalid file while processing: %s", exc)
            failed_files.append(
                {
                    "file_id": current_file_id,
                    "signal": ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value,
                }
            )
            continue
        except Exception as exc:
            logger.exception("Unexpected processing error: %s", exc)
            failed_files.append(
                {"file_id": current_file_id, "signal": ResponseSignal.PROCESSING_FAILED.value}
            )
            continue

        if file_chunks is None or len(file_chunks) == 0:
            failed_files.append(
                {"file_id": current_file_id, "signal": ResponseSignal.PROCESSING_FAILED.value}
            )
            continue

        file_chunks_records = [
            {
                "chunk_text": chunk.page_content,
                "chunk_metadata": chunk.metadata,
                "chunk_order": i + 1,
                "project_uuid": project_uuid,
                "asset_uuid": asset_uuid,
            }
            for i, chunk in enumerate(file_chunks)
        ]

        inserted_chunks += await chunk_repository.insert_many_chunks(chunks=file_chunks_records)
        processed_files.append(current_file_id)

    if len(processed_files) == 0:
        await db_session.rollback()
        return {
            "signal": ResponseSignal.PROCESSING_FAILED.value,
            "project_id": project_id,
            "inserted_chunks": inserted_chunks,
            "processed_files": processed_files,
            "failed_files": failed_files,
            "no_files": len(processed_files),
        }

    await db_session.commit()
    return {
        "signal": ResponseSignal.PROCESSING_SUCCESS.value,
        "inserted_chunks": inserted_chunks,
        "processed_files": processed_files,
        "failed_files": failed_files,
        "no_files": len(processed_files),
    }
