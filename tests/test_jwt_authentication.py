from src.controllers.jwt_authentication import JwtAuthenticationApiClient
from src.utils.randoms import random_string


def test_authentication_positive():
    jwt_auth_controller = JwtAuthenticationApiClient()
    jwt_auth_controller.post_create_auth_token(login="chemodko2", password="password", status_code=200)  # existing user


def test_authentication_negative():
    jwt_auth_controller = JwtAuthenticationApiClient()
    jwt_auth_controller.post_create_auth_token(login=random_string(), password=random_string(), status_code=401)  # non-existing user



