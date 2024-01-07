# LLMServiceManager.py

import json
from LLMConnector import LLMConnector

class LLMServiceManager:
    def __init__(self):
        self.llmConfig = self.loadLLMConfig()
        self.llmConnector = LLMConnector(self.llmConfig)

    def loadLLMConfig(self):
        # Ideally, load this configuration from a secure place
        config = {
            "api_key": "Your_ChatGPT_API_Key",
            "model": "gpt-3.5-turbo"  # or "text-davinci-003" for GPT-3
        }
        return config

    def handleRequest(self, input_text):
        validated_input = self.validateInput(input_text)
        user_story = self.llmConnector.generateUserStory(validated_input)
        return user_story

    def validateInput(self, input_text):
        # Add input validation logic as needed
        return input_text.strip()

if __name__ == "__main__":
    manager = LLMServiceManager()
    input_text = "Example input for the LLM"
    print(manager.handleRequest(input_text))
