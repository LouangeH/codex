from django.db import models
from users.models.user import User
from core.models.business import Business

class Contract(models.Model):
    employee = models.OneToOneField(User, on_delete=models.CASCADE, related_name='contract')
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='contracts')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text="Laisser vide si contrat indéterminé")
    salary = models.DecimalField(max_digits=10, decimal_places=2, help_text="Salaire mensuel")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contract for {self.employee.username} at {self.business.name}"
