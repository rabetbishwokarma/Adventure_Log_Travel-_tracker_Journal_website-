from django import forms
from .models import HotelExperience

class HotelForm(forms.ModelForm):
    class Meta:
        model = HotelExperience
        fields = ['trip', 'experience_details']





