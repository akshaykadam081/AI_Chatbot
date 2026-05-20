import os
from groq import Groq

print("Connecting to Groq...")

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

print("Connected successfully.")
