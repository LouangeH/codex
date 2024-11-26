from django.views.generic import ListView, UpdateView
from django.urls import reverse_lazy
from billing.models.currency_rate import CurrencyRate

class TauxConversionListView(ListView):
    model = CurrencyRate
    template_name = 'billing/taux_conversion_list.html'
    context_object_name = 'rates'

class TauxConversionUpdateView(UpdateView):
    model = CurrencyRate
    fields = ['currency', 'rate']
    template_name = 'billing/taux_conversion_form.html'
    success_url = reverse_lazy('billing:taux_conversion_list')
