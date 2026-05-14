"""
Tasks aligned with POST /api/v1/data/upload/{project_id} follow-up checks.

Upload itself stays in the FastAPI handler (streaming multipart). Workers can
verify the stored object on disk before downstream processing.
"""

from __future__ import annotations

import asyncio
import logging
import os

from celery_app import celery_app
from controllers import ProcessController
from models import ResponseSignal

logger = logging.getLogger(__name__)


@celery_app.task(name="tasks.file_processing.verify_uploaded_file")
def verify_uploaded_file_task(project_id: str, file_id: str) -> dict:
    return asyncio.run(_verify_uploaded_file_async(project_id, file_id))


async def _verify_uploaded_file_async(project_id: str, file_id: str) -> dict:
    try:
        pc = ProcessController(project_id=project_id)
        path = pc.get_file_path(file_id=file_id)
    except Exception as exc:
        logger.exception("verify_uploaded_file: invalid project or file_id: %s", exc)
        return {
            "signal": ResponseSignal.FILE_UPLOAD_FAILED.value,
            "project_id": project_id,
            "file_id": file_id,
            "detail": str(exc),
        }

    if not os.path.isfile(path):
        return {
            "signal": ResponseSignal.FILE_NOT_FOUND.value,
            "project_id": project_id,
            "file_id": file_id,
            "path": path,
        }

    try:
        _ = pc.get_file_loader(file_id=file_id)
    except ValueError:
        return {
            "signal": ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value,
            "project_id": project_id,
            "file_id": file_id,
        }

    return {
        "signal": ResponseSignal.FILE_VALIDATED_SUCCESS.value,
        "project_id": project_id,
        "file_id": file_id,
        "size_bytes": os.path.getsize(path),
    }
