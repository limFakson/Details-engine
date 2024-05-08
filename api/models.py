from django.db import models
from django.db.models import JSONField


# Create your models here.
class SoleoDetails(models.Model):
    data = JSONField()
