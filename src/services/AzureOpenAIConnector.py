# AzureOpenAIConnector.py

import requests
from LLMConnector import LLMConnector

class AzureOpenAIConnector(LLMConnector):
    def generateUserStory(self, input_text):
        headers = self.config["headers"]
        data = {
            "prompt": input_text,
            "max_tokens": self.config["additional_params"]["max_tokens"],
            # Other parameters as needed
        }
        response = requests.post(self.config["endpoint"], headers=headers, json=data)
        return response.json()["choices"][0]["text"].strip()
