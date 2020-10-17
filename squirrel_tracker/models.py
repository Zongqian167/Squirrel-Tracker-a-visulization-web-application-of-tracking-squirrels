from django.db import models
from django.contrib.gis.db import models as geomodels
#class sightings(models.Model):
#    latitude = models.FloatField(
#            max_length=100,
#            )
#    longitude = models.FloatField(
#            max_length=100,)
#   from django.contrib.gis.db import models as geomodels


class sightings(geomodels.Model):
    point = geomodels.PointField(
        srid=4326,
        blank=True,
        )         
# Create your models here.
