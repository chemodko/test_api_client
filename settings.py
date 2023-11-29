from pydantic import BaseModel


class Settings(BaseModel):
    login: str
    password: str
    base_url: str


