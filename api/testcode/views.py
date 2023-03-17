from rest_framework.viewsets import ModelViewSet

from api.testcode.models import Notice
from api.testcode.serializers import NoticeSerializer


class NoticeViewSet(ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer