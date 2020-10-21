from django.shortcuts import render
from django.http import JsonResponse
from map.models import Sighting
from .forms import squirrelform


def sightings(request):
	sightings_data = Sighting.objects.all()
			
	return render(request, 'sightings.html', {"sightings_data":sightings_data} )

def add(request):
    if request.method == "POST":
        form = squirrelform(request.POST)
        if form.is_valid():
            form.save
            return redirect("/sightings/")
        else:
            return redirect("/sightings/")
    return JsonResponse({})
