from django import forms


class ActivitiesForm(forms.Form):
    OPTIONS_CHOICES = (
        ('create_playlist', 'Create A Playlist'),
        ('choose_channel', 'Choose A Channel For Other Activities'),
        ('delete_episodes_from_playlist', 'Delete Episodes From Playlist'),
    )

    options = forms.CharField(label='Options', widget=forms.Select(choices=OPTIONS_CHOICES))


class ChooseChannelForActivitiesForm(forms.Form):
    ACTIVITY_CHOICES = (
        ('add_episodes_to_playlist', 'Add Episodes To Your Playlist'),
        ('like_episode', 'Like Episodes'),
    )

    activity = forms.CharField(label='Activities', widget=forms.Select(choices=ACTIVITY_CHOICES))


class CreatePlaylistForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
