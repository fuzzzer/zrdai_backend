from fastapi import HTTPException
from typing import Optional, Dict, Any

class ApiException(HTTPException):
    def __init__(
        self,
        status_code: int,
        code: str,
        message: str,
        book_name: str,
        details: Optional[Dict[str, Any]] = None,
    ):
        self.status_code = status_code
        self.code = code
        self.message = message
        self.book_name = book_name
        self.details = details
        super().__init__(status_code=status_code, detail=message)

class TaskAlreadyInProgressException(ApiException):
    def __init__(self, book_name: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(
            status_code=409,
            code="ALREADY_IN_PROGRESS",
            message=f"A process for book '{book_name}' is already running.",
            book_name=book_name,
            details=details,
        )

class BookAlreadyCompletedException(ApiException):
    def __init__(self, book_name: str):
        super().__init__(
            status_code=409,
            code="ALREADY_COMPLETED",
            message=f"Book '{book_name}' has already been generated. Set 'regenerate' to true to start over.",
            book_name=book_name,
        )

class BookIsReadyException(ApiException):
    def __init__(self, book_name: str):
        super().__init__(
            status_code=409,
            code="BOOK_IS_READY",
            message=f"Book '{book_name}' is marked as Ready and is read-only. Please revert it to Draft to make changes.",
            book_name=book_name,
        )