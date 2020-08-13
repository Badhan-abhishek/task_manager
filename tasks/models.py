from django.db import models
from datetime import date


class Task(models.Model):
    task_choices = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4)
    ]
    task_type = models.IntegerField(choices=task_choices)
    task_desc = models.CharField(max_length=250, null=True)
    task_date = models.DateField(null=True) # auto_now_add=True

    def __str__(self):
        num = str(self.task_type)
        return "Task  " + num


class TaskTracker(models.Model):
    update_choices = [
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly')
    ]
    task_type = models.ForeignKey(Task, on_delete=models.CASCADE)
    update_type = models.CharField(max_length=250, choices=update_choices)
    email = models.EmailField(null=True, unique=True)

    def __str__(self):
        num = str(self.task_type)
        return "Tracker " + num
