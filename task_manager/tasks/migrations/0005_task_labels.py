# Generated by Django 5.0.6 on 2024-06-10 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0004_rename_created_task_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(blank=True, related_name='tasks', to='labels.label', verbose_name='labels'),
        ),
    ]
