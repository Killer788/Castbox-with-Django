from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

from .forms import SignUpForm, SignInForm
from .member_handler import MemberHandler


# Create your views here.
def sign_up_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'member_area/sign_up_form.html', context)


def sign_in_view(request):
    message = ''
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            member_handler = MemberHandler(username=username, password=password)
            message = member_handler.sign_in()
    else:
        form = SignInForm()

    return render(request, 'member_area/sign_in_form.html', {'form': form, 'message': message})

