from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".minio_env",
        env_prefix="minio_",
        env_file_encoding="utf-8",
    )
    endpoint: str
    root_user: str
    root_password: str
    bucket_name: str
    volumes: str


settings = Settings()
