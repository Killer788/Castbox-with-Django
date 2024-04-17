from .models import User


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
