import pytest
from fastapi.testclient import TestClient

from hyper_reader_api.agent_runner import TranslationRequest, TranslationResult
from hyper_reader_api.app import create_app
from hyper_reader_api.settings import Settings

API_KEY = "test-api-key"


class FakeAgentRunner:
    """Stands in for the real AI agents; records what it was asked."""

    def __init__(self) -> None:
        self.translate_requests: list[TranslationRequest] = []

    async def translate(self, request: TranslationRequest) -> TranslationResult:
        self.translate_requests.append(request)
        return TranslationResult(
            translation="margem",
            lemma="bank",
            note="Margem de um rio, não instituição financeira.",
        )


@pytest.fixture
def runner() -> FakeAgentRunner:
    return FakeAgentRunner()


@pytest.fixture
def client(runner: FakeAgentRunner) -> TestClient:
    settings = Settings(api_key=API_KEY, model="test-model")
    return TestClient(create_app(settings, agent_runner=runner))


def translate_body(**overrides: str) -> dict[str, str]:
    return {
        "bookLanguage": "en",
        "targetLanguage": "pt-BR",
        "word": "bank",
        "sentence": "They sat on the bank of the river.",
        **overrides,
    }


def test_translate_returns_translation_lemma_and_note(client: TestClient) -> None:
    response = client.post(
        "/translate", json=translate_body(), headers={"X-API-Key": API_KEY}
    )

    assert response.status_code == 200
    assert response.json() == {
        "translation": "margem",
        "lemma": "bank",
        "note": "Margem de um rio, não instituição financeira.",
    }


def test_rejects_request_without_api_key(
    client: TestClient, runner: FakeAgentRunner
) -> None:
    response = client.post("/translate", json=translate_body())

    assert response.status_code == 401
    assert runner.translate_requests == []


def test_rejects_request_with_wrong_api_key(
    client: TestClient, runner: FakeAgentRunner
) -> None:
    response = client.post(
        "/translate", json=translate_body(), headers={"X-API-Key": "wrong-key"}
    )

    assert response.status_code == 401
    assert runner.translate_requests == []


def test_passes_languages_word_and_sentence_to_the_translator(
    client: TestClient, runner: FakeAgentRunner
) -> None:
    client.post(
        "/translate",
        json=translate_body(
            bookLanguage="es",
            targetLanguage="en-US",
            word="banco",
            sentence="Se sentó en el banco del parque.",
        ),
        headers={"X-API-Key": API_KEY},
    )

    assert runner.translate_requests == [
        TranslationRequest(
            book_language="es",
            target_language="en-US",
            word="banco",
            sentence="Se sentó en el banco del parque.",
        )
    ]


def test_rejects_request_without_context_sentence(
    client: TestClient, runner: FakeAgentRunner
) -> None:
    body = translate_body()
    del body["sentence"]

    response = client.post("/translate", json=body, headers={"X-API-Key": API_KEY})

    assert response.status_code == 422
    assert runner.translate_requests == []
