from django.contrib import admin
from .models import Employees
from .models import Projects

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'middle_name', 'inn', 'position', 'data')
    list_display_links = ('first_name',)
    search_fields = ('first_name', 'last_name', 'middle_name', 'data')
    
admin.site.register(Employees, EmployeesAdmin)
#admin.site.register(Projects, ProjectsAdmin)