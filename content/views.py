from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import ChannelAreaActionForm


# Create your views here.
@login_required(login_url='../../memberarea/signin')
def channel_area_action_view(request):
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
                return redirect('mention_author')
            elif data == 'add_link':
                return redirect('add_link')

    context = {'form': form}
    return render(request, 'content/channel_area_action_form.html', context)


@login_required(login_url='../../../memberarea/signin')
def create_channel_view(request):
    pass


@login_required(login_url='../../../memberarea/signin')
def add_episode_view(request):
    pass


@login_required(login_url='../../../memberarea/signin')
def mention_author_view(request):
    pass


@login_required(login_url='../../../memberarea/signin')
def add_link_view(request):
    pass
