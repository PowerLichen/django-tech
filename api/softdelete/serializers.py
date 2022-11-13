from rest_framework import serializers
from rest_framework.exceptions import NotAcceptable

from api.softdelete.models import Bean, Coffee


class BeanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bean
        fields = ['id', 'desc', 'origin', 'price']

class BeanDestroySerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        if instance.DEL_FL == True:
            raise NotAcceptable
        instance.DEL_FL = True
        instance.save()
        return instance


class CoffeeSerializer(serializers.ModelSerializer):
    bean = serializers.SerializerMethodField()

    class Meta:
        model = Coffee
        fields = ['id', 'bean', 'syrup', 'price']

    def get_bean(self, obj):
        if (obj.bean == None) or (obj.bean.DEL_FL == None):
            return None
        return obj.bean