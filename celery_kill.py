# To kill celery and beat if they are already running.
import shlex
import subprocess

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        kill_worker_cmd = 'pkill -9 celery'
        subprocess.call(shlex.split(kill_worker_cmd))
