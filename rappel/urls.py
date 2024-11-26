from django.urls import path
from rappel.views.notification import NotificationListView
from rappel.views.rappel import UpcomingRemindersView

app_name = 'rappel'

urlpatterns = [
    # Notifications
    path('notifications/', NotificationListView.as_view(), name='notification_list'),
    # Rappels
    path('rappels/', UpcomingRemindersView.as_view(), name='reminder_list'),
]
