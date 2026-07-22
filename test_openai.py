# test_openai.py

from app.services.llm_service import LLMService

llm = LLMService()

response = llm.ask(
    "Reply with only: Hello from OpenAI"
)

print(response)