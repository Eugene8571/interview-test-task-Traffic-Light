from django.contrib import admin

# Register your models here.
from list_of_employees.models import Employees
admin.site.register(Employees)