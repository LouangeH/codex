from django.db import models
from core.models.business import Business

class Invoice(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='invoices')
    client_name = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('paid', 'Payée'),
        ('unpaid', 'Non payée'),
        ('cancelled', 'Annulée')
    ])
    details = models.JSONField(help_text="Détails des services : Hôtel, Restaurant, etc.")
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(help_text="Date limite de paiement", blank=True, null=True)

    def __str__(self):
        return f"Invoice {self.id} ({self.status}) - {self.business.name}"
