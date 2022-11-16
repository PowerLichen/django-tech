from io import BytesIO

from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
from rest_framework import serializers

from api.imageprocess.models import ImageProcess


class ImgProcSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageProcess
        fields = ['id', 'img']

    def img_resize(self, img: InMemoryUploadedFile) -> InMemoryUploadedFile:
        pil_img = Image.open(img).convert('RGBA')
        pil_img = pil_img.resize((1000,1000))

        new_img_io = BytesIO()
        pil_img.save(new_img_io, format='PNG')
        result = InMemoryUploadedFile(
            new_img_io, 'ImageField', img.name, 'image/png', new_img_io.getbuffer().nbytes, img.charset
        )

        return result


    def create(self, validated_data):
        result = self.img_resize(validated_data['img'])
        validated_data['img'] = result
        return super().create(validated_data)