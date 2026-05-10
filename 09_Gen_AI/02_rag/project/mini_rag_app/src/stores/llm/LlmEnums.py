from enum import Enum

class LLMEnum(Enum):
    OPENAI = "OPENAI"
    COHERE = "COHERE"
    

class OpenAIEnums(Enum):
    SYSTEM = "system"
    User = "user"
    ASSISTANT = "assistant"

class CoHereEnums(Enum):
    SYSTEM = "SYSTEM"
    User = "USER"
    ASSISTANT = "CHATBOT"

    DOCUMENT="search_document"
    QUERY="search_query"

class DocumentTypeEnum(Enum):
    DOCUMENT="document"
    QUERY="query"