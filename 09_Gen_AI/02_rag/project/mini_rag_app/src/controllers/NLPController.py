from .BaseController import BaseController
from models.db_schemes import Project, DataChunk, RetrievedDocument
from typing import Any, Dict, List, Optional, Tuple
from stores.llm.LlmEnums import DocumentTypeEnum
from stores.llm.templates import TemplateParser
from stores.vectordb.VectorStoreInterface import VectorStoreInterface
from string import Template
import logging
import uuid

logger = logging.getLogger(__name__)

class NLPController(BaseController):
    def __init__(
        self,
        vector_store: VectorStoreInterface,
        generation_client,
        embedding_client,
        template_parser: Optional[TemplateParser] = None,
    ):
        super().__init__()
        self.vector_store = vector_store
        self.generation_client = generation_client
        self.embedding_client = embedding_client
        self.template_parser = template_parser
        # Debug/audit: last messages/prompts we sent to the LLM.
        self.last_llm_payload: Optional[Dict[str, Any]] = None

    def create_collection_name(self, project_id: str):
        return f"project_{project_id}_collection".strip()
    
    def reset_vector_db_collection(self, project: Project):
        collection_name = self.create_collection_name(project.project_id)
        if self.vector_store.index_exists(collection_name):
            return self.vector_store.delete(collection_name)
    
    def get_vector_db_collection_info(self, project: Project):
        collection_name = self.create_collection_name(project.project_id)
        if self.vector_store.index_exists(collection_name):
            return self.vector_store.get_index_info(collection_name)
        return None

    def search_vector_db_collection(self, project: Project, query_text: str, top_k: int = 5, limit: int = 5):
        collection_name = self.create_collection_name(project.project_id)

        if not self.vector_store.index_exists(collection_name):
            return None, collection_name

        query_vector = self.embedding_client.embed_text(
            query_text,
            document_type=DocumentTypeEnum.QUERY.value,
        )

        if query_vector is None:
            return None, collection_name

        hits = self.vector_store.similarity_search(
            index_name=collection_name,
            query_vector=query_vector,
            top_k=top_k,
            limit=limit,
        )

        return hits, collection_name

    def answer_rag_question(
        self,
        project: Project,
        question: str,
        top_k: int = 5,
        limit: int = 5,
        language: Optional[str] = None,
        system_message: Optional[str] = None,
        max_output_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
    ) -> Tuple[Optional[str], Optional[List[RetrievedDocument]], str]:
        """
        Retrieve relevant documents from the vector DB, build a RAG prompt, store the exact
        messages we send to the LLM, then generate the answer.
        Returns: (answer_text, retrieved_docs, collection_name)
        """
        docs, collection_name = self.search_vector_db_collection(
            project=project,
            query_text=question,
            top_k=top_k,
            limit=limit,
        )

        default_language = getattr(self.app_settings, "DEFAULT_LANGUAGE", "en")
        language = (language or default_language).strip().lower()

        template_parser = self.template_parser or TemplateParser(default_language=default_language)
        tpl = template_parser.load(name="rag", language=language)

        # Allow caller to override the localized system prompt if needed.
        system_message = system_message if system_message is not None else tpl.prompts.get("system", "")

        if not docs:
            self.last_llm_payload = {
                "language": tpl.language,
                "system_message": system_message,
                "question": question,
                "collection_name": collection_name,
                "retrieved_docs": [],
                "llm_messages": [],
                "last_two_lines": None,
            }
            return None, None, collection_name

        doc_tpl = tpl.prompts.get("document")
        user_tpl = tpl.prompts.get("user")
        footer_tpl = tpl.prompts.get("footer")

        if not isinstance(doc_tpl, Template):
            raise ValueError("RAG template must provide PROMPTS['document'] as string.Template")
        if user_tpl is not None and not isinstance(user_tpl, Template):
            raise ValueError("RAG template must provide PROMPTS['user'] as string.Template (or omit it)")
        if footer_tpl is not None and not isinstance(footer_tpl, Template):
            raise ValueError("RAG template must provide PROMPTS['footer'] as string.Template (or omit it)")

        context_blocks: List[str] = []
        for i, doc in enumerate(docs, start=1):
            meta = doc.metadata or {}
            meta_str = ", ".join(f"{k}={v}" for k, v in meta.items()) if len(meta) else ""
            context_blocks.append(
                doc_tpl.safe_substitute(
                    index=i,
                    score=doc.score,
                    metadata=meta_str,
                    text=doc.text or "",
                )
            )

        context_text = "\n---\n".join(context_blocks).strip()

        # Keep the last two lines stable and easy to inspect/debug.
        if user_tpl is not None:
            user_prompt = user_tpl.safe_substitute(context=context_text, question=question)
        else:
            footer = footer_tpl.safe_substitute(question=question) if footer_tpl is not None else ""
            user_prompt = "\n".join(["Context:", context_text, footer]).strip()

        prompt_lines = user_prompt.splitlines()
        last_two_lines = "\n".join(prompt_lines[-2:]) if len(prompt_lines) >= 2 else user_prompt

        # Construct the exact message dicts the provider will send (after its own input processing).
        system_msg = (
            self.generation_client.construct_prompt(system_message, "system")
            if hasattr(self.generation_client, "construct_prompt")
            else {"role": "system", "content": system_message}
        )
        user_msg = (
            self.generation_client.construct_prompt(user_prompt, "user")
            if hasattr(self.generation_client, "construct_prompt")
            else {"role": "user", "content": user_prompt}
        )

        self.last_llm_payload = {
            "language": tpl.language,
            "system_message": system_message,
            "question": question,
            "collection_name": collection_name,
            "retrieved_docs": [
                d.model_dump() if hasattr(d, "model_dump") else d.dict()
                for d in docs
            ],
            "llm_messages": [system_msg, user_msg],
            "last_two_lines": last_two_lines,
        }

        answer = self.generation_client.generate_text(
            prompt=user_prompt,
            chat_history=[system_msg],
            max_output_tokens=max_output_tokens,
            temperature=temperature,
        )

        return answer, docs, collection_name

    def create_record_id(self, project: Project, chunk: DataChunk) -> str:
        seed = f"{project.project_id}:{chunk.id}:{chunk.asset_uuid}:{chunk.chunk_order}"
        return str(uuid.uuid5(uuid.NAMESPACE_URL, seed))
    
    def index_into_vector_db(self, project: Project, chunks: List[DataChunk], do_reset: Optional[int] = 0):
        try:
            collection_name = self.create_collection_name(project.project_id)
            if do_reset:
                self.reset_vector_db_collection(project)

            texts = [chunk.chunk_text for chunk in chunks]
            metadata = [chunk.chunk_metadata for chunk in chunks]
            record_ids = [self.create_record_id(project, chunk) for chunk in chunks]

            if hasattr(self.embedding_client, "embed_texts"):
                vectors = self.embedding_client.embed_texts(
                    texts,
                    document_type=DocumentTypeEnum.DOCUMENT.value,
                )
            else:
                vectors = [
                    self.embedding_client.embed_text(
                        text,
                        document_type=DocumentTypeEnum.DOCUMENT.value,
                    )
                    for text in texts
                ]

            if not vectors or len(vectors) != len(texts) or any(vector is None for vector in vectors):
                logger.error("Embedding generation failed for project '%s'", project.project_id)
                return False

            if not self.vector_store.index_exists(collection_name):
                self.vector_store.ensure_index(
                    index_name=collection_name,
                    do_reset=do_reset,
                    embedding_size=self.embedding_client.embedding_size,
                )

            return self.vector_store.add_documents(
                index_name=collection_name,
                texts=texts,
                vectors=vectors,
                metadata=metadata,
                record_ids=record_ids,
            )
        except Exception as exc:
            logger.exception("Failed to index project '%s': %s", project.project_id, exc)
            return False
