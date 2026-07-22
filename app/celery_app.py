from celery import Celery

from app.config import settings

celery_app = Celery(
    "document_ai",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
)

celery_app.conf.update(
    task_track_started=True,
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
)

celery_app.autodiscover_tasks(["app.tasks"])