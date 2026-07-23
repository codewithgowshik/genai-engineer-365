import sys
from urllib.parse import urlparse

from rich.console import Console, Group
from rich.markdown import Markdown
from rich.panel import Panel
from rich.text import Text


# ---------------------------------------------------------------
# Windows console safety
#
# The default Windows codepage (cp1252) cannot encode emoji, and a
# UnicodeEncodeError here would bubble up and look like an API
# failure. Try UTF-8 first, then fall back to ASCII glyphs.
# ---------------------------------------------------------------
def _enable_utf8():
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except Exception:
            pass


_enable_utf8()


def _supported(glyph: str) -> bool:
    encoding = getattr(sys.stdout, "encoding", None) or "ascii"
    try:
        glyph.encode(encoding)
        return True
    except Exception:
        return False


_FANCY = _supported("🔧🌐🔎✅")

TOOL_ICON = "🔧" if _FANCY else "[>]"
WEB_ICON = "🌐" if _FANCY else "[~]"
FOUND_ICON = "🔎" if _FANCY else "[#]"
DONE_ICON = "✅" if _FANCY else "[OK]"
WARN_ICON = "⚠" if _FANCY else "[!]"

console = Console()


# ---------------------------------------------------------------
# Spinners
# ---------------------------------------------------------------
def thinking(label: str = "Thinking..."):
    # Shown while Gemini is deciding what to do next
    return console.status(f"[bold magenta]{label}[/]", spinner="dots")


def searching_web(query: str = ""):
    # Shown while a search tool is actually executing
    spinner = "earth" if _FANCY else "line"

    if query:
        label = f'{WEB_ICON} Searching the web for [italic]"{query}"[/]'
    else:
        label = f"{WEB_ICON} Searching the web..."

    return console.status(f"[bold cyan]{label}[/]", spinner=spinner)


# ---------------------------------------------------------------
# Agent step rendering
# ---------------------------------------------------------------
def tool_call(step: int, name: str, args: dict):
    """Render the model's decision to call a tool."""

    body = Text()
    body.append(f"{name}", style="bold yellow")
    body.append("(\n")

    for key, value in (args or {}).items():
        body.append(f"    {key}", style="cyan")
        body.append(" = ")
        body.append(f"{value!r}\n", style="green")

    body.append(")")

    console.print(
        Panel(
            body,
            title=f"[bold]{TOOL_ICON} Step {step} · Tool Call[/]",
            title_align="left",
            border_style="yellow",
            padding=(0, 2),
        )
    )


def tool_result(name: str, result: dict):
    """Render what came back from the tool."""

    # Tool failed — surface it rather than hiding it
    if isinstance(result, dict) and result.get("error"):
        console.print(
            Panel(
                Text(str(result["error"]), style="red"),
                title=f"[bold]{WARN_ICON} {name} failed[/]",
                title_align="left",
                border_style="red",
                padding=(0, 2),
            )
        )
        return

    results = (result or {}).get("results") or []

    if not results:
        console.print("[dim]  no results returned[/]\n")
        return

    lines = []

    for index, item in enumerate(results, start=1):
        title = (item.get("title") or "Untitled").strip()
        url = item.get("url") or ""

        # Show the domain — it's the useful part at a glance
        domain = urlparse(url).netloc.replace("www.", "") if url else ""

        line = Text()
        line.append(f"{index}. ", style="dim")
        line.append(title, style="bold white")

        if domain:
            line.append(f"  ({domain})", style="dim cyan")

        lines.append(line)

    console.print(
        Panel(
            Group(*lines),
            title=f"[bold]{FOUND_ICON} {len(results)} sources found[/]",
            title_align="left",
            border_style="cyan",
            padding=(0, 2),
        )
    )


def final_answer(text: str):
    """Render the model's final response as markdown."""

    console.print(
        Panel(
            Markdown(text),
            title=f"[bold]{DONE_ICON} Answer[/]",
            title_align="left",
            border_style="green",
            padding=(1, 2),
        )
    )


def notice(message: str):
    console.print(f"[dim]{message}[/]")
