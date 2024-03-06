from pydantic import BaseModel
from typing import List
from .user_requirement import UserRequirement

class Project(BaseModel):
    id: int
    name: str
    description: str
    user_requirements: List[UserRequirement] = []