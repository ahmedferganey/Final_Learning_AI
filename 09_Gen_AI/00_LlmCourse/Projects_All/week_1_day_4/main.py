from anthropic import Anthropic
import os
from dotenv import load_dotenv

# ======================
# LOAD ENV
# ======================
load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    raise ValueError("❌ ANTHROPIC_API_KEY is not set")

# ======================
# CLIENT
# ======================
client = Anthropic(api_key=api_key)


def extract_text(response):
    return " ".join(
        block.text for block in response.content
        if block.type == "text"
    )


# ======================
# 1️⃣ First Interaction
# ======================
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=100,
    system="You are a helpful assistant",
    messages=[
        {"role": "user", "content": "Hi! I'm Ed!"}
    ]
)

answer = extract_text(response)

print("Claude response 1️⃣ First Interaction:")
print(answer)
print("-" * 50)


# ======================
# 2️⃣ No Memory Example
# ======================
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=100,
    system="You are a helpful assistant",
    messages=[
        {"role": "user", "content": "What's my name?"}
    ]
)

answer = extract_text(response)

print("Claude response 2️⃣ No Memory Example:")
print(answer)
print("-" * 50)


# ======================
# 3️⃣ With Memory
# ======================
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=100,
    system="You are a helpful assistant",
    messages=[
        {"role": "user", "content": "Hi! I'm Ed!"},
        {"role": "assistant", "content": "Hi Ed! How can I assist you today?"},
        {"role": "user", "content": "What's my name?"}
    ]
)

answer = extract_text(response)

print("Claude response 3️⃣ With Memory:")
print(answer)
print("-" * 50)
