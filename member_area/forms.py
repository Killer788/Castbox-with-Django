from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import BaseUser


class SignInForm(forms.Form):
    username = forms.CharField(label='Username', max_length=25)
    password = forms.CharField(label='Password', max_length=25)


class SignUpForm(UserCreationForm):
    class Meta:
        model = BaseUser
        fields = ('username', 'email', 'password1', 'password2')
