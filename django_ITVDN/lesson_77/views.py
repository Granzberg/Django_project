from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView
from . import forms


def my_form_accounts(request):
    form = forms.Accounts(request.GET)
    return render(request, 'authorization.html', context={'form': form})
