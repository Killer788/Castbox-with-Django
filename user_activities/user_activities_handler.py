from member_area.models import Channel
from content.models import Episode
from .models import Like, Playlist


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

    def create_playlist(self, title):
        user_playlists = self.user.playlists
        user_playlist_objects = user_playlists.all()
        playlist_titles = [playlist.title for playlist in user_playlist_objects]
        if title in playlist_titles:
            return 'You already have a playlist with this name. Please choose another name for the playlist'

        Playlist.objects.create(
            title=title,
            user=self.user,
        )

        return 'Playlist created successfully'
