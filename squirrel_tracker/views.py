from django.shortcuts import render
from .models import sighting

def index(request):
    return render(request, 'squirrel_tracker/index.html', {} )
