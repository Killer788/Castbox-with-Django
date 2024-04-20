from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required

from member_area.models import Channel
from .forms import ActivitiesForm, ChooseChannelForActivitiesForm


# Create your views here.
@login_required(login_url='../../memberarea/signin')
def activities_view(request):
    message = ''
    form = ActivitiesForm()
    if request.method == 'POST':
        form = ActivitiesForm(request.POST)
        if form.is_valid() and not request.user.is_superuser:
            data = form.cleaned_data['options']
            if data == 'create_playlist':
                return redirect('create_playlist')
            elif data == 'choose_channel':
                return redirect('choose_channel_for_activities')
            elif data == 'delete_episodes_from_playlist':
                return redirect('delete_episodes_from_playlist')
        else:
            message = 'This action is unavailable for the admin'

    context = {'form': form, 'message': message}
    return render(request, 'user_activities/activities_form.html', context)


@login_required(login_url='../../../memberarea/signin')
def choose_channel_for_activities_view(request):
    message = ''
    channels = Channel.objects.all()
    titles = [channel.title for channel in channels]
    if not titles:
        titles = ['No channels to show']

    form = ChooseChannelForActivitiesForm()
    if request.method == 'POST':
        form = ChooseChannelForActivitiesForm(request.POST)
        if form.is_valid() and not request.user.is_superuser:
            if titles[0] != 'No channels to show':
                data = form.cleaned_data['activity']
                if data == 'add_episodes_to_playlist':
                    request.session['channel_title_for_adding_to_playlist'] = request.POST['channel_titles']
                    return redirect('add_to_playlist')
                elif data == 'like_episode':
                    request.session['channel_title_for_activities'] = request.POST['channel_titles']
                    return redirect('like_episodes')
            else:
                message = 'No channels in the database. Please create channels to continue.'

        else:
            message = 'This action is unavailable for the admin'

    context = {'titles': titles, 'form': form, 'message': message}
    return render(request, 'user_activities/choose_channel_for_activities.html', context)


@login_required(login_url='../../../../memberarea/signin')
def like_episodes_view(request):
    return HttpResponse(request.session['channel_title_for_activities'])


@login_required(login_url='../../../../memberarea/signin')
def add_episodes_to_playlist_view(request):
    return HttpResponse(request.session['channel_title_for_adding_to_playlist'])


@login_required(login_url='../../../memberarea/signin')
def create_playlist_view(request):
    return HttpResponse('Create your playlist here')


@login_required(login_url='../../../memberarea/signin')
def delete_episodes_from_playlist_view(request):
    return HttpResponse('Delete episodes from your playlist here')
