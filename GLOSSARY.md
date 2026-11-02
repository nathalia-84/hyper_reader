# Hyper Reader

An EPUB reader for learning a language by reading books: the reader asks for translations of words and passages in context, and the app collects what they looked up.

## Reading

**Reader**:
The single person using the app: a language learner reading a book.
_Avoid_: User, student

**Book**:
A DRM-free EPUB the reader imported into the app's library.
_Avoid_: Ebook, document, file

**Book language**:
The language a book is written in (English or Spanish in the MVP).
_Avoid_: Source language, reading language

**Native language**:
The language the reader thinks in; every translation and note is written in it (PT-BR by default).
_Avoid_: Target language, mother tongue

**Location**:
A position in a book expressed as chapter, paragraph and token, independent of how the text is paginated.
_Avoid_: Page number, position

**Page**:
One screenful of text; transient, recomputed whenever layout changes, and never used to record where something is.

## Translation

**Word lookup**:
The reader long-presses a single word and gets its translation in context; when the word belongs to an expression in that sentence, the expression is explained first.
_Avoid_: Tap-to-translate

**Selection**:
A contiguous span of text on the current page that the reader chose by long-pressing and dragging.
_Avoid_: Highlight

**Phrase translation**:
The translation of a selection, requested from the selection's action sheet.

**Translation context**:
The text that accompanies a translation request so the right sense is chosen: the book's title and author plus the passage the reader has just read, never anything beyond the reader's location.
_Avoid_: Book summary

**Expression**:
A multi-word unit whose meaning is learned as a whole: an idiom ("kick the bucket"), a phrasal verb ("give up") or a fixed phrase.
_Avoid_: Multi-word term, collocation

**Lemma**:
The dictionary form of a word or expression in the book language ("go" for "went").
_Avoid_: Base form, root

## Learning

**Learning Glossary**:
The reader's personal collection of the words and expressions they have looked up; whole sentences are translated but never collected.
_Avoid_: Vocabulary list, word bank

**Glossary entry**:
One lemma in one book language within the Learning Glossary, with every sense the reader has met.

**Occurrence**:
One place where the reader looked up a glossary entry: the sentence, the book and the location.

**Re-reading mark**:
A passage the reader marked to come back to, with an optional note.
_Avoid_: Bookmark, highlight, annotation
