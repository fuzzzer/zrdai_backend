import sys
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from app.api.routes import router as api_router
from app.containers import Container
from app.api.errors.api_errors import ApiException

def create_app() -> FastAPI:
    load_dotenv()
    
    container = Container()
    container.wire(modules=[
        sys.modules[__name__], 
        "app.api.routes"
    ]) 
    
    settings = container.config()
    
    app = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        docs_url=f"{settings.API_V1_STR}/docs"
    )
    app.container = container

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    app.include_router(api_router, prefix=settings.API_V1_STR)

    @app.exception_handler(ApiException)
    async def api_exception_handler(request: Request, exc: ApiException):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "code": exc.code,
                "message": exc.message,
                "details": exc.details,
            },
        )

    return app

app = create_app()
