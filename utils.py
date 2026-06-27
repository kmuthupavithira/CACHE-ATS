import PyPDF2
import docx2txt
import pytesseract
from pdf2image import convert_from_bytes

# --------------------------------------------------
# Set Tesseract OCR Path
# Change this path if Tesseract is installed elsewhere
# --------------------------------------------------

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# --------------------------------------------------
# Extract Text From PDF
# --------------------------------------------------

def extract_text_from_pdf(file):

    text = ""

    try:
        # Move file pointer to beginning
        file.seek(0)

        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    except Exception as e:
        print("PDF Extraction Error:", e)

    # --------------------------------------------------
    # If no text found, use OCR
    # --------------------------------------------------

    if len(text.strip()) == 0:

        try:

            file.seek(0)

            images = convert_from_bytes(file.read())

            for img in images:

                text += pytesseract.image_to_string(img)

        except Exception as e:

            print("OCR Error:", e)

    return text


# --------------------------------------------------
# Extract Text From DOCX
# --------------------------------------------------

def extract_text_from_docx(file):

    try:

        file.seek(0)

        text = docx2txt.process(file)

        return text

    except Exception as e:

        print("DOCX Error:", e)

        return ""


# --------------------------------------------------
# Main Extraction Function
# --------------------------------------------------

def extract_text(file):

    filename = file.name.lower()

    if filename.endswith(".pdf"):

        return extract_text_from_pdf(file)

    elif filename.endswith(".docx"):

        return extract_text_from_docx(file)

    else:

        return ""