from django.db import models
import _datetime as datetime

class Trip(models.Model):
    country = models.CharField(max_length=100)
    tour_area = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    # ... other fields

    def __str__(self):
        return self.country

class HotelExperience(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    experience_details = models.TextField()
    # ... other fields

    def __str__(self):
        return str(self.trip)
