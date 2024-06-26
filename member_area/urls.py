from django.urls import path, include
from rest_framework import routers

from .views import sign_up_view, sign_in_view, sign_out_view, edit_profile_view, subscribe_to_channel_view
from .views import ChannelViewSet, FollowedChannelsViewSet


channel_router = routers.DefaultRouter()
channel_router.register('', ChannelViewSet)

followed_channels_router = routers.DefaultRouter()
followed_channels_router.register('', FollowedChannelsViewSet, basename='followed_channels')


urlpatterns = [
    path('signup/', sign_up_view, name='signup'),
    path('signin/', sign_in_view, name='signin'),
    path('signout/', sign_out_view, name='signout'),
    path('editprofile/', edit_profile_view, name='editprofile'),
    path('channels_list/', include(channel_router.urls)),
    path('subscribe/', subscribe_to_channel_view, name='subscribe'),
    path('show_followed_channels/', include(followed_channels_router.urls)),
]
