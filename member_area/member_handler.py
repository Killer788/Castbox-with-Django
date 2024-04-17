from .models import User


class MemberHandler:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def sign_up(self, user):
        User.objects.create(
            user=user,
        )

    def sign_in(self):
        pass
