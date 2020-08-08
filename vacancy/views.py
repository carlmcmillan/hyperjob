from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.views import View
from vacancy.models import Vacancy


class MenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancy/index.html')


class VacanciesView(View):
    def get(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.all()
        return render(request, 'vacancy/vacancies.html', context={'vacancies': vacancies})


class CreateVacancyView(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            vacancy = Vacancy(description=request.POST['description'], author=request.user)
            vacancy.save()
            return redirect('/home')
        else:
            return HttpResponseForbidden()
