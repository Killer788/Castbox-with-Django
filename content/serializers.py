from rest_framework import serializers

from .models import Episode


class ShowEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = (
            'id',
            'image_source',
            'title',
            'description',
            'created_at',
            'updated_at',
        )
