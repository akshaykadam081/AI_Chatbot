# AI Chatbot using Llama 2

I built this project to understand how a real-world AI chatbot works end-to-end — from loading a Large Language Model (LLM) to creating an interactive chatbot UI.

This project uses **Llama 2** for response generation and **Gradio** for the chatbot interface. I also tried to organize the logic into separate files to better understand how a modular Python project is structured.

## Features

- Load and run Llama 2 model using Hugging Face Transformers
- Generate AI-based conversational responses
- Maintain chat history for better conversation flow
- Interactive Gradio chatbot UI
- Modular project structure for easy understanding and maintenance

---

## Project Structure

```text
chatbot_project/
│
├── app.py
├── config.py
├── model_loader.py
├── chatbot_service.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Project Flow (File-wise Execution)

1. app.py → Starts Gradio UI, accepts user input, and connects frontend with chatbot backend  

2. chatbot_service.py → Builds conversation prompt, manages chat history, and generates chatbot response  

3. model_loader.py → Loads Llama 2 model, tokenizer, and device configuration (CPU/GPU)  

4. config.py → Stores model name and generation settings like temperature and max tokens  

---

## Technologies Used

- Python
- Hugging Face Transformers
- Llama 2
- PyTorch
- Gradio

---

## Setup

Install required packages:

```bash
pip install -r requirements.txt
```

Set Hugging Face token securely:

```python
from getpass import getpass
import os

os.environ["HF_TOKEN"] = getpass("Enter HF token: ")
```

Run the application:

```bash
python app.py
```

---

## Learning Outcome

Through this project, I learned how to:

- Load and use pre-trained LLMs
- Build prompt-based chatbot logic
- Handle multi-turn conversation history
- Create modular Python project structure
- Build and deploy simple AI applications