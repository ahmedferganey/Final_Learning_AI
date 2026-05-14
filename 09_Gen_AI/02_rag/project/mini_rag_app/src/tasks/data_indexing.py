"""
Celery tasks for NLP routes under /api/v1/nlp: index push, index info, search, RAG.
"""

from __future__ import annotations

import asyncio
import logging
from typing import Any, Optional

from celery_app import celery_app
from controllers import NLPController
from models import ResponseSignal
from repositories.minirag import ChunkRepository, ProjectRepository
from services.index_push import run_index_push_job
from tasks.worker_context import worker_bundle

logger = logging.getLogger(__name__)


def _normalize_role(role: str | None) -> str:
    if not role:
        return "user"
    r = str(role).strip().lower()
    if r in ("system",):
        return "system"
    if r in ("user",):
        return "user"
    if r in ("assistant", "chatbot"):
        return "assistant"
    if r in ("system", "user", "assistant"):
        return r
    return r


@celery_app.task(name="tasks.data_indexing.push_project_index")
def push_project_index_task(project_id: str, do_reset: int = 0) -> dict[str, Any]:
    return asyncio.run(_push_project_index_async(project_id, do_reset))


async def _push_project_index_async(project_id: str, do_reset: int) -> dict[str, Any]:
    async with worker_bundle() as bundle:
        async with bundle.session_factory() as db_session:
            outcome = await run_index_push_job(
                db_session,
                project_id=project_id,
                do_reset=do_reset,
                vector_store=bundle.vector_store,
                generation_client=bundle.generation_client,
                embedding_client=bundle.embedding_client,
                template_parser=bundle.template_parser,
            )
            return outcome.body


@celery_app.task(name="tasks.data_indexing.get_project_index_info")
def get_project_index_info_task(project_id: str) -> dict[str, Any]:
    return asyncio.run(_get_project_index_info_async(project_id))


async def _get_project_index_info_async(project_id: str) -> dict[str, Any]:
    async with worker_bundle() as bundle:
        async with bundle.session_factory() as db_session:
            project_repository = ProjectRepository(db_session)
            project = await project_repository.get_project_by_project_id(project_id)

            if not project:
                return {
                    "signal": ResponseSignal.PROJECT_NOT_FOUND.value,
                    "project_id": project_id,
                }

            nlp_controller = NLPController(
                vector_store=bundle.vector_store,
                generation_client=bundle.generation_client,
                embedding_client=bundle.embedding_client,
                template_parser=bundle.template_parser,
            )

            collection_name = nlp_controller.create_collection_name(project.project_id)
            collection_info = await nlp_controller.get_vector_db_collection_info(project)

            if not collection_info:
                return {
                    "signal": ResponseSignal.VECTORDB_INDEX_NOT_FOUND.value,
                    "project_id": project.project_id,
                    "collection_name": collection_name,
                }

            return {
                "signal": ResponseSignal.VECTORDB_INDEX_INFO_SUCCESS.value,
                "project_id": project.project_id,
                "collection_name": collection_name,
                "index_info": collection_info,
            }


@celery_app.task(name="tasks.data_indexing.search_vector_index")
def search_vector_index_task(
    project_id: str,
    query_text: str,
    top_k: int = 5,
    limit: int = 5,
) -> dict[str, Any]:
    return asyncio.run(_search_vector_index_async(project_id, query_text, top_k, limit))


async def _search_vector_index_async(
    project_id: str,
    query_text: str,
    top_k: int,
    limit: int,
) -> dict[str, Any]:
    async with worker_bundle() as bundle:
        async with bundle.session_factory() as db_session:
            project_repository = ProjectRepository(db_session)
            project = await project_repository.get_project_by_project_id(project_id)

            if not project:
                return {
                    "signal": ResponseSignal.PROJECT_NOT_FOUND.value,
                    "project_id": project_id,
                }

            nlp_controller = NLPController(
                vector_store=bundle.vector_store,
                generation_client=bundle.generation_client,
                embedding_client=bundle.embedding_client,
                template_parser=bundle.template_parser,
            )

            search_result, collection_name = await nlp_controller.search_vector_db_collection(
                project=project,
                query_text=query_text,
                top_k=top_k,
                limit=limit,
            )

            if not search_result:
                return {
                    "signal": ResponseSignal.VECTORDB_SEARCH_FAILED.value,
                    "project_id": project.project_id,
                    "collection_name": collection_name,
                    "hits": 0,
                }

            hits = [
                item.model_dump() if hasattr(item, "model_dump") else item.dict()
                for item in search_result
            ]

            return {
                "signal": ResponseSignal.VECTORDB_SEARCH_SUCCESS.value,
                "project_id": project.project_id,
                "collection_name": collection_name,
                "hits": hits,
            }


@celery_app.task(name="tasks.data_indexing.rag_answer")
def rag_answer_task(
    project_id: str,
    question: str,
    language: Optional[str] = None,
    top_k: int = 5,
    limit: int = 5,
    temperature: Optional[float] = None,
    max_output_tokens: Optional[int] = None,
    system_message: Optional[str] = None,
    debug: bool = False,
    include_chat_history: bool = False,
) -> dict[str, Any]:
    return asyncio.run(
        _rag_answer_async(
            project_id=project_id,
            question=question,
            language=language,
            top_k=top_k,
            limit=limit,
            temperature=temperature,
            max_output_tokens=max_output_tokens,
            system_message=system_message,
            debug=debug,
            include_chat_history=include_chat_history,
        )
    )


async def _rag_answer_async(
    project_id: str,
    question: str,
    language: Optional[str],
    top_k: int,
    limit: int,
    temperature: Optional[float],
    max_output_tokens: Optional[int],
    system_message: Optional[str],
    debug: bool,
    include_chat_history: bool,
) -> dict[str, Any]:
    async with worker_bundle() as bundle:
        async with bundle.session_factory() as db_session:
            project_repository = ProjectRepository(db_session)
            project = await project_repository.get_project_by_project_id(project_id)

            if not project:
                return {
                    "signal": ResponseSignal.PROJECT_NOT_FOUND.value,
                    "project_id": project_id,
                }

            default_language = getattr(bundle.settings, "DEFAULT_LANGUAGE", "en")

            nlp_controller = NLPController(
                vector_store=bundle.vector_store,
                generation_client=bundle.generation_client,
                embedding_client=bundle.embedding_client,
                template_parser=bundle.template_parser,
            )

            answer, docs, collection_name = await nlp_controller.answer_rag_question(
                project=project,
                question=question,
                top_k=top_k or 5,
                limit=limit or 5,
                language=(language or default_language),
                system_message=system_message,
                max_output_tokens=max_output_tokens,
                temperature=temperature,
            )

            if not docs:
                return {
                    "signal": ResponseSignal.RAG_ANSWER_FAILED.value,
                    "project_id": project.project_id,
                    "collection_name": collection_name,
                    "answer": None,
                    "hits": [],
                }

            hits = [
                item.model_dump() if hasattr(item, "model_dump") else item.dict()
                for item in docs
            ]

            if not answer:
                return {
                    "signal": ResponseSignal.RAG_ANSWER_FAILED.value,
                    "project_id": project.project_id,
                    "collection_name": collection_name,
                    "answer": None,
                    "hits": hits,
                }

            payload: dict[str, Any] = {
                "signal": ResponseSignal.RAG_ANSWER_SUCCESS.value,
                "project_id": project.project_id,
                "collection_name": collection_name,
                "answer": answer,
                "hits": hits,
            }

            if include_chat_history:
                raw_messages = None
                if nlp_controller.last_llm_payload and isinstance(nlp_controller.last_llm_payload, dict):
                    raw_messages = nlp_controller.last_llm_payload.get("llm_messages")

                chat_history: list[dict[str, Any]] = []
                if isinstance(raw_messages, list):
                    for msg in raw_messages:
                        if not isinstance(msg, dict):
                            continue
                        role = _normalize_role(msg.get("role"))
                        content = msg.get("content")
                        if content is None:
                            content = msg.get("text")
                        chat_history.append({"role": role, "content": content or ""})
                chat_history.append({"role": "assistant", "content": answer})
                payload["chat_history"] = chat_history

            if debug:
                payload["debug"] = nlp_controller.last_llm_payload

            return {
                "signal": ResponseSignal.RAG_ANSWER_SUCCESS.value,
                "answer": payload["answer"],
                "fullpayload": {k: v for k, v in payload.items() if k not in ("answer", "signal")},
            }
