# Hyper Reader API

FastAPI backend that serves contextual translations (and, later, text analysis) through AI agents built with the OpenAI Agents SDK. Python is managed by uv (see `.python-version`).

## Configuration

Copy `.env.example` to `.env` and fill it in, or set the variables in the environment:

| Variable | Required | Meaning |
| --- | --- | --- |
| `HYPER_READER_API_KEY` | yes | Fixed token clients must send in the `X-API-Key` header |
| `OPENAI_API_KEY` | yes (for real calls) | OpenAI credentials |
| `HYPER_READER_MODEL` | no | AI model for the agents (default `gpt-5-mini`) |

## Run locally

```sh
uv run hyper-reader-api
```

The server listens on `0.0.0.0:8000`, so the phone can reach it at `http://<this-computer's-LAN-IP>:8000` on the same Wi-Fi.

Try it:

```sh
curl -X POST http://localhost:8000/translate \
  -H "X-API-Key: $HYPER_READER_API_KEY" -H "Content-Type: application/json" \
  -d '{"bookLanguage": "en", "targetLanguage": "pt-BR", "word": "bank", "sentence": "They sat on the bank of the river."}'
```

## Bruno collection

`bruno/` is a [Bruno](https://www.usebruno.com/) collection with requests for every endpoint, including the auth and validation error cases.

1. Copy `bruno/.env.example` to `bruno/.env` (gitignored) and set `HYPER_READER_API_KEY` to the same value as in `backend/.env`.
2. In Bruno, open the `bruno/` folder as a collection and select the **Local** environment.
3. Start the server (`uv run hyper-reader-api`) and send requests.

Requests marked "real AI" call OpenAI and spend credits. To run the whole collection from the terminal:

```sh
cd bruno && npx @usebruno/cli run --env Local
```

## Checks

```sh
uv run pytest           # HTTP-boundary tests with fake agents; no network
uv run mypy src tests
uv run ruff check . && uv run ruff format --check .
```
