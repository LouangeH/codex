from django.db import models
from .notification import Notification

class Reminder(models.Model):
    notification = models.OneToOneField(Notification, on_delete=models.CASCADE, related_name='reminder')
    schedule_at = models.DateTimeField(help_text="Quand envoyer le rappel")
    is_sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reminder for {self.notification.recipient.username} - Scheduled at {self.schedule_at}"
