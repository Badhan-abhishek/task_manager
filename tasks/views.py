from django.shortcuts import render, redirect, HttpResponse
from .models import Task
from .forms import TaskTrackerForm, TaskForm
from django.contrib import messages 
from .tasks import celery_task

# Create your views here.
def index(request):
    return render(request, "tasks/index.html")

def tracker(request):
    form = TaskTrackerForm()
    if request.method == 'POST':
        form = TaskTrackerForm(request.POST)
        try:
            if form.is_valid:
                form.save()
                messages.success(request, "Data saved successfully!")
                return redirect('tracker')
        except ValueError:
            messages.warning(request, "The email is not valid please use valid email address")
            return redirect('tracker')
    context = {'form': form}
    return render(request, "tasks/create_tracker.html", context)

def taskComplete(request):
    form = TaskForm
    if request.method == 'POST':
        form = TaskForm(request.POST)
        try:
            if form.is_valid:
                form.save()
                messages.success(request, "Data saved successfully!")
                return redirect('task-complete')
        except ValueError:
            messages.warning(request, "Wrong data!")
            return redirect('task-complete')
    context = {'form': form}
    return render(request, "tasks/complete_task.html", context)

def testMain(request):
    for counter in range(2):
        celery_task.delay(counter)
    return HttpResponse("<h1>Loaded </h1>")