from .models import User
from user_activities.models import UserSubscribe


class MemberHandler:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def sign_up(self, user):
        User.objects.create(
            user=user,
        )

    def edit_profile(self, user, new_username, gender, age):
        user.username = new_username
        user.save()

        user_profile = User.objects.get(user=user)
        user_profile.gender = gender
        user_profile.age = age
        user_profile.save()

    def check_subscription(self, user, channel):
        user_subscribe, created = UserSubscribe.objects.get_or_create(
            user=user,
            channel=channel,
        )
        if created:
            if user_subscribe.is_subscribed:
                user_subscribe.is_subscribed = False
                user_subscribe.save()

                return 'Unsubscribed from the channel successfully.'
            else:
                user_subscribe.is_subscribed = True
                user_subscribe.save()

        return 'Subscribed to the channel successfully.'
