import PyPDF2
from pathlib import Path


def search(pdf_path: str) -> bool:
    """Searches for plain text content in a PDF file.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        bool: True if the PDF contains searchable text, False otherwise.

    Raises:
        FileNotFoundError: If the PDF file does not exist.
        PyPDF2.utils.PdfReadError: If the PDF file is not a valid PDF.

    """
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file, strict=False)
        num_pages = reader.numPages

        for page_num in range(num_pages):
            page = reader.getPage(page_num)
            text = page.extractText()

            if text.strip():  # If extracted text is not empty or only whitespace
                print("Is searchable")
                return True

    file_path = Path(pdf_path)
    file_name = file_path.name

    print(f'The PDF ({file_name}) is not searchable (no plain text, but pictures of texts). Initialization of AI powered Computer Vision (OpenCV) to translate the image into text.')

    return False





if __name__ == '__main__':
    search("/home/nesov/Programmation/LLM-LangChain/Use Case/Multi_doc_legal_examples_pdf/status_ses.pdf")