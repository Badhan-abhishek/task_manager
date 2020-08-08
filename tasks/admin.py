from django.contrib import admin
from .models import Task, TaskTracker

# Register your models here.
admin.site.register(Task)
admin.site.register(TaskTracker)