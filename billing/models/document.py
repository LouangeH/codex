from django.db import models
from core.models.business import Business

class Document(models.Model):
    DOCUMENT_TYPES = [
        ('invoice', 'Facture'),
        ('receipt', 'Reçu'),
        ('contract', 'Contrat'),
        ('proforma', 'Facture Proforma')
    ]

    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='documents')
    type = models.CharField(max_length=20, choices=DOCUMENT_TYPES)
    content = models.JSONField(help_text="Contenu du document au format JSON")
    generated_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.get_type_display()} - {self.business.name} - {self.generated_at}"
