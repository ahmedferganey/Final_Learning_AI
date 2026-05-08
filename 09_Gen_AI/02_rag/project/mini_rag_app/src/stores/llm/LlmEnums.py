from enum import Enum

class LLMEnum(Enum):
    OPENAI = "OPENAI"
    COHERE = "COHERE"
    

class OpenAIEnums(Enum):
    SYSTEM = "system"
    User = "user"
    ASSISTANT = "assistant"