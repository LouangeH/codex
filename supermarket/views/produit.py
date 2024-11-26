from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from supermarket.models.product import Product
from supermarket.forms.product_form import ProductForm


# Liste des produits
class ProductListView(ListView):
    model = Product
    template_name = 'supermarket/product_list.html'
    context_object_name = 'products'


# Création d'un produit
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'supermarket/product_form.html'
    success_url = reverse_lazy('supermarket:product_list')


# Modification d'un produit
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'supermarket/product_form.html'
    success_url = reverse_lazy('supermarket:product_list')


# Suppression d'un produit
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'supermarket/product_confirm_delete.html'
    success_url = reverse_lazy('supermarket:product_list')
