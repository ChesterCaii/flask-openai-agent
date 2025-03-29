# 🧠 Flask + OpenAI Agent Starter

A production-ready starter kit for building AI-powered chat applications using Flask and OpenAI's API. Perfect for hackathons, research projects, or building your own AI-powered SaaS tools.

## 🚀 Features
- 🧠 OpenAI integration with conversation history support
- 🔄 RESTful API with CORS enabled
- 🎨 Modern, responsive frontend
- ⚙️ Configurable through environment variables
- 🧪 Health check endpoint
- 📝 Comprehensive documentation and examples
- 🧪 Unit tests included

## ⚠️ Security Note
**IMPORTANT**: Never commit your actual OpenAI API key to version control. Always use environment variables and keep your `.env` file in your `.gitignore`. The `.env.example` file contains placeholder values only.

## 🛠 Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flask-openai-agent.git
   cd flask-openai-agent
   ```

2. Set up your environment:
   ```bash
   # Create and activate virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

   # Install dependencies
   pip install -r requirements.txt

   # Set up environment variables
   cp .env.example .env
   ```

3. Edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

4. Run the application:
   ```bash
   # Terminal 1: Start the Flask server
   python app.py

   # Terminal 2: Start the frontend server
   python server.py
   ```

5. Open http://localhost:8000 in your browser

> **Note**: On macOS, port 5000 is often used by AirPlay. The application defaults to port 5001 to avoid conflicts. If you need to use a different port, update the `FLASK_PORT` in your `.env` file.

## 🔍 Testing

Run the test suite:
```bash
pytest tests/
```

## 📡 API Examples

### Health Check
```bash
curl http://localhost:5001/ping
```

### Chat with the Agent
```bash
curl -X POST http://localhost:5001/ask \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "What is the capital of France?",
    "system": "You are a helpful geography expert.",
    "history": []
  }'
```

### Multi-turn Conversation
```bash
curl -X POST http://localhost:5001/ask \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Tell me more about that.",
    "history": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "What is Python?"},
      {"role": "assistant", "content": "Python is a programming language."}
    ]
  }'
```

## 🎯 Use Cases

### 🤖 AI Chatbots
- Customer support automation
- FAQ bots
- Lead qualification
- Appointment scheduling

### 📚 Educational Tools
- **Student Assistant**: Create an AI tutor that explains complex topics step-by-step
  ```json
  {
    "system": "You are a patient and knowledgeable tutor. Break down complex topics into simple steps, use examples, and check for understanding.",
    "prompt": "Can you explain quantum computing in simple terms?"
  }
  ```
- Interactive problem-solving guides
- Homework help systems
- Language learning companions

### 🔍 Research & Analysis
- **Research Summarizer**: Build an AI that answers questions about uploaded papers
  ```json
  {
    "system": "You are a research assistant. Analyze papers and provide concise, accurate summaries. Always cite specific sections.",
    "prompt": "What are the key findings about climate change in this paper?"
  }
  ```
- Literature review assistants
- Data analysis interpreters
- Citation generators

### 💼 SaaS Support
- **AI Support Agent**: Create a 24/7 support system for your SaaS product
  ```json
  {
    "system": "You are a technical support specialist for [Your Product]. Help users troubleshoot issues, explain features, and provide best practices.",
    "prompt": "How do I integrate the API with my application?"
  }
  ```
- Feature guides
- Troubleshooting assistants
- Onboarding helpers

## 📁 Project Structure
```
flask-openai-agent/
├── agent/             # OpenAI agent implementation
│   ├── __init__.py
│   └── agent.py
├── api/              # API routes and handlers
│   ├── __init__.py
│   └── routes.py
├── frontend/         # Frontend assets
│   └── index.html
├── tests/           # Test suite
│   └── test_api.py
├── app.py           # Main application entry point
├── config.py        # Configuration management
├── requirements.txt # Python dependencies
└── .env.example     # Environment variables template
```

## 🔧 Configuration

The application can be configured through environment variables in `.env`:

```env
# OpenAI Configuration
OPENAI_API_KEY=your-api-key-here  # Get your API key from https://platform.openai.com/api-keys
OPENAI_MODEL=gpt-3.5-turbo       # Default model to use (gpt-3.5-turbo or gpt-4)

# Flask Configuration
FLASK_HOST=0.0.0.0               # Use 127.0.0.1 for local-only access
FLASK_PORT=5001                  # Port for the Flask API server (5000 is often used by AirPlay on macOS)
FLASK_DEBUG=True                 # Set to False in production

# Frontend Configuration (optional)
FRONTEND_PORT=8000               # Port for the frontend server
```

## 📝 License

MIT License - feel free to use this project for your own purposes.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request 