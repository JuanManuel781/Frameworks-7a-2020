from django.db import models

# Create your models here.
class Category(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    status= models.BooleanField(default=True)
    description=models.TextField(default='')

