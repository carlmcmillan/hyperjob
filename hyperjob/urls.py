"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.views.generic import RedirectView
from vacancy.views import MenuView, VacanciesView, CreateVacancyView
from resume.views import ResumesView, CreateResumeView
from hyperjob.views import HyperSignupView, HyperLoginView, HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MenuView.as_view()),
    path('signup', HyperSignupView.as_view()),
    path('login', HyperLoginView.as_view()),
    path('login/', RedirectView.as_view(url='/login')),
    path('signup/', RedirectView.as_view(url='/signup')),
    path('vacancies', VacanciesView.as_view()),
    path('resumes', ResumesView.as_view()),
    path('home', HomeView.as_view()),
    path('resume/new', CreateResumeView.as_view()),
    path('vacancy/new', CreateVacancyView.as_view()),
]
