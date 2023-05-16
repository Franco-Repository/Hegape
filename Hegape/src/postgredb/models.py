from django.db import models

# Create your models here.
#PONER FPUSER
#Agregar E-mail y Type (que tiene un name y un ID) clase aparte.
class CustomUser(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
