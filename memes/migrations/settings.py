from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_prefix="psql_", env_file_encoding="utf-8"
    )
    dbname: str
    user: str
    password: str
    host: str
    port: str
    echo: bool

    @property
    def conninfo(self):
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}"


settings = Settings()
