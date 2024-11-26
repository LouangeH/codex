from django.views.generic import TemplateView
from hotel.models.reservation import Reservation
from django.utils.timezone import now, timedelta

class ReservationRapportView(TemplateView):
    template_name = 'hotel/reservation_rapport.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Ajouter des statistiques, par exemple, réservations des 7 derniers jours
        last_week = now().date() - timedelta(days=7)
        context['reservations_semaine'] = Reservation.objects.filter(start_date__gte=last_week)
        return context
