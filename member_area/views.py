from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm, EditProfileForm
from .member_handler import MemberHandler
from .models import BaseUser


# Create your views here.
def sign_up_view(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        print(request.user.username)
        return redirect('../')
    else:
        form = SignUpForm()
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                messages.success(request, f'Account was created for {username}')

                base_user_instance = BaseUser.objects.get(username=username)
                member_handler = MemberHandler(username=username, password=password)
                member_handler.sign_up(user=base_user_instance)

                return redirect('signin')

        context = {'form': form}
        return render(request, 'member_area/sign_up_form.html', context)


def sign_in_view(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        return redirect('../')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                redirect('../')
            else:
                messages.info(request, 'Username or Password is incorrect.')

        context = {}
        return render(request, 'member_area/sign_in_form.html', context)


def sign_out_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def edit_profile_view(request):
    message = ''
    username = request.user.username
    password = request.user.password
    member_handler = MemberHandler(username=username, password=password)
    form = EditProfileForm()
    if request.method == 'POST':
        form = EditProfileForm(request.POST)
        if form.is_valid():
            pass

    return render(request, 'member_area/edit_profile_form.html', {'form': form, 'message': message})
