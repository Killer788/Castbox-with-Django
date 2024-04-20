from django.urls import path, include

from .views import activities_view, choose_channel_for_activities_view, like_episodes_view, \
    add_episodes_to_playlist_view, create_playlist_view, delete_episodes_from_playlist_view

urlpatterns = [
    path('activities/', activities_view, name='activities'),
    path('activities/choose_channel/', choose_channel_for_activities_view, name='choose_channel_for_activities'),
    path('activities/choose_channel/like_episodes/', like_episodes_view, name='like_episodes'),
    path('activities/choose_channel/add_to_playlist', add_episodes_to_playlist_view, name='add_to_playlist'),
    path('activities/create_playlist/', create_playlist_view, name='create_playlist'),
    path('activities/delete_from_playlist/', delete_episodes_from_playlist_view, name='delete_episodes_from_playlist'),
]
