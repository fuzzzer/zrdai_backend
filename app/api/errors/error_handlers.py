from fastapi import Request
from fastapi.responses import JSONResponse
from .api_errors import ApiException

async def api_exception_handler(request: Request, exc: ApiException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "code": exc.code,
            "message": exc.message,
            "book_name": exc.book_name,
            "details": exc.details,
        },
    )