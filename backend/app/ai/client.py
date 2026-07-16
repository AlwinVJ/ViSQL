from openai import OpenAI

from app.core.settings import settings


def get_openai_client() -> OpenAI:
    """Create the AI client only when an AI use case requires it."""
    return OpenAI(api_key=settings.openai_api_key)

