# Groq-Powered Chatbot

A Flask-based chatbot application that uses the Groq API to provide intelligent responses. This chatbot is powered by Llama 3 8B model running on Groq's infrastructure for fast and efficient AI conversations.

## Features

- Web-based chat interface
- Session management to maintain conversation history
- Powered by Groq's fast inference API
- Uses Llama 3 8B model for high-quality responses
- Error handling and graceful degradation

## Prerequisites

1. Python 3.7 or higher
2. A Groq API key (free tier available)

## Setup Instructions

### 1. Get a Groq API Key

1. Visit [Groq Console](https://console.groq.com/)
2. Sign up for a free account
3. Generate an API key from your dashboard

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit the `.env` file and add your Groq API key:
   ```
   GROQ_API_KEY=your_actual_groq_api_key_here
   ```

### 4. Run the Application

```bash
python3 app.py
```

The application will start on `http://localhost:5000`

## Usage

### Web Interface

1. Open your web browser and navigate to `http://localhost:5000`
2. Start chatting with the AI-powered chatbot
3. The chatbot will maintain conversation history during your session
4. Ask questions, get advice, or have general conversations

### Command Line Interface

Alternatively, you can use the command-line version:

```bash
python3 cli_chatbot.py
```

CLI commands:
- `/help` - Show available commands
- `/clear` - Clear conversation history
- `/quit` or `/exit` - Exit the chatbot
- Just type your message to chat!

## Available Models

The chatbot currently uses the `llama3-8b-8192` model. You can modify the model in `app.py` by changing the `model` parameter in the `generate_response()` function. Available models include:

- `llama3-8b-8192` (default)
- `llama3-70b-8192`
- `mixtral-8x7b-32768`
- `gemma-7b-it`

## Configuration

You can modify the following parameters in the `generate_response()` function:

- `temperature`: Controls randomness (0.0 to 1.0)
- `max_tokens`: Maximum response length
- `top_p`: Nucleus sampling parameter

## Error Handling

The application includes error handling for:
- Invalid API keys
- Network connectivity issues
- API rate limits
- Model unavailability

## Troubleshooting

1. **API Key Issues**: Make sure your Groq API key is valid and properly set in the `.env` file
2. **Module Not Found**: Ensure all dependencies are installed with `pip install -r requirements.txt`
3. **Connection Errors**: Check your internet connection and Groq API status

## License

This project is open source and available under the MIT License.