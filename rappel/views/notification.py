from django.views.generic import ListView
from rappel.models.notification import Notification


# Liste des notifications
class NotificationListView(ListView):
    model = Notification
    template_name = 'rappel/notification_list.html'
    context_object_name = 'notifications'