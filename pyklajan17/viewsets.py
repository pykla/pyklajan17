from rest_framework import viewsets

from pyklajan17.models import Item
from pyklajan17.serializers import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.filter()
