from django import forms
from billing.models.payment import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['invoice', 'method', 'amount']
