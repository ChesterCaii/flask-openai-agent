import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Agent:
    def __init__(self, model="gpt-3.5-turbo"):
        self.model = model
        # Set the API key from environment variable
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def run(self, history):
        """
        Run the agent with a conversation history.
        history: List of message dictionaries with 'role' and 'content' keys
        """
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=history
        )
        return response.choices[0].message["content"].strip() 