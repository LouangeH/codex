from django import forms
from hotel.models.reservation import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['room', 'client_name', 'client_id_type', 'client_id_number', 'start_date', 'end_date', 'is_confirmed']
