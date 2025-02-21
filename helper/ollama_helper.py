import requests
import sys
import json
from dotenv import load_dotenv
import os

load_dotenv()


def generate_response_stream(prompt):
    response = requests.post('http://localhost:11434/api/generate',
                             json={
                                 "model": os.getenv("LLM_MODEL_NAME"),
                                 "prompt": prompt,
                                 "stream": True
                             },
                             stream=True)

    for line in response.iter_lines():
        if line:
            chunk = line.decode('utf-8')
            data = json.loads(chunk)  # Parse JSON correctly
            if 'response' in data:
                yield data['response']


def generate_response(prompt):
    response = requests.post('http://localhost:11434/api/generate',
                             json={
                                 "model": os.getenv("LLM_MODEL_NAME"),
                                 "prompt": prompt
                             })

    full_response = ""
    for line in response.text.splitlines():
        try:
            data = json.loads(line)
            if 'response' in data:
                full_response += data['response']
        except json.JSONDecodeError:
            # Skip lines that aren't valid JSON
            continue

    return full_response


def print_streaming_response(prompt):
    for chunk in generate_response_stream(prompt):
        sys.stdout.write(chunk)
        sys.stdout.flush()
    print()  # New line at the end of the response


if __name__ == "__main__":
    # Typing like response
    prompt = "Explain the concept of Retrieval Augmented Generation in one sentence."
    print("AI: ", end="", flush=True)
    print_streaming_response(prompt)

    # Full response all at once
    prompt = "Explain the concept of Retrieval Augmented Generation in one sentence."
    print(generate_response(prompt))
