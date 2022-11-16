from rest_framework.viewsets import ModelViewSet

from api.softdelete.models import Bean, Coffee
from api.softdelete.serializers import BeanSerializer, BeanDestroySerializer, CoffeeSerializer


class BeanViewSet(ModelViewSet):
    queryset = Bean.objects.all()
    serializer_class = BeanSerializer

    def get_serializer_class(self):
        if hasattr(self, 'action') == False:
            return self.serializer_class
            
        if self.action == 'destroy':
            return BeanDestroySerializer        
        return self.serializer_class

    def destroy(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class CoffeeViewSet(ModelViewSet):
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer