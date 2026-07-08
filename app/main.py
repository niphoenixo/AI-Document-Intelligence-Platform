from fastapi import FastAPI

from app.api.router import api_router

app = FastAPI(
    title="AI Document Intelligence Platform",
    description="Backend API for AI-powered document processing",
    version="1.0.0",
)


@app.get("/", tags=["Health"])
def root():
    return {
        "message": "Welcome to AI Document Intelligence Platform"
    }


@app.get("/health", tags=["Health"])
def health():
    return {
        "status": "healthy"
    }


app.include_router(api_router)