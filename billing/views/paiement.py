from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from billing.models.payment import Payment
from billing.forms.payment_form import PaymentForm


# Liste des paiements
class PaymentListView(ListView):
    model = Payment
    template_name = 'billing/payment_list.html'
    context_object_name = 'payments'


# Création d'un paiement
class PaymentCreateView(CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'billing/payment_form.html'
    success_url = reverse_lazy('billing:payment_list')