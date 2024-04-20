from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from rest_framework import viewsets, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend

from .forms import ChannelAreaActionForm, CreateChannelForm, AddLinkForm, AddEpisodeForm
from member_area.models import BaseUser, Channel
from .content_handler import ContentHandler
from .serializers import ShowEpisodesSerializer
from .models import Episode


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
    content_handler = ContentHandler(user=user)

    user_channels = content_handler.get_user_channels()
    titles = content_handler.get_channel_titles(channels=user_channels)

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
    try:
        channel_title = request.session['channel_title']
        if channel_title == '':
            raise KeyError
    except KeyError:
        return redirect('choose_your_channel')

    message = ''
    username = request.user.username
    user = BaseUser.objects.get(username=username)
    content_handler = ContentHandler(user=user)

    channel = Channel.objects.get(title=channel_title)
    channel_episodes = channel.episodes
    channel_episode_objects = channel_episodes.all()
    titles = [episode.title for episode in channel_episode_objects]
    if not titles:
        titles = ['No episodes to show']

    author_objects = BaseUser.objects.all()
    authors = [author.username for author in author_objects]
    if not authors:
        authors = ['No authors to show']

    if request.method == 'POST':
        if not request.user.is_superuser:
            if titles[0] != 'No episodes to show' and authors[0] != 'No authors to show':
                episode_title = request.POST['episode_titles']
                author_username = request.POST['author_usernames']
                message = content_handler.mention_author(
                    channel=channel,
                    author_username=author_username,
                    episode_title=episode_title
                )

                request.session['channel_title'] = ''
                redirect('choose_your_channel')
            else:
                message = 'Please make sure that there are authors and episodes to choose from'

        else:
            message = 'This action is unavailable for the admin'

    context = {'titles': titles, 'authors': authors, 'message': message}
    return render(request, 'content/mention_author_form.html', context)


@login_required(login_url='../../../memberarea/signin')
def choose_channel_to_mention_author_view(request):
    message = ''
    username = request.user.username
    user = BaseUser.objects.get(username=username)
    content_handler = ContentHandler(user=user)

    user_channels = content_handler.get_user_channels()
    titles = content_handler.get_channel_titles(channels=user_channels)

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
    content_handler = ContentHandler(user=user)

    user_channels = content_handler.get_user_channels()
    titles = content_handler.get_channel_titles(channels=user_channels)
    media = [media[0] for media in settings.SOCIAL_MEDIA_CHOICES]

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


@login_required(login_url='../../memberarea/signin')
def choose_channel_to_show_episodes(request):
    message = ''
    channels = Channel.objects.all()
    titles = [channel.title for channel in channels]
    if not titles:
        titles = ['No channels to show']

    if request.method == 'POST':
        if not request.user.is_superuser:
            if titles[0] != 'No channels to show':
                request.session['channel_title_for_episode'] = request.POST['channel_titles']
                return redirect('show_episodes/')
            else:
                message = 'No channels in the database. Please create channels to continue.'

        else:
            message = 'This action is unavailable for the admin'

    context = {'titles': titles, 'message': message}
    return render(request, 'content/choose_channel_for_episodes_form.html', context)


class ShowEpisodesView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ShowEpisodesSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        try:
            channel_title = self.request.session['channel_title_for_episode']
        except KeyError:
            raise Exception('404 Error')

        channel = Channel.objects.get(title=channel_title)
        return Episode.objects.filter(channel=channel, is_active=True).all()
