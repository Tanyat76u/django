# Generated by Django 4.1.3 on 2022-12-04 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nii', '0003_alter_employees_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='num_ser',
            field=models.IntegerField(blank=True, null=True, verbose_name='Номер и серия паспорта'),
        ),
    ]
