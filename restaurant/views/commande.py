from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from restaurant.models.order import Order
from restaurant.forms.order_form import OrderForm

# Liste des commandes
class OrderListView(ListView):
    model = Order
    template_name = 'restaurant/order_list.html'
    context_object_name = 'orders'


# Création d'une commande
class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'restaurant/order_form.html'
    success_url = reverse_lazy('restaurant:order_list')


# Modification d'une commande
class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'restaurant/order_form.html'
    success_url = reverse_lazy('restaurant:order_list')
