"""
Flask OpenAI Agent

A simple Flask application that provides a chat interface to OpenAI's API.
This application serves as a starter kit for building AI-powered chat applications.
"""

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
    
    return app

def main():
    """Main entry point for the application."""
    app = create_app()
    
    # Run the application
    app.run(
        host=FLASK_HOST,
        port=FLASK_PORT,
        debug=FLASK_DEBUG
    )

if __name__ == "__main__":
    main() 