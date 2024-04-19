from django.urls import path

from .views import channel_area_action_view


urlpatterns = [
    path('channel_area/', channel_area_action_view, name='channel_area'),
]
