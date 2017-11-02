from django.db import models

# Create your models here.
class Debit(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    #tags = 
    description = models.CharField(max_length=400)
