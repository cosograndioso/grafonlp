from pdfminer.high_level import extract_text
import logging

# Create a logger for this module
logger = logging.getLogger(__name__)

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    try:
        # Attempt to extract text from the PDF at the given path
        return extract_text(pdf_path)
    except Exception as e:
        # Log an error if something goes wrong during extraction
        logger.error(f"Error analyzing the text: {e}")
        # Re-raise the exception so it can be handled elsewhere if needed
        raise e
