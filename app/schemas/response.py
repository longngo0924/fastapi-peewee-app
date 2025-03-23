from pydantic import BaseModel
from typing import Generic, TypeVar, Optional

T = TypeVar("T")


class APIError(BaseModel):
    code: str
    message: str


class APIResponse(BaseModel, Generic[T]):
    status: str
    data: Optional[T]
    error: Optional[APIError]
