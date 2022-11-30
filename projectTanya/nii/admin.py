from django.contrib import admin
from .models import Employees

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'middle_name', 'inn', 'position', 'data')
    list_display_links = ('first_name', 'inn')
    search_fields = ('first_name', 'last_name', 'middle_name', 'inn', 'position', 'data')
    
admin.site.register(Employees, EmployeesAdmin)
# Register your models here.