from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    amqp_url: str = "amqp://guest:guest@microservices-rabbitmq-1:5672"
    postgres_url: str = "postgresql://secUREusER:StrongEnoughPassword)@51.250.26.59:5432/orders"
    port: str = "80"

settings = Settings()