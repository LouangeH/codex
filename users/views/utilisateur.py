from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from users.models.user import User
from users.forms.user_form import UserForm


# Liste des utilisateurs
class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'


# Création d'un utilisateur
class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('users:user_list')


# Modification d'un utilisateur
class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('users:user_list')


# Suppression d'un utilisateur
class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/user_confirm_delete.html'
    success_url = reverse_lazy('users:user_list')
