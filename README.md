# AI Document Intelligence Platform

A backend service built with **FastAPI** for uploading, processing, and managing documents. The platform extracts text from uploaded documents and provides a foundation for AI-powered document understanding.

## Features

- User Authentication (JWT)
- Document Upload & Storage
- Document Download & Delete
- Document Listing with Pagination
- Document Processing Workflow
- Document Status Tracking
- OCR Content Storage
- Retrieve Extracted Document Text
- RESTful APIs with OpenAPI (Swagger)

## Tech Stack

- Python 3.13
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Pydantic
- JWT Authentication

## Project Structure

```
app/
├── api/
├── models/
├── repositories/
├── schemas/
├── services/
├── core/
└── utils/
```

## Processing Workflow

```
Upload Document
       │
       ▼
Process Document
       │
       ▼
OCR Service
       │
       ▼
Store Extracted Text
       │
       ▼
Retrieve OCR Content
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register user |
| POST | `/auth/login` | Login |
| POST | `/documents/upload` | Upload document |
| GET | `/documents` | List documents |
| GET | `/documents/{uuid}` | Get document details |
| GET | `/documents/{uuid}/download` | Download document |
| DELETE | `/documents/{uuid}` | Delete document |
| POST | `/documents/{uuid}/process` | Process document |
| GET | `/documents/{uuid}/content` | Get extracted text |

## Current Status

- ✅ Authentication
- ✅ Document Management
- ✅ Processing Pipeline
- ✅ OCR Service Architecture
- ✅ OCR Content Storage

## Planned Features

- Real OCR using Tesseract
- AI-based Field Extraction (OpenAI)
- Background Processing with Celery & Redis
- Search & Filtering
- Document Summarization