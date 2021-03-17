import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_tree.settings')
django.setup()

from list_of_employees.models import Departments

def generate_departments():
    list_of_departments = 'abcdefghijklmnopqrstuvwxyz'
    for char in list_of_departments:
        dep = Departments(department_name=char.upper())
        dep.save()

