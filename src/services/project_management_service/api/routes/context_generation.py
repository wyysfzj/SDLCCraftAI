from fastapi import APIRouter, Depends
from pydantic import BaseModel
from services.context_generation_service import ContextGenerationService

router = APIRouter(prefix="/context-generation", tags=["context-generation"])

class ContextGenerationRequest(BaseModel):
    user_requirement_id: int
    project_id: Optional[int] = None
    additional_context: Optional[str] = None

class ContextGenerationResponse(BaseModel):
    generated_context: str

@router.post("/generate-context", response_model=ContextGenerationResponse)
def generate_context(request: ContextGenerationRequest):
    generated_context = ContextGenerationService.generate_context(
        user_requirement_id=request.user_requirement_id,
        project_id=request.project_id,
        additional_context=request.additional_context
    )
    return ContextGenerationResponse(generated_context=generated_context)