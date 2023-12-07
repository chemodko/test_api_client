import allure
from src.http_api_client import HttpApiClient
from src.models.jwt_authentication import AuthenticationResponse


class JwtAuthenticationApiClient(HttpApiClient):
    @allure.step("Creating authentication token")
    def post_create_auth_token(self, login: str = None, password: str = None, status_code: int = 200, model=AuthenticationResponse):
        log_in_data = {
            "username": login,
            "password": password
        }
        token_resp = self.post(f"{self.base_url}/login", json=log_in_data, status_code=status_code)
        return model(**token_resp)

