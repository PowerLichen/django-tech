from rest_framework import serializers

from api.composite.models import CoffeeBean

class CoffeeBeanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeBean
        fields = ['id', 'origin', 'date', 'price' ]