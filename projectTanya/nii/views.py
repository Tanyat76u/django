from django.http import HttpResponse
from .models import Employees, Projects
from django.shortcuts import render
def index(request):
    employeess = Employees.objects.all()
    projectss = Projects.objects.all()
    return render(request, "nii/index.html", {'employeess': employeess, 'projectss': projectss})