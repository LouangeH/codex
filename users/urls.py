from django.urls import path
from users.views.utilisateur import UserListView, UserCreateView, UserUpdateView, UserDeleteView
from users.views.role import RoleListView, RoleCreateView, RoleUpdateView, RoleDeleteView

app_name = 'users'

urlpatterns = [
    # Utilisateurs
    path('utilisateurs/', UserListView.as_view(), name='user_list'),
    path('utilisateurs/ajouter/', UserCreateView.as_view(), name='user_create'),
    path('utilisateurs/<int:pk>/modifier/', UserUpdateView.as_view(), name='user_update'),
    path('utilisateurs/<int:pk>/supprimer/', UserDeleteView.as_view(), name='user_delete'),
    # Rôles
    path('roles/', RoleListView.as_view(), name='role_list'),
    path('roles/ajouter/', RoleCreateView.as_view(), name='role_create'),
    path('roles/<int:pk>/modifier/', RoleUpdateView.as_view(), name='role_update'),
    path('roles/<int:pk>/supprimer/', RoleDeleteView.as_view(), name='role_delete'),
]
