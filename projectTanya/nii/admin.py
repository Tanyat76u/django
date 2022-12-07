from django.contrib import admin
from .models import Employees
from .models import Projects

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'middle_name', 'num_ser', 'inn', 'position', 'data')
    list_display_links = ('num_ser', 'inn')
    search_fields = ('num_ser', 'inn', 'data')

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'amount_of_financing')
    list_display_links = ('name',)
    search_fields = ('start_date', 'end_date', 'amount_of_financing')
    # list_display = ('num_ser')
    
admin.site.register(Employees, EmployeesAdmin)
admin.site.register(Projects, ProjectsAdmin)