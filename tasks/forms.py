from django.forms import ModelForm
from django import forms 
from .models import Task, TaskTracker


class TaskTrackerForm(ModelForm):
    class Meta:
        model = TaskTracker
        fields = '__all__'

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'