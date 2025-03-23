from app.models.user import User
from app.schemas.user import UserCreate
from passlib.context import CryptContext
from app.schemas.response import PaginatedData, PaginationMeta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user_by_email(email: str):
    return User.get_or_none(User.email == email)


def create_user(user: UserCreate):
    hashed_pw = get_password_hash(user.password)
    return User.create(email=user.email, hashed_password=hashed_pw)


def get_list_user(page: int, limit: int):
    offset = (page - 1) * limit
    total_count = User.select().count()
    users = User.select().limit(limit).offset(offset).order_by(User.id)
    paginated_users = PaginatedData(
        items=list(users),
        meta=PaginationMeta(
            page=page,
            size=limit,
            total=total_count
        )
    )
    return paginated_users
