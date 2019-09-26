from celery import Celery
from pathlib import Path

_dir = Path('C:/Users/UI585722/Downloads/results.txt')

app = Celery('tasks', broker='amqp://Deep:Hexis_17@localhost:5672//')
app.conf.update(task_track_started=True,
                result_backend=_dir)


@app.task
def reverse(string):
    return string[::-1]
