import openai
import os

class ChatGPT():
    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.openai.api_key = self.chatopenai_api_key
    def chat(self,text):
        res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": self.text
            }
            ]
        )
        return res["choices"][0]["message"]["content"]