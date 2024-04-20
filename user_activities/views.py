from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required

from member_area.models import Channel


# Create your views here.
@login_required(login_url='../../memberarea/signin')
def likes_view(request):
    message = ''
    channels = Channel.objects.all()
    titles = [channel.title for channel in channels]
    if not titles:
        titles = ['No channels to show']

    if request.method == 'POST':
        if not request.user.is_superuser:
            if titles[0] != 'No channels to show':
                request.session['channel_title_for_like'] = request.POST['channel_titles']
                return redirect('like_episodes')
            else:
                message = 'No channels in the database. Please create channels to continue.'

        else:
            message = 'This action is unavailable for the admin'

    context = {'titles': titles, 'message': message}
    return render(request, 'user_activities/choose_channel_for_liking_episodes.html', context)


@login_required(login_url='../../../memberarea/signin')
def like_episodes_view(request):
    return HttpResponse(request.session['channel_title_for_like'])
