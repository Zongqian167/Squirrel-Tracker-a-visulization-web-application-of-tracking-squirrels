import csv
from django.core.management import BaseCommand
import sys
from map.models import Sighting

class Command(BaseCommand):
	help = 'export data'

	def add_arguments(self, parser):
		parser.add_argument('path', type=str, help="csv file")

	def handle(self, path, **options):
		with open(path, 'w', newline='') as f:
			field_names = [data.name for data in Sighting._meta.fields]
			writer = csv.writer(f, quoting=csv.QUOTE_ALL)
			writer.writerow(field_names)
			for obj in Sighting.objects.all():
				writer.writerow([getattr(obj, f) for f in field_names])
