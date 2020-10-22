from django.shortcuts import render,redirect,get_object_or_404
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
            form.save()
            return redirect("/sightings/")
        else:
            return JsonResponse({'errors':form.errors},status=400)
    else:
        form =squirrelform()
        context = {
                'form':form,
        }
    return render(request,'sightings/add.html',context)

def stats(request):
    data = Sighting.objects.all()
    total_number = len(Sighting.objects.all())
    age = Sighting.objects.filter(age='Adult').count()
    primary_fur_color = Sighting.objects.filter(primary_fur_color='Cinnamon').count() 
    location = Sighting.objects.filter(location="Ground Plane").count()
    shift = Sighting.objects.filter(shift="PM").count()
    specific_location = Sighting.objects.filter(specific_location="tree").count()
    context = {
            'total_number':total_number, 
            'age':age,
            'primary_fur_color':primary_fur_color,
            'shift':shift,
            'location':location,
            'specific_location':specific_location,
    }
    return render(request,'sightings/stats.html',context)

def update(request,unique_squirrel_id):
    number =  Sighting.objects.filter(unique_squirrel_id = unique_squirrel_id).first()
    if request.method == "POST":
        form = squirrelform(request.POST,instance = number)
        if form.is_valid():
            form.save
            form.save()
            return redirect("/sightings/")       
    else:
        form =squirrelform(instance = number)
        context = {
                'form':form,
        }
    return render(request,'sightings/update.html',context)
