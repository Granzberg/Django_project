import datetime

from django.db import models
from django.forms import ModelForm
from django.db import models


class Accounts22(models.Model):
    SEX_CHOICES = (
        ("1","male"),
        ("2", "female"),)
    name = models.CharField(blank=True, max_length=60)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=10, blank=True)
    birthday = models.DateField(default=datetime.date(year=1980,month=12,day=30), blank=True)
    gender = models.CharField(max_length=60,choices= SEX_CHOICES)


class AccountsModel(ModelForm):
    class Meta:
        model = Accounts22
        fields = ('__all__')
        labels = {
            'name': ('Your name'),
        }
        error_messages = {
            'name': {'required': ('Please enter your name'),},
            'email': {'required': ('Please enter your available email'),},
            'password': {'required':('Enter a password 6 and 10 symbols')},
        }