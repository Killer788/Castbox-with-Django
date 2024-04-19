from django import forms


class ChannelAreaActionForm(forms.ModelForm):
    ACTION_CHOICES = (
        ('create_channel', 'Create A New Channel'),
        ('add_episode', 'Add Episodes To A Channel'),
        ('mention_author', 'Mention Other Authors For An Episode'),
    )

    actions = forms.CharField(label='Actions', widget=forms.Select(choices=ACTION_CHOICES), initial='create_channel')
