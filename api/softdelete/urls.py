from django.urls import include, path
from rest_framework import routers

from api.softdelete import views


router = routers.DefaultRouter()
router.register(r'bean', views.BeanViewSet, basename="sd-bean")
router.register(r'coffee', views.CoffeeViewSet, basename="sd-coffee")

urlpatterns = [
    path('', include(router.urls)),
]