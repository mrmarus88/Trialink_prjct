from django import forms
from django.contrib.auth.models import User

 
class UserForm(forms.Form):
    login = forms.CharField(label="login")
    password = forms.CharField(label="password",widget=forms.PasswordInput)
    