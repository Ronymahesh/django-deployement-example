from django.db import models

# Create your models here.
class Mahesh(models.Model):
    """docstring for ."""
    kolo=models.CharField(max_length=10,unique=True)

    def __str__(self):
        return self.kolo
