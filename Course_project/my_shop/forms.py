from django import forms
from django.contrib.auth.models import User


class RegistrationUser(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['is_staff', 'is_active', 'date_joined']


class SearchForm(forms.Form):
    search_field = forms.CharField(max_length=100)