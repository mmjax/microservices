from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    amqp_url: str
    class Config:
        env_file = ".env"

settings = Settings()