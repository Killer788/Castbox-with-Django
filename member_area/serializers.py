from rest_framework import serializers

from .models import Channel, BaseUser


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
