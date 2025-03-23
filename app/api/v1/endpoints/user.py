from fastapi import APIRouter
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user, get_user_by_email
from app.schemas.response import APIResponse, APIError
from app.core.error_codes import ErrorCode

router = APIRouter()


@router.post("/", response_model=APIResponse[UserResponse])
def register_user(user: UserCreate):
    existing_user = get_user_by_email(user.email)
    if existing_user:
        return APIResponse(
            status="error",
            data=None,
            error=APIError(
                code=ErrorCode.USER_ALREADY_EXISTS,
                message="User already exists"
            )
        )
    new_user = create_user(user)
    return APIResponse(status="success", data=new_user, error=None)
