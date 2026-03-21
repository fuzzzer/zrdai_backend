import logging
from openai import AsyncOpenAI
from app.config.settings import Settings
from app.ai.text.text_generation_service import TextGenerationService

logger = logging.getLogger(__name__)

class OpenAITextService(TextGenerationService):
    def __init__(self, settings: Settings):
        self._settings = settings
        self._client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
        self._model_name = settings.OPENAI_MODEL_NAME

    async def generate_agent_response(self, *, system_prompt: str, user_input: str) -> str:
        try:
            response = await self._client.chat.completions.create(
                model=self._model_name,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Failed to generate response from OpenAI: {e}")
            raise e
