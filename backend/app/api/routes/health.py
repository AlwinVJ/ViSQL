from fastapi import APIRouter, status
from pydantic import BaseModel

from app.core.settings import settings

router = APIRouter()


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str


@router.get(
    "/health",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK,
    summary="Service health check",
)
def health_check() -> HealthResponse:
    return HealthResponse(status="healthy", service=settings.app_name, version=settings.app_version)
