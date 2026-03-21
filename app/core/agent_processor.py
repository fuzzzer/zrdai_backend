import logging
from app.storage.prompt.prompt_repository import PromptRepository
from app.ai.text.text_generation_service import TextGenerationService

logger = logging.getLogger(__name__)

class AgentProcessor:
    def __init__(
        self,
        prompt_repo: PromptRepository,
        text_service: TextGenerationService,
    ):
        self._prompt_repo = prompt_repo
        self._text_service = text_service

    async def process_interaction(self, demo_id: str, user_input: str) -> str:
        system_prompt = await self._prompt_repo.get_prompt(name=demo_id)
        
        response_text = await self._text_service.generate_agent_response(
            system_prompt=system_prompt,
            user_input=user_input
        )
        
        return response_text
