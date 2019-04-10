import time
import hashlib

from celery import Celery
import requests

from storage.in_file_storage import InFileStorage

celery = Celery('test', backend='amqp', broker='amqp://')
storage = InFileStorage('db/db.txt')


@celery.task(bind=True)
def my_background_task(self, file_url):
    response = requests.get(file_url)

    if response.status_code == 404:
        raise Exception('resource not found')

    m = hashlib.md5()
    m.update(response.content)
    md5 = m.hexdigest()

    storage.save(self.request.id, file_url, md5)

    time.sleep(0.5)
    return md5
