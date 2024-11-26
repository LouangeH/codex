from django.db import models

class Reservation(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE, related_name='reservations')
    client_name = models.CharField(max_length=100)
    client_id_type = models.CharField(max_length=20, choices=[
        ('CNI', 'Carte Nationale'), 
        ('Passport', 'Passeport'), 
        ('DriverLicense', 'Permis de Conduire')
    ])
    client_id_number = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation for Room {self.room.number} by {self.client_name}"
