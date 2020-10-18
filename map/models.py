from django.db import models

class Sighting(models.Model):
    longitude = models.FloatField(max_length=100,)
    latitude = models.FloatField(max_length=100,) 
    unique_squirrel_id = models.CharField(max_length=200,)
    shift=models.CharField(max_length=200, )
    date=models.DateField()
    age=models.CharField(max_length=200, )



# Create your models here.
