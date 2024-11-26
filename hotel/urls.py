from django.urls import path
from hotel.views.room import RoomListView, RoomCreateView, RoomUpdateView, RoomDeleteView
from hotel.views.reservation import ReservationListView, ReservationCreateView, ReservationUpdateView

app_name = 'hotel'

urlpatterns = [
    # Chambres
    path('chambres/', RoomListView.as_view(), name='room_list'),
    path('chambres/ajouter/', RoomCreateView.as_view(), name='room_create'),
    path('chambres/<int:pk>/modifier/', RoomUpdateView.as_view(), name='room_update'),
    path('chambres/<int:pk>/supprimer/', RoomDeleteView.as_view(), name='room_delete'),
    # Réservations
    path('reservations/', ReservationListView.as_view(), name='reservation_list'),
    path('reservations/ajouter/', ReservationCreateView.as_view(), name='reservation_create'),
    path('reservations/<int:pk>/modifier/', ReservationUpdateView.as_view(), name='reservation_update'),
]
