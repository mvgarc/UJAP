from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://usuario:password@localhost/mibd"

    class Config:
        env_file = ".env"

settings = Settings()
