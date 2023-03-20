from django.urls import include, path
from rest_framework import routers

from api.testcode import views

router = routers.DefaultRouter()
router.register(r'notice', views.NoticeViewSet, basename="notice")

urlpatterns = [
    path('', include(router.urls)),
]