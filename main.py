import logging
from pdf import extract_text_from_pdf
from spacyproj import SpacyAnalyzer
from graph import KeywordGraph as graphprincipalword

# Configure the logger to display INFO level messages with a simple format
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    # Define the path to the PDF file
    path = "1.pdf"

    # Extract text content from the PDF
    text = extract_text_from_pdf(path)
    logger.info("PDF extracted successfully.")
    logger.info(f"Text extracted from PDF (first 500 characters): {text[:500]}")

    # Initialize the spaCy-based analyzer
    analyzer = SpacyAnalyzer()

    # Tokenize the text using spaCy
    tokens = analyzer.tokenize(text)
    logger.info("Text tokenized successfully.")
    logger.info(f"First 50 tokens: {tokens[:50]}")

    # Define a set of keywords to search in the text
    keywords = {
        "environment", "crisis", "climate", "global", "warming",
        "pollution", "emissions", "carbon", "energy", "sustainability"
    }

    # Search for the keywords in the text and get their context
    results = analyzer.search_keywords(text=text, key_words=keywords)

    # Log the first 30 matched keywords and their contexts
    for word, context in results[:30]:
        logger.info(f"Found keyword: {word}")
        logger.info(f"Context: {context}\n")

    # Create and build the keyword graph based on co-occurrences
    grafo_kw = graphprincipalword(keywords)
    grafo_kw.build(results)

    # Display the graph
    grafo_kw.show()

    # Log a message and show the graph again (optional redundancy)
    logger.info("Displaying the graph...")
    grafo_kw.show()
