from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'sightings'
urlpatterns = [
		path('',views.sightings,name="sightings"),
                path('add/',views.add,name="add"),
                path('stats/',views.stats,name="stats"),
                path('<str:unique_squirrel_id>/',views.update,name="update"),
]

