import csv
from django.core.management.base import BaseCommand
from sightings.models import Sighting

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
				longitude=dict_['X'],
				latitude=dict_['Y'],
				unique_squirrel_id=dict_['Unique Squirrel ID'],
				shift=dict_['Shift']
				date=dict_['Date']
				age=['Age']
			))

		Sighting.objects.bulk_create(sighting_data)
		msg = f"You are importing from {options['csv_file']}"
		self.stdout.write(self.style.SUCCESS(msg))
