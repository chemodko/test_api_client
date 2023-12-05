from pydantic import BaseModel


class AuthenticationResponse(BaseModel):
    token: str


class UnauthorizedError(BaseModel):
    timestamp: str
    status: int = 401
    error: str = "Unauthorized"
    path: str


