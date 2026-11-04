import requests

OLLAMA_URL = "http://localhost:11434/api/chat"

def ask_qwen(question):

    payload = {
        "model": "qwen3.5:9b",
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ],
        "stream": False
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload
    )

    response.raise_for_status()

    result = response.json()

    return result["message"]["content"]


question = input("Ask Qwen: ")

answer = ask_qwen(question)

print("\nQwen:", answer)