from pydantic import BaseModel
from typing import List, Optional

class UserRequirement(BaseModel):
    id: int
    title: str
    description: str
    project_id: int
    dependencies: List[int] = []
    generated_context: Optional[str] = None