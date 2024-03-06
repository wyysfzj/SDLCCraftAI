from pydantic import BaseModel

class UserStory(BaseModel):
    id: int
    user_requirement_id: int
    description: str