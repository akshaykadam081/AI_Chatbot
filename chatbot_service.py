from model_loader import client
from config import MODEL_NAME, MAX_TOKENS, TEMPERATURE


def generate_response(message, history):

    messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant."
        }
    ]

    # Keep last 3 turns
    recent_history = history[-3:]

    for item in recent_history:
        print("DEBUG:", item, flush=True)

        role = item.get("role")

        # Gradio gives content like:
        # [{'text': 'hey', 'type': 'text'}]
        content_list = item.get("content", [])

        if content_list and isinstance(content_list, list):
            text = content_list[0].get("text", "")

            messages.append({
                "role": role,
                "content": text
            })

    # Add current user message
    messages.append({
        "role": "user",
        "content": message
    })


    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE
    )

    return response.choices[0].message.content
