from pydantic import BaseModel, Field
from src.utils.constants.messages import StatusMessage, UserMessage
from src.models.game_controller import Game


class UserInfoResponse(BaseModel):
    id: int
    login: str
    password: str = Field(alias="pass")
    games: list[Game] = None


class Info(BaseModel):
    status: StatusMessage
    message: UserMessage


class UserDTOResponse(BaseModel):
    info: Info
    register_data: UserInfoResponse = None


class InfoResponse(BaseModel):
    info: Info


class UsersInfoResponse(BaseModel):
    info: list


class UnauthorizedError(BaseModel):
    timestamp: str
    status: int = 401
    error: str = "Unauthorized"
    path: str
