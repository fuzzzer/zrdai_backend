from pydantic import BaseModel

class AgentInteractionRequest(BaseModel):
    demo_id: str
    user_input: str

class AgentInteractionResponse(BaseModel):
    response_content: str
