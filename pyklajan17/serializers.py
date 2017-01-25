from rest_framework import serializers

from pyklajan17.models import Item


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('name', 'volume')
