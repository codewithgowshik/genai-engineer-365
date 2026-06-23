import json


# Save history and summary to a JSON file
def save_conversation(
    history,
    summary
):

    # Create a dictionary
    data = {
        "history": history,
        "summary": summary
    }

    # Open conversation.json in write mode
    with open(
        "conversation.json",
        "w"
    ) as file:

        # Convert dictionary to JSON and store it
        json.dump(
            data,
            file,
            indent=4
        )


# Load conversation from JSON file
def load_conversation():

    try:

        # Open conversation.json in read mode
        with open(
            "conversation.json",
            "r"
        ) as file:

            # Convert JSON into a Python dictionary
            data = json.load(
                file
            )

            # Return history and summary
            return (
                data["history"],
                data["summary"]
            )

    # First run: file does not exist
    except FileNotFoundError:

        # Start with empty memory
        return [], ""