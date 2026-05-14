from fastapi import APIRouter, status, Request, Depends
from fastapi.responses import JSONResponse
import logging

from routes.schemes.nlp import PushRequest, SearchRequest, RagAnswerRequest
from controllers import NLPController
from models import ResponseSignal
from repositories.minirag import ProjectRepository
from database.dependencies import get_db_session
from services.index_push import run_index_push_job
from stores.vectordb.VectorStoreInterface import VectorStoreInterface
from stores.vectordb.dependencies import get_vector_store
from sqlalchemy.ext.asyncio import AsyncSession
from tasks.data_indexing import push_project_index_task

logger = logging.getLogger('uvicorn.error')

nlp_router = APIRouter(
    prefix="/api/v1/nlp",
    tags=["api_v1", "nlp"],
)

@nlp_router.post("/index/push/{project_id}")
async def index_project(
    request: Request,
    project_id: str,
    push_request: PushRequest,
    db_session: AsyncSession = Depends(get_db_session),
    vector_store: VectorStoreInterface = Depends(get_vector_store),
):
    outcome = await run_index_push_job(
        db_session,
        project_id=project_id,
        do_reset=push_request.do_reset or 0,
        vector_store=vector_store,
        generation_client=request.app.generation_client,
        embedding_client=request.app.embedding_client,
        template_parser=getattr(request.app, "template_parser", None),
    )
    return JSONResponse(status_code=outcome.status_code, content=outcome.body)


@nlp_router.post("/index/push/{project_id}/async", status_code=status.HTTP_202_ACCEPTED)
async def index_project_async(
    project_id: str,
    push_request: PushRequest,
):
    async_result = push_project_index_task.delay(project_id, push_request.do_reset or 0)
    return JSONResponse(
        status_code=status.HTTP_202_ACCEPTED,
        content={
            "task_id": async_result.id,
            "status_path": f"/api/v1/jobs/{async_result.id}",
            "signal": "async_task_accepted",
            "project_id": project_id,
        },
    )

@nlp_router.get("/index/info/{project_id}")
async def get_project_index_info(
    request: Request,
    project_id: str,
    db_session: AsyncSession = Depends(get_db_session),
    vector_store: VectorStoreInterface = Depends(get_vector_store),
):
    project_repository = ProjectRepository(db_session)
    project = await project_repository.get_project_by_project_id(project_id)

    if not project:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "signal": ResponseSignal.PROJECT_NOT_FOUND.value,
                "project_id": project_id,
            }
        )

    nlp_controller = NLPController(
        vector_store=vector_store,
        generation_client=request.app.generation_client,
        embedding_client=request.app.embedding_client,
        template_parser=getattr(request.app, "template_parser", None),
    )

    collection_name = nlp_controller.create_collection_name(project.project_id)
    collection_info = await nlp_controller.get_vector_db_collection_info(project)

    if not collection_info:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "signal": ResponseSignal.VECTORDB_INDEX_NOT_FOUND.value,
                "project_id": project.project_id,
                "collection_name": collection_name,
            }
        )

    return JSONResponse(
        content={
            "signal": ResponseSignal.VECTORDB_INDEX_INFO_SUCCESS.value,
            "project_id": project.project_id,
            "collection_name": collection_name,
            "index_info": collection_info,
        }
    )


@nlp_router.post("/index/search/{project_id}")
async def search_index(
    request: Request,
    project_id: str,
    search_request: SearchRequest,
    db_session: AsyncSession = Depends(get_db_session),
    vector_store: VectorStoreInterface = Depends(get_vector_store),
):
    project_repository = ProjectRepository(db_session)
    project = await project_repository.get_project_by_project_id(project_id)

    if not project:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "signal": ResponseSignal.PROJECT_NOT_FOUND.value,
                "project_id": project_id,
            }
        )

    nlp_controller = NLPController(
        vector_store=vector_store,
        generation_client=request.app.generation_client,
        embedding_client=request.app.embedding_client,
        template_parser=getattr(request.app, "template_parser", None),
    )

    search_result, collection_name = await nlp_controller.search_vector_db_collection(
        project=project,
        query_text=search_request.query_text,
        top_k=search_request.top_k,
        limit=search_request.limit,
    )

    if not search_result:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "signal": ResponseSignal.VECTORDB_SEARCH_FAILED.value,
                "project_id": project.project_id,
                "collection_name": collection_name,
                "hits": 0,
            }
        )

    # Qdrant provider returns app-level schemas (RetrievedDocument); dump them directly.
    hits = [
        item.model_dump()
        if hasattr(item, "model_dump")
        else item.dict()  # Fallback for Pydantic v1
        for item in search_result
    ]

    return JSONResponse(
        content={
            "signal": ResponseSignal.VECTORDB_SEARCH_SUCCESS.value,
            "project_id": project.project_id,
            "collection_name": collection_name,
            "hits": hits,
        }
    )


@nlp_router.post("/rag/answer/{project_id}")
async def rag_answer(
    request: Request,
    project_id: str,
    rag_request: RagAnswerRequest,
    db_session: AsyncSession = Depends(get_db_session),
    vector_store: VectorStoreInterface = Depends(get_vector_store),
):
    project_repository = ProjectRepository(db_session)
    project = await project_repository.get_project_by_project_id(project_id)

    if not project:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "signal": ResponseSignal.PROJECT_NOT_FOUND.value,
                "project_id": project_id,
            }
        )

    nlp_controller = NLPController(
        vector_store=vector_store,
        generation_client=request.app.generation_client,
        embedding_client=request.app.embedding_client,
        template_parser=getattr(request.app, "template_parser", None),
    )

    default_language = getattr(getattr(request.app, "settings", None), "DEFAULT_LANGUAGE", "en")

    answer, docs, collection_name = await nlp_controller.answer_rag_question(
        project=project,
        question=rag_request.question,
        top_k=rag_request.top_k or 5,
        limit=rag_request.limit or 5,
        language=(rag_request.language or default_language),
        system_message=rag_request.system_message,
        max_output_tokens=rag_request.max_output_tokens,
        temperature=rag_request.temperature,
    )

    if not docs:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "signal": ResponseSignal.RAG_ANSWER_FAILED.value,
                "project_id": project.project_id,
                "collection_name": collection_name,
                "answer": None,
                "hits": [],
            }
        )

    hits = [
        item.model_dump()
        if hasattr(item, "model_dump")
        else item.dict()  # Fallback for Pydantic v1
        for item in docs
    ]

    if not answer:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": ResponseSignal.RAG_ANSWER_FAILED.value,
                "project_id": project.project_id,
                "collection_name": collection_name,
                "answer": None,
                "hits": hits,
            }
        )

    payload = {
        "signal": ResponseSignal.RAG_ANSWER_SUCCESS.value,
        "project_id": project.project_id,
        "collection_name": collection_name,
        "answer": answer,
        "hits": hits,
    }

    if rag_request.include_chat_history:
        raw_messages = None
        if nlp_controller.last_llm_payload and isinstance(nlp_controller.last_llm_payload, dict):
            raw_messages = nlp_controller.last_llm_payload.get("llm_messages")

        def normalize_role(role: str | None) -> str:
            if not role:
                return "user"
            r = str(role).strip().lower()
            if r in ("system",):
                return "system"
            if r in ("user",):
                return "user"
            if r in ("assistant", "chatbot"):
                return "assistant"
            # Cohere may send uppercase roles; keep normalized lowercase.
            if r in ("system", "user", "assistant"):
                return r
            return r

        chat_history = []
        if isinstance(raw_messages, list):
            for msg in raw_messages:
                if not isinstance(msg, dict):
                    continue
                role = normalize_role(msg.get("role"))
                content = msg.get("content")
                if content is None:
                    content = msg.get("text")
                chat_history.append({"role": role, "content": content or ""})

        # Append the generated assistant response for downstream reuse.
        chat_history.append({"role": "assistant", "content": answer})
        payload["chat_history"] = chat_history

    if rag_request.debug:
        payload["debug"] = nlp_controller.last_llm_payload

    return JSONResponse(
        content={
            "signal": ResponseSignal.RAG_ANSWER_SUCCESS.value,
            "answer": payload["answer"],
            "fullpayload": {k: v for k, v in payload.items() if k not in ("answer", "signal")},
        }
    )
