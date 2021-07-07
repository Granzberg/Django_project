from django.forms import ModelForm
from . import models
from django import forms


class Accounts(forms.Form):
    name= forms.CharField
    email = forms.EmailField
    password = forms.PasswordInput
    age = forms.IntegerField
