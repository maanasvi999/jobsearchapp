from django.db import models
from datetime import datetime
import random
import string 

def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


class JobCategory(models.Model):
    job_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length = 200)
    category_slug = models.CharField(max_length = 100, default = 1)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.job_category


class JobInformation(models.Model):
    job_title = models.CharField(max_length = 100)
    job_company = models.CharField(max_length = 150)
    job_salary = models.CharField(max_length = 100)
    job_location = models.CharField(max_length = 100)
    job_published = models.DateTimeField("Job Published", default = datetime.now)
    job_category = models.ForeignKey(JobCategory, default = 1, verbose_name="Category", on_delete = models.SET_DEFAULT)
    job_summary = models.CharField(max_length = 200)
    job_slug = models.CharField(max_length=6, unique=True, default=rand_slug())
    
    class Meta:
        verbose_name_plural = "Information"
    
    def __str__(self):
        return self.job_title + " " + self.job_company

class Profile(models.Model):
    open_to_work=(
        ('yes', 'Yes',),
        ('no','No'))
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    bio = models.CharField(max_length = 200, verbose_name = "About Me")
    job_category = models.ForeignKey(JobCategory, default = 1, verbose_name="Interested Job Category", on_delete = models.SET_DEFAULT)
    opentowork = models.CharField(max_length = 200, choices = open_to_work, verbose_name = "Open To Work")

    def __str__(self):
        return self.first_name + " " + self.last_name

class CandidateApplication(models.Model):
    category=(
        ('male', 'Male',),
        ('female','Female'),
        ('prefer not to say','Prefer Not To Say'),
    )
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    date_of_birth = models.DateField(help_text = 'yyyy/mm/dd format', null = True)
    gender = models.CharField(max_length = 200, null = True, choices = category)
    contact_number = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    job_category = models.ForeignKey(JobCategory, default = 1, verbose_name="Category", on_delete = models.SET_DEFAULT)
    job_company = models.ForeignKey(JobInformation, default = 1, verbose_name="Job Company", on_delete = models.SET_DEFAULT)

    class Meta:
        verbose_name_plural = "CandidateApplications"

    def __str__(self):
        return self.first_name + " "+ self.last_name

class Post(models.Model):
    post_title = models.CharField(max_length = 50)
    post_description = models.CharField(max_length = 250)
    post_slug = models.CharField(max_length=6, unique=True, default=rand_slug())

    def __str__(self):
        return self.post_title