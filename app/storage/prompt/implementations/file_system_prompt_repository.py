import logging
import aiofiles
from app.config.settings import Settings
from app.storage.prompt.prompt_repository import PromptRepository
from app.domain.errors.api_errors import PromptNotFoundError

logger = logging.getLogger(__name__)

class FileSystemPromptRepository(PromptRepository):
    def __init__(self, settings: Settings):
        self._settings = settings

    async def get_prompt(self, *, name: str) -> str:
        prompt_path = f"{self._settings.PROMPTS_PATH}/{name}.txt"
        try:
            async with aiofiles.open(prompt_path, mode='r', encoding='utf-8') as f:
                return await f.read()
        except FileNotFoundError:
            logger.error(f"Prompt file not found at '{prompt_path}'.")
            raise PromptNotFoundError(demo_id=name)
