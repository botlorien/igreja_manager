from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass  # Aqui podemos estender depois se necessário
