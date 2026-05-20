import os
from openai import OpenAI

print("Connecting to Together AI...")

client = OpenAI(
    api_key=os.getenv("TOGETHER_API_KEY"),
    base_url="https://api.together.xyz/v1"
)

print("Connected successfully.")
