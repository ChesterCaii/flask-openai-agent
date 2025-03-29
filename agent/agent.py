"""
OpenAI Agent Module

This module provides a simple interface to interact with OpenAI's API.
It handles message formatting and response processing for chat completions.
"""

from openai import OpenAI, OpenAIError
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
            
        Raises:
            ValueError: If OPENAI_API_KEY is not set
        """
        if not OPENAI_API_KEY:
            raise ValueError("OpenAI API key is not set. Please set OPENAI_API_KEY in your .env file.")
            
        self.model = model
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def run(self, history):
        """
        Process a conversation history and get a response from OpenAI.
        
        Args:
            history (list): List of message dictionaries with 'role' and 'content' keys.
                          Example: [{"role": "user", "content": "Hello"}, ...]
        
        Returns:
            str: The assistant's response text
        
        Raises:
            ValueError: If history is empty or invalid
            OpenAIError: If there's an error communicating with OpenAI
            Exception: For other unexpected errors
        """
        if not history:
            raise ValueError("Conversation history cannot be empty")
            
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=history,
                temperature=0.7,
            )
            return response.choices[0].message.content.strip()
            
        except OpenAIError as e:
            raise OpenAIError(f"OpenAI API error: {str(e)}")
        except Exception as e:
            raise Exception(f"Unexpected error while communicating with OpenAI: {str(e)}") 