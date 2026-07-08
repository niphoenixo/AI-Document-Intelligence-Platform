
#Step 1 – Create the project
mkdir ai-document-intelligence-platform

cd ai-document-intelligence-platform
Initialize Git:
git init

## =====================
#Step 2 – Create folders
mkdir -p app/{api/routes,models,schemas,services,workers,database/migrations,repositories,utils,middleware}
mkdir -p tests
mkdir -p docs
mkdir -p sample_documents
mkdir -p scripts

touch README.md LICENSE .gitignore .env.example requirements.txt docker-compose.yml Dockerfile

touch app/main.py
touch app/config.py
touch app/dependencies.py

touch app/api/router.py

touch app/api/routes/auth.py
touch app/api/routes/documents.py
touch app/api/routes/jobs.py
touch app/api/routes/health.py
touch app/api/routes/users.py

touch app/models/document.py
touch app/models/job.py
touch app/models/user.py

touch app/schemas/document.py
touch app/schemas/job.py
touch app/schemas/auth.py

touch app/services/auth_service.py
touch app/services/document_service.py
touch app/services/ocr_service.py
touch app/services/llm_service.py
touch app/services/extraction_service.py
touch app/services/storage_service.py
touch app/services/notification_service.py

touch app/workers/celery_app.py
touch app/workers/tasks.py

touch app/database/session.py
touch app/database/base.py

touch app/repositories/document_repository.py
touch app/repositories/job_repository.py
touch app/repositories/user_repository.py

touch app/utils/logger.py
touch app/utils/validators.py
touch app/utils/security.py
touch app/utils/helpers.py

touch app/middleware/auth.py
touch app/middleware/request_logger.py

touch tests/test_api.py
touch tests/test_ocr.py
touch tests/test_llm.py
touch tests/test_jobs.py
touch tests/test_auth.py

touch docs/architecture.png
touch docs/sequence_diagram.png
touch docs/api_examples.md

touch scripts/seed_database.py
touch scripts/create_admin.py

touch app/__init__.py
touch app/api/__init__.py
touch app/api/routes/__init__.py
touch app/models/__init__.py
touch app/schemas/__init__.py
touch app/services/__init__.py
touch app/workers/__init__.py
touch app/database/__init__.py
touch app/repositories/__init__.py
touch app/utils/__init__.py
touch app/middleware/__init__.py

## ====================
#Step 3 – Create virtual environment
python -m venv .venv
Mac/Linux
source .venv/bin/activate

##================

#Step 4 – Install packages

pip install fastapi
pip install uvicorn
pip install sqlalchemy
pip install psycopg2-binary
pip install python-dotenv
pip install python-multipart
pip install passlib[bcrypt]
pip install python-jose[cryptography]
pip install alembic
pip install pydantic-settings



 docker exec -it ai-document-db psql -U postgres
 \l
 \c document_ai
 \dt
 \d users



 curl -X GET \
  http://localhost:8000/api/v1/auth/me \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuaXNoYUBleGFtcGxlLmNvbSIsInJvbGUiOiJVU0VSIiwiZXhwIjoxNzgzNTMxMjk1fQ.RX9l535YP0PV3DNMHCsp_28o8MJOB2t29PI_EEJ50_k"