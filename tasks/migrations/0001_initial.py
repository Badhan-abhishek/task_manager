# Generated by Django 3.1 on 2020-08-08 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_type', models.IntegerField(choices=[('1', 'one'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four')])),
                ('task_desc', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskTracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_type', models.CharField(choices=[('daily', 'Daily'), ('week', 'Weekly'), ('month', 'Monthly')], max_length=250)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('task_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
            ],
        ),
    ]