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

#trim history and implementing the context window 
def trim_history(history , max_messages=5):
    if len(history) > max_messages:
        history[:] = history[-max_messages:]