from utils.clients.http_api_client import HttpApiClient
from models_responses.jwt_authentication_controller import AuthenticationResponse


class JwtAuthenticationApiClient(HttpApiClient):
    def post_create_auth_token(self) -> AuthenticationResponse:
        log_in_data = {
            "username": self.login,
            "password": self.password
        }
        token_resp = self.post(f"{self.base_url}/login", json=log_in_data, status_code=200)
        # self.set_token(token_resp["token"])
        return AuthenticationResponse(**token_resp)

    # def auth(self) -> None:
    #     """Calls log_in method and sets the authorization headers."""
    #     self.__log_in()
    #     self.headers["Authorization"] = f"Bearer {self.token}"
