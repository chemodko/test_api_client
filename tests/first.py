from controllers_clients.jwt_authentication_api_client import JwtAuthenticationApiClient
from controllers_clients.user_controller_api_client import UserControllerApiClient


if __name__ == "__main__":

    api = UserControllerApiClient()
    print("Api:\n", api)
    api.post_new_user(api.login, api.password)
    api.auth()
    print("Authorized api\n", api)

    print("User info:\n", api.get_user_info())
    print("New password:\n", api.put_user_password("password"))

    print("Users info:\n", api.get_users_info().response[-10:])
    print("User delete:\n", api.delete_user())








