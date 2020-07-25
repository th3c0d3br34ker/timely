from django.shortcuts import render
from .models import Meetings
from .serializers import MeetingsSerializer
from rest_framework import generics


class MeetingsListCreate(generics.ListCreateAPIView):
    queryset = Meetings.objects.all()
    serializer_class = MeetingsSerializer


class MeetingDetail(generics.RetrieveAPIView):
    queryset = Meetings.objects.all()
    serializer_class = MeetingsSerializer
