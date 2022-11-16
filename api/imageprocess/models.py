from django.db import models
from io import BytesIO


class ImageProcess(models.Model):
    img = models.ImageField('img', upload_to='image/')