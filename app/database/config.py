from typing import Annotated, TypeVar

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

T = TypeVar("T")

ExcludedField = Annotated[T, Field(exclude=True)]


class DBSettings(BaseSettings):

    model_config = SettingsConfigDict(env_file=".env")

    database_hostname:str
    database_port:str
    database_password:str
    database_name:str
    database_username:str
    secret_key:str
    admin_secret_key:str
    algorithm:str
    access_token_expire_minutes:int

    run_path: ExcludedField[str | None] = None
    out_path: ExcludedField[str | None] = None
    file_path: ExcludedField[str | None] = None

settings = DBSettings()