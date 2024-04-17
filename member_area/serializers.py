from rest_framework import serializers

from .models import Channel, BaseUser
from user_activities.models import UserSubscribe


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = ('username',)


class ChannelSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    channel_links = serializers.StringRelatedField(many=True)
    episodes = serializers.StringRelatedField(many=True)

    class Meta:
        model = Channel
        fields = (
            'id',
            'image_source',
            'title',
            'description',
            'author',
            'channel_links',
            'episodes',
        )


class ChannelTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('title',)


class FollowedChannelsSerializer(serializers.ModelSerializer):
    channel = ChannelTitleSerializer()

    class Meta:
        model = UserSubscribe
        fields = (
            'channel',
        )

    def get_username(self):
        return self.context['request'].user.username
