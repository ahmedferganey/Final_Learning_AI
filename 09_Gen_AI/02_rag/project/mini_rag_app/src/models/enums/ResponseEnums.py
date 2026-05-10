from enum import Enum

class ResponseSignal(Enum):

    FILE_VALIDATED_SUCCESS = "file_validate_successfully"
    FILE_TYPE_NOT_SUPPORTED = "file_type_not_supported"
    FILE_NOT_FOUND = "file_not_found"
    FILE_SIZE_EXCEEDED = "file_size_exceeded"
    FILE_UPLOAD_SUCCESS = "file_upload_success"
    FILE_UPLOAD_FAILED = "file_upload_failed"
    PROCESSING_SUCCESS = "processing_success"
    PROCESSING_FAILED = "processing_failed"
    FILE_ID_ERORR = "file_id_error"

    PROJECT_NOT_FOUND = "project_not_found"
    PROJECT_CREATED = "project_created"
    PROJECT_CREATION_FAILED = "project_creation_failed"

    INSERT_INTO_VECTORDB_ERROR= "insert_into_vectordb_error"
    INSERT_INTO_VECTORDB_SUCESS= "insert_into_vectordb_sucess"
    VECTORDB_INDEX_INFO_SUCCESS = "vectordb_index_info_success"
    VECTORDB_INDEX_NOT_FOUND = "vectordb_index_not_found"
    VECTORDB_SEARCH_SUCCESS = "vectordb_search_success"
    VECTORDB_SEARCH_FAILED = "vectordb_search_failed"

    RAG_ANSWER_SUCCESS = "rag_answer_success"
    RAG_ANSWER_FAILED = "rag_answer_failed"
