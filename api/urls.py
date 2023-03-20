from django.urls import include, path

urlpatterns = [
    path('composite/', include('api.composite.urls')),
    path('softdelete/', include('api.softdelete.urls')),
    path('imgproc/', include('api.imageprocess.urls')),
    path('extra-action/', include('api.extraaction.urls')),
]