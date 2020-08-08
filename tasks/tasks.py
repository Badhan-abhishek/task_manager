from __future__ import absolute_import, unicode_literals 
import time 
from celery import shared_task


@shared_task
def celery_task(counter):
    email = "hassanzadeh.sd@gmail.com"
    time.sleep(30)
    return '{} Done!'.format(counter)