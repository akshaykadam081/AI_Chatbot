import torch
from model_loader import tokenizer, model, device
from config import MAX_NEW_TOKENS, TEMPERATURE, TOP_P


def generate_response(message, history):
    
    prompt = ""

    for user_msg, bot_msg in history:
        prompt += f"User: {user_msg}\nAssistant: {bot_msg}\n"

    prompt += f"User: {message}\nAssistant:"

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        padding=True,
        truncation=True
    ).to(device)

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=MAX_NEW_TOKENS,
            temperature=TEMPERATURE,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )

    decoded = tokenizer.decode(
        output[0],
        skip_special_tokens=True
    )

    response = decoded.split("Assistant:")[-1].strip()

    return response