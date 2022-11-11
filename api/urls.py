from django.urls import include, path

urlpatterns = [
    path('composite/', include('api.composite.urls')),
]