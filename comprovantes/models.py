from django.db import models
from membros.models import Membro
from cloudinary.models import CloudinaryField

class Comprovante(models.Model):
    TIPO_CHOICES = [
        ('D', 'Dízimo'),
        ('O', 'Oferta'),
    ]
    membro = models.ForeignKey(Membro, on_delete=models.CASCADE, related_name='comprovantes')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    data_comprovante = models.DateField()
    #arquivo = models.FileField(upload_to='comprovantes/')
    arquivo = CloudinaryField('arquivo', 
                                folder='comprovantes', 
                                resource_type='auto',
                                type='upload',
                                blank=True,   # Permite que o campo seja deixado em branco nos formulários
                                null=True     # Permite que o campo seja nulo no banco de dados
                                )  
    def __str__(self):
        return f'{self.get_tipo_display()} - {self.valor} ({self.membro.nome})'
