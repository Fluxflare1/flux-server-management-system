from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'process-pending-commissions-daily': {
        'task': 'backend.tasks.commission_tasks.process_pending_commissions',
        'schedule': crontab(hour=0, minute=0),  # Runs at midnight
    },
}
