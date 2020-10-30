from django.db import models

# Create your models here.
class Paises(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100) 
    abbreviation= models.CharField(max_length=10)
    status= models.BooleanField(default=True)
    creation_date= models.DateTimeField()   
    modification_date= models.DateTimeField()

class Ciudades(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100) 
    abbreviation= models.CharField(max_length=10)
    id_pais= models.ForeignKey(Paises,on_delete=models.CASCADE)
    status= models.BooleanField(default=True)
    creation_date= models.DateTimeField()   
    modification_date= models.DateTimeField()

class afiliados(models.Model):
    name = models.CharField(max_length=100) 
    last_name=models.CharField(max_length=100)
    cellphone_number=models.CharField(max_length=15)
    address= models.CharField(max_length=20)
    email= models.CharField(max_length=100)
    id_ciudad= models.ForeignKey(Ciudades, on_delete=models.CASCADE)
    status= models.BooleanField(default=True)
    creation_date= models.DateTimeField()   
    modification_date= models.DateTimeField()

   