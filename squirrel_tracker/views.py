from django.shortcuts import render
from .models import Sighting

def index(request):
    map_data = Sighting.objects.all()[:100]
    return render(request, 'squirrel_tracker/index.html', {"sightings":map_data} )
