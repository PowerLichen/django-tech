from django.db import models


class ExtraModel(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    password = models.CharField(max_length=50)


