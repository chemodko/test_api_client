import allure
from src.controllers.jwt_authentication import JwtAuthenticationApiClient
from src.utils.randoms import random_string
from src.models.jwt_authentication import UnauthorizedError


@allure.feature("Create authentication token")
class TestJwtAuthentication:
    @allure.title("Create authentication token for existing user")
    def test_authentication(self):
        jwt_auth_controller = JwtAuthenticationApiClient()
        resp = jwt_auth_controller.post_create_auth_token(login="chemodko2", password="password",
                                                          status_code=200)
        assert len(resp.token) > 0

    @allure.feature("Create authentication token for non-existing user")
    def test_authentication_unauthorized(self):
        jwt_auth_controller = JwtAuthenticationApiClient()
        jwt_auth_controller.post_create_auth_token(login=random_string(), password=random_string(),
                                                   status_code=401, model=UnauthorizedError)
