from django.urls import path

from .views import sign_up_view, sign_in_view, sign_out_view


urlpatterns = [
    path('signup/', sign_up_view, name='signup'),
    path('signin/', sign_in_view, name='signin'),
    path('signout/', sign_out_view, name='signout'),
]
