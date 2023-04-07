from django.db import models

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    title = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    vacation_days = models.IntegerField(default=15)
    hour_rate = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"
    
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_in = models.DateTimeField(null=True)#auto_now_add=True)
    check_out = models.DateTimeField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if self.check_out is not None and self.check_out.date() != self.check_in.date():
            raise ValueError("Check out must be on the same day as check in.")
        super().save(*args, **kwargs)
    
    def hours_attended(self):
        if self.check_out is None:
            return None
        return (self.check_out - self.check_in).total_seconds() / 3600
    
class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.DateField(auto_now_add=True)
    attendance_hours = models.DecimalField(max_digits=8, decimal_places=2)
    
    @property
    def salary_amount(self):
        return self.employee.hour_rate * self.attendance_hours
    
    def __str__(self):
        return f"{self.employee} - {self.month}"

