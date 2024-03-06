from fastapi import APIRouter, Depends
from pydantic import BaseModel
from services.user_story_generation_service import UserStoryGenerationService

router = APIRouter(prefix="/user-story-generation", tags=["user-story-generation"])

class UserStoryGenerationRequest(BaseModel):
    user_requirement_id: int
    context: Optional[str] = None

class UserStoryGenerationResponse(BaseModel):
    generated_user_story: str

@router.post("/generate-user-story", response_model=UserStoryGenerationResponse)
def generate_user_story(request: UserStoryGenerationRequest):
    generated_user_story = UserStoryGenerationService.generate_user_story(
        user_requirement_id=request.user_requirement_id,
        context=request.context
    )
    return UserStoryGenerationResponse(generated_user_story=generated_user_story)