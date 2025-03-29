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

## 🔍 Testing

Run the test suite:
```bash
pytest tests/
```

## 📡 API Examples

### Health Check
```bash
curl http://localhost:5000/ping
```

### Chat with the Agent
```bash
curl -X POST http://localhost:5000/ask \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "What is the capital of France?",
    "system": "You are a helpful geography expert.",
    "history": []
  }'
```

### Multi-turn Conversation
```bash
curl -X POST http://localhost:5000/ask \
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
OPENAI_API_KEY=your-api-key-here
OPENAI_MODEL=gpt-3.5-turbo

# Flask Configuration
FLASK_HOST=0.0.0.0
FLASK_PORT=5000
FLASK_DEBUG=True
```

## 📝 License

MIT License - feel free to use this project for your own purposes.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request 