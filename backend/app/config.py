from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "WB Analytics API"
    wb_api_token: str = "eyJhbGciOiJFUzI1NiIsImtpZCI6IjIwMjUwNTIwdjEiLCJ0eXAiOiJKV1QifQ.eyJlbnQiOjEsImV4cCI6MTc3MTgzMDIxNCwiaWQiOiIwMTk4ZGQ3Ni1lYWM5LTcxYmYtYmE2YS1hZTFiMTgxYWVmZGYiLCJpaWQiOjg3NDA4MzczLCJvaWQiOjQzODI2OTYsInMiOjg0MzYsInNpZCI6IjU4YWJkNGVjLTY5MmUtNDdlYS04MDY3LThiMTczNGVlNThlYSIsInQiOmZhbHNlLCJ1aWQiOjg3NDA4MzczfQ.Mt2y7A0h6l2FtiUS2Y4trr0FTRJ2s3yEWCGDQun_L17ywXJvFtwh_YSxvnATIE9N1XKP_2XJul2n-_gYv3sYfQ"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
