import asyncio

from google.genai import types

import agentic_ui as ui
from config import client
from logger_config import logger
from metrics import calculate_cost, estimate_tokens, update_metrics
from models import requests, response
from prompts.system_prompts import SYSTEM_PROMPT
from tools.web_search import TOOL_DECLARATIONS, TOOL_REGISTRY

# Safety net so a model that keeps calling tools can't loop forever
MAX_TOOL_STEPS = 6


def _build_config():
    """Expose our tools, but tell the SDK NOT to call them for us."""

    return types.GenerateContentConfig(
        tools=[
            types.Tool(function_declarations=TOOL_DECLARATIONS)
        ],
        # This is what switches automatic -> manual tool calling.
        # Without it the SDK executes the function behind our back
        # and we never see the individual steps.
        automatic_function_calling=types.AutomaticFunctionCallingConfig(
            disable=True
        ),
    )


async def _execute_tool(name, args):
    """Run one tool the model asked for, and never raise."""

    function = TOOL_REGISTRY.get(name)

    if function is None:
        logger.error(f"Model requested unknown tool: {name}")
        return {"error": f"Unknown tool: {name}"}

    try:
        # Tavily's client is blocking, so keep the event loop free
        return await asyncio.to_thread(function, **args)

    except Exception as error:
        logger.error(f"Tool '{name}' failed: {error}")

        # Hand the failure back to the model instead of crashing —
        # it can then apologise or answer from its own knowledge.
        return {"error": f"{type(error).__name__}: {error}"}


def _record_usage(api_response, prompt_text, answer_text):
    """Prefer real token counts, fall back to the estimate."""

    usage = getattr(api_response, "usage_metadata", None)

    if usage and usage.prompt_token_count is not None:
        input_tokens = usage.prompt_token_count
        output_tokens = usage.candidates_token_count or 0

    else:
        input_tokens = estimate_tokens(prompt_text)
        output_tokens = estimate_tokens(answer_text)

    update_metrics(
        input_tokens,
        output_tokens,
        calculate_cost(input_tokens, output_tokens),
    )


def _split_parts(candidate):
    """Separate a candidate's parts into tool calls and plain text."""

    calls = []
    text = ""

    content = getattr(candidate, "content", None)

    for part in getattr(content, "parts", None) or []:

        if getattr(part, "function_call", None):
            calls.append(part.function_call)

        elif getattr(part, "text", None):
            text += part.text

    return calls, text


async def _agent_loop(full_prompt, model, show_output):
    """Drive the model/tool conversation until it produces an answer."""

    config = _build_config()

    # The running transcript we resend on every turn
    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=full_prompt)],
        )
    ]

    for step in range(1, MAX_TOOL_STEPS + 1):

        with ui.thinking():
            api_response = await client.aio.models.generate_content(
                model=model,
                contents=contents,
                config=config,
            )

        if not api_response.candidates:
            return "Gemini returned no response."

        candidate = api_response.candidates[0]
        calls, text = _split_parts(candidate)

        _record_usage(api_response, full_prompt, text)

        # No tool requested -> this is the final answer
        if not calls:
            logger.info(f"Answer produced after {step - 1} tool call(s)")
            return text

        # Keep the model's tool-call turn in the transcript, otherwise
        # the function responses below have nothing to attach to.
        contents.append(candidate.content)

        response_parts = []

        for call in calls:

            args = dict(call.args or {})

            if show_output:
                ui.tool_call(step, call.name, args)

            # Show the spinner while the tool actually runs
            if show_output and call.name == "search_web":
                with ui.searching_web(args.get("query", "")):
                    result = await _execute_tool(call.name, args)
            else:
                result = await _execute_tool(call.name, args)

            if show_output:
                ui.tool_result(call.name, result)

            response_parts.append(
                types.Part.from_function_response(
                    name=call.name,
                    response=result,
                )
            )

        # Feed every tool result back so the model can continue
        contents.append(
            types.Content(
                role="user",
                parts=response_parts,
            )
        )

    logger.error(f"Hit MAX_TOOL_STEPS ({MAX_TOOL_STEPS}) without an answer")

    return "I used too many tool steps without reaching an answer."


async def llm(
    request: requests,
    model: str = "gemini-2.5-flash",
    show_output: bool = True,
):
    # Retry up to 3 times
    for attempt in range(3):

        try:

            logger.info("Sending request to Gemini...")

            # Combine system prompt with user prompt
            full_prompt = (
                f"{SYSTEM_PROMPT}\n\n"
                f"{request.prompt}"
            )

            answer = await _agent_loop(
                full_prompt,
                model,
                show_output,
            )

            logger.info("Response received successfully")

            if show_output and answer:
                ui.final_answer(answer)

            return response(answer=answer)

        except Exception as error:

            logger.error(f"Attempt {attempt + 1} failed: {error}")

            # Wait before retrying
            await asyncio.sleep(2)

    return response(
        answer="Unable to get response from Gemini."
    )
