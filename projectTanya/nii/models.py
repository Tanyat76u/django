from django.db import models

class Employees(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    inn = models.TextField(null=True, blank=True)
    position = models.CharField(max_length=50)
    data = models.DateField(auto_now_add=True, db_index=True)
# Create your models here.
