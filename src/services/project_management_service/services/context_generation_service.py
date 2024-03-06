from typing import Optional
from core.models.user_requirement import UserRequirement
from core.models.project import Project
from services.llm_service import LLMService
from data.repositories.user_requirement_repository import UserRequirementRepository
from data.repositories.project_repository import ProjectRepository

class ContextGenerationService:
    @staticmethod
    def generate_context(user_requirement_id: int, project_id: Optional[int] = None, additional_context: Optional[str] = None):
        user_requirement = UserRequirementRepository.get_user_requirement_by_id(user_requirement_id)
        project = ProjectRepository.get_project_by_id(project_id) if project_id else None

        input_data = {
            "user_requirement": user_requirement.dict(),
            "project": project.dict() if project else None,
            "additional_context": additional_context
        }

        llm_service = LLMService()
        generated_context = llm_service.generate_context(input_data)

        user_requirement.generated_context = generated_context
        UserRequirementRepository.update_user_requirement(user_requirement_id, user_requirement)

        return generated_context