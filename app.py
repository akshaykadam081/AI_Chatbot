import gradio as gr
from chatbot_service import generate_response


def chatbot(message, history):
    response = generate_response(message, history)
    return response


demo = gr.ChatInterface(
    fn=chatbot,
    title="AI Chatbot",
    description="Llama 2 powered chatbot"
)

demo.launch()