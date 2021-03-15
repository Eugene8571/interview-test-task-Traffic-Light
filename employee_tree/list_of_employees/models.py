from django.db import models

# Create your models here.

class Employees(models.Model):
    first_name = models.CharField("Имя", max_length=150, default="***")
    middle_name = models.CharField("Отчество", max_length=150, default="***")
    last_name = models.CharField("Фамилия", max_length=150, default="***")
    date_of_employment = models.DateField("Дата приёма на работу", default="2021-01-01")
    salary = models.IntegerField(default=10)
    department = models.CharField("Департамент", max_length=150, default="***")
    position = models.CharField("Должность", max_length=150, default="***")
    rank = models.CharField("Ранг", max_length=150, default="***")
    
    def __str__(self):
        return self.last_name + ' '\
         + self.first_name[0] + '. '\
          + self.middle_name[0] + '.'


