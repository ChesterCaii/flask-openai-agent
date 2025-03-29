# Flask OpenAI Agent Starter Kit

A production-ready starter kit for building AI-powered chat applications using Flask and OpenAI's API.

## Features
- 🧠 OpenAI integration with conversation history support
- 🔄 RESTful API with CORS enabled
- 🎨 Modern, responsive frontend
- ⚙️ Configurable through environment variables
- 🧪 Health check endpoint
- 📝 Comprehensive documentation

## Project Structure
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
├── app.py           # Main application entry point
├── config.py        # Configuration management
├── requirements.txt # Python dependencies
└── .env.example     # Environment variables template
```

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flask-openai-agent.git
   cd flask-openai-agent
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your OpenAI API key and any other custom settings.

## Running the Application

1. Start the Flask server:
   ```bash
   python app.py
   ```

2. In a separate terminal, start the frontend server:
   ```bash
   python server.py
   ```

3. Open your browser and navigate to:
   ```
   http://localhost:8000
   ```

## API Endpoints

- `GET /ping`: Health check endpoint
- `POST /ask`: Chat endpoint
  ```json
  {
    "prompt": "Your message here",
    "system": "Optional system prompt",
    "history": [] // Optional conversation history
  }
  ```

## Development

- The application uses Flask's debug mode by default
- CORS is enabled for all routes
- Frontend is served on port 8000
- Backend API runs on port 5000

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License - feel free to use this project for your own purposes. 