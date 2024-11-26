from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from restaurant.models.menu_item import MenuItem
from restaurant.forms.menu_item_form import MenuItemForm

# Liste des articles du menu
class MenuItemListView(ListView):
    model = MenuItem
    template_name = 'restaurant/menu_list.html'
    context_object_name = 'menu_items'


# Création d'un article
class MenuItemCreateView(CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'restaurant/menu_form.html'
    success_url = reverse_lazy('restaurant:menu_list')


# Modification d'un article
class MenuItemUpdateView(UpdateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'restaurant/menu_form.html'
    success_url = reverse_lazy('restaurant:menu_list')


# Suppression d'un article
class MenuItemDeleteView(DeleteView):
    model = MenuItem
    template_name = 'restaurant/menu_confirm_delete.html'
    success_url = reverse_lazy('restaurant:menu_list')
