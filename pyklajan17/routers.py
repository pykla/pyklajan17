from rest_framework import routers

from pyklajan17.viewsets import ItemViewSet

router = routers.DefaultRouter()
router.register(r'stock', ItemViewSet)
