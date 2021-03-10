from django.db import models

# Create your models here.

class Employees(models.Model):
    first_name = models.CharField("Имя", max_length=150)
    middle_name = models.CharField("Отчество", max_length=150)
    last_name = models.CharField("Фамилия", max_length=150)
    date_of_employment = models.DateField("Дата приёма на работу")
    salary = models.IntegerField()
    department = models.CharField("Департамент", max_length=150)
    position = models.CharField("Должность", max_length=150)

    def __str__(self):
        return self.last_name + ' '\
         + self.first_name[0] + '. '\
          + self.middle_name[0] + '.'


