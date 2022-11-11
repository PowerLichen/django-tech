from django.db import models


class CoffeeBean(models.Model):
    origin = models.CharField(max_length=100)
    date = models.DateField('get_bean_date', auto_now_add=True)
    price = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields= ['origin', 'date'],
                name = 'origin-date composite key'
            )
        ]

