import logging
import spacy

# Create a logger for this module
logger = logging.getLogger(__name__)

class SpacyAnalyzer:
    def __init__(self, model="en_core_web_sm"):
        # Load the spaCy NLP model (default: small English model)
        self.nlp = spacy.load(model)

    def tokenize(self, text):
        """
        Tokenizes input text using spaCy, returning a list of unique lemmatized tokens
        excluding stopwords and punctuation.
        """
        try:
            doc = self.nlp(text)
            seen = set()     # To avoid duplicate tokens
            tokens = []

            for token in doc:
                word = token.lemma_.lower()
                # Filter out stopwords, punctuation, and already-seen words
                if not token.is_stop and not token.is_punct and word not in seen:
                    tokens.append(word)
                    seen.add(word)

            return tokens

        except Exception as e:
            logger.error(f"Error analyzing the text: {e}")
            raise e

    def search_keywords(self, *args, **kwargs):
        """
        Searches for specified keywords in the text and extracts the context around them.
        Returns a list of tuples (keyword, context).
        """
        try:
            # Support both positional and keyword arguments
            if args:
                text = args[0]
            else:
                text = kwargs.get("text", None)

            keywords = kwargs.get("key_words", [])

            if text is None:
                raise ValueError("Text is missing")

            doc = self.nlp(text)
            results = []

            for i, token in enumerate(doc):
                token_text = token.lemma_.lower()
                if token_text in keywords:
                    # Extract a context window: 5 tokens before and after
                    start = max(0, i - 5)
                    end = min(len(doc), i + 6)
                    context = doc[start:end].text
                    results.append((token_text, context))

            return results

        except Exception as e:
            logger.error(f"Error analyzing the text: {e}")
            raise e
