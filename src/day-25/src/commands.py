from metrics import show_metrics
from storage import save_conversation
from personas import PERSONAS

def handle_command(
    question,
    history,
    summary,
    current_profile
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

        return True, summary,current_profile

    # Usage command
    if question == "/usage":

        show_metrics()

        return True, summary,current_profile

    # Save command
    if question == "/save":

        save_conversation(
            history,
            summary,
            current_profile
        )

        print(
            "Conversation Saved"
        )

        return True, summary,current_profile

    # Reset command
    if question == "/reset":

        history.clear()

        summary = ""

        print(
            "Memory Reset"
        )

        return True, summary,current_profile
    if question.startswith("/profile"):
        profile = question.replace(
            "/profile",
            "").strip().lower()
        if profile in PERSONAS:
            print(f"profile changed to..{profile}")
            return(
                True,
                summary,
                PERSONAS[profile]
            )
        print("profile not found...")
        return(True,
               summary,
               current_profile)
    # Exit command
    if question == "/exit":

        raise SystemExit

    # Not a command
    return False, summary, current_profile