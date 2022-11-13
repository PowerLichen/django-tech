from django.urls import include, path

urlpatterns = [
    path('composite/', include('api.composite.urls')),
    path('softdelete/', include('api.softdelete.urls')),
]