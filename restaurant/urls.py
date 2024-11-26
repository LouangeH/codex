from django.urls import path
from restaurant.views.menu import MenuItemListView, MenuItemCreateView, MenuItemUpdateView, MenuItemDeleteView
from restaurant.views.commande import OrderListView, OrderCreateView, OrderUpdateView

app_name = 'restaurant'

urlpatterns = [
    # Menu
    path('menu/', MenuItemListView.as_view(), name='menu_list'),
    path('menu/ajouter/', MenuItemCreateView.as_view(), name='menu_create'),
    path('menu/<int:pk>/modifier/', MenuItemUpdateView.as_view(), name='menu_update'),
    path('menu/<int:pk>/supprimer/', MenuItemDeleteView.as_view(), name='menu_delete'),
    # Commandes
    path('commandes/', OrderListView.as_view(), name='order_list'),
    path('commandes/ajouter/', OrderCreateView.as_view(), name='order_create'),
    path('commandes/<int:pk>/modifier/', OrderUpdateView.as_view(), name='order_update'),
]
