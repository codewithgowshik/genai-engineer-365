# Session metrics

total_input_tokens = 0

total_output_tokens = 0

total_cost = 0

INPUT_COST_PER_1K = 0.0001

OUTPUT_COST_PER_1K = 0.0004


def estimate_tokens(
    text
):
    # 1 token = 4char
    return len(
        text
    ) // 4


def calculate_cost(
    input_tokens,
    output_tokens
):

    input_cost = (
        input_tokens / 1000
    ) * INPUT_COST_PER_1K

    output_cost = (
        output_tokens / 1000
    ) * OUTPUT_COST_PER_1K

    return (
        input_cost
        +
        output_cost
    )


def update_metrics(
    input_tokens,
    output_tokens,
    cost
):

    global total_input_tokens

    global total_output_tokens

    global total_cost

    total_input_tokens += (
        input_tokens
    )

    total_output_tokens += (
        output_tokens
    )

    total_cost += (
        cost
    )


def show_metrics():

    print()

    print(
        f"Input Tokens : {total_input_tokens}"
    )

    print(
        f"Output Tokens: {total_output_tokens}"
    )

    print(
        f"Total Tokens : {total_input_tokens + total_output_tokens}"
    )

    print(
        f"Total Cost   : ${total_cost:.6f}" #  used to display the decimal value in 6 digit.
    )

    print()