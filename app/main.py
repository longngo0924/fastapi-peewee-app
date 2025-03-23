from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from app.api.v1.router import api_router
from app.core.config import settings
from app.core.database import db
from app.models.user import User
from app.schemas.response import APIResponse, APIError
from app.core.error_codes import ErrorCode


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Connect database and create tables at startup
    if db.is_closed():
        db.connect()

    # Only create tables automatically if they don't exist yet
    # For production, migrations should be used
    if hasattr(db, 'bind_ctx') and not User.table_exists():
        db.create_tables([User], safe=True)
    yield
    # Close database at shutdown
    if not db.is_closed():
        db.close()

app = FastAPI(title=settings.PROJECT_NAME, lifespan=lifespan)


@app.exception_handler(RequestValidationError)
async def handle_validation_error(request: Request, err: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content=APIResponse(
            status="error",
            data=None,
            error=APIError(
                code=ErrorCode.VALIDATION_ERROR,
                message=str(err)
            )
        ).model_dump()
    )


@app.exception_handler(Exception)
async def handle_app_error(request: Request, err: Exception):
    return JSONResponse(
        status_code=500,
        content=APIResponse(
            status="error",
            data=None,
            error=APIError(
                code=ErrorCode.UNKNOWN_ERROR,
                message=str(err)
            )
        ).model_dump()
    )


app.include_router(api_router, prefix="/api/v1")
