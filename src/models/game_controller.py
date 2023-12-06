from pydantic import BaseModel, Field
from src.utils.constants.messages import StatusMessage, UserMessage
from src.utils.randoms import *
from datetime import datetime, timezone


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
    rating: int = None
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


class RequirementsFactory(BaseModel):
    hard_drive: int = Field(alias="hardDrive", default_factory=random_number)
    os_name: str = Field(alias="osName", default_factory=random_string)
    ram_gb: int = Field(alias="ramGb", default_factory=random_number)
    video_card: str = Field(alias="videoCard", default_factory=random_string)


class SimilarDLCFactory(BaseModel):
    dlc_name_from_another_game: str = Field(alias="dlcNameFromAnotherGame", default_factory=random_string)
    is_free: bool = Field(alias="isFree", default_factory=random_bool)


class DLCFactory(BaseModel):
    description: str = Field(default_factory=random_string)
    dlc_name: str = Field(alias="dlcName", default_factory=random_string)
    is_dlc_free: bool = Field(alias="isDlcFree", default=False)
    price: float = Field(default_factory=random_float)
    rating: int = Field(default_factory=random_number)
    similar_dlc: SimilarDLC = Field(alias="similarDlc", default_factory=SimilarDLCFactory)


def dlc_factory():
    return [DLCFactory() for _ in range(2)]


class GameFactory(BaseModel):
    company: str = Field(default_factory=random_string)
    description: str = Field(default_factory=random_string)
    dlcs: list[DLC] = Field(default_factory=dlc_factory)
    game_id: int = Field(alias="gameId", default_factory=random_number)
    genre: str = Field(default_factory=random_string)
    is_free: bool = Field(alias="isFree", default=False)
    price: float = Field(default_factory=random_float)
    publish_date: str = Field(default=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%fZ'))
    rating: int = Field(default_factory=random_number)
    required_age: int = Field(alias="requiredAge", default_factory=random_number)
    requirements: Requirements = Field(default_factory=RequirementsFactory)
    tags: list[str] = Field(default_factory=random_list_of_strings)
    title: str = Field(default_factory=random_string)


# if __name__ == "__main__":
#     print(GameFactory().model_dump(by_alias=True))
#     current_time = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%fZ')
#     print(current_time)

