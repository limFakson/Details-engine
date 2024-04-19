from django.db import models

# Create your models here.
class SoleoDetails(models.Model):
    name = models.CharField(max_length=300)
    age = models.IntegerField()
    status = models.CharField(max_length=30)
    address = models.CharField(max_length=500)
    card = models.ImageField(upload_to='card/', blank=True)
    