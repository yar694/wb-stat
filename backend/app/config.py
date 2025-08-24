from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "WB Analytics API"
    wb_api_token: str = | None = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
