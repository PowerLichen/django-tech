from rest_framework import serializers

from api.testcode.models import Notice


class NoticeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Notice
        fields = ["id", "user", "title", "context"]