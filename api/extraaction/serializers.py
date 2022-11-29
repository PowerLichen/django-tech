from rest_framework import serializers

from api.extraaction.models import ExtraModel

class ExtraModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraModel
        fields = ['id', 'title', 'desc', 'password' ]