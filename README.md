# Local AI Chatbot & Voice Assistant

This project is a Django-powered web application that provides a real-time chat and voice interface to interact with local Large Language Models (LLMs) running via Ollama. It uses Django Channels for WebSocket communication to deliver a seamless, streaming chat experience.

![Chatbot UI](https://user-images.githubusercontent.com/your-username/your-repo/your-image-link.png) <!-- It's recommended to add a screenshot of your application here -->

## Key Features

- **Real-Time Chat**: Engage in live conversations with a local AI model.
- **Streaming Responses**: AI responses are streamed token-by-token, creating a dynamic "typing" effect.
- **Voice-to-Text**: Use your microphone to speak your prompts, which are transcribed and sent to the AI.
- **Text-to-Speech**: The AI's text responses are spoken back to you using the browser's built-in speech synthesis.
- **Local First**: All AI processing is done on your local machine via Ollama, ensuring privacy and offline capability.
- **Modern UI**: A clean, responsive, and visually appealing user interface built with HTML, CSS, and JavaScript.

## Technology Stack

- **Backend**:
  - [Django](https://www.djangoproject.com/): The web framework for building the application.
  - [Django Channels](https://channels.readthedocs.io/en/latest/): Enables WebSocket support for real-time communication.
  - [Daphne](https://github.com/django/daphne): The ASGI server required to run Django Channels.
- **AI & Machine Learning**:
  - [Ollama](https://ollama.ai/): Runs large language models locally.
  - [LangChain](https://www.langchain.com/): A framework for developing applications powered by language models.
- **Frontend**:
  - HTML5
  - CSS3
  - JavaScript (for WebSocket handling, DOM manipulation, and voice features)

## Prerequisites

Before you begin, ensure you have the following installed on your system:

1.  **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
2.  **Ollama**: You must have Ollama installed and running. [Download Ollama](https://ollama.ai/)
3.  **A Local LLM**: You need to have at least one model pulled from Ollama. For example, to get `Llama 3.1`:
    ```bash
    ollama pull llama3.1:8b
    ```

## Setup and Installation

Follow these steps to get your development environment set up:

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2.  **Create and Activate a Virtual Environment**
    - On Windows:
      ```bash
      python -m venv venv
      .\venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

3.  **Install Dependencies**
    Install all the required Python packages from the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply Database Migrations**
    This will set up the necessary database tables for the Django application.
    ```bash
    python manage.py migrate
    ```

## How to Run the Application

Because this project uses WebSockets, you need to run it using an ASGI server (Daphne), not the standard Django development server.

1.  **Ensure Ollama is Running**: Open your terminal or command prompt and make sure the Ollama service is active.

2.  **Start the Daphne Server**:
    Run the following command from the root of the project directory:
    ```bash
    daphne -p 8000 core.asgi:application
    ```

3.  **Access the Application**:
    Open your web browser and navigate to:
    [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

You should now see the AI Hub interface and be able to start a conversation.

## Project Structure

```
/
├── chatbot/            # Django app for handling chat logic and WebSocket consumers.
├── core/               # Core Django project settings, ASGI/WSGI config, and routing.
├── templates/          # Contains the main index.html for the frontend.
├── voice_assistant/    # Django app for handling voice input/output.
├── db.sqlite3          # SQLite database file.
├── manage.py           # Django's command-line utility.
├── requirements.txt    # List of Python dependencies.
└── README.md           # This file.
```
