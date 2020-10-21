from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from map.models import Sighting
from .forms import squirrelform
from django.db.models import Avg, Max, Min, Count


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
    age =  list(data.values_list('age').annotate(Count('age')))
    primary_fur_color = list(data.values_list('primary_fur_color').annotate(Count('primary_fur_color')))
    chasing =  list(data.values_list('chasing').annotate(Count('chasing')))
    location =  list(data.values_list('location').annotate(Count('location')))
    eating =  list(data.values_list('eating').annotate(Count('eating')))
    context = {
            'total_number':total_number, 
            'age':age,
            'primary_fur_color':primary_fur_color,
            'chasing':chasing,
            'location':location,
            'eating':eating,
    }
    return render(request,'sightings/stats.html',context)

def update(request,unique_squirrel_id):
    data = get_object_or_404(Sighting,unique_squirrel_id = unique_squirrel_id)
    if request.method == "POST":
        form = squirrelform(request.POST,instance = data)
        if form.is_valid():
            form.save
            return redirect("/sightings/")
        
    else:
        form =squirrelform(instance = data)
        context = {
                'form':form,
        }
    return render(request,'sightings/update.html',context)
