from django.db import models

# Create your models here.
class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    Date_of_birth = models.DateField()
    PhoneNumber  = models.CharField(max_length=500)
    Email = models.CharField(max_length=50)
    Address_Employee =models.CharField(max_length=1000)
    Department = models.CharField(max_length=500)
    Position_Employee=models.CharField(max_length=500)
    Avatar = models.ImageField(upload_to='images',null='False')
    Image = models.ImageField(upload_to='images',null='True')
  #  DateOfJoining = models.DateField()
 #   PhotoFileName = models.CharField(max_length=500)