from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://learnclew:learnclew_dev@localhost:5432/learnclew"
    SECRET_KEY: str = "dev-secret-key"
    STORAGE_PATH: str = "./storage"

    class Config:
        env_file = ".env"


settings = Settings()
