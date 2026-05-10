from ..LlmInterface import LlmInterface
from openai import OpenAI
import logging
from ..LlmEnums import OpenAIEnums

class OpenAIProvider(LlmInterface):
    def __init__(self, api_key: str, api_url: str = None,
                default_input_max_characters: int = 1000, default_generation_max_output_tokens: int = 1000, default_temperature: float = 0.1):
        self.api_key = api_key
        self.api_url = api_url
        self.default_input_max_characters = default_input_max_characters
        self.default_generation_max_output_tokens = default_generation_max_output_tokens
        self.default_temperature = default_temperature

        self.generation_model_id = None
        self.embedding_model_id = None
        
        self.embedding_size = None

        self.client = OpenAI(api_key=self.api_key, base_url=self.api_url)

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
            self.logger.error("OpenAi client was not set")
            return None

        if not self.generation_model_id:
            self.logger.error("Generation model for openai was not set")
            return None
        
        max_output_tokens = max_output_tokens if max_output_tokens is not None else self.default_generation_max_output_tokens
        temperature = temperature if temperature is not None else self.default_temperature

        chat_history_messages = [{"role": message.get("role", OpenAIEnums.User.value), "content": message.get("content", "")} for message in chat_history]
        chat_history_messages.append(
            self.construct_prompt(prompt, OpenAIEnums.User.value)
        )

        response = self.client.chat.completions.create(
            model=self.generation_model_id,
            messages=chat_history_messages,
            max_tokens=max_output_tokens,
            temperature=temperature
        )

        if not response or not response.choices or len(response.choices) == 0 or not response.choices[0].message or not response.choices[0].message.content:
            self.logger.error("No valid response returned from OpenAI")
            return None

        return response.choices[0].message.content.strip()

    def embed_text(self, text: str, document_type: str = None):
        embeddings = self.embed_texts([text], document_type=document_type)
        if not embeddings:
            return None

        return embeddings[0]

    def embed_texts(self, texts: list[str], document_type: str = None):
        if not self.client:
            self.logger.error("OpenAi client was not set")
            return None

        if not self.embedding_model_id:
            self.logger.error("Emedding model for openai was not set")
            return None

        if not self.embedding_size:
            self.logger.warning("Embedding size for openai was not set")
            return None

        processed_texts = [
            self.process_text_input(text)
            for text in texts
            if text is not None and len(text.strip()) > 0
        ]
        if len(processed_texts) == 0:
            self.logger.error("No valid texts received for openai embeddings")
            return None

        try:
            response = self.client.embeddings.create(
                input=processed_texts,
                model=self.embedding_model_id
            )
        except Exception as exc:
            self.logger.error("OpenAI embedding request failed: %s", exc)
            return None

        if not response or not response.data or len(response.data) == 0 or not response.data[0].embedding:
            self.logger.error("No embedding data returned from OpenAI")
            return None 
        return [item.embedding for item in response.data]

    def construct_prompt(self, prompt: str, role: str):
        return {
            "role" : role,
            "content" : self.process_text_input(prompt)
        }
