from llm import generate_text


prompt = """
Write a short story about a student who discovers a mysterious door
inside an old university building.
"""


temperatures = [0.0, 0.25, 0.5, 0.75, 1.0]

for temperature in temperatures:
    print("\n" + "=" * 60)
    print(f"TEMPERATURE: {temperature}")
    print("=" * 60)

    output = generate_text(prompt, temperature)

    print(output)