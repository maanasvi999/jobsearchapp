# Generated by Django 3.1.4 on 2021-02-09 20:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210209_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidateapplication',
            name='prev_experience',
        ),
        migrations.AlterField(
            model_name='jobinformation',
            name='job_published',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Job Published'),
        ),
    ]
