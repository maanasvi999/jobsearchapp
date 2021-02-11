from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CandidateApplication, JobInformation, Profile, Post
from django.forms import ModelForm

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required = True)
    CHOICES = (('JobSeeker', 'JobSeeker'),('Employer', 'Employer'))
    login_category = forms.ChoiceField(widget = forms.Select(), choices = (CHOICES), initial='JobSeeker', required = True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2","login_category",)
    
    def save(self, commit = True):
        user = super(NewUserForm, self).save(commit = False)
        user.email = self.cleaned_data.get('email')
        user.login_category = self.cleaned_data['login_category']
        if commit:
            user.save()
        return user

class ApplyJobForm(ModelForm):
    class Meta:
        model = CandidateApplication
        fields = "__all__"

class Jobs(ModelForm):
    class Meta:
        model = JobInformation
        fields = ('job_title', 'job_company', 'job_salary', 'job_location', 'job_published','job_category', 'job_summary')

class ProfileInfoForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ("post_title", "post_description")