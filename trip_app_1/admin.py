from django.contrib import admin
from .models import Trip, HotelExperience



@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('country', 'tour_area', 'duration', 'check_in', 'check_out')
    # Add more customization options as needed

@admin.register(HotelExperience)
class HotelExperienceAdmin(admin.ModelAdmin):
    list_display = ('trip', 'experience_details')
    # Add more customization options as needed
