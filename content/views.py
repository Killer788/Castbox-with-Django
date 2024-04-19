from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .forms import ChannelAreaActionForm, CreateChannelForm, AddLinkForm, AddEpisodeForm
from member_area.models import BaseUser, Channel
from .content_handler import ContentHandler


# Create your views here.
@login_required(login_url='../../memberarea/signin')
def channel_area_action_view(request):
    message = ''
    form = ChannelAreaActionForm()
    if request.method == 'POST':
        form = ChannelAreaActionForm(request.POST)
        if form.is_valid() and not request.user.is_superuser:
            data = form.cleaned_data['actions']
            if data == 'create_channel':
                return redirect('create_channel')
            elif data == 'add_episode':
                return redirect('add_episode')
            elif data == 'mention_author':
                return redirect('choose_your_channel')
            elif data == 'add_link':
                return redirect('add_link')
        else:
            message = 'This action is unavailable for the admin'

    context = {'form': form, 'message': message}
    return render(request, 'content/channel_area_action_form.html', context)


@login_required(login_url='../../../memberarea/signin')
def create_channel_view(request):
    message = ''
    username = request.user.username
    user = BaseUser.objects.get(username=username)
    content_handler = ContentHandler(user=user)

    form = CreateChannelForm()
    if request.method == 'POST':
        form = CreateChannelForm(request.POST)
        if form.is_valid() and not request.user.is_superuser:
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            message = content_handler.create_channel(title=title, description=description)
        else:
            message = 'This action is unavailable for the admin'

    context = {'form': form, 'message': message}
    return render(request, 'content/create_channel_form.html', context)


@login_required(login_url='../../../memberarea/signin')
def add_episode_view(request):
    message = ''
    username = request.user.username
    user = BaseUser.objects.get(username=username)

    channel = Channel()
    channels = channel.get_all_active_channels()
    user_channels = list()
    for channel in channels:
        if channel.author == user:
            user_channels.append(channel)

    titles = [channel.title for channel in user_channels]
    if not titles:
        titles = ['No channels to show']

    content_handler = ContentHandler(user=user)
    form = AddEpisodeForm()
    if request.method == 'POST':
        form = AddEpisodeForm(request.POST)
        if form.is_valid() and not request.user.is_superuser:
            if titles[0] != 'No channels to show':
                channel_title = request.POST['channel_titles']
                episode_title = form.cleaned_data['title']
                episode_description = form.cleaned_data['description']
                episode_play_link = form.cleaned_data['play_link']

                message = content_handler.add_episode(
                    channel_title=channel_title,
                    episode_title=episode_title,
                    episode_description=episode_description,
                    episode_play_link=episode_play_link,
                )
            else:
                message = 'No channels in the database. Please create channels to continue.'

        else:
            message = 'This action is unavailable for the admin'

    context = {'titles': titles, 'form': form, 'message': message}
    return render(request, 'content/add_episode_form.html', context)


@login_required(login_url='../../../../memberarea/signin')
def mention_author_view(request):
    return HttpResponse(request.session['channel_title'])


@login_required(login_url='../../../memberarea')
def choose_channel_to_add_episode_view(request):
    message = ''
    username = request.user.username
    user = BaseUser.objects.get(username=username)

    channel = Channel()
    channels = channel.get_all_active_channels()
    user_channels = list()
    for channel in channels:
        if channel.author == user:
            user_channels.append(channel)

    titles = [channel.title for channel in user_channels]
    if not titles:
        titles = ['No channels to show']
    if request.method == 'POST':
        if not request.user.is_superuser:
            if titles[0] != 'No channels to show':
                request.session['channel_title'] = request.POST['channel_titles']
                return redirect('mention_author')
            else:
                message = 'No channels in the database. Please create channels to continue.'

        else:
            message = 'This action is unavailable for the admin'

    context = {'titles': titles, 'message': message}
    return render(request, 'content/choose_channel_form.html', context)


@login_required(login_url='../../../memberarea/signin')
def add_link_view(request):
    message = ''
    username = request.user.username
    user = BaseUser.objects.get(username=username)

    channel = Channel()
    channels = channel.get_all_active_channels()
    user_channels = list()
    for channel in channels:
        if channel.author == user:
            user_channels.append(channel)

    titles = [channel.title for channel in user_channels]
    if not titles:
        titles = ['No channels to show']

    media = [media[0] for media in settings.SOCIAL_MEDIA_CHOICES]

    content_handler = ContentHandler(user=user)
    form = AddLinkForm()
    if request.method == 'POST':
        form = AddLinkForm(request.POST)
        if form.is_valid() and not request.user.is_superuser:
            if titles[0] != 'No channels to show':
                channel_title = request.POST['channel_titles']
                link = form.cleaned_data['link']
                social_media = request.POST['social_media']
                message = content_handler.add_link(channel_title=channel_title, social_media=social_media, link=link)
            else:
                message = 'No channels in the database. Please create channels to continue.'
        else:
            message = 'This action is unavailable for the admin'

    context = {'titles': titles, 'media': media, 'form': form, 'message': message}
    return render(request, 'content/add_link_form.html', context)

