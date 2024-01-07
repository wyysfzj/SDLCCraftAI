# LLMServiceManager.py

import json
from LLMConnector import LLMConnector
from ErrorHandler import ErrorHandler
from ConnectorFactory import create_connector

class LLMServiceManager:
    def __init__(self):
        self.llmConfig = self.loadLLMConfig()
        # self.llmConnector = LLMConnector(self.llmConfig)
        self.llmConnector = create_connector()

    def loadLLMConfig(self):
        # Ideally, load this configuration from a secure place
        config = {
            "api_key": "Your_ChatGPT_API_Key",
            "model": "gpt-3.5-turbo"  # or "text-davinci-003" for GPT-3
        }
        return config

    def handleRequest(self, input_text):
        validation_error = ErrorHandler.handleInputValidationError(input_text)
        if validation_error:
            return validation_error
        
        validated_input = self.validateInput(input_text)
        user_story = self.llmConnector.generateUserStory(validated_input)
        
        if "error" in user_story:
            return user_story["error"]
        
        return user_story

    def validateInput(self, input_text):
        # Add input validation logic as needed
        return input_text.strip()

if __name__ == "__main__":
    manager = LLMServiceManager()
    input_text = "Example input for the LLM"
    print(manager.handleRequest(input_text))
