from abc import ABC, abstractmethod

class PromptRepository(ABC):
    @abstractmethod
    async def get_prompt(self, *, name: str) -> str:
        pass
