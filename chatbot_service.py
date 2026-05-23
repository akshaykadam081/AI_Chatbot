from model_loader import client
from config import MODEL_NAME, MAX_TOKENS, TEMPERATURE


def generate_response(message, history):

    print(message+"***1")
    messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant."
        }
    ]
    
    prompt = ""
    # Only keep last 3 turns → saves tokens
    recent_history = history[-3:]

    for item in recent_history:
        print("DEBUG:", item)
        if isinstance(item, dict):
            print(message+"####")
            messages.append(item)
            
            
    print(messages+"####2222") 
    messages.append({"role": "user", "content": message})

    print(messages+"####3333") 
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE
    )

    return response.choices[0].message.content
