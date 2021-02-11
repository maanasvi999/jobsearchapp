from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import JobInformation, JobCategory, CandidateApplication, Post, Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm, ApplyJobForm, Jobs, ProfileInfoForm, PostForm
from django.contrib.auth.models import User

def single_slug(request, single_slug):
    categories = [j.category_slug for j in JobCategory.objects.all()]
    
    if single_slug in categories:
        matching_jobs = JobInformation.objects.filter(job_category__category_slug = single_slug)

        jobs_urls = {}

        for m in matching_jobs.all():
            part_one = JobInformation.objects.filter(job_category__job_category = m.job_category)
            jobs_urls[m] = part_one

        return render(request, 
                        "main/jobs.html",
                        {"part_ones": jobs_urls})
    
    jobs = [j.job_slug for j in JobInformation.objects.all()]
    
    if single_slug in jobs:
        this_job = JobInformation.objects.get(job_slug = single_slug)
        jobs_from_category = JobInformation.objects.filter(job_category__job_category = this_job.job_category)
        this_job_idx = list(jobs_from_category).index(this_job)

        return render(request,
                        "main/jobdetails.html",
                        {"job":this_job,
                        "sidebar": jobs_from_category,
                        "this_job_idx": this_job_idx})
    
    return HttpResponse(f"{single_slug} does not correspond to anything!")

def homepage(request):
    return render(request = request,
                  template_name = "main/home.html",
                  context = {"jobs": JobCategory.objects.all()})

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST, initial={'login_category': 'JobSeeker'})
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login_category = form.cleaned_data['login_category']
            messages.success(request, f"New Account Successfully created:{username} {login_category}")
            login(request, user)
            messages.info(request, f"You are now logged in as {username} {login_category}")
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")
    form = NewUserForm(initial={'login_category': 'JobSeeker'})
    return render(request, 
                    "main/register.html",
                    context = {"form": form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect("main:homepage")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid Username or Password")
        else:
                messages.error(request, "Invalid Username or Password")

    form = AuthenticationForm(initial={'login_category': 'JobSeeker'})
    return render(request, 
                "main/login.html",
                {"form":form})

def search(request):
    if request.method == 'GET':
        srh = request.GET.get('query')
        if srh!="":
            jobs = JobInformation.objects.filter(job_title__icontains = srh)
        else:
            messages.error(request, "Invalid Search. Try Again")
            return redirect("main:homepage")
    return render(request, 'main/search.html', {'search_jobs': jobs, 'search':srh})

def application(request):
    form = ApplyJobForm()
    if request.method == 'POST':
        form = ApplyJobForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Applied Successfully!")
            return redirect('main:homepage')
        else:
            messages.error(request, "Try Checking the Date Format")
    context = {'form':form}
    return render(request, 'main/apply.html', context)

def employer(request):
    form = Jobs()
    if request.method == 'POST':
        form = Jobs(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Applied Successfully!")
            return redirect('main:homepage')
        else:
            messages.error(request, "Try Again")
    context = {'form':form}
    return render(request, 'main/information.html', context)

def jobseeker(request):
    form = Jobs()
    if request.method == 'POST':
        form = Jobs(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Applied Successfully!")
            return redirect('main:homepage')
        else:
            messages.error(request, "Try Again")
    context = {'form':form}
    return render(request, 'main/profile.html', context)

def profile(request):
    form = ProfileInfoForm()
    if request.method == 'POST':
        form = ProfileInfoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Added Info Successfully!")
            context = {'form':form}
            return render(request, 'main/profile.html', context)
        else:
            messages.error(request, "Try Again")
    context = {'form':form}
    return render(request, 'main/fillprofileform.html', context)


def showposts(request):
    context = {}
    posts = [p for p in Post.objects.all()]
    context  = {'posts': posts}
    return render(request, 'main/showposts.html', context)

def post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Saved Post!")
            return redirect('main:showposts')
        else:
            messages.error(request, "Try Again")
    context = {'form':form}
    return render(request, 'main/post.html', context)

from rest_framework import viewsets

from .serializers import CandidateApplicationSerializer
class CandidateApplicationViewSet(viewsets.ModelViewSet):
    queryset = CandidateApplication.objects.all().order_by('date_of_birth')
    serializer_class = CandidateApplicationSerializer