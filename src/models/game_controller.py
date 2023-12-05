from pydantic import BaseModel, Field
from src.utils.constants.messages import StatusMessage, UserMessage


class Requirements(BaseModel):
    hard_drive: int = Field(alias="hardDrive")
    os_name: str = Field(alias="osName")
    ram_gb: int = Field(alias="ramGb")
    video_card: str = Field(alias="videoCard")


class SimilarDLC(BaseModel):
    dlc_name_from_another_game: str = Field(alias="dlcNameFromAnotherGame", default=None)
    is_free: bool = Field(alias="isFree", default=None)


class DLC(BaseModel):
    description: str = None
    dlc_name: str = Field(alias="dlcName", default=None)
    is_dlc_free: bool = Field(alias="isDlcFree", default=None)
    price: float = None
    rating: float = None
    similar_dlc: SimilarDLC = Field(alias="similarDlc", default=None)


class Game(BaseModel):
    company: str
    description: str
    dlcs: list[DLC] = None
    game_id: int = Field(alias="gameId")
    genre: str
    is_free: bool = Field(alias="isFree")
    price: float
    publish_date: str
    rating: int
    required_age: int = Field(alias="requiredAge")
    requirements: Requirements
    tags: list[str]
    title: str


class Games(BaseModel):
    games: list[Game]


class UnauthorizedError(BaseModel):
    timestamp: str
    status: int = 401
    error: str = "Unauthorized"
    path: str


class Info(BaseModel):
    status: StatusMessage
    message: UserMessage


class GameAddedResponse(BaseModel):
    info: Info
    register_data: Game = None


class InfoResponse(BaseModel):
    info: Info


