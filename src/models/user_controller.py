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
    games: list
    id: int
    login: str
    password: str = Field(alias="pass")


class UserNewPasswordResponse(BaseModel):
    info: dict


class UserDeleteInfoResponse(BaseModel):
    info: dict


class UsersInfoResponse(BaseModel):
    info: list
