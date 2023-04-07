import json
from django.shortcuts import render
from .models import Attendance, Employee
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def main_view(request):
    context = {'compName': 'NumBase'}
    return render(request, 'index.html', context)

def attendance_view(request):
    return render(request, 'calendar.html')


def home_view(request):
    myemployee = Employee.objects.get(id=1)
    empAttendance = Attendance.objects.get(employee= myemployee)
    context = serialize_employee(myemployee)
    context.update({'compName': 'NumBase'})
   # context.update({'salary' : myemployee.hour_rate * empAttendance.hours_attended})
    return render(request,'home.html',context)

@csrf_exempt
def home_view_submit(request):
    form_data = request.POST.dict()
    myemployee = Employee()
    myemployee.id = form_data['id']
    myemployee.email = form_data['email']
    myemployee.hour_rate = form_data['hour_rate']
    myemployee.last_name = form_data['last_name']
    myemployee.first_name = form_data['first_name']
    myemployee.phone = form_data['phone']
    myemployee.save()
    return render(request,'index.html')


def serialize_employee(employee):
    return {'id' : employee.id,
            'firstName': employee.first_name,
            'lastName': employee.last_name,
            'title' : employee.title,
            'phone' : str(employee.phone),
            'annaulLeaves':str(employee.vacation_days),
            'hourRate' : str(employee.hour_rate),
            'email' : str(employee.email)
            }
    