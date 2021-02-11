# Generated by Django 3.1.4 on 2021-02-10 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_applicantprofile_appliedjobs_employerprofile_savedjobs_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appliedjobs',
            name='job_company',
        ),
        migrations.RemoveField(
            model_name='appliedjobs',
            name='user',
        ),
        migrations.RemoveField(
            model_name='employerprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='savedjobs',
            name='job_company',
        ),
        migrations.RemoveField(
            model_name='savedjobs',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='ApplicantProfile',
        ),
        migrations.DeleteModel(
            name='AppliedJobs',
        ),
        migrations.DeleteModel(
            name='EmployerProfile',
        ),
        migrations.DeleteModel(
            name='SavedJobs',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
