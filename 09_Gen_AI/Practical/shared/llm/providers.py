from shared.llm.base import LLMClient


class MockLLMClient(LLMClient):
    async def generate(self, prompt: str) -> str:
        return f"Mock response for: {prompt}"
