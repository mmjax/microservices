from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    amqp_url: str = "amqp://guest:guest@microservices-rabbitmq-1:5672/"
    postgres_url: str = "postgresql://postgres:password@microservices-postgres-1:5432/test"


settings = Settings()