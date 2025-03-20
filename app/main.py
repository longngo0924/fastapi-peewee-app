from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.v1.router import api_router
from app.core.config import settings
from app.core.database import db
from app.models.user import User


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

app.include_router(api_router, prefix="/api/v1")
