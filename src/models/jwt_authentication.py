from pydantic import BaseModel


class AuthenticationResponse(BaseModel):
    token: str = None

    timestamp: str = None
    status: int = 401
    error: str = "Unauthorized"
    path: str = "/api/user"

