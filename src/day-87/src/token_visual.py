import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

text = input("Enter text: ")

tokens = encoding.encode(text)

print("\nToken Visualisation:\n")

for i, token_id in enumerate(tokens):
    token_text = encoding.decode([token_id])

    print(
        f"[{i}] "
        f"{repr(token_text)} "
        f"→ ID: {token_id}"
    )