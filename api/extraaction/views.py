from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from api.extraaction.models import ExtraModel
from api.extraaction.serializers import ExtraModelSerializer


class ExtraActionViewSet(ModelViewSet):
    queryset = ExtraModel.objects.all()
    serializer_class = ExtraModelSerializer


    @action(detail=False, methods=['get'], url_path='last')
    def get_last(self, request, *args, **kwargs):
        pass

    @action(detail=True, methods=['post'], url_path="password")
    def set_password(self, request, *args, **kwargs):
        pass