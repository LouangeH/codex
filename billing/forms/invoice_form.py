from django import forms
from billing.models.invoice import Invoice

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['client_name', 'total_amount', 'status', 'details', 'due_date']
