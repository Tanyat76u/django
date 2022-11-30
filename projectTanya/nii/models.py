from django.db import models

class Employees(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=50, verbose_name='Отчество')
    inn = models.TextField(null=True, blank=True, verbose_name='ИНН')
    position = models.CharField(max_length=50, verbose_name='Должность')
    data = models.DateField(auto_now_add=True, db_index=True, verbose_name='Дата рождения')
    
    class Meta:
        verbose_name_plural = 'Сотрудники'
        verbose_name = 'Сотрудник'
        ordering = ['-data']
# Create your models here.
