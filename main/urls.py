"""JobSearch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

from rest_framework import routers
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'candidateapplication', views.CandidateApplicationViewSet)

app_name = 'main'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path("register/", views.register, name = "register"),
    path("logout/", views.logout_request, name = "logout"),
    path("login", views.login_request, name = "login"),
    path('search', views.search, name = 'search'),
    path('apply', views.application, name = 'apply'),
    path('information', views.employer, name = 'information'),
    path('profile', views.jobseeker, name = 'profile'),
    path('fillprofile', views.profile, name = 'fillprofile'),
    path('post', views.post, name = 'post'),
    path('showposts', views.showposts, name = 'showposts'),
    path('scraped', views.scraped, name = 'scraped'),
    path('api/applicants/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('<single_slug>', views.single_slug, name = "single_slug"),
]
