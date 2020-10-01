from rest_framework import serializers
from app.models import UserData, ActivityPeriods


class ActivityPeriodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriods
        fields = ['start_time', 'end_time']
        # fields = '__all__'


class UserDataSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodsSerializer(many=True)
    
    class Meta:
        model = UserData
        fields = ['id', 'real_name', 'tz', 'activity_periods']
        # fields = '__all__'
        depth = 1
       