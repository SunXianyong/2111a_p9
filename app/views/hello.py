import json
from channels.generic.websocket import WebsocketConsumer
from django.http import HttpResponse
from rest_framework import viewsets, serializers
from rest_framework.views import APIView
import time

from app.models import User


class UserPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserViewsSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserPointSerializer

    def list(self, request, *args, **kwargs):
        print(time.time(),"lai le ")
        time.sleep(3)
        return HttpResponse(f"{time.time()}")

