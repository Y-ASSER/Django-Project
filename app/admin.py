from django.contrib import admin
from .models import Employee, Attendance, Salary

admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(Salary)

