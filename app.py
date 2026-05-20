import gradio as gr
from chatbot_service import generate_response


def chatbot(message, history):
    return generate_response(message, history)


demo = gr.ChatInterface(
    fn=chatbot,
    title="AI Chatbot",
    description="Together AI powered chatbot"
)

demo.launch(share=True)
