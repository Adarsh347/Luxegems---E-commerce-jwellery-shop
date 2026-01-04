from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'from-control my-2','placeholder':'Enter Username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'from-control my-2','placeholder':'Enter email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'from-control my-2','placeholder':'Enter the password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'from-control my-2','placeholder':'conform the password'}))

class meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']

    