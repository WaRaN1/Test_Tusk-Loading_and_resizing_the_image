from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_app_img.settings')

app = Celery('web_app_img', backend='amqp', broker='amqp://guest@localhost//')

app.conf.update(result_expires=3600,)

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

result_backend = 'db+sqlite:///web_app_img.db.sqlite3'

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

if __name__ == '__main__':
     app.start()


