from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from api.composite.models import CoffeeBean
from api.composite.serializers import CoffeeBeanSerializer

# Create your views here.
class CoffeeBeanViewSet(ModelViewSet):    
    queryset = CoffeeBean.objects.all()
    serializer_class = CoffeeBeanSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        lookup_url_kwarg = ('origin', 'date')
        values = (self.request.data[kwarg] for kwarg in lookup_url_kwarg)

        filter_kwargs = dict(zip(lookup_url_kwarg, values))
        obj = get_object_or_404(queryset, **filter_kwargs)

        self.check_object_permissions(self.request, obj)

        return obj