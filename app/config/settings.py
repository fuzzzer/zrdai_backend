# app/config/settings.py

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Custom AI Agents Proxy"
    API_V1_STR: str = "/api/v1"
    PROMPTS_PATH: str = "prompts"
    OPENAI_API_KEY: str
    OPENAI_MODEL_NAME: str = "gpt-5.4"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )