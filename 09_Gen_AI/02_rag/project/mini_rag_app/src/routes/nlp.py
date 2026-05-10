from fastapi import FastAPI, APIRouter, status, Request
from fastapi.responses import JSONResponse
import logging

from routes.schemes.nlp import PushRequest, SearchRequest, RagAnswerRequest
from models.ProjectModel import ProjectModel
from models.ChunkModel import ChunkModel


from controllers import NLPController 
from models import ResponseSignal
from stores.llm.LlmEnums import DocumentTypeEnum

logger = logging.getLogger('uvicorn.error')

nlp_router = APIRouter(
    prefix="/api/v1/nlp",
    tags=["api_v1", "nlp"],
)

@nlp_router.post("/index/push/{project_id}")
async def index_project(request: Request, project_id: str, push_request: PushRequest):
    project_model = await ProjectModel.create_instance(
        db_client=request.app.db_client,
        )

    chunk_model = await ChunkModel.create_instance(
        db_client=request.app.db_client,
    )

    project = await project_model.get_project_or_create_one(project_id)

    if not project:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, 
            content={
                "signal": ResponseSignal.PROJECT_CREATION_FAILED.value,
                "message": f"Project with id {project_id} not found and failed to create one."
            }
        )

    nlp_controller = NLPController(
        vectordb_client=request.app.vectordb_client,
        generation_client=request.app.generation_client,
        embedding_client=request.app.embedding_client,
        template_parser=getattr(request.app, "template_parser", None),
    )

    has_records = True
    page_no = 1
    inserted_items_count=0

    while has_records:
        page_chunks = await chunk_model.get_project_chunks(
            project_id=project.id,
            page_no=page_no,
        )
        if len(page_chunks):
            page_no+=1
        
        if not page_chunks or len(page_chunks) == 0:
            has_records = False
            break


        is_inserted = nlp_controller.index_into_vector_db(
            project= project,
            chunks= page_chunks,
            do_reset= push_request.do_reset,
        )

        if not is_inserted:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST, 
                content={
                    "signal": ResponseSignal.INSERT_INTO_VECTORDB_ERROR.value,
                }
            )
        inserted_items_count += len(page_chunks)

    return JSONResponse(
        content={
            "signal" : ResponseSignal.INSERT_INTO_VECTORDB_SUCESS.value,
            "inserted_items_count" : inserted_items_count
        }
    )

@nlp_router.get("/index/info/{project_id}")
async def get_project_index_info(request: Request, project_id: str):
    project_model = await ProjectModel.create_instance(
        db_client=request.app.db_client,
    )
    project = await project_model.get_project_by_project_id(project_id)

    if not project:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "signal": ResponseSignal.PROJECT_NOT_FOUND.value,
                "project_id": project_id,
            }
        )

    nlp_controller = NLPController(
        vectordb_client=request.app.vectordb_client,
        generation_client=request.app.generation_client,
        embedding_client=request.app.embedding_client,
        template_parser=getattr(request.app, "template_parser", None),
    )

    collection_name = nlp_controller.create_collection_name(project.project_id)
    collection_info = nlp_controller.get_vector_db_collection_info(project)

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
async def search_index(request: Request, project_id: str, search_request: SearchRequest):
    project_model = await ProjectModel.create_instance(
        db_client=request.app.db_client,
    )
    project = await project_model.get_project_by_project_id(project_id)

    if not project:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "signal": ResponseSignal.PROJECT_NOT_FOUND.value,
                "project_id": project_id,
            }
        )

    nlp_controller = NLPController(
        vectordb_client=request.app.vectordb_client,
        generation_client=request.app.generation_client,
        embedding_client=request.app.embedding_client,
        template_parser=getattr(request.app, "template_parser", None),
    )

    search_result, collection_name = nlp_controller.search_vector_db_collection(
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
async def rag_answer(request: Request, project_id: str, rag_request: RagAnswerRequest):
    project_model = await ProjectModel.create_instance(
        db_client=request.app.db_client,
    )
    project = await project_model.get_project_by_project_id(project_id)

    if not project:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "signal": ResponseSignal.PROJECT_NOT_FOUND.value,
                "project_id": project_id,
            }
        )

    nlp_controller = NLPController(
        vectordb_client=request.app.vectordb_client,
        generation_client=request.app.generation_client,
        embedding_client=request.app.embedding_client,
        template_parser=getattr(request.app, "template_parser", None),
    )

    default_language = getattr(getattr(request.app, "settings", None), "DEFAULT_LANGUAGE", "en")

    answer, docs, collection_name = nlp_controller.answer_rag_question(
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
