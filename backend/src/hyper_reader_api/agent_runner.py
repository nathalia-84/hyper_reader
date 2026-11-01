from typing import Protocol

from hyper_reader_api.schemas import TranslationRequest, TranslationResult


class AgentRunner(Protocol):
    """Boundary between the HTTP routes and the AI agent, so tests can
    substitute a fake."""

    async def translate(self, request: TranslationRequest) -> TranslationResult: ...
