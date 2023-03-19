from rest_framework import serializers

from admin_panel.models import TlgUser


class TlgUserSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для модели TlgUser
    """
    class Meta:
        model = TlgUser
        fields = '__all__'
