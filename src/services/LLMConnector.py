# LLMConnector.py

# import requests
# from ErrorHandler import ErrorHandler


# class LLMConnector:
#     def __init__(self, config):
#         self.api_key = config["api_key"]
#         self.model = config["model"]
#         self.endpoint = "https://api.openai.com/v1/engines/{}/completions".format(self.model)

#     def generateUserStory(self, input_text):
#         response = self.callChatGPTAPI(input_text)
#         user_story = self.processResponse(response)
#         return user_story

#     def callChatGPTAPI(self, input_text):
#         headers = {
#             "Authorization": f"Bearer {self.api_key}",
#             "Content-Type": "application/json"
#         }

#         data = {
#             "prompt": input_text,
#             "max_tokens": 150  # Adjust as needed
#         }

#         response = requests.post(self.endpoint, headers=headers, json=data)
#         error_message = ErrorHandler.handleAPIError(response)
#         if error_message:
#             return {"error": error_message}
        
#         return response.json()

#     def processResponse(self, response):
#         if response.get("choices"):
#             return response["choices"][0].get("text", "").strip()
#         return "Error: No response from LLM"
# LLMConnector.py

from abc import ABC, abstractmethod

class LLMConnector(ABC):
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def generateUserStory(self, input_text):
        pass
