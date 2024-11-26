from django.views.generic import ListView
from rappel.models.reminder import Reminder
from django.utils.timezone import now


# Liste des rappels
class ReminderListView(ListView):
    model = Reminder
    template_name = 'rappel/reminder_list.html'
    context_object_name = 'reminders'

class UpcomingRemindersView(ListView):
    model = Reminder
    template_name = 'rappel/upcoming_reminders.html'
    context_object_name = 'reminders'

    def get_queryset(self):
        # Afficher uniquement les rappels à venir
        return Reminder.objects.filter(schedule_at__gte=now(), is_sent=False)