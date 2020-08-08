from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.forms import Form, CharField
from django.views import View
from django.shortcuts import render

class HyperSignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'signup.html'

class HyperLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'

class JobForm(Form):
    description = CharField()

class HomeView(View):
    def get(self, request, *args, **kwargs):
        job_form = JobForm()
        return render(request, 'home.html', context={'job_form': job_form})
