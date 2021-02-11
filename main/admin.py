from django.contrib import admin

# Register your models here.
from .models import JobCategory, JobInformation, CandidateApplication, Profile, Post

admin.site.register(JobCategory)
admin.site.register(JobInformation)
admin.site.register(CandidateApplication)
admin.site.register(Profile)
admin.site.register(Post)