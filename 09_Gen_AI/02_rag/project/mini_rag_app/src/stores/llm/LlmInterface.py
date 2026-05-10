from abc import ABC, abstractmethod


#Factory pattern for LLMs, allowing us to easily switch between different LLM providers (e.g., OpenAI, Hugging Face, etc.) without changing the rest of the codebase.
class LlmInterface(ABC):
    
    @abstractmethod
    def set_generation_model(self, model_id: str):
        pass

    @abstractmethod
    def set_embedding_model(self, model_id: str, embeddding_size: int):
        pass

    @abstractmethod
    def generate_text(self, prompt: str, chat_history: list=[], max_output_tokens: int=None, temperature: float= None):
        pass
    
    @abstractmethod
    def embed_text(self, text: str, document_type: str = None):
        pass

    @abstractmethod
    def construct_prompt(self, prompt: str, role: str):
        pass
