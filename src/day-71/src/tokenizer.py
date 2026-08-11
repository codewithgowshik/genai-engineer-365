import tiktoken


def count_tokens(text):
    encoding = tiktoken.get_encoding("cl100k_base")
    tokens = encoding.encode(text)

    return tokens


text = input("Enter some text: ")

tokens = count_tokens(text)

print("\nOriginal text:")
print(text)

print("\nToken IDs:")
print(tokens)

print("\nToken count:")
print(len(tokens))

print("\nWord count:")
print(len(text.split()))
