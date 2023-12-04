from pydantic import BaseModel, Field


class Requirements(BaseModel):
    hard_drive: int = Field(alias="hardDrive")
    os_name: str = Field(alias="osName")
    ram_gb: int = Field(alias="ramGb")
    video_card: str = Field(alias="videoCard")


class SimilarDLC(BaseModel):
    dlc_name_from_another_game: str = Field(alias="dlcNameFromAnotherGame")
    is_free: bool = Field(alias="isFree")


class DLC(BaseModel):
    description: str
    dlc_name: str = Field(alias="dlcName")
    is_dlc_free: bool = Field(alias="isDlcFree")
    price: float
    rating: float
    similar_dlc: SimilarDLC = Field(alias="similarDlc")


class Game(BaseModel):
    company: str
    description: str
    dlcs: list[DLC]
    game_id: int = Field(alias="gameId")
    genre: str
    is_free: bool = Field(alias="isFree")
    price: float
    publish_date: str
    rating: float
    required_age: int = Field(alias="requiredAge")
    requirements: Requirements
    tags: list[str]
    title: str


class Games(BaseModel):
    games: list[Game]


