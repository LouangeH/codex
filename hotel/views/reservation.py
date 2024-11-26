from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from hotel.models.reservation import Reservation
from django.utils.timezone import now, timedelta
from hotel.models.reservation import Reservation
from hotel.forms.reservation_form import ReservationForm


# Liste des réservations
class ReservationListView(ListView):
    model = Reservation
    template_name = 'hotel/reservation_list.html'
    context_object_name = 'reservations'


# Création d'une réservation
class ReservationCreateView(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'hotel/reservation_form.html'
    success_url = reverse_lazy('hotel:reservation_list')


# Modification d'une réservation
class ReservationUpdateView(UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'hotel/reservation_form.html'
    success_url = reverse_lazy('hotel:reservation_list')

class ReservationsEnAttenteView(ListView):
    model = Reservation
    template_name = 'hotel/reservations_en_attente.html'
    context_object_name = 'reservations'

    def get_queryset(self):
        return Reservation.objects.filter(is_confirmed=False)

class RappelsReservationView(ListView):
    model = Reservation
    template_name = 'hotel/rappels_reservations.html'
    context_object_name = 'reservations'

    def get_queryset(self):
        return Reservation.objects.filter(
            start_date__lte=now().date() + timedelta(days=1),
            is_confirmed=True
        )