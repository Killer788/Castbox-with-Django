from django.db.models import Prefetch
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend

from .forms import SignUpForm, EditProfileForm
from .member_handler import MemberHandler
from .models import BaseUser, Channel
from .serializers import ChannelSerializer, FollowedChannelsSerializer
from user_activities.models import UserSubscribe
from content.models import Episode


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
                return redirect('../')
            else:
                messages.info(request, 'Username or Password is incorrect.')

        context = {}
        return render(request, 'member_area/sign_in_form.html', context)


def sign_out_view(request):
    logout(request)
    return redirect('signin')


@login_required(login_url='../signin')
def edit_profile_view(request):
    message = ''
    username = request.user.username
    password = request.user.password
    member_handler = MemberHandler(username=username, password=password)
    form = EditProfileForm()
    if request.method == 'POST':
        form = EditProfileForm(request.POST)
        if form.is_valid() and not request.user.is_superuser:
            base_user_instance = BaseUser.objects.get(username=username)
            new_username = request.POST['new_username']
            gender = request.POST['gender']
            age = request.POST['age']
            member_handler.edit_profile(user=base_user_instance, new_username=new_username, gender=gender, age=age)
            message = 'Profile updated successfully.'

    context = {'form': form, 'message': message, 'username': username}
    return render(request, 'member_area/edit_profile_form.html', context)


class ChannelViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ChannelSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Channel.objects.prefetch_related(
        Prefetch('episodes', queryset=Episode.objects.filter(is_active=True).all())).filter(is_active=True).all()

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    filterset_fields = (
        'author',
    )
    search_fields = (
        'id',
        'title',
        'description',
    )


@login_required(login_url='../signin')
def subscribe_to_channel_view(request):
    message = ''
    username = request.user.username
    password = request.user.password

    channel = Channel()
    channels = channel.get_all_active_channels()
    titles = [channel.title for channel in channels]
    if not titles:
        titles = ['No channels to show']

    member_handler = MemberHandler(username=username, password=password)

    if request.method == 'POST':
        if not request.user.is_superuser:
            if titles[0] != 'No channels to show':
                base_user_instance = BaseUser.objects.get(username=username)
                title = request.POST['channel_titles']
                channel_instance = Channel.objects.get(title=title)
                message = member_handler.check_subscription(user=base_user_instance, channel=channel_instance)
            else:
                message = 'No channels in the database. Please create channels to continue.'

    context = {'titles': titles, 'message': message}
    return render(request, 'member_area/subscribe_form.html', context)


class FollowedChannelsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FollowedChannelsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        username = self.request.user.username
        user = BaseUser.objects.get(username=username)
        return UserSubscribe.objects.filter(user=user, is_subscribed=True).all()

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    search_fields = (
        'channel__title',
    )
