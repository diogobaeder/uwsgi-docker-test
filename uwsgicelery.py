import time

from celery import Celery


WORK_TIME = 30
CONCURRENCY = 200
TASK_TIME_LIMIT = 24 * 60 * 60


app = Celery(
    'uwsgi-test',
    broker='amqp://guest@localhost//',
)
app.conf.update({
    'worker_concurrency': 200,
    'timezone': 'UTC',
    'worker_pool_restarts': True,
    'worker_prefetch_multiplier': 1,
    'task_time_limit': TASK_TIME_LIMIT,
})


@app.task
def slow():
    start = time.time()
    while time.time() <= (start + WORK_TIME):
        print('Processing...')
        time.sleep(1)
    print('Done.')
