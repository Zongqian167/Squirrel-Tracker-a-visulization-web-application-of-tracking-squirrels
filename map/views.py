from django.shortcuts import render
from .models import Sighting

def map(request):
    map_data = Sighting.objects.all()[:100]
    return render(request, 'map/map.html', {"sightings":map_data} )
