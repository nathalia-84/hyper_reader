from typing import Annotated

from fastapi import Depends, FastAPI, Request

from hyper_reader_api.agent_runner import (
    AgentRunner,
    TranslationRequest,
    TranslationResult,
)
from hyper_reader_api.auth import require_api_key
from hyper_reader_api.settings import Settings


def get_agent_runner(request: Request) -> AgentRunner:
    runner: AgentRunner = request.app.state.agent_runner
    return runner


def create_app(settings: Settings, agent_runner: AgentRunner) -> FastAPI:
    # Every route requires the API key.
    app = FastAPI(title="Hyper Reader API", dependencies=[Depends(require_api_key)])
    app.state.settings = settings
    app.state.agent_runner = agent_runner

    @app.post("/translate")
    async def translate(
        body: TranslationRequest,
        runner: Annotated[AgentRunner, Depends(get_agent_runner)],
    ) -> TranslationResult:
        return await runner.translate(body)

    return app
