import pdfplumber
import docx2txt

# Extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Extract text from DOCX
def extract_text_from_docx(docx_path):
    text = docx2txt.process(docx_path)
    return text
