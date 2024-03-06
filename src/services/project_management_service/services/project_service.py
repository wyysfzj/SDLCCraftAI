from typing import List
from core.models.project import Project
from data.repositories.project_repository import ProjectRepository

class ProjectService:
    @staticmethod
    def create_project(project: Project):
        return ProjectRepository.create_project(project)

    @staticmethod
    def get_all_projects() -> List[Project]:
        return ProjectRepository.get_all_projects()

    @staticmethod
    def get_project_by_id(project_id: int) -> Project:
        return ProjectRepository.get_project_by_id(project_id)

    @staticmethod
    def update_project(project_id: int, project: Project):
        return ProjectRepository.update_project(project_id, project)

    @staticmethod
    def delete_project(project_id: int):
        ProjectRepository.delete_project(project_id)