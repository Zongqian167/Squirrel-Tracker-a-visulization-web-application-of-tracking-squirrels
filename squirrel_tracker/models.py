from django.db import models

class sighting(models.Model):
    latitude = models.FloatField(
            max_length=100,
            )
    longitude = models.FloatField(
            max_length=100,)

# Create your models here.
