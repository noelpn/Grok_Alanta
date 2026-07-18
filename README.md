# Grok_Alanta
Alanta AI Chatbot

Alanta AI Chatbot is a simple and user-friendly conversational AI application built with Groq and Gradio. It provides a clean web interface where users can interact with an AI assistant in real time.

Features

- AI-powered chatbot using the Groq API
- Simple and responsive Gradio interface
- Easy to set up and run
- Lightweight project structure
- Suitable for learning and experimentation

---

Project Structure

.
├── main.py
├── requirements.txt
└── README.md

«Note: The entire chatbot implementation is contained in "main.py".»

---

Requirements

- Python 3.9 or later
- Groq API Key

---

Installation

1. Clone the repository

git clone https://github.com/yourusername/alanta-ai-chatbot.git
cd alanta-ai-chatbot

2. Install dependencies

pip install -r requirements.txt

Or install manually:

pip install groq gradio

---

Configure the Groq API Key

Set your Groq API key before running the application.

Linux/macOS

export GROQ_API_KEY="your_api_key"

Windows (Command Prompt)

set GROQ_API_KEY=your_api_key

Windows (PowerShell)

$env:GROQ_API_KEY="your_api_key"

---

Run the Chatbot

Start the application with:

python main.py

Gradio will generate a local URL similar to:

http://127.0.0.1:7860

Open the URL in your browser and start chatting with Alanta AI.

---

Technologies Used

- Python
- Groq API
- Gradio

---

Future Improvements

- Conversation history
- Multiple AI models
- Dark mode
- Streaming responses
- Chat export
- User authentication
- Voice input and output

---

License

This project is licensed under the MIT License.

---

Author

Developed by Noel PN
