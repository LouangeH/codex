from django.db import models

class CurrencyRate(models.Model):
    currency = models.CharField(max_length=3, unique=True, help_text="Code de la devise (ex. : USD, EUR)")
    rate = models.DecimalField(max_digits=10, decimal_places=4, help_text="Taux de conversion par rapport à la devise par défaut")

    def __str__(self):
        return f"{self.currency}: {self.rate}"
