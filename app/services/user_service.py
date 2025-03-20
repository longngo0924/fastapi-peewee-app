from app.models.user import User
from app.schemas.user import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user_by_email(email: str):
    return User.get_or_none(User.email == email)


def create_user(user: UserCreate):
    hashed_pw = get_password_hash(user.password)
    return User.create(email=user.email, hashed_password=hashed_pw)
