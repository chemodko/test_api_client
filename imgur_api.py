import requests


class ApiClient:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None
        self.headers = {
            "Authorization": f"Client-ID {self.client_id}"
        }

    def auth(self, access_token):
        self.access_token = access_token
        self.headers["Authorization"] = f"Bearer {self.access_token}"

    def __base_call(self, method, url, params=None, data=None, json=None):
        resp = requests.request(method, url, headers=self.headers, params=params, data=data, json=json)
        # resp.raise_for_status()
        assert resp.status_code == 200
        return resp.json()

    def get(self, url, params=None):
        return self.__base_call("get", url, params=params)

    def post(self, url, data=None, json=None):
        return self.__base_call("post", url, data=data, json=json)

    def put(self, url, data=None, json=None):
        return self.__base_call("put", url, data=data, json=json)

    def delete(self, url):
        return self.__base_call("delete", url)


if __name__ == "__main__":
    # Пример использования:
    client_id = "client_id"
    client_secret = "client_secret"
    access_token = "access_token"

    api = ApiClient(client_id, client_secret)
    api.auth(access_token=access_token)

    # Пример запроса GET
    image_hash = "nK9EbaU"
    # response = api.get(f"https://api.imgur.com/3/image/{image_hash}")
    response = api.get("https://api.imgur.com/3/account/me/images")  # GET Account Images
    print(response)
    print()

    # Пример запроса POST
    data = {"refresh_token": "17746de109a0f5ff17e78d00d629ba40e158ad62",
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "refresh_token"}

    response = api.post("https://api.imgur.com/oauth2/token", data=data)
    print(response)