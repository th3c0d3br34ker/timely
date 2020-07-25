from django.db import models
from django.contrib.postgres.fields import ArrayField


class Meetings(models.Model):
    id = models.IntegerField()
    start_time = models.DateTimeField(primary_key=True)
    stop_time = models.DateTimeField()
    organizer = models.CharField(max_length=9)
    members = ArrayField(models.CharField(max_length=9))
