from django.urls import path
from . import views

app_name = 'sightings'
urlpatterns = [
		path('',views.sightings,name="sightings"),
                path('add',views.add,name="add"),
]

