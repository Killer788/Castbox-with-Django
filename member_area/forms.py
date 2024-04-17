from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import BaseUser, Channel


class SignUpForm(UserCreationForm):
    class Meta:
        model = BaseUser
        fields = ('username', 'email', 'password1', 'password2')


class EditProfileForm(forms.Form):
    GENDER_CHOICES = (
        ('Hide', 'Hide'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    AGE_CHOICES = (
        ('Hide', 'Hide'),
        ('Before 1950', 'Before 1950'),
        ('1950 - 1959', '1950 - 1959'),
        ('1960 - 1969', '1960 - 1969'),
        ('1970 - 1979', '1970 - 1979'),
        ('1980 - 1989', '1980 - 1989'),
        ('1990 - 1999', '1990 - 1999'),
        ('After 2000', 'After 2000'),
    )

    gender = forms.CharField(label='Gender', widget=forms.Select(choices=GENDER_CHOICES), initial='Hide')
    age = forms.CharField(label='Age', widget=forms.Select(choices=AGE_CHOICES), initial='Hide')


class SubscribeForm(forms.Form):
    try:
        channel_instances = Channel.objects.filter(is_active=True).all()
        choose_channel = [('Choose a channel', 'Choose a channel'),]
        titles = [(channel.title, channel.title) for channel in channel_instances]
        channel_choices_list = choose_channel + titles
        CHANNELS_CHOICES = tuple(channel_choices_list)
    except Exception as e:
        CHANNELS_CHOICES = (
            ('No channels to show', 'No channels to show'),
        )

    channels = forms.CharField(
        label='Channels',
        widget=forms.Select(choices=CHANNELS_CHOICES),
        initial='Choose a channel'
    )
