import openai

class Agent:
    def __init__(self, model="gpt-3.5-turbo"):
        self.model = model

    def run(self, prompt):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message["content"].strip() 