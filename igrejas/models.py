from django.db import models
from cloudinary.models import CloudinaryField

class Igreja(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    endereco = models.TextField(blank=True, null=True)
    contato = models.CharField(max_length=50, blank=True, null=True)
    #imagem_da_igreja = models.ImageField(upload_to='imagens_igrejas/', blank=True, null=True)
    imagem_da_igreja = CloudinaryField('imagem_da_igreja', 
                                folder='imagem_da_igreja', 
                                resource_type='auto',
                                blank=True,   # Permite que o campo seja deixado em branco nos formulários
                                null=True     # Permite que o campo seja nulo no banco de dados
                                ) 
    def __str__(self):
        return self.nome
