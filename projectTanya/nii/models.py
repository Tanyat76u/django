from django.db import models

class Employees(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=50, verbose_name='Отчество')
    num_ser = models.IntegerField(blank=True, null=True, verbose_name= 'Номер и серия паспорта')
    inn = models.TextField(null=True, blank=True, verbose_name='ИНН')
    position = models.CharField(max_length=50, verbose_name='Должность')
    data = models.CharField(max_length=30, verbose_name='Дата рождения')
    def __str__(self):
        #return self.first_name
        return f'{self.first_name} {self.last_name} {self.middle_name}'
        
    class Meta:
        verbose_name_plural = 'Сотрудники'
        verbose_name = 'Сотрудник'
        ordering = ['-num_ser']

class Projects(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    start_date = models.CharField(max_length=50, verbose_name='Дата начала')
    end_date = models.CharField(max_length=50, verbose_name='Дата окончания')
    amount_of_financing = models.CharField(max_length=20, verbose_name='Объем финансирования')
    employeess = models.ManyToManyField(Employees, verbose_name='Сотрудники')
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = 'Проекты'
        verbose_name = 'Проект'
        ordering = ['-start_date']