"""
API Routes Module

This module contains all the route handlers for the Flask application.
It separates the routing logic from the main application setup.
"""

from flask import jsonify, request
from agent.agent import Agent
from config import DEFAULT_SYSTEM_PROMPT

# Initialize the agent
agent = Agent()

def setup_routes(app):
    """
    Set up all routes for the Flask application.
    
    Args:
        app: The Flask application instance
    """
    
    @app.route("/ping", methods=["GET"])
    def ping():
        """Health check endpoint to verify the server is running."""
        return jsonify({"status": "ok", "message": "Server is running"})

    @app.route("/ask", methods=["POST"])
    def ask():
        """
        Handle chat requests from the frontend.
        
        Expected JSON payload:
        {
            "prompt": "user message",
            "system": "system prompt (optional)",
            "history": [{"role": "user", "content": "..."}, ...]
        }
        """
        try:
            data = request.json
            history = data.get("history", [])
            prompt = data.get("prompt", "")
            system = data.get("system", DEFAULT_SYSTEM_PROMPT)

            # Add system message if it's not already in history
            if not any(msg["role"] == "system" for msg in history):
                history.insert(0, {"role": "system", "content": system})

            # Add the new user message
            history.append({"role": "user", "content": prompt})

            # Get response from agent
            reply = agent.run(history)

            # Add the assistant's response to history
            history.append({"role": "assistant", "content": reply})

            return jsonify({
                "response": reply,
                "history": history
            })
            
        except Exception as e:
            return jsonify({
                "error": str(e)
            }), 500 