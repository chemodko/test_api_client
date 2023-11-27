import requests
import time


class ApiClient:
    def __init__(self, login, password, headers=None, token=None):
        self.login = login
        self.password = password
        self.headers = headers
        self.token = token
        self.session = requests.Session()

    def auth(self):
        self.headers = {
             'Authorization': f'Bearer {self.token}'
        }

    def __base_call(self, method, url, params=None, data=None, json=None):
        resp = self.session.request(method, url, headers=self.headers, params=params, data=data, json=json)
        resp.raise_for_status()
        return resp.json()

    def set_token(self, token):
        self.token = token

    def get_token(self):
        return self.token

    def get(self, url, params=None):
        return self.__base_call("get", url, params=params)

    def post(self, url, data=None, json=None):
        return self.__base_call("post", url, data=data, json=json)

    def put(self, url, data=None, json=None):
        return self.__base_call("put", url, data=data, json=json)

    def delete(self, url):
        return self.__base_call("delete", url)


if __name__ == "__main__":
    login = "chemodko"
    password = "password"
    api = ApiClient(login, password)

    # Регистрация нового пользователя
    # json_data = {
    #     "login": api.login,
    #     "pass": api.password
    # }
    # resp = api.post("http://85.192.34.140:8080/api/signup", json=json_data)
    # print(resp)

    # Получение токена
    json_data = {
        "username": api.login,
        "password": api.password
    }
    token_resp = api.post("http://85.192.34.140:8080/api/login", json=json_data)
    print(token_resp)
    api.set_token(token_resp["token"])

    # Авторизация
    api.auth()

    # Получение информации о пользователе
    user_info_resp = api.get("http://85.192.34.140:8080/api/user")
    print(user_info_resp)

    # Показать всех существующих пользователей (10)
    users_info_resp = api.get("http://85.192.34.140:8080/api/users")
    print(users_info_resp[:10])


