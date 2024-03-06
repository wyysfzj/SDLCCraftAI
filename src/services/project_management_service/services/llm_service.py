from langchain import OpenAI
from langchain.prompts import PromptTemplate
from core.config import settings

class LLMService:
    def __init__(self):
        self.llm = OpenAI(api_key=settings.llm_api_key)

    def generate_context(self, input_data):
        with open("prompts/context_generation_prompt.txt", "r") as file:
            prompt_template = file.read()

        prompt = PromptTemplate(
            input_variables=["user_requirement", "project", "additional_context"],
            template=prompt_template
        )
        formatted_input = prompt.format(
            user_requirement=input_data["user_requirement"],
            project=input_data["project"],
            additional_context=input_data["additional_context"]
        )
        response = self.llm(formatted_input)
        generated_context = self._postprocess_context(response)
        return generated_context

    def generate_user_story(self, input_data):
        with open("prompts/user_story_generation_prompt.txt", "r") as file:
            prompt_template = file.read()

        prompt = PromptTemplate(
            input_variables=["user_requirement", "context"],
            template=prompt_template
        )
        formatted_input = prompt.format(
            user_requirement=input_data["user_requirement"],
            context=input_data["context"]
        )
        response = self.llm(formatted_input)
        generated_user_story = self._postprocess_user_story(response)
        return generated_user_story

    def _postprocess_context(self, response: str):
        # Implement any necessary postprocessing of the generated context
        return response

    def _postprocess_user_story(self, response: str):
        # Implement any necessary postprocessing of the generated user story
        return response