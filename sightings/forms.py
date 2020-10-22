from django.forms import ModelForm 
from map.models import Sighting

class squirrelform(ModelForm):
    class Meta:
        model = Sighting
        fields = [
                'latitude',
                'longitude',
                'unique_squirrel_id',
                'shift',
                'date',
                'age',
                'primary_fur_color',
                'location',
               'specific_location',
                'other_activities',
        ]


