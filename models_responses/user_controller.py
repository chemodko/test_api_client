from pydantic import BaseModel, Field
from utils.constants.messages import StatusMessage, UserMessage


class RegisterData(BaseModel):
    id: int
    login: str
    password: str = Field(alias="pass")
    games: list


class Info(BaseModel):
    status: StatusMessage
    message: UserMessage


class UserDTOResponse(BaseModel):
    info: Info
    register_data: RegisterData


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
    response: list











