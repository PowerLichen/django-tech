from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from api.extraaction.models import ExtraModel
from api.extraaction.serializers import ExtraModelSerializer
from api.extraaction.serializers import ExtraModelPasswordSerializer


class ExtraActionViewSet(ModelViewSet):
    queryset = ExtraModel.objects.all()
    serializer_class = ExtraModelSerializer

    def get_serializer_class(self):
        if self.action == "set_password":
            return ExtraModelPasswordSerializer
        return super().get_serializer_class()

    @action(detail=False, methods=['get'], url_path='last')
    def get_last(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @action(detail=True, methods=['post'], url_path="password")
    def set_password(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
