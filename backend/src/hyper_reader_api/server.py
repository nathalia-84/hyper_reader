from agents import set_default_openai_key
from fastapi import FastAPI

from hyper_reader_api.app import create_app
from hyper_reader_api.openai_agent_runner import OpenAIAgentRunner
from hyper_reader_api.settings import Settings


def build_app() -> FastAPI:
    """Production app factory: configuration from the environment, real agents."""
    settings = Settings()
    if settings.openai_api_key is not None:
        set_default_openai_key(settings.openai_api_key.get_secret_value())
    return create_app(settings, agent_runner=OpenAIAgentRunner(model=settings.model))
