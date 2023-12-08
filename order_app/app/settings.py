from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
load_dotenv()
import os

class Settings(BaseSettings):
    amqp_url: str = os.load_dotenv(AMQP_URL)
    postgres_url: str = os.load_dotenv(POSTGRES_URL)
    port: str = os.load_dotenv(PORT)

settings = Settings()