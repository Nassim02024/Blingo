from django import forms
from django.contrib.auth.forms import UserCreationForm
from users import models


class SingUpForm(UserCreationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Usename'}))
  email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
  password1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'password'}))
  password2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'confirme password'}))
  witget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'})
  class Meta:
    model = models.User
    fields = ['email', 'username', 'password1', 'password2']

  