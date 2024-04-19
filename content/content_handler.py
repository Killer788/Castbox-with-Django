from member_area.models import Channel, ChannelLink
from django.db.utils import IntegrityError


class ContentHandler:
    def __init__(self, user):
        self.user = user

    def create_channel(self, title, description):
        try:
            channel = Channel.objects.create(title=title, description=description, author=self.user)
            
            return 'Channel created successfully'

        except IntegrityError:
            return 'Channel already exists'

    def add_link(self, channel_title, social_media, link):
        channel = Channel.objects.get(title=channel_title)

        channel_link, created = ChannelLink.objects.get_or_create(channel=channel, social_media=social_media, link=link)
        if created:
            return 'Link added to your channel successfully'

        return 'This link already exists'
