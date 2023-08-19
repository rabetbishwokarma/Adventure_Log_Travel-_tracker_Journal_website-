from django.shortcuts import render, redirect
from .forms import HotelForm
from .models import Trip, HotelExperience

def index(request):
    # Implement your index view logic here
    return render(request, 'trip_app_1/index.html')

def create_hotel_experience(request):
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            # Set the trip based on user session or input
            experience.trip = Trip.objects.get(pk=1)  # Replace with actual trip selection
            experience.save()
            return redirect('success')  # Redirect to a success page or another view
    else:
        form = HotelForm()
    return render(request, 'trip_app_1/hotel_form.html', {'form': form})


