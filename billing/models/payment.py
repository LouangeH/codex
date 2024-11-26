from django.db import models

class Payment(models.Model):
    invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE, related_name='payments')
    method = models.CharField(max_length=50, choices=[
        ('cash', 'Espèces'),
        ('card', 'Carte Bancaire'),
        ('mobile', 'Paiement Mobile')
    ])
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment of {self.amount} for Invoice {self.invoice.id}"
