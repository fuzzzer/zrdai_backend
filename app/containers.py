from dependency_injector import containers, providers
from app.config.settings import Settings
from app.storage.prompt.implementations.file_system_prompt_repository import FileSystemPromptRepository
from app.ai.text.implementations.openai_text_service import OpenAITextService
from app.core.agent_processor import AgentProcessor

class Container(containers.DeclarativeContainer):
    config = providers.Singleton(Settings)

    prompt_repo = providers.Singleton(
        FileSystemPromptRepository, 
        settings=config
    )

    text_service = providers.Singleton(
        OpenAITextService, 
        settings=config
    )

    agent_processor = providers.Factory(
        AgentProcessor,
        prompt_repo=prompt_repo,
        text_service=text_service,
    )
