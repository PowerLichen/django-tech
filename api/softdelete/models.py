from django.db import models

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(DEL_FL=False)

class Bean(models.Model):
    desc = models.CharField(max_length=200)
    origin = models.CharField(max_length=100)
    price = models.IntegerField()
    DEL_FL = models.BooleanField(default=False)

    all_objects = models.Manager()
    objects = ActiveManager()

class Coffee(models.Model):
    bean = models.ForeignKey('Bean', related_name='coffee-bean', on_delete=models.SET_NULL, null=True)
    syrup = models.CharField(max_length=10)
    price = models.IntegerField()
