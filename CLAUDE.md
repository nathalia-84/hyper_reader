# hyper_reader

## Language

- Write all specs, issues, PRs, docs (including `GLOSSARY.md` and ADRs) and code in English: identifiers, comments, log messages, test names and commit messages.
- The app UI is English-only in the MVP; UI strings go through Flutter's localization resources (other UI languages are v2).
- Translations shown to the reader are generated in the reader's configured native language (default PT-BR); never hardcode PT-BR in prompts or code.

## Git

- Never add AI attribution to commits or PRs: no `Co-Authored-By: Claude ...` trailer in commit messages, and no "Generated with Claude Code" line (or similar) in PR descriptions.

## Backend endpoints

- Every new backend endpoint, and every change to an endpoint's request or response, ships with Bruno requests in `backend/bruno/` (one folder per endpoint): the success case plus each error status the endpoint returns, each with `assert` checks. Put "(real AI)" in the name of requests that reach OpenAI. Done means `npx @usebruno/cli run --env Local` passes against a locally running server.

## Agent skills

### Issue tracker

Issues are tracked in GitHub Issues (`nathalia-84/hyper_reader`) via the `gh` CLI. See `docs/agents/issue-tracker.md`.

### Triage labels

The five default labels: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: one `GLOSSARY.md` + `docs/adr/` at the repo root. See `docs/agents/domain.md`.
