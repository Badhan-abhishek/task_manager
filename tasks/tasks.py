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
    full_date = date.today()
    date = date.strftime("%y %m %d")
    date_created = datetime.datetime.strptime(y, '%d %m %Y').weekday()
    day = calendar.day_name(date_created)
    some_day_last_week = timezone.now().date() - timedelta(days=7)
    monday_of_last_week = some_day_last_week - \
        timedelta(days=(some_day_last_week.isocalendar()[2] - 1))
    monday_of_this_week = monday_of_last_week + timedelta(days=7)
    filtered_tasks = Task.objects.filter(task_date__gte=monday_of_last_week,
                                         task_date__lt=monday_of_this_week)
    week_task = set()
    for new_task in filtered_tasks:
        week_task.add(new_task)
    print("To {mail},\n Task number is {task_num}".format(
        mail=mail, task_num=task_num))
    messages = set()
    for tasks in selected_task:
        messages.add(tasks.task_desc)
    real_message = tasks.intersection(week_task, messages)
    for i in range(len(real_message)):
        print("This is messsage {num}, \n {message}".format(
            num=i+1, message=real_message[i]))


def weekly_task(mail, task_num, selected_task):
    full_date = date.today()
    date = date.strftime("%y %m %d")
    # month_task = set()
    # for month in tasks:
    #     month.task_date.strftime("%m")
    new_selected_message = []
    if selected_task.task_date.strftime("%m") == date:
        new_selected_message.append(selected_task)
    print("To {mail},\n Task number is {task_num}".format(
        mail=mail, task_num=task_num))
    for i in range(len(new_selected_message)):
        print("This is messsage {num}, \n {message}".format(
            num=i+1, message=new_selected_message[i]))


@shared_task
def task_creator():
    for tracker in trackers:
        if tracker.update_type == 'Daily':
            mail = tracker.email
            task_num = tracker.task_type.task_type
            selected_task = Task.objects.filter(task_type=task_num)
            daily_task(mail, task_num, selected_task)
        else:
            return None


@shared_task
def monthly_task():
    for tracker in trackers:
        if tracker.update_type == 'Monthly':
            mail = tracker.email
            task_num = tracker.task_type.task_type
            selected_task = Task.objects.filter(task_type=task_num)
            monthly_task(mail, task_num, selected_task)
        else:
            return None


@shared_task
def weekly_task_gen():
    for tracker in trackers:
        if tracker.update_type == 'Weekly':
            mail = tracker.email
            task_num = tracker.task_type.task_type
            selected_task = Task.objects.filter(task_type=task_num)
            weekly_task(mail, task_num, selected_task)
        else:
            return None
