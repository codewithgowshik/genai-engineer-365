from llm import generate_text


prompt = "Write the beginning of a story about a young explorer."


top_p_values = [0.1, 0.3, 0.5, 0.7, 0.9, 1.0]


for top_p in top_p_values:

    print("\n" + "=" * 60)
    print(f"TOP-P: {top_p}")
    print("=" * 60)

    output = generate_text(prompt, top_p)

    print(output)