from django.urls import path

from .views import sign_up_view, sign_in_view


urlpatterns = [
    path('signup/', sign_up_view),
    path('signin/', sign_in_view),
]
