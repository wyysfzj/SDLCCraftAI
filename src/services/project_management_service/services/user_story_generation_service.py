from typing import Optional
from core.models.user_requirement import UserRequirement
from services.llm_service import LLMService
from data.repositories.user_requirement_repository import UserRequirementRepository
from data.repositories.user_story_repository import UserStoryRepository

class UserStoryGenerationService:
    @staticmethod
    def generate_user_story(user_requirement_id: int, context: Optional[str] = None):
        user_requirement = UserRequirementRepository.get_user_requirement_by_id(user_requirement_id)

        input_data = {
            "user_requirement": user_requirement.dict(),
            "context": context
        }

        llm_service = LLMService()
        generated_user_story = llm_service.generate_user_story(input_data)

        user_story = UserStory(
            user_requirement_id=user_requirement_id,
            description=generated_user_story
        )
        UserStoryRepository.create_user_story(user_story)

        return generated_user_story