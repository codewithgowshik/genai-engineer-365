from google import genai
from google.genai import types
from config import GEMINI_API_KEY, MODEL_NAME
import math


client = genai.Client(api_key=GEMINI_API_KEY)

prompt = "The capital of France is"


response = client.models.generate_content(
    model=MODEL_NAME,
    contents=prompt,
    config=types.GenerateContentConfig(
        temperature=0.0,
        response_logprobs=True,
        logprobs=5,
        max_output_tokens=20,
    ),
)


print("=" * 60)
print("GENERATED RESPONSE")
print("=" * 60)

print(response.text)


candidate = response.candidates[0]

print("\n" + "=" * 60)
print("AVERAGE LOGPROB")
print("=" * 60)

print(candidate.avg_logprobs)


print("\n" + "=" * 60)
print("CHOSEN TOKENS")
print("=" * 60)

logprobs_result = candidate.logprobs_result

for token in logprobs_result.chosen_candidates:

    probability = math.exp(token.log_probability)

    print(f"Token: {token.token!r}")
    print(f"Logprob: {token.log_probability:.6f}")
    print(f"Probability: {probability:.2%}")
    print()