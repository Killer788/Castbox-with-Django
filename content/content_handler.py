from member_area.models import Channel


class ContentHandler:
    def __init__(self, user):
        self.user = user

    def create_channel(self, title, description):
        channel, created = Channel.objects.get_or_create(title=title, description=description, author=self.user)
        if created:
            return 'Channel created successfully'

        return 'Channel already exists'
