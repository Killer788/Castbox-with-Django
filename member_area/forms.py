from django import forms


class SignInForm(forms.Form):
    username = forms.CharField(label='Username', max_length=25)
    password = forms.CharField(label='Password', max_length=25)


class SignUpForm(SignInForm):
    repeat_password = forms.CharField(label='Repeat Password', max_length=25)
