# Generated by Django 5.0.6 on 2024-06-10 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_remove_task_executer_task_executor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='created',
            new_name='created_at',
        ),
    ]
