# OpenAIConnector.py

import openai
from LLMConnector import LLMConnector

class OpenAIConnector(LLMConnector):
    def generateUserStory(self, input_text):
        openai.api_key = self.config["api_key"]
        response = openai.Completion.create(
            engine=self.config["additional_params"]["model"],
            prompt=input_text,
            max_tokens=self.config["additional_params"]["max_tokens"],
            # Other parameters as needed
        )
        return response.choices[0].text.strip()
