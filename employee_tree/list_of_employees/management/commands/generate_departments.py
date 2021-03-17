from django.core.management.base import BaseCommand, CommandError

import sys

sys.path.insert(0,'../../..')

from db_scripts.generate_departments import generate_departments

class Command(BaseCommand):
    help = 'Generate A .. Z departments'

    def handle(self, *args, **options):
        generate_departments()