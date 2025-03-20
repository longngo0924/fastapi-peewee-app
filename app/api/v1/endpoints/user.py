from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user, get_user_by_email
from app.dependencies.db import get_db

router = APIRouter()


@router.post("/", response_model=UserResponse)
def register_user(user: UserCreate):
    existing_user = get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    new_user = create_user(user)
    return new_user
