from pydantic import BaseModel, Field


class UserDTO(BaseModel):
    login: str
    password: str = Field(alias="pass")












