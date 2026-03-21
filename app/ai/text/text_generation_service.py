from abc import ABC, abstractmethod

class TextGenerationService(ABC):
    @abstractmethod
    async def generate_agent_response(self, *, system_prompt: str, user_input: str) -> str:
        pass
