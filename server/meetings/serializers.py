from rest_framework import serializers
from .models import Meetings


class MeetingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meetings
        fields = ("id", "start_time", "stop_time", "organizer", "members")
