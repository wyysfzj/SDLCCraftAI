# LLMConnector.py

import requests

class LLMConnector:
    def __init__(self, config):
        self.api_key = config["api_key"]
        self.model = config["model"]
        self.endpoint = "https://api.openai.com/v1/engines/{}/completions".format(self.model)

    def generateUserStory(self, input_text):
        response = self.callChatGPTAPI(input_text)
        user_story = self.processResponse(response)
        return user_story

    def callChatGPTAPI(self, input_text):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "prompt": input_text,
            "max_tokens": 150  # Adjust as needed
        }

        response = requests.post(self.endpoint, headers=headers, json=data)
        return response.json()

    def processResponse(self, response):
        if response.get("choices"):
            return response["choices"][0].get("text", "").strip()
        return "Error: No response from LLM"
