from django.http import HttpResponse
from .models import Employees

def index(request):
    s = 'Список объявлений\r\n\r\n\r\n\r\n\r\n\r\n'
    for employees in Employees.objects.order_by('-data'):
        s += employees.first_name + '\r\n' + employees.last_name + '\r\n' + employees.middle_name + '\r\n' + employees.inn + '\r\n' + employees.position + '\r\n\r\n'
    return HttpResponse(s, content_type='text/plain; charset=utf-8')
#def index(request):
   #return HttpResponse("Привет! Это твое первое приложение!")
   #добавила \r\n\r\n\r\n, ('-data'), вместо bb employees