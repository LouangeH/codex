from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from hotel.models.room import Room
from hotel.forms.room_form import RoomForm


# Liste des chambres
class RoomListView(ListView):
    model = Room
    template_name = 'hotel/room_list.html'
    context_object_name = 'rooms'


# Création d'une chambre
class RoomCreateView(CreateView):
    model = Room
    form_class = RoomForm
    template_name = 'hotel/room_form.html'
    success_url = reverse_lazy('hotel:room_list')


# Modification d'une chambre
class RoomUpdateView(UpdateView):
    model = Room
    form_class = RoomForm
    template_name = 'hotel/room_form.html'
    success_url = reverse_lazy('hotel:room_list')


# Suppression d'une chambre
class RoomDeleteView(DeleteView):
    model = Room
    template_name = 'hotel/room_confirm_delete.html'
    success_url = reverse_lazy('hotel:room_list')
