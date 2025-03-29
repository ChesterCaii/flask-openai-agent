"""
Configuration Module

This module handles all configuration settings for the application,
loading them from environment variables with sensible defaults.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

# Flask Configuration
FLASK_HOST = os.getenv("FLASK_HOST", "0.0.0.0")
FLASK_PORT = int(os.getenv("FLASK_PORT", "5001"))  # Default to 5001 to avoid AirPlay conflicts
FLASK_DEBUG = os.getenv("FLASK_DEBUG", "True").lower() == "true"

# Frontend Configuration
FRONTEND_PORT = int(os.getenv("FRONTEND_PORT", "8000"))

# Default system prompt
DEFAULT_SYSTEM_PROMPT = "You are a helpful assistant."

# Validate required settings
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is required") 