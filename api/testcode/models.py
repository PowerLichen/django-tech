from django.db import models

# Create your models here.
class Notice(models.Model):
    title = models.CharField("notice title", max_length=150)
    context = models.TextField("notice content")