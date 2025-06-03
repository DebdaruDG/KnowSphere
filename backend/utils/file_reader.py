from PyPDF2 import PdfReader
from backend.services.doc_splitter import split_text

def read_pdf(file_path: str):
    reader = PdfReader(file_path)
    text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    return split_text(text)
