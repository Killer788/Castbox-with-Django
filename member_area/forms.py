from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import BaseUser


class SignUpForm(UserCreationForm):
    class Meta:
        model = BaseUser
        fields = ('username', 'email', 'password1', 'password2')
