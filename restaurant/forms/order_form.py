from django import forms
from restaurant.models.order import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['menu_item', 'table_number', 'quantity']
