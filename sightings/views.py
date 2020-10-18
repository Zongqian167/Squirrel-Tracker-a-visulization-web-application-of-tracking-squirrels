from django.shortcuts import render
  
from map.models import Sighting

def sightings(request):
	sightings_data = Sighting.objects.all()
			
	return render(request, 'sightings.html', {"sightings_data":sightings_data} )

