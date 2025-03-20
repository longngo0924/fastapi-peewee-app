from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.v1.router import api_router
from app.core.config import settings
from app.core.database import db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Connect database and create tables at startup
    db.connect()
    yield
    # Close database at shutdown
    if not db.is_closed():
        db.close()

app = FastAPI(title=settings.PROJECT_NAME, lifespan=lifespan)

app.include_router(api_router, prefix="/api/v1")
