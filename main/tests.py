from django.test import TestCase

# Create your tests here.
from main.models import JobInformation, JobCategory, Post
from datetime import datetime
from django.urls import reverse
from main.forms import Jobs, PostForm
from main.views import *

class JobInformationTest(TestCase):
    def create_jobinformation(self, job_title="Test", 
            job_company = "Test Company",
            job_salary = "10000 per month",
            job_location = "India",
            job_summary = "Job Available"):
        categ = JobCategory.objects.create(job_category = "Cook Jobs", category_summary = "XYX", category_slug = "zzz")
        return JobInformation.objects.create(job_title = job_title, job_company = job_company, job_location = job_location, job_category = categ, job_summary = job_summary)

    def test_job_creation(self):
        j = self.create_jobinformation()
        self.assertTrue(isinstance(j, JobInformation))
        self.assertEqual(j.__str__(), j.job_title+" "+j.job_company)

class PostTest(TestCase):
    def create_post(self, post_title="Test Post title", post_description = "Test Post"):
        return Post.objects.create(post_title = post_title, post_description = post_description)

    def test_post_creation(self):
        p = self.create_post()
        self.assertTrue(isinstance(p, Post))
        self.assertEqual(p.__str__(), p.post_title)
        