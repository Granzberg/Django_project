from django import forms
from django.contrib.auth.models import User


class RegistrationUser(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['is_staff', 'is_active', 'date_joined']

    def __init__(self, email, *args, **kwargs):
        super(RegistrationUser, self).__init__(self, *args, **kwargs)
        self.fields['email'].queryset = User.objects.filter(email='email')


class SearchForm(forms.Form):
    search_field = forms.CharField(max_length=100)
