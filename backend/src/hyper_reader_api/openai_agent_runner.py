import json

from agents import Agent, RunContextWrapper, Runner

from hyper_reader_api.schemas import TranslationRequest, TranslationResult


def _translator_instructions(
    context: RunContextWrapper[TranslationRequest],
    agent: Agent[TranslationRequest],
) -> str:
    request = context.context
    return (
        "You help a language learner who is reading a book. "
        f"The book is written in the language with BCP 47 tag "
        f"'{request.book_language}'. The learner's native language has BCP 47 "
        f"tag '{request.target_language}'.\n"
        "You receive a word (or a short multi-word span) and the sentence it "
        "appears in. Translate the word as it is used in that sentence, "
        "choosing the sense that fits the context.\n"
        "Return:\n"
        f"- translation: the translation in '{request.target_language}', a "
        "word or short phrase, not a full sentence;\n"
        f"- lemma: the dictionary form of the word in "
        f"'{request.book_language}' (e.g. the infinitive of a verb, the "
        "singular of a noun);\n"
        f"- note: one short sentence in '{request.target_language}' explaining "
        "the meaning or usage in this context."
    )


translator_agent: Agent[TranslationRequest] = Agent(
    name="TranslatorAgent",
    instructions=_translator_instructions,
    output_type=TranslationResult,
)


class OpenAIAgentRunner:
    """Runs the agents against the OpenAI API."""

    def __init__(self, model: str) -> None:
        self._translator = translator_agent.clone(model=model)

    async def translate(self, request: TranslationRequest) -> TranslationResult:
        message = json.dumps(
            {"word": request.word, "sentence": request.sentence},
            ensure_ascii=False,
        )
        result = await Runner.run(
            self._translator, message, context=request, max_turns=1
        )
        return result.final_output_as(TranslationResult, raise_if_incorrect_type=True)
