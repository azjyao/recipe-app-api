from rest_framework import serializers

from core.models import Tag


class TagSerializer(serializers.ModelSerializer):
    """Serailizer for tag objects"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        ready_only_fields = ('id')
