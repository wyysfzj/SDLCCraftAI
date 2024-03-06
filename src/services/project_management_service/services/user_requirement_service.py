from typing import List
from core.models.user_requirement import UserRequirement
from data.repositories.user_requirement_repository import UserRequirementRepository

class UserRequirementService:
    @staticmethod
    def create_user_requirement(user_requirement: UserRequirement):
        return UserRequirementRepository.create_user_requirement(user_requirement)

    @staticmethod
    def get_user_requirements_by_project(project_id: int) -> List[UserRequirement]:
        return UserRequirementRepository.get_user_requirements_by_project(project_id)

    @staticmethod
    def get_user_requirement_by_id(user_requirement_id: int) -> UserRequirement:
        return UserRequirementRepository.get_user_requirement_by_id(user_requirement_id)

    @staticmethod
    def update_user_requirement(user_requirement_id: int, user_requirement: UserRequirement):
        return UserRequirementRepository.update_user_requirement(user_requirement_id, user_requirement)

    @staticmethod
    def delete_user_requirement(user_requirement_id: int):
        UserRequirementRepository.delete_user_requirement(user_requirement_id)