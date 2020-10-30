from django.db import models

# Create your models here.
class mascotas(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10)
    id_tipo = models.ForeignKey(
        'tipos', on_delete=models.CASCADE)
    id_raza = models.ForeignKey(
        'razas', on_delete=models.CASCADE)
    nombre = models.TextField()
    tiene_vacunas = models.BooleanField()
    estado = models.CharField(max_length=1)
    fecha_creacion = models.DateField()
    fecha_modificacion = models.DateField()


class tipos(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10)
    nombre = models.TextField()
    abreviatura = models.CharField(max_length=4)
    estado = models.CharField(max_length=1)
    fecha_creacion = models.DateField()
    fecha_modificacion = models.DateField()


class razas(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10)
    nombre = models.TextField()
    abreviatura = models.CharField(max_length=4)
    id_tipo = models.ForeignKey(
        'tipos', on_delete=models.CASCADE)
    estado = models.CharField(max_length=1)
    fecha_creacion = models.DateField()
    fecha_modificacion = models.DateField()