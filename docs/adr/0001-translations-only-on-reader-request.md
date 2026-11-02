# Translations only on reader request

The app calls the AI only when the reader asks: a word lookup (long-press) or a phrase translation (from a selection). There is no proactive page analysis, so nothing is pre-loaded, cached ahead of time or underlined on the page. To pick the right sense, each request carries the book's title and author plus the passage just read: the sentence, the current paragraph up to the end of the visible page, and the two paragraphs before it in the same chapter, trimmed to about 1,500 characters. A book summary is not sent.

We chose this because proactive analysis cost an AI call for every page turned, mostly for words the reader already knew. It also needed a prefetch, debounce, deduplication and cancellation pipeline before the first useful result. With on-request translation, API spend tracks what the reader actually asks, and the reader decides what deserves attention.

## Considered Options

- **Proactive analysis with underlines (rejected).** The original spec analyzed the current and next page's paragraphs in the background, then underlined difficult words (for the reader's CEFR level) and idioms. It helped readers discover expressions they would not have noticed, but it spent calls on every page and added the most complex part of the app. CEFR levels existed only to tune it, so they went with it.
- **Book summary as translation context (rejected).** Summarizing the whole book means an expensive call at import and spoilers beyond the reader's location. It also adds little to word-sense choice, which depends on the nearby text. A per-chapter summary of chapters already read stays a possible v2 if long-range context ever proves necessary.
- **Sentence only as context (rejected).** This is what `POST /translate` sent first. It is cheap, but it misses pronoun referents and senses set up in the previous paragraphs.

## Consequences

- Expressions are found at lookup time. The translator checks whether the long-pressed word belongs to an expression in its sentence and explains the expression first, with a "just this word" fallback.
- The translation cache key ignores context (text + sentence + native language), so the same lookup in the same sentence is free, even if the preceding paragraphs differ.
- Book text (the selection and its context) leaves the device. Re-reading marks and their notes never do.
