# AI Agent Starter

This is a minimal Flask-based agent server using OpenAI's API. Built as a hackathon-ready base for AI tools.

## Features
- Flask backend with `/ask` endpoint
- Agent logic using OpenAI Chat API
- Simple HTML frontend for testing

## Setup
1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

2. Set OpenAI API key:
   ```bash
   export OPENAI_API_KEY=your-key-here
   ```

3. Run the server:
   ```bash
   python api/app.py
   ```

## Demo
Once the server is running, open `frontend/index.html` in your browser to interact with the agent. 