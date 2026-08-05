def build_extraction_prompt(document_text: str) -> str:
    """
    Builds a prompt for Gemini to extract structured sustainability
    information from a document.

    Args:
        document_text (str): The extracted text from the PDF.

    Returns:
        str: A complete prompt ready to send to the LLM.
    """

    prompt = f"""
You are an expert Sustainability and ESG Analyst.

Your task is to analyse the following sustainability report and extract the requested information.

Extract the following fields:

- Company Name
- Industry
- Country
- Report Year
- Revenue
- Number of Employees
- Carbon Reduction Target
- Net Zero Target
- Renewable Energy Percentage

Rules:

1. Return ONLY valid JSON.
2. Do NOT explain your reasoning.
3. If a value is missing, return null.
4. Do NOT invent information.
5. Use exactly these field names:

{{
    "company_name": "",
    "industry": "",
    "country": "",
    "report_year": "",
    "revenue": "",
    "employees": "",
    "carbon_reduction_target": "",
    "net_zero_target": "",
    "renewable_energy_percentage": ""
}}

Document:

-------------------------

{document_text}

-------------------------
"""

    return prompt