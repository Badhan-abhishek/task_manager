# Generated by Django 3.1 on 2020-08-08 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20200808_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasktracker',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]