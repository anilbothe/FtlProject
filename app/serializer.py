from rest_framework import serializers
from app.models import UserData


class UserDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = '__all__'
        depth = 1