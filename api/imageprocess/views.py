from rest_framework.viewsets import ModelViewSet

from api.imageprocess.models import ImageProcess
from api.imageprocess.serializers import ImgProcSerializer

class ImgprocViewSet(ModelViewSet):
    queryset = ImageProcess.objects.all()
    serializer_class = ImgProcSerializer