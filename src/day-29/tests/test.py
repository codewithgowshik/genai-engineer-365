from src.helper import clean_prompt

from src.memory import (
    add_to_history,
    add_assistant_response,
    trim_history
)

from src.storage import (
    save_conversation,
    load_conversation
)

import src.metrics as metrics


# Test that clean_prompt() removes unwanted spaces.
def test_clean_prompt():

    assert clean_prompt("  hello  ") == "hello"


# Test that a user message is added correctly.
def test_add_to_history():

    history = []

    add_to_history(
        history,
        "Hello"
    )

    assert history == [
        "User: Hello"
    ]


# Test that an assistant response is added correctly.
def test_add_assistant_response():

    history = []

    add_assistant_response(
        history,
        "Hello"
    )

    assert history == [
        "Assistant: Hello"
    ]


# Test that trim_history() keeps only the latest 5 messages.
def test_trim_history():

    history = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7"
    ]

    trim_history(history)

    assert history == [
        "3",
        "4",
        "5",
        "6",
        "7"
    ]


# Test that token estimation returns the expected number of tokens.
def test_estimate_tokens():

    tokens = metrics.estimate_tokens(
        "HelloWorld"
    )

    assert tokens == 2


# Test that calculate_cost() returns the correct total cost.
def test_calculate_cost():

    cost = metrics.calculate_cost(
        1000,
        1000
    )

    assert cost == 0.0005


# Test that update_metrics() updates all session metrics correctly.
def test_update_metrics():

    previous_input = metrics.total_input_tokens
    previous_output = metrics.total_output_tokens
    previous_cost = metrics.total_cost

    metrics.update_metrics(
        100,
        50,
        25
    )

    assert metrics.total_input_tokens == previous_input + 100

    assert metrics.total_output_tokens == previous_output + 50

    assert metrics.total_cost == previous_cost + 25


# Test that save_conversation() and load_conversation() preserve the same data.
def test_save_and_load_conversation():

    history = [
        "User: Hi",
        "Assistant: Hello"
    ]

    summary = "Test Summary"

    save_conversation(
        history,
        summary
    )

    loaded_history, loaded_summary = load_conversation()

    assert loaded_history == history

    assert loaded_summary == summary
