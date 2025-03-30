from django.db import models
from igrejas.models import Igreja

class Membro(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    igreja = models.ForeignKey(Igreja, on_delete=models.CASCADE, related_name='membros')

    def __str__(self):
        return f'{self.nome} - {self.igreja}'
