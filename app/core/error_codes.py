from enum import Enum


class ErrorCode(str, Enum):
    # General Errors
    UNKNOWN_ERROR = "UNKNOWN_ERROR"
    VALIDATION_ERROR = "VALIDATION_ERROR"

    # User Errors
    USER_NOT_FOUND = "USER_NOT_FOUND"
    USER_ALREADY_EXISTS = "USER_ALREADY_EXISTS"
    INVALID_CREDENTIALS = "INVALID_CREDENTIALS"

    # Item Errors
    ITEM_NOT_FOUND = "ITEM_NOT_FOUND"
    ITEM_ALREADY_EXISTS = "ITEM_ALREADY_EXISTS"
