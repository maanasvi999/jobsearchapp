# Generated by Django 3.1.4 on 2021-02-09 17:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210209_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobinformation',
            name='job_published',
            field=models.DateTimeField(default=datetime.date(2021, 2, 9), verbose_name='Job Published'),
        ),
    ]