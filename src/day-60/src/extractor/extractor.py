from src.tools.pdf_reader import read_pdf
from src.prompts.extraction_prompt import build_extraction_prompt
from src.llm import generate


async def extract(file_path: str) -> str:
    print("=" * 50)
    print("🚀 Starting Extraction Pipeline")
    print("=" * 50)

    # Step 1 - Read PDF
    print("\nReading PDF...")
    text = read_pdf(file_path)
    print(f"PDF Read Successfully")
    print(f"Characters Extracted: {len(text)}")

    # Step 2 - Build Prompt
    print("\nBuilding Prompt...")
    prompt = build_extraction_prompt(text)
    print("Prompt Built Successfully")

    # Step 3 - Send to Gemini
    print("\nSending Prompt to Gemini...")
    response = await generate(prompt)
    print("Response Received")

    print("\nExtraction Complete")
    print("=" * 50)

    return response