from django.urls import include, path

from api.composite import views

urlpatterns = [
    path('create/', views.CoffeeBeanCreateViewSet.as_view()),
]