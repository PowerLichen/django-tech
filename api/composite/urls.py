from django.urls import include, path
from rest_framework import routers

from api.composite import views


router = routers.DefaultRouter()
router.register(r'', views.CoffeeBeanViewSet, basename="composite-bean")

urlpatterns = [ 
    path('', include(router.urls)),
]