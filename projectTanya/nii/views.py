from django.http import HttpResponse
from .models import Employees, Projects
#from .models import Projects
from django.shortcuts import render
def index(request):
    employeess = Employees.objects.all()
    projectss = Projects.objects.all()
        #s += employees.first_name + '\r\n' + employees.last_name + '\r\n' + employees.middle_name + '\r\n' + employees.inn + '\r\n' + employees.position + '\r\n\r\n'
    return render(request, "nii/index.html", {'employeess': employeess, 'projectss': projectss})