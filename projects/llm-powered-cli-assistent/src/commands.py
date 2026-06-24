from metrics import show_metrics
from storage import save_conversation


def handle_command(
    question,
    history,
    summary
):
    
    # Help command
    if question == "/help":

        print("""
Available Commands

/help   - Show commands
/usage  - Show token usage
/save   - Save conversation
/reset  - Clear memory
/exit   - Exit application
""")

        return True, summary

    # Usage command
    if question == "/usage":

        show_metrics()

        return True, summary

    # Save command
    if question == "/save":

        save_conversation(
            history,
            summary
        )

        print(
            "Conversation Saved"
        )

        return True, summary

    # Reset command
    if question == "/reset":

        history.clear()

        summary = ""

        print(
            "Memory Reset"
        )

        return True, summary

    # Exit command
    if question == "/exit":

        raise SystemExit

    # Not a command
    return False, summary