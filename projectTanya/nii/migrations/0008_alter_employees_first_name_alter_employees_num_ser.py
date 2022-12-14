# Generated by Django 4.1.3 on 2022-12-13 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nii', '0007_alter_employees_first_name_alter_employees_num_ser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='num_ser',
            field=models.IntegerField(blank=True, null=True, verbose_name='Номер и серия паспорта'),
        ),
    ]