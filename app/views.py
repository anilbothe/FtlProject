from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import UserData
from app.serializer import UserDataSerializer

"""
Requirement 

    Design and implement a Django application with User and ActivityPeriod models, write
    a custom management command to populate the database with some dummy data, and design
    an API to serve that data in the json format given.
"""
class UserActivityApi(APIView):
    def get(self, request):
        obj = UserData.objects.all()
        result = UserDataSerializer(obj, many=True)
        return Response(result.data)
    
    def post(self, request):
        json = request.data
        serializer = UserDataSerializer(data=json)
        # print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer)
        return Response("Data Not Validated!")