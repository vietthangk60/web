from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Main_ThemnhanVien.models import Employees
from Main_ThemnhanVien.serializers import EmployeeSerializer

from django.core.files.storage import default_storage


@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employees_serializer=EmployeeSerializer(employees,many=True)
        return render(request, "themnhanvien.html", {})
        #return JsonResponse(employees_serializer.data,safe=False)
    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
       # serializer = EmployeeSerializer(data=request.data)
      #  a=request.POST['EmployeeName'] 
        print("da chay fffsfsfs",employee_data)
        employees_serializer=EmployeeSerializer(data=employee_data)
        
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        print(employees_serializer.errors)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        employee_data=JSONParser().parse(request)
        employee=Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employees_serializer=EmployeeSerializer(employee,data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        employee=Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Successfully",safe=False)

#def register_attempt(request):

 #   if request.method == 'POST':
   #     username = request.POST.get('inputname')
   #     print(username)
    #    phone = request.POST.get('phone')
 #      email = request.POST.get('email')
    #    password = request.POST.get('password')
        




  #  return render(request, "themnhanvien.html", {})