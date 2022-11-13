from django.db import models


class Bean(models.Model):
    desc = models.CharField(max_length=200)
    origin = models.CharField(max_length=100)
    price = models.IntegerField()

class Coffee(models.Model):
    bean = models.ForeignKey('Bean', related_name='coffee-bean', on_delete=models.SET_NULL, null=True)
    syrup = models.CharField(max_length=10)
    price = models.IntegerField()
