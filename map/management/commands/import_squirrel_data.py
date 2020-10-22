import csv
from django.core.management.base import BaseCommand
from django.urls import reverse
from map.models import Sighting
    
class Command(BaseCommand):
    help = 'Got squirrel data into pot'

    def add_arguments(self,parser):
        parser.add_argument('csv_file', help = 'file containing squirrel data')


    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)



        sighting_data = []
        for dict_ in data:
            sighting_data.append(Sighting(
                longitude = dict_['X'],
                latitude = dict_['Y'],
                unique_squirrel_id = dict_['Unique Squirrel ID'],
                shift = dict_['Shift'],
                date = dict_['Date'][4:8]+'-'+dict_['Date'][0:2]+'-'+dict_['Date'][2:4],
                age = dict_['Age'],
                primary_fur_color = dict_['Primary Fur Color'],
                location = dict_['Location'],
                specific_location = dict_['Specific Location'],
                running = True if dict_['Running'] =='TRUE' else False,
                chasing = True if dict_['Chasing'] =='TRUE' else False,
                climbing = True if dict_['Climbing'] =='TRUE' else False,
                eating = True if dict_['Eating'] =='TRUE' else False,
                foraging = True if dict_['Foraging'] =='TRUE' else False,
                other_activities=dict_['Other Activities'],
                kuks = True if dict_['Kuks'] =='TRUE' else False,
                quaas = True if dict_['Quaas'] =='TRUE' else False,
                moans = True if dict_['Moans'] =='TRUE' else False,
                tail_flags = True if dict_['Tail flags'] =='TRUE' else False,
                tail_twitches = True if dict_['Tail twitches'] =='TRUE' else False,
                approaches = True if dict_['Approaches'] =='TRUE' else False,
                indifferent = True if dict_['Indifferent'] =='TRUE' else False,
            ))

   
   

        Sighting.objects.bulk_create(sighting_data)
        msg = f"You are importing from {options['csv_file']}"
        self.stdout.write(self.style.SUCCESS(msg))

