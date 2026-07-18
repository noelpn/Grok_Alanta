from groq import Groq
import gradio as gr
import os

api = Groq(api_key="YOUR_API_KEY_HERE")


def initial_message():
    return [
        {
            "role": "system",
            "content": "You are Alanta AI agent and you are a helpful assistant"
        }
    ]


message = initial_message()


def LLMBot(u_input, history):
    global message

    message.append(
        {
            "role": "user",
            "content": u_input
        }
    )

    response = api.chat.completions.create(
        messages=message,
        model="llama-3.3-70b-versatile"
    )

    reply = response.choices[0].message.content

    message.append(
        {
            "role": "assistant",
            "content": reply
        }
    )

    return reply


demo = gr.ChatInterface(
    fn=LLMBot,
    chatbot=gr.Chatbot(height=300),
    title="Alanta AI Bot",
    textbox=gr.Textbox(placeholder="Ask Alanta..."),
    description="A Friendly chatbot",
    examples=[
        "Hi",
        "Have a great day",
        "I'm feeling lucky"
    ]
)

demo.launch(share=True)
