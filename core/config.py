from typing import Set
import os

from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "secret")
    JWT_REFRESH_SECRET_KEY = os.getenv("JWT_REFRESH_SECRET_KEY", "refreshSecret")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    ALLOWED_METHODS: Set[str] = ["*"]
    ALLOWED_HEADERS: Set[str] = ["*"]
    ALLOWED_CREDENTIALS: bool = True

    PROJECT_NAME: str = "Tienda Pelcastre"

    MONGO_CONNECTION_STRING: str = os.getenv("MONGO_CONNECTION_STRING", "mongodb://localhost:27017")

    class Config:
        case_sensitive = True


settings = Settings()
