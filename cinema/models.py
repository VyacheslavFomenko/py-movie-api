from datetime import timedelta

from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    duration = models.IntegerField()


    #DurationField())

    # def set_duration_in_minutes(self, minutes):
    #     self.duration = timedelta(minutes=minutes)
    #
    # def get_duration_in_minutes(self):
    #     return self.duration.total_seconds() / 60
