# Generated by Django 3.1 on 2020-08-08 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_date',
            field=models.DateField(null=True),
        ),
    ]