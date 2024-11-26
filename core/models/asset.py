from django.db import models
from core.models.business import Business

class Asset(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='assets')
    name = models.CharField(max_length=100)
    purchase_date = models.DateField()
    purchase_price = models.DecimalField(max_digits=12, decimal_places=2)
    depreciation_rate = models.DecimalField(max_digits=5, decimal_places=2, help_text="Taux d'amortissement annuel (%)")
    current_value = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ('operational', 'Opérationnel'),
        ('non_operational', 'Non Opérationnel'),
        ('sold', 'Vendu')
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Calcul de la valeur actuelle basée sur le taux d'amortissement
        import datetime
        years_elapsed = (datetime.date.today() - self.purchase_date).days / 365
        self.current_value = max(0, self.purchase_price * (1 - self.depreciation_rate / 100) ** years_elapsed)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Asset: {self.name} ({self.business.name})"
