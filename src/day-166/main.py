import time
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# 1. Choose the Hugging Face model
MODEL_NAME = "distilgpt2"

# 2. Load the tokenizer
print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# 3. Load the pretrained model
print("Loading model...")
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

# 4. Generate a response
def generate_response(prompt):

    # Convert text into tokens
    inputs = tokenizer(prompt, return_tensors="pt")

    # Measure inference time
    start_time = time.perf_counter()

    # Generate tokens
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=100,
            do_sample=True,
            temperature=0.7,
            pad_token_id=tokenizer.eos_token_id
        )

    end_time = time.perf_counter()

    # Convert generated tokens back into text
    response = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    inference_time = end_time - start_time

    return response, inference_time


# 5. Interactive application
print("\n===== Hugging Face Local AI =====")

while True:

    prompt = input("\nYou: ")

    if prompt.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    response, duration = generate_response(prompt)

    print("\nGenerated response:")
    print(response)

    print(f"\nInference time: {duration:.2f} seconds")