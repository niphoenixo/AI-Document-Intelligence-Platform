from app.celery_app import celery_app


@celery_app.task
def test_task():
    print("Running background task...")
    return "Hello from Celery!"