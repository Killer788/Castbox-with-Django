from django.urls import path

from .views import channel_area_action_view, create_channel_view, add_episode_view, mention_author_view, add_link_view


urlpatterns = [
    path('channel_area/', channel_area_action_view, name='channel_area'),
    path('channel_area/create_channel/', create_channel_view, name='create_channel'),
    path('channel_area/add_episode/', add_episode_view, name='add_episode'),
    path('channel_area/mention_author/', mention_author_view, name='mention_author'),
    path('channel_area/add_link/', add_link_view, name='add_link'),
]
