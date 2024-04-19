from member_area.models import Channel, ChannelLink


class ContentHandler:
    def __init__(self, user):
        self.user = user

    def create_channel(self, title, description):
        channel, created = Channel.objects.get_or_create(title=title, description=description, author=self.user)
        if created:
            return 'Channel created successfully'

        return 'Channel already exists'

    def add_link(self, channel_title, social_media, link):
        channel = Channel.objects.get(title=channel_title)

        channel_link, created = ChannelLink.objects.get_or_create(channel=channel, social_media=social_media, link=link)
        if created:
            return 'Link added to your channel successfully'

        return 'This link already exists'
