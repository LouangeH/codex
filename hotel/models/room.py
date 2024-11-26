from django.db import models
from core.models.business import Business

class Room(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='rooms')
    number = models.CharField(max_length=10, unique=True)
    status = models.CharField(
        max_length=20,
        choices=[('occupied', 'Occupée'), ('unoccupied', 'Non occupée'), ('repair', 'En réparation')]
    )
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Room {self.number} ({self.business.name})"
