import fitz
from pathlib import Path


def read_pdf(file_path: str) -> str:

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"file not found{file_path}")
    if path.suffix.lower() != '.pdf':
        raise ValueError("pdf is only supported")
    extracted_text =""
    try:
        document = fitz.open(path)
        for page in document:
            extracted_text += page.get_text()
        document.close()
    except Exception as e:
        raise RuntimeError(f"Unable to read PDF: {e}")
    if not extracted_text.strip():
        raise ValueError("The PDF contains no readable text.")

    return extracted_text
    