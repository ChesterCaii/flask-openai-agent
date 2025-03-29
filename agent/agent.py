"""
OpenAI Agent Module

This module provides a simple interface to interact with OpenAI's API.
It handles message formatting and response processing for chat completions.
"""

import openai
from config import OPENAI_API_KEY, OPENAI_MODEL

class Agent:
    """
    A class to handle interactions with OpenAI's API.
    
    This class manages the conversation with OpenAI's models, handling
    message formatting and response processing.
    """
    
    def __init__(self, model=OPENAI_MODEL):
        """
        Initialize the agent with a specific OpenAI model.
        
        Args:
            model (str): The OpenAI model to use (default: from config)
        """
        self.model = model
        openai.api_key = OPENAI_API_KEY

    def run(self, history):
        """
        Process a conversation history and get a response from OpenAI.
        
        Args:
            history (list): List of message dictionaries with 'role' and 'content' keys.
                          Example: [{"role": "user", "content": "Hello"}, ...]
        
        Returns:
            str: The assistant's response text
        
        Raises:
            Exception: If there's an error communicating with OpenAI
        """
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=history
            )
            return response.choices[0].message["content"].strip()
        except Exception as e:
            raise Exception(f"Error communicating with OpenAI: {str(e)}") 