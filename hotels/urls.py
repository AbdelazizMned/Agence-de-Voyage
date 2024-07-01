from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HotelViewSet, RoomViewSet, PriceViewSet, SeasonViewSet
router = DefaultRouter()
router.register(r'hotels', HotelViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'seasons', SeasonViewSet)
router.register(r'roompricings', PriceViewSet)
urlpatterns = [
    path("", include(router.urls)),
]
