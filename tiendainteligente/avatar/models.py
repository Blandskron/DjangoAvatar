from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Avatar de {self.usuario.username}"
