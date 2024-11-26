from django import forms
from core.models.business import Business

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'logo', 'address', 'email', 'phone_number', 'nif', 'rc', 'types']
