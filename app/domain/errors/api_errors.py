from fastapi import HTTPException
from typing import Optional, Dict, Any

class ApiException(HTTPException):
    def __init__(
        self,
        status_code: int,
        code: str,
        message: str,
        details: Optional[Dict[str, Any]] = None,
    ):
        self.status_code = status_code
        self.code = code
        self.message = message
        self.details = details
        super().__init__(status_code=status_code, detail=message)

class PromptNotFoundError(ApiException):
    def __init__(self, demo_id: str):
        super().__init__(
            status_code=404,
            code="PROMPT_NOT_FOUND",
            message=f"System prompt for demo '{demo_id}' could not be found.",
            details={"demo_id": demo_id}
        )
