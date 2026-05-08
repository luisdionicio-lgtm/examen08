from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlatoViewSet, PedidoViewSet

router = DefaultRouter()
router.register('platos', PlatoViewSet)
router.register('pedidos', PedidoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]