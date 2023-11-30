from pydantic_settings import BaseSettings, SettingsConfigDict


class TestUser(BaseSettings):
    login: str = ""
    password: str = ""


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_nested_delimiter='.'
    )

    base_url: str
    test_user: TestUser = TestUser()


base_settings = Settings()


