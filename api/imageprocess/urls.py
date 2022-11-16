from django.urls import include, path
from rest_framework import routers

from api.imageprocess import views


router = routers.DefaultRouter()
router.register(r'', views.ImgprocViewSet, basename="imgproc")

urlpatterns = [ 
    path('', include(router.urls)),
]