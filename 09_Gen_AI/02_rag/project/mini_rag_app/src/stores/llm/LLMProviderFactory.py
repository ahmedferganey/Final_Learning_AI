from .LlmEnums import LLMEnum
from .providers import OpenAIProvider, CoHereProvider



class LLMProviderFactory:
    def __init__(self, config: dict):
        self.config = config

    def create(self, provider: str):
        if provider == LLMEnum.OPENAI.value:
            return OpenAIProvider(
                api_key=self.config.get("OPENAI_API_KEY"),
                api_url=self.config.get("OPENAI_API_URL"),
                default_input_max_characters=self.config.get("INPUT_DAFAULT_MAX_CHARACTERS"),
                default_generation_max_output_tokens=self.config.get("GENERATION_DAFAULT_MAX_TOKENS"),
                default_temperature=self.config.get("GENERATION_DAFAULT_TEMPERATURE"),
            )
        elif provider == LLMEnum.COHERE.value:
            return CoHereProvider(
                api_key=self.config.get("COHERE_API_KEY"),
                default_input_max_characters=self.config.get("INPUT_DAFAULT_MAX_CHARACTERS"),
                default_generation_max_output_tokens=self.config.get("GENERATION_DAFAULT_MAX_TOKENS"),
                default_temperature=self.config.get("GENERATION_DAFAULT_TEMPERATURE"),
            )
        else:
            raise ValueError(f"Unsupported provider: {provider}")
