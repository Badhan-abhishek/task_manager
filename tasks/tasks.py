from django.utils import timezone
from __future__ import absolute_import, unicode_literals
import time
from celery import shared_task
from .models import TaskTracker, Task
from datetime import date
import datetime
import calendar

tasks = Task.objects.all()
trackers = TaskTracker.objects.all()


def daily_task(mail, task_num, selected_task):
    print("To {mail},\n Task number is {task_num}".format(
        mail=mail, task_num=task_num))
    messages = []
    for tasks in selected_task:
        if tasks.task_date == date.today():
            messages.append(tasks.task_desc)
    for i in range(len(messages)):
        print("This is messsage {num}, \n {message}".format(
            num=i+1, message=messages[i]))


def weekly_task(mail, task_num, selected_task):
    date = date.today("%y %m %d")
    date_created = datetime.datetime.strptime(y, '%d %m %Y').weekday()
    day = calendar.day_name(date_created)
    some_day_last_week = timezone.now().date() - timedelta(days=7)
    monday_of_last_week = some_day_last_week - \
        timedelta(days=(some_day_last_week.isocalendar()[2] - 1))
    monday_of_this_week = monday_of_last_week + timedelta(days=7)
    Entry.objects.filter(task_date__gte=monday_of_last_week,
                         task_date__lt=monday_of_this_week)
    if date_created == 0:
        print("To {mail},\n Task number is {task_num}".format(
            mail=mail, task_num=task_num))
        messages = []
        for tasks in selected_task:
            if tasks.task_date == date.today():
                messages.append(tasks.task_desc)
        for i in range(len(messages)):
            print("This is messsage {num}, \n {message}".format(
                num=i+1, message=messages[i]))


@shared_task
def task_creator():
    for tracker in trackers:
        if tracker.update_type == 'Daily':
            mail = tracker.email
            task_num = tracker.task_type.task_type
            selected_task = Task.objects.filter(task_type=task_num)
            daily_task(mail, task_num, selected_task)
        elif tracker.update_type == 'Weekly':
            mail = tracker.email
            task_num = tracker.task_type.task_type
            selected_task = Task.objects.filter(task_type=task_num)
            daily_task(mail, task_num, selected_task)
