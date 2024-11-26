from django import forms
from core.models.asset import Asset

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['name', 'category', 'status', 'purchase_date', 'current_value']
