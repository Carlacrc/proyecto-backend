from django.db import models

# Create your models here.

#Tabla registro cliente
class Register(models.Model):
    name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=30)
    confirm_password=models.CharField(max_length=30)

# AGREGANDO NUEVOS CAMBIOS jeje