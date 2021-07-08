from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView
from .forms import Accounts, Accounts2


def my_form_accounts(request):
    form = Accounts(request.POST)
    return render(request, 'authorization.html', context={'form': form})

def my_second_form(request):
    form = Accounts2(request.POST)
    return render(request, 'accounts.html', context={'form':form})