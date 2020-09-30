from rest_framework import serializers
from app.models import UserData, ActivityPeriods


class ActivityPeriodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriods
        fields = ['start_time', 'end_time']


class UserDataSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodsSerializer(many=True)
    
    class Meta:
        model = UserData
        fields = ['id', 'real_name', 'tz', 'activity_periods']
        depth = 1
    
    
    def create(self, validated_data):
        profile_data = validated_data.pop('activity_periods')
        obj1 = ActivityPeriods.objects.create(**profile_data)
        obj2 = UserData.objects.create(activity_periods=obj1, **validated_data)
        return obj2
        

"""

 {
        "id": "W07QCRDA4",
        "real_name": "Glinda Southgood",
        "tz": "Asia/Kolkata",
        "activity_periods": [
            {
                "start_time": "2020-03-16T17:33:00Z",
                "end_time": "2020-03-16T18:02:00Z"
            },
            {
                "start_time": "2020-09-30T09:19:49Z",
                "end_time": "2020-09-30T13:19:52Z"
            }
        ]
    }


    """