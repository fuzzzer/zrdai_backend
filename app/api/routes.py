import logging
from fastapi import APIRouter, Body, Depends, status
from dependency_injector.wiring import inject, Provide

from app.containers import Container
from app.core.agent_processor import AgentProcessor
from app.api.schemas.agent_schemas import AgentInteractionRequest, AgentInteractionResponse

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post(
    "/interact",
    response_model=AgentInteractionResponse,
    status_code=status.HTTP_200_OK,
)
@inject
async def handle_agent_interaction(
    request: AgentInteractionRequest = Body(...),
    agent_processor: AgentProcessor = Depends(Provide[Container.agent_processor]),
):
    response_content = await agent_processor.process_interaction(
        demo_id=request.demo_id,
        user_input=request.user_input
    )
    
    return AgentInteractionResponse(response_content=response_content)
