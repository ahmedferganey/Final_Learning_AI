from celery import Celery
from helpers.config import get_settings


settings = get_settings()



# Create Celery application instance
celery_app = Celery(
    "minirag",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
)



# Configure Celery with essential settings
celery_app.conf.update(
    task_serializer=settings.CELERY_TASK_SERIALIZER,
    result_serializer=settings.CELERY_TASK_SERIALIZER,
    accept_content=[
        settings.CELERY_TASK_SERIALIZER
    ],

    # Task safety - Late acknowledgment prevents task loss on worker crash
    task_acks_late=settings.CELERY_TASK_ACKS_LATE,

    # Time limits - Prevent hanging tasks
    task_time_limit=settings.CELERY_TASK_TIME_LIMIT,

    # Result backend - Store results for status tracking
    task_ignore_result=False,
    result_expires=3600,

    # Register task modules (run worker from `src/`: celery -A celery_app worker)
    imports=[
        "tasks.file_processing",
        "tasks.process_workflow",
        "tasks.data_indexing",
        "tasks.maintenance",
    ],

    # Worker settings
    worker_concurrency=settings.CELERY_WORKER_CONCURRENCY,

    # Connection settings for better reliability
    broker_connection_retry_on_startup=True,
    broker_connection_retry=True,
    broker_connection_max_retries=10,
    worker_cancel_long_running_tasks_on_connection_loss=True,

    task_routes={
        "tasks.file_processing.process_project_files": {"queue": "file_processing"},
        "tasks.data_indexing.index_data_content": {"queue": "data_indexing"},
        "tasks.process_workflow.process_and_push_workflow": {"queue": "file_processing"},
        "tasks.maintenance.clean_celery_executions_table": {"queue": "default"},
        "tasks.data_indexing.push_project_index": {"queue": "data_indexing"},
        "tasks.data_indexing.get_project_index_info": {"queue": "data_indexing"},
        "tasks.data_indexing.search_vector_index": {"queue": "data_indexing"},
        "tasks.data_indexing.rag_answer": {"queue": "data_indexing"},
    },

    beat_schedule={
        'cleanup-old-task-records': {
            'task': "tasks.maintenance.clean_celery_executions_table",
            'schedule': 10,
            'args': ()
        }
    },

    timezone='UTC',
)

celery_app.conf.task_default_queue = "default"
