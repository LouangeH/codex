from django.db import models

class Business(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='business_logos/', blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    nif = models.CharField(max_length=50, unique=True)  # Numéro d'identification fiscale
    rc = models.CharField(max_length=50, unique=True)  # Registre de commerce
    types = models.JSONField(default=list, help_text="Types d'activités : ['Hotel', 'Restaurant', 'Supermarché']")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
