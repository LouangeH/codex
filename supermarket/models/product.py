from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    threshold = models.PositiveIntegerField(help_text="Seuil d'alerte pour le stock")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
