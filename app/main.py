from fastapi import FastAPI

app = FastAPI(
    title="AI Document Intelligence Platform",
    description="Backend API for AI-powered document processing",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to AI Document Intelligence Platform"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }