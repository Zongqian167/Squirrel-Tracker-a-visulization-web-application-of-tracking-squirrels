from django.db import models

class Sighting(models.Model):
    longitude = models.FloatField(
            max_length=100,
            )
    latitude = models.FloatField(
            max_length=100,
            )
# Create your models here.
