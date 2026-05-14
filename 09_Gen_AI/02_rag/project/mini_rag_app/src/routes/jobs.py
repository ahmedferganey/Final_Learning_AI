"""
Celery job status for async task IDs (result backend).
"""

from __future__ import annotations

from typing import Any

from celery.result import AsyncResult
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from celery_app import celery_app

jobs_router = APIRouter(
    prefix="/api/v1/jobs",
    tags=["api_v1", "jobs"],
)


def _serialize_result(raw: Any) -> Any:
    if raw is None:
        return None
    if isinstance(raw, (str, int, float, bool)):
        return raw
    if isinstance(raw, dict):
        return raw
    if isinstance(raw, (list, tuple)):
        return [_serialize_result(x) for x in raw]
    if hasattr(raw, "model_dump"):
        return raw.model_dump()
    if hasattr(raw, "dict"):
        return raw.dict()
    return str(raw)


@jobs_router.get("/{task_id}")
async def get_job_status(task_id: str):
    result = AsyncResult(task_id, app=celery_app)
    state = result.state
    payload: dict[str, Any] = {
        "task_id": task_id,
        "state": state,
        "ready": result.ready(),
    }

    if state == "SUCCESS":
        payload["result"] = _serialize_result(result.result)
        return JSONResponse(content=payload)

    if state == "FAILURE":
        try:
            err = result.result
        except Exception as exc:
            err = exc
        payload["error"] = repr(err) if err is not None else "task_failed"
        tb = getattr(result, "traceback", None)
        if tb:
            payload["traceback"] = tb
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=payload)

    if state in ("PENDING", "STARTED", "RETRY"):
        return JSONResponse(status_code=status.HTTP_200_OK, content=payload)

    if result.ready():
        try:
            payload["result"] = _serialize_result(result.result)
        except Exception as exc:
            payload["result"] = None
            payload["error"] = repr(exc)
    return JSONResponse(content=payload)
