from typing import Union

from src.http_api_client import HttpApiClient
from src.models.jwt_authentication import AuthenticationResponse, UnauthorizedError


class JwtAuthenticationApiClient(HttpApiClient):
    def post_create_auth_token(self, login: str = None, password: str = None, status_code: int = 200) -> Union[AuthenticationResponse, UnauthorizedError]:
        log_in_data = {
            "username": login,
            "password": password
        }
        token_resp = self.post(f"{self.base_url}/login", json=log_in_data, status_code=status_code)
        if status_code == 200:
            return AuthenticationResponse(**token_resp)
        elif status_code == 401:
            return UnauthorizedError(**token_resp)

