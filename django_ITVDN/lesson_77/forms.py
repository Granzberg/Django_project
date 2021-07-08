from . import models
from django import forms


class Accounts(forms.Form):
    name= forms.CharField(label="Your name", error_messages={'required':'Please enter your name'})
    email = forms.EmailField(error_messages={'required':'Please enter your available email'})
    password = forms.CharField(max_length=8, min_length=6, widget=forms.PasswordInput())
    age = forms.IntegerField(required=False, help_text="Please enter your current age")
    agreement = forms.BooleanField(required=False)


class Accounts2(forms.Form):
    name = forms.CharField(label="Your name", error_messages={'required':'Please enter your name'})
    email = forms.EmailField(error_messages={'required':'Please enter your available email'})
    password = forms.CharField(max_length=10, min_length=6, widget=forms.PasswordInput())
    birthday = forms.DateField(widget=forms.SelectDateWidget())
    gender = forms.ChoiceField(choices=[("1","male"), ("2", "female")])


class ReviewForm(forms.Form):
    file = forms.FileField(required=False)
    email = forms.EmailField(error_messages={'required':'Please enter your available email'})
    description = forms.CharField(max_length=10, min_length=6, required=False)
    rating = forms.IntegerField(required=False, help_text="Please enter rating")
    comment =forms.ChoiceField(choices=[("1","positive"), ("2", "negative")])
    telephone_number = forms.IntegerField(required=False, help_text="Please enter your telephone number")
