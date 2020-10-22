from django.db import models

class Sighting(models.Model):
    longitude = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100) 
    unique_squirrel_id = models.CharField(max_length=200)
    shift=models.CharField(max_length=200, null=True, blank=True)
    date=models.DateField(null=True, blank=True)
    age=models.CharField(max_length=200, null=True, blank=True)
    primary_fur_color=models.CharField(max_length=200, null=True, blank=True)
    location=models.CharField(max_length=200, null=True, blank=True)
    specific_location=models.CharField(max_length=200, null=True, blank=True)
    other_activities=models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):
        return self.unique_squirrel_id


# Create your models here.
