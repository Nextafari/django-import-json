from django.urls import include, path
from rest_framework.routers import DefaultRouter

from pilotlog import views

router = DefaultRouter()
router.register("aircraft", views.AirCraftViewSet, "aircraft_data")


urlpatterns = [
    path("", include(router.urls)),
]
