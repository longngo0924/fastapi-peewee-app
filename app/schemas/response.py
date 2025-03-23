from pydantic import BaseModel, model_validator
from typing import Generic, TypeVar, Optional

T = TypeVar("T")


class APIError(BaseModel):
    code: str
    message: str


class APIResponse(BaseModel, Generic[T]):
    status: str
    data: Optional[T]
    error: Optional[APIError]


class PaginationMeta(BaseModel):
    total: int
    page: int
    size: int
    pages: int = 1

    @model_validator(mode="after")
    def calculate_pages(cls, values: "PaginationMeta") -> "PaginationMeta":
        if values.size > 0:
            values.pages = (values.total + values.size - 1) // values.size
        else:
            values.pages = 1
        return values



class PaginatedData(BaseModel, Generic[T]):
    items: list[T]
    meta: PaginationMeta


class PaginatedResponse(APIResponse[PaginatedData[T]]):
    pass
