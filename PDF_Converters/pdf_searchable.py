

import PyPDF2
import sys
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Get the directory one level above
parent_dir = os.path.dirname(current_dir)
# Append the parent directory to sys.path
sys.path.append(parent_dir)


def pdf_to_txt(pdf_path: str, save_location: str):
    text = ''
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        num_pages = reader.numPages
        for page_num in range(num_pages):
            page = reader.getPage(page_num)
            text += page.extractText()

    with open(save_location, 'w', encoding='utf-16') as f:
        f.write(text)

    return save_location


if __name__ == '__main__':
    # Example usage
    pdf_path = '/home/nesov/Programmation/LLM-LangChain/Use Case/Multi_doc_legal_examples_pdf/status_ses.pdf'
    save_location = '/home/nesov/Programmation/LLM-LangChain/Use Case/Multi_doc_legal_examples_txt/status_ses.txt'
    extracted_text = pdf_to_txt(pdf_path, save_location)
