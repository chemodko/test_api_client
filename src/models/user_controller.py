from typing import Union

from pydantic import BaseModel, Field
from src.utils.constants.messages import StatusMessage, UserMessage


class Game(BaseModel):
    pass


class Games(BaseModel):  # list of dicts
    games: list[Game]


class RegisterData(BaseModel):
    id: int
    login: str
    password: str = Field(alias="pass")
    games: list  # TODO: Games


class Info(BaseModel):
    status: StatusMessage
    message: UserMessage


class UserDTOResponse(BaseModel):
    info: Info
    register_data: RegisterData = None


class UserInfoResponse(BaseModel):
    games: list = None  # TODO: Games
    id: int = None
    login: str = None
    password: str = Field(alias="pass", default=None)

    timestamp: str = None
    status: int = 401
    error: str = "Unauthorized"
    path: str = "/api/user"


class UserNewPasswordResponse(BaseModel):
    info: Info = None

    timestamp: str = None
    status: int = 401
    error: str = "Unauthorized"
    path: str = "/api/user"


class UserDeleteInfoResponse(BaseModel):
    info: Info = None

    timestamp: str = None
    status: int = 401
    error: str = "Unauthorized"
    path: str = "/api/user"


class UsersInfoResponse(BaseModel):
    info: list
