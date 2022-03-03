from rest_framework import serializers
from Main_ThemnhanVien.models import Employees



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees 
        fields=('EmployeeId','EmployeeName','Date_of_birth','PhoneNumber','Address_Employee','Department','Position_Employee')