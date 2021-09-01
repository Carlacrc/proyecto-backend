from django.db import models

# Create your models here.

#Clase Registro
class Register(models.Model):
    name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=30)
    confirm_password=models.CharField(max_length=30)