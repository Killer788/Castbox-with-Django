from django.db.utils import IntegrityError

from member_area.models import Channel, ChannelLink
from .models import Episode


class ContentHandler:
    def __init__(self, user):
        self.user = user

    def create_channel(self, title, description):
        try:
            Channel.objects.create(title=title, description=description, author=self.user)

            return 'Channel created successfully'

        except IntegrityError:
            return 'You already have a channel with this name.'

    def add_link(self, channel_title, social_media, link):
        channel = Channel.objects.get(title=channel_title)

        channel_link, created = ChannelLink.objects.get_or_create(channel=channel, social_media=social_media, link=link)
        if created:
            return 'Link added to your channel successfully'

        return 'This link already exists'

    def add_episode(self, channel_title, episode_title, episode_description, episode_play_link):
        channel = Channel.objects.get(title=channel_title)

        try:
            Episode.objects.create(
                title=episode_title,
                description=episode_description,
                channel=channel,
                play_link=episode_play_link,
            )

            return 'Episode added to your channel successfully'
        except IntegrityError:
            return ('An episode this name already exists in the selected channel.'
                    ' Please choose another name for the episode')
