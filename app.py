"""
Flask OpenAI Agent

A simple Flask application that provides a chat interface to OpenAI's API.
This application serves as a starter kit for building AI-powered chat applications.
"""

import os
from flask import Flask
from flask_cors import CORS
from api.routes import setup_routes
from config import FLASK_HOST, FLASK_PORT, FLASK_DEBUG

def create_app():
    """
    Create and configure the Flask application.
    
    Returns:
        Flask: The configured Flask application
    """
    app = Flask(__name__)
    
    # Enable CORS for all routes
    CORS(app)
    
    # Set up routes
    setup_routes(app)
    
    # Error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return {"error": "Not found"}, 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return {"error": "Internal server error"}, 500
    
    return app

def main():
    """Main entry point for the application."""
    # Check for required environment variables
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable is not set")
        print("Please copy .env.example to .env and add your OpenAI API key")
        return
    
    app = create_app()
    
    # Run the application
    app.run(
        host=FLASK_HOST,
        port=FLASK_PORT,
        debug=FLASK_DEBUG
    )

if __name__ == "__main__":
    main() 