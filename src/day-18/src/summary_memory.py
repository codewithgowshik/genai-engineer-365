from llm import llm 
from models import requests, response

async def summarize_memory(summary , old_messages):
    summary_prompt = f"""
        current_summary : {summary}
        old_messages: {"\n".join(old_messages)}

        Update the summary.
        Keep only important information.
        Be concise.
        """
    request = requests(
        prompt = summary_prompt
    )
    response = await llm(
        request
    )
    return response.answer