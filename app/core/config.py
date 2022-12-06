import logging
import os
from enum import Enum
from functools import lru_cache
from typing import Optional

from pydantic import BaseSettings

logger = logging.getLogger(__name__)


class EnvironmentEnum(str, Enum):
    PRODUCTION = "production"
    LOCAL = "local"


class GlobalConfig(BaseSettings):
    TITLE: str = "APP Project Title"
    DESCRIPTION: str = "APP Project Description"

    ROOT_URL = os.getenv("ROOT_URL", "http://localhost:8000/")
    STATIC_FILES_URL = os.getenv("STATIC_FILES_URL", "http://localhost:8000/static/")
    STATIC_FILES_PATH = os.getenv("STATIC_FILES_PATH", "./static/")
    STATIC_FILES_ENGINE = "local"

    DATABASE_URI_TEST = os.getenv(
        "DATABASE_URI_TEST",
        "postgresql+asyncpg://postgres:postgres@localhost:5432/fastapi_test",
    )
    DATABASE_URI = os.getenv(
        "DATABASE_URI",
        "postgresql+asyncpg://postgres:postgres@localhost:5432/fastapi",
    )

    ENVIRONMENT: EnvironmentEnum
    DEBUG: bool = False
    TESTING: bool = False
    TIMEZONE: str = "UTC"

    DB_ECHO_LOG: bool = True

    # Api V1 prefix
    API_V1_STR = "/v1"

    class Config:
        case_sensitive = True


class LocalConfig(GlobalConfig):
    """Local configurations."""

    DEBUG: bool = True
    ENVIRONMENT: EnvironmentEnum = EnvironmentEnum.LOCAL


class ProdConfig(GlobalConfig):
    """Production configurations."""

    DEBUG: bool = False
    ENVIRONMENT: EnvironmentEnum = EnvironmentEnum.PRODUCTION


class FactoryConfig:
    def __init__(self, environment: Optional[str]):
        self.environment = environment

    def __call__(self) -> GlobalConfig:
        if self.environment == EnvironmentEnum.LOCAL.value:
            salida = LocalConfig()
            return salida
        return ProdConfig()


@lru_cache()
def get_configuration() -> GlobalConfig:
    return FactoryConfig(os.environ.get("ENVIRONMENT"))()


settings = get_configuration()
