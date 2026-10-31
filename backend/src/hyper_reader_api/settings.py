from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Server configuration, read from environment variables (or a local
    `.env` file)."""

    model_config = SettingsConfigDict(
        env_prefix="HYPER_READER_", env_file=".env", extra="ignore"
    )

    api_key: str = Field(min_length=1)
    """Fixed token every client must send in the `X-API-Key` header
    (`HYPER_READER_API_KEY`)."""

    model: str = "gpt-5-mini"
    """AI model used by the agents (`HYPER_READER_MODEL`)."""

    openai_api_key: SecretStr | None = Field(
        default=None, validation_alias="OPENAI_API_KEY"
    )
    """OpenAI credentials (`OPENAI_API_KEY`). Optional here because the
    OpenAI SDK also reads it from the process environment."""
