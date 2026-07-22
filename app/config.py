from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str
    DATABASE_URL: str

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    OPENAI_API_KEY: str
    OPENAI_MODEL: str = "gpt-4.1-mini"
    REDIS_URL: str

    class Config:
        env_file = ".env"


settings = Settings()
