from fastapi import APIRouter, Depends
from typing import List
from core.models.user_requirement import UserRequirement
from services.user_requirement_service import UserRequirementService

router = APIRouter(prefix="/user-requirements", tags=["user-requirements"])

@router.post("/", response_model=UserRequirement)
def create_user_requirement(user_requirement: UserRequirement):
    return UserRequirementService.create_user_requirement(user_requirement)

@router.get("/", response_model=List[UserRequirement])
def get_user_requirements(project_id: int):
    return UserRequirementService.get_user_requirements_by_project(project_id)

@router.get("/{user_requirement_id}", response_model=UserRequirement)
def get_user_requirement(user_requirement_id: int):
    return UserRequirementService.get_user_requirement_by_id(user_requirement_id)

@router.put("/{user_requirement_id}", response_model=UserRequirement)
def update_user_requirement(user_requirement_id: int, user_requirement: UserRequirement):
    return UserRequirementService.update_user_requirement(user_requirement_id, user_requirement)

@router.delete("/{user_requirement_id}")
def delete_user_requirement(user_requirement_id: int):
    UserRequirementService.delete_user_requirement(user_requirement_id)