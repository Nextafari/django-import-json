from django.core.management.base import BaseCommand

from pilotlog.models import Aircraft, Flight
from pilotlog.utils import export_csv


class Command(BaseCommand):
    help = 'Export pilot log data to CSV'

    def handle(self, *args, **kwargs):
        aircraft_queryset = Aircraft.objects.all()
        flight_queryset = Flight.objects.all()
        
        export_csv(aircraft_queryset, flight_queryset)

        self.stdout.write(self.style.SUCCESS('Data exported successfully!!'))
