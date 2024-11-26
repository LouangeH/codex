from django import forms
from hotel.models.room import Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['number', 'status', 'price_per_night', 'description']
