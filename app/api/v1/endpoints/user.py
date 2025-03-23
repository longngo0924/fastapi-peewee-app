from fastapi import APIRouter, Query
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user, get_user_by_email, get_list_user
from app.schemas.response import APIResponse, APIError, PaginatedResponse
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


@router.get("/", response_model=PaginatedResponse[UserResponse])
def get_users(page: int = Query(1, ge=1),
              limit: int = Query(10, ge=1)):
    paginated_data = get_list_user(page, limit)
    return PaginatedResponse(
        status="sucess",
        data=paginated_data,
        error=None
    )
