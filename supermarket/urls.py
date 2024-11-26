from django.urls import path
from supermarket.views.produit import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = 'supermarket'

urlpatterns = [
    # Produits
    path('produits/', ProductListView.as_view(), name='product_list'),
    path('produits/ajouter/', ProductCreateView.as_view(), name='product_create'),
    path('produits/<int:pk>/modifier/', ProductUpdateView.as_view(), name='product_update'),
    path('produits/<int:pk>/supprimer/', ProductDeleteView.as_view(), name='product_delete'),
]
