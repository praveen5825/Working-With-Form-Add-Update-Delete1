from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=35)
    age=models.IntegerField()
    salary=models.IntegerField()
    doj=models.DateField()

    def __str__(self):
        return self.name
