from rich.console import Console

console = Console()


def searching_web():
    return console.status(
        "[bold cyan]🌐 Searching the web...[/]",
        spinner="earth"
    )