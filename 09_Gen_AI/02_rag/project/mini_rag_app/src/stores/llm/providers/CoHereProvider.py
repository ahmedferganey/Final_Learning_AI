from ..LlmInterface import LlmInterface
import logging
from ..LlmEnums import CoHereEnums, DocumentTypeEnum
import cohere

class CoHereProvider(LlmInterface):
    def __init__(self, api_key: str,
                default_input_max_characters: int = 1000, 
                default_generation_max_output_tokens: int = 1000, 
                default_temperature: float = 0.1):
        
        self.api_key = api_key

        self.default_input_max_characters = default_input_max_characters
        self.default_generation_max_output_tokens = default_generation_max_output_tokens
        self.default_temperature = default_temperature

        self.generation_model_id = None

        self.embedding_model_id = None
        self.embedding_size = None

        self.client = cohere.Client(api_key=self.api_key)

        self.logger = logging.getLogger(__name__)



    def set_generation_model(self, model_id: str):
        self.generation_model_id = model_id

    def set_embedding_model(self, model_id: str, embeddding_size: int):
        self.embedding_model_id = model_id
        self.embedding_size = embeddding_size

    def process_text_input(self, text: str):
        if len(text) > self.default_input_max_characters:
            self.logger.warning(f"Input text exceeds the maximum character limit of {self.default_input_max_characters}. Truncating input.")
            return text[:self.default_input_max_characters]
        return text[:self.default_input_max_characters].strip()

    def generate_text(self, prompt: str, chat_history: list=[], max_output_tokens: int=None, temperature: float= None):
        if not self.client:
            self.logger.error("Cohere client was not set")
            return None

        if not self.generation_model_id:
            self.logger.error("Generation model for cohere was not set")
            return None
        
        max_output_tokens = max_output_tokens if max_output_tokens is not None else self.default_generation_max_output_tokens
        temperature = temperature if temperature is not None else self.default_temperature

        response = self.client.chat(
            model=self.generation_model_id,
            chat_history=chat_history,
            message=self.process_text_input(prompt),
            temperature=temperature,
            max_tokens=max_output_tokens
            )
        if not response or not response.text or len(response.text) == 0:
            self.logger.error("No response or generations received from cohere")
            return None

        return response.text

    def embed_text(self, text: str, document_type: str = None):
        if not self.client:
            self.logger.error("OpenAi client was not set")
            return None

        if not self.embedding_model_id:
            self.logger.error("Emedding model for openai was not set")
            return None

        if not self.embedding_size:
            self.logger.warning("Embedding size for openai was not set")
            return None

        input_type = CoHereEnums.DOCUMENT.value if document_type == CoHereEnums.DOCUMENT.value else CoHereEnums.QUERY.value
        response = self.client.embed(
            model=self.embedding_model_id,
            input=[self.process_text_input(text)],
            truncate="END",
            embedding_types=['float'],
            input_type=input_type,
        )

        if not response or not response.embeddings or not response.embedding.float  or len(response.embeddings) == 0:
            self.logger.error("No response or embeddings received from cohere")
            return None

        return response.embeddings.float[0]

    def construct_prompt(self, prompt: str, role: str):
        return {
            "role" : role,
            "text" : self.process_text_input(prompt)
        }