from django.shortcuts import render,redirect
from django.http import JsonResponse
from map.models import Sighting
from .forms import squirrelform


def sightings(request):
	sightings_data = Sighting.objects.all()
			
	return render(request,'sightings/sightings.html',{"sightings_data":sightings_data} )

def add(request):
    if request.method == "POST":
        form = squirrelform(request.POST)
        if form.is_valid():
            form.save
            return redirect("/sightings/")
        else:
            return redirect("/sightings/")
    else:
        form =squirrelform()

    return render(request,'sightings/sightings/add.html',{"form":form})
