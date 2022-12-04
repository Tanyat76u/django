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

class Projects(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    start_date = models.CharField(max_length=50, verbose_name='Дата начала')
    end_date = models.CharField(max_length=50, verbose_name='Дата окончания')
    amount_of_financing = models.CharField(max_length=20, verbose_name='Объем финансирования')
    
    class Meta:
        verbose_name_plural = 'Проекты'
        verbose_name = 'Проект'
        ordering = ['-start_date']