from enum import Enum


class APIRoutes(str, Enum):
    LOGIN = "/login"
    SIGNUP = "/signup"
    USER = "/user"
    USERS = "/users"

    def __str__(self) -> str:
        return self.value
