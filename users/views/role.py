from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from users.models.role import Role
from users.forms.role_form import RoleForm

# Liste des rôles
class RoleListView(ListView):
    model = Role
    template_name = 'users/role_list.html'
    context_object_name = 'roles'


# Création d'un rôle
class RoleCreateView(CreateView):
    model = Role
    form_class = RoleForm
    template_name = 'users/role_form.html'
    success_url = reverse_lazy('users:role_list')


# Modification d'un rôle
class RoleUpdateView(UpdateView):
    model = Role
    form_class = RoleForm
    template_name = 'users/role_form.html'
    success_url = reverse_lazy('users:role_list')


# Suppression d'un rôle
class RoleDeleteView(DeleteView):
    model = Role
    template_name = 'users/role_confirm_delete.html'
    success_url = reverse_lazy('users:role_list')
