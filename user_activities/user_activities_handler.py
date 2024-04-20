from member_area.models import Channel
from content.models import Episode
from .models import Like


class UserActivitiesHandler:
    def __init__(self, user):
        self.user = user

    def get_channel_episodes(self, channel_title):
        channel = Channel.objects.get(title=channel_title)
        channel_episodes = channel.episodes
        channel_episode_objects = channel_episodes.all()
        titles = [episode.title for episode in channel_episode_objects]
        if not titles:
            titles = ['No episodes to show']

        return titles

    def check_like(self, episode_title, channel_title):
        channel = Channel.objects.get(title=channel_title)
        episode = Episode.objects.get(title=episode_title, channel=channel)

        like_episode, created = Like.objects.get_or_create(user=self.user, episode=episode)
        if not created:
            if like_episode.is_liked:
                like_episode.is_liked = False
                like_episode.save()

                return 'You Unliked the episode successfully.'
            else:
                like_episode.is_liked = True
                like_episode.save()

        return 'You liked th episode successfully.'
