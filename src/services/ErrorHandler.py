# ErrorHandler.py

class ErrorHandler:
    @staticmethod
    def handleAPIError(response):
        # Handles errors related to ChatGPT API calls
        if response.status_code != 200:
            return f"API Error: {response.status_code} - {response.text}"
        return None

    @staticmethod
    def handleInputValidationError(input_text):
        # Handles input validation errors
        if not input_text or not isinstance(input_text, str):
            return "Invalid input: Input must be a non-empty string."
        return None
