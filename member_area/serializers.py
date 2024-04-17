from rest_framework import serializers

from .models import Channel, BaseUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = ('username',)


class ChannelSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Channel
        fields = '__all__'
