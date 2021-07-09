from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView
from .forms import Accounts, Accounts2, ReviewForm
from .models import AccountsModel


def my_form_accounts(request):
    form = Accounts(request.POST)
    return render(request, 'authorization.html', context={'form': form})

def my_second_form(request):
    form = Accounts(request.POST)
    return render(request, 'accounts.html', context={'form':form})


class MyModelform(FormView):
    form_class = AccountsModel
    template_name = "accounts2.html"


def Review(request):
    form = ReviewForm(request.POST)
    return render(request, 'review.html', context={'form':form})
