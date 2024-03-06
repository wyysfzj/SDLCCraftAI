from fastapi import APIRouter, Depends
from typing import List
from core.models.project import Project
from services.project_service import ProjectService

router = APIRouter(prefix="/projects", tags=["projects"])

@router.post("/", response_model=Project)
def create_project(project: Project):
    return ProjectService.create_project(project)

@router.get("/", response_model=List[Project])
def get_projects():
    return ProjectService.get_all_projects()

@router.get("/{project_id}", response_model=Project)
def get_project(project_id: int):
    return ProjectService.get_project_by_id(project_id)

@router.put("/{project_id}", response_model=Project)
def update_project(project_id: int, project: Project):
    return ProjectService.update_project(project_id, project)

@router.delete("/{project_id}")
def delete_project(project_id: int):
    ProjectService.delete_project(project_id)