from openai import OpenAI

from app.config import settings


class LLMService:

    def __init__(self):
        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY,
        )

    def ask(
        self,
        prompt: str,
        model: str = None,
    ) -> str:

        response = self.client.responses.create(
            model=model or settings.OPENAI_MODEL,
            input=prompt,
        )

        return response.output_text