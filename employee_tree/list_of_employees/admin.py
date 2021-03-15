from django.contrib import admin

# Register your models here.
from list_of_employees.models import Employees

class EmployeessProfileAdmin(admin.ModelAdmin):
    list_display = ['employee', 'position', 'department', 'salary', 'date_of_employment']

    def employee(self, obj):
        return obj.last_name + ' '\
         + obj.first_name[0] + '. '\
          + obj.middle_name[0] + '.'

    employee.short_description = 'ФИО'

admin.site.register(Employees, EmployeessProfileAdmin)

