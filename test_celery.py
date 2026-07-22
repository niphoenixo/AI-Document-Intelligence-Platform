from app.tasks import test_task

result = test_task.delay()

print(f"Task ID: {result.id}")

print("Waiting for task to complete...")

print(result.get(timeout=10))