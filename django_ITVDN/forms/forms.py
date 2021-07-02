from django.forms import ModelForm
from . import models
from django import forms
from .models import Human


class HumanForm(ModelForm):
    class Meta:
        model = Human
        fields = ['name', 'surname', 'age', 'company', 'salary']