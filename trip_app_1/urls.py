# trip_app_1/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # ...
    path('create/hotel/', views.create_hotel_experience, name='create_hotel'),
    # ...
]
