from django.db.utils import IntegrityError

from member_area.models import Channel, ChannelLink
from .models import Episode, EpisodeOtherAuthor
from member_area.models import BaseUser


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
        channel_episodes = channel.episodes
        channel_episode_objects = channel_episodes.all()
        episode_titles = [episode.title for episode in channel_episode_objects]
        if episode_title in episode_titles:
            return ('An episode with this name already exists in the selected channel.'
                    'Please choose another name for the episode')

        Episode.objects.create(
            title=episode_title,
            description=episode_description,
            channel=channel,
            play_link=episode_play_link,
        )

        return 'Episode added to your channel successfully'

    def get_user_channels(self):
        channel = Channel()
        channels = channel.get_all_active_channels()
        user_channels = list()
        for channel in channels:
            if channel.author == self.user:
                user_channels.append(channel)

        return user_channels

    def get_channel_titles(self, channels):
        titles = [channel.title for channel in channels]
        if not titles:
            titles = ['No channels to show']

        return titles

    def mention_author(self, channel,  author_username, episode_title):
        author = BaseUser.objects.get(username=author_username)
        episode = Episode.objects.get(channel=channel, title=episode_title)

        mention_object, created = EpisodeOtherAuthor.objects.get_or_create(author=author, episode=episode)
        if created:
            return 'This author is already mentioned for this episode'

        return 'Author mentioned successfully'
