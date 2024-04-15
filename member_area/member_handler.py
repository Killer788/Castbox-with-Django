from .models import User


class MemberHandler:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def sign_up(self):
        result, message = self.sign_up_validation()
        if not result:
            return message

        User.objects.create(
            username=self.username,
            password=self.password,
        )

        return "Signed up successfully."

    def sign_up_validation(self):
        if len(self.username) < 8 or len(self.password) < 8:
            return False, "Username & Password must be at least 8 characters long."

        usernames = User.objects.filter(username__iexact=self.username)
        if usernames:
            return False, "Username already exists"

        return True, ''

    def sign_in(self):
        try:
            user = User.objects.get(username=self.username, password=self.password)

            return "Signed in successfully."

        except User.DoesNotExist:
            return "Username or Password is incorrect."
