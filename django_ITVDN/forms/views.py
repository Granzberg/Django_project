from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from . import models
from django.views import generic


def form(request):
    form_for_humans = forms.HumanForm
    context = {
        'form_for_humans':form_for_humans,
    }
    return render(request, 'human_form.html', context)


def index_human(request):
    form = forms.HumanForm(request.POST)
    result = "Данные сохранены %s" %request.path
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            print(data['name'])
            return HttpResponse("Сохранено! %s" %request.path)
