from django.urls import include, path
from rest_framework import routers

from api.extraaction import views


router = routers.DefaultRouter()
router.register(r"", views.ExtraActionViewSet, basename="extra-action")

urlpatterns = [
    path("", include(router.urls)),
]