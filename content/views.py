from django.shortcuts import render, redirect

from .forms import ChannelAreaActionForm


# Create your views here.
def channel_area_action_view(request):
    form = ChannelAreaActionForm()
    if request.method == 'POST':
        form = ChannelAreaActionForm(request.POST)
        if form.is_valid() and not request.user.is_superuser:
            pass

    context = {'form': form}
    return render(request, 'content/channel_area_action_form.html', context)

