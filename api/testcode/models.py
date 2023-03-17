from django.contrib.auth import get_user_model
from django.db import models


class Notice(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField("notice title", max_length=150)
    context = models.TextField("notice content")