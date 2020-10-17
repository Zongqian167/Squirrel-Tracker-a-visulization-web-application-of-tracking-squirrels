import csv
from django.core.management.base import BaseCommand
from squirrel_tracker.models import sightings
    
class Command(BaseCommand):
    help = 'Got squirrel data into pot'

    def add_arguments(self,parser):
        parser.add_argument('squirrel_file', help = 'file containing squirrel data')

    def handle(self, *args, **options):
        file_ = options['squirrel_file']

        with open(file_, 'r',encoding='UTF-8') as fp:
            reader = csv.DictReader(fp)

            for item in reader:
                obj = sightings()
                obj.point = item['Lat/Long']
               # obj.latitude = item['Y']
               # obj.longitude = item['X']

                obj.save()
        msg = f'You are importing from {file_}'
        self.stdout.write(self.style.SUCCESS(msg))
