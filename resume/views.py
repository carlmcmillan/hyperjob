from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.views import View
from resume.models import Resume


class ResumesView(View):
    def get(self, request, *args, **kwargs):
        resumes = Resume.objects.all()
        return render(request, 'resume/resumes.html', context={'resumes': resumes})


class CreateResumeView(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and not request.user.is_staff:
            resume = Resume(description=request.POST['description'], author=request.user)
            resume.save()
            return redirect('/home')
        else:
            return HttpResponseForbidden()
