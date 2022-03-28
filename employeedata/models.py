from django.db import models

class EmployeeData(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    salary = models.IntegerField()
    email = models.EmailField(max_length = 20)
    company = models.CharField(max_length = 20)
    job = models.CharField(max_length = 20)
    location = models.CharField(max_length = 20)
    address = models.CharField(max_length = 100)