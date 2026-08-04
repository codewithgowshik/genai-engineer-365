def build_extraction_prompt(document_text: str) -> str:
    """
    Build a prompt for extracting structured sustainability
    information from a document.

    Args:
        document_text (str): Text extracted from the PDF.

    Returns:
        str: Prompt ready to send to Gemini.
    """

    prompt = f"""
You are an expert Sustainability and ESG Analyst.

Your task is to analyse the sustainability report provided below and extract the requested information.

Return ONLY valid JSON.

The JSON must contain exactly these fields:

{{
    "company_name": null,
    "industry": null,
    "country": null,
    "report_year": null,
    "revenue": null,
    "employees": null,
    "carbon_reduction_target": null,
    "net_zero_target": null,
    "renewable_energy_percentage": null
}}

Rules:

1. Return ONLY valid JSON.
2. Do NOT include markdown.
3. Do NOT include explanations.
4. Do NOT include code blocks.
5. Do NOT invent information.
6. If a field is not available, return null.
7. Keep the same field names.
8. report_year must be an integer.
9. employees must be an integer.
10. renewable_energy_percentage must be a number.

Document:

-----------------------------
{document_text}
-----------------------------
"""

    return prompt