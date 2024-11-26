from django.views.generic import TemplateView
from billing.models.invoice import Invoice
from django.utils.timezone import now, timedelta
from django.db import models

class RapportFinancierView(TemplateView):
    template_name = 'billing/rapport_financier.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Calcul des revenus des 7 derniers jours
        last_week = now().date() - timedelta(days=7)
        context['revenus_hebdo'] = Invoice.objects.filter(
            status='paid', created_at__gte=last_week
        ).aggregate(total=models.Sum('total_amount'))['total'] or 0
        return context
    
class RapportMensuelView(TemplateView):
    template_name = 'billing/rapport_mensuel.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        debut_mois = now().date().replace(day=1)
        context['total_factures'] = Invoice.objects.filter(
            created_at__gte=debut_mois,
            status='paid'
        ).aggregate(total=models.Sum('total_amount'))['total'] or 0
        return context

