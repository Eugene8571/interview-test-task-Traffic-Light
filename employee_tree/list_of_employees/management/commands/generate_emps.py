from django.core.management.base import BaseCommand, CommandError

import sys

sys.path.insert(0,'../../..')

from db_scripts.generate_employee_fboy import generate_employee

class Command(BaseCommand):
    help = 'Generate n employees'

    def handle(self, *args, **options):
        print('How many?')
        n = int(input())
        for i in range(n):
            generate_employee()

