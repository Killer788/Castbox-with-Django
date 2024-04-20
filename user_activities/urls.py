from django.urls import path, include

from .views import likes_view, like_episodes_view


urlpatterns = [
    path('likes/', likes_view, name='likes'),
    path('like_episodes/', like_episodes_view, name='like_episodes'),
]
