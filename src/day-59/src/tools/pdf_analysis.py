from pathlib import Path

import fitz  # PyMuPDF
from google.genai import types

from config import BASE_DIR
from logger_config import logger
from schemas import PdfAnalysis, PdfPage

# Where user-supplied documents live. Relative filenames the model
# passes are resolved against this folder so it never needs to know
# the machine's absolute paths.
UPLOADS_DIR = BASE_DIR / "uploads"

# Cap the extracted text so a large report doesn't blow up the
# transcript (and the per-turn token cost) on every following turn.
MAX_TEXT_CHARS = 12000


# ---------------------------------------------------------------
# The actual tool implementation
#
# Mirrors tools/web_search.py: a plain function returning JSON-
# serialisable data. The agent loop owns execution and display.
# ---------------------------------------------------------------
def analyze_pdf(filename: str, max_chars: int = MAX_TEXT_CHARS) -> dict:
    """Extract text from a PDF in src/uploads and return it for analysis."""

    # Resolve the path. Bare filenames go through the uploads folder;
    # an absolute path is honoured as-is.
    candidate = Path(filename)
    path = candidate if candidate.is_absolute() else UPLOADS_DIR / candidate

    if not path.exists():
        available = [p.name for p in UPLOADS_DIR.glob("*.pdf")] if UPLOADS_DIR.exists() else []
        return {
            "error": f"File not found: {path.name}",
            "available_files": available,
        }

    logger.info(f"Extracting text from PDF: {path.name}")

    pages = []
    full_text = ""
    truncated = False

    with fitz.open(path) as document:
        page_count = document.page_count

        for index, page in enumerate(document, start=1):
            page_text = page.get_text().strip()

            # Stop accumulating once we hit the budget, but keep
            # counting pages so the model knows how much it missed.
            if not truncated:
                remaining = max_chars - len(full_text)

                if remaining <= 0:
                    truncated = True
                else:
                    chunk = page_text[:remaining]
                    full_text += chunk + "\n\n"
                    pages.append(PdfPage(page=index, text=chunk))

    # Validate the payload against the schema before it leaves the
    # tool. If extraction ever produces the wrong shape this raises
    # here, and the agent loop turns it into a clean tool error
    # instead of feeding Gemini a malformed response.
    analysis = PdfAnalysis(
        filename=path.name,
        page_count=page_count,
        char_count=len(full_text),
        truncated=truncated,
        text=full_text.strip(),
        pages=pages,
    )

    # The SDK needs plain JSON-serialisable data for the
    # function_response, so hand back a dict rather than the model.
    return analysis.model_dump()


# ---------------------------------------------------------------
# The declaration Gemini sees
#
# Hand-written so we control the wording the model reasons over,
# which is what drives tool-choice quality.
# ---------------------------------------------------------------
ANALYZE_PDF_DECLARATION = types.FunctionDeclaration(
    name="analyze_pdf",
    description=(
        "Read and extract the text of a PDF document stored in the "
        "uploads folder. Use this whenever the user refers to a report, "
        "policy, statement, or any document by filename and asks you to "
        "summarise, analyse, classify, or answer questions about its "
        "contents. Pass just the filename (for example "
        "'sustainability_report.pdf') and the tool resolves it."
    ),
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "filename": types.Schema(
                type=types.Type.STRING,
                description=(
                    "The PDF filename to read, e.g. "
                    "'sustainability_report.pdf'. A bare filename is "
                    "resolved against the uploads folder."
                ),
            ),
            "max_chars": types.Schema(
                type=types.Type.INTEGER,
                description=(
                    "Maximum characters of text to extract. Defaults to "
                    "12000. Raise it only if a first read was truncated "
                    "and you still need more of the document."
                ),
            ),
        },
        required=["filename"],
    ),
)


# Name -> callable, merged into the agent loop's registry
TOOL_REGISTRY = {
    "analyze_pdf": analyze_pdf,
}

# Everything this module exposes to Gemini
TOOL_DECLARATIONS = [
    ANALYZE_PDF_DECLARATION,
]
