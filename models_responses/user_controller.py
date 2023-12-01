from pydantic import BaseModel, Field


class UserDTOResponse(BaseModel):
    id: int
    login: str
    password: str = Field(alias="pass")


class UserInfoResponse(BaseModel):
    id: int
    login: str
    password: str = Field(alias="pass")


class UserNewPasswordResponse(BaseModel):
    info: dict


class UserDeleteInfoResponse(BaseModel):
    info: dict


class UsersInfoResponse(BaseModel):
    info: list[str]











