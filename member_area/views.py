from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import SignUpForm
from .member_handler import MemberHandler


# Create your views here.
def sign_up_view(request):
    if request.user.is_authenticated:
        print(request.user.username)
        return redirect('memberarea')
    else:
        form = SignUpForm()
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data['username']
                messages.success(request, f'Account was created for {user}')

                return redirect('signin')

        context = {'form': form}
        return render(request, 'member_area/sign_up_form.html', context)


def sign_in_view(request):
    if request.user.is_authenticated:
        return redirect('memberarea')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            else:
                messages.info(request, 'Username or Password is incorrect.')

        context = {}
        return render(request, 'member_area/sign_in_form.html', context)


def sign_out_view(request):
    logout(request)
    return redirect('login')
