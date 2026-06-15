# this functions are used to store the data from the user questions and ai response
history = []


def add_to_history(
    history,
    question
):

    history.append(
        f"User: {question}"
    )


def add_assistant_response(
    history,
    answer
):

    history.append(
        f"Assistant: {answer}"
    )