from django.db import models

# Create your models here.
class SoleoDetails(models.Model):
    name = models.CharField(max_length=300)
    age = models.IntegerField()
    status = models.CharField(max_length=30)
    address = models.CharField(max_length=500)
    id_card = models.ImageField(upload_to='card/', blank=True, null=True)
    ssn_card = models.ImageField(upload_to='sncard/', blank=True, null=True)
    