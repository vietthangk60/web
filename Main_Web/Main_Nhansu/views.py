from django.shortcuts import render
from django.http import HttpRequest
from Main_ThemnhanVien.models import Employees
from Main_ThemnhanVien.serializers import EmployeeSerializer
# Create your views here.
def func_Nhansuview(request, *args, **kwargs): # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
   if request.method=='GET':
      employees = Employees.objects.all()
      employees_serializer=EmployeeSerializer(employees,many=True)
      return render(request, "nhansu.html", {"employee":employees_serializer.data})
   elif request.method=='POST' and 'delete' in request.POST:
      print(request.POST)
      manhavien=request.POST['delete']
      record = Employees.objects.get(EmployeeId=manhavien)
      record.delete()
      employees = Employees.objects.all()
      employees_serializer=EmployeeSerializer(employees,many=True)
      return render(request, "nhansu.html", {"employee":employees_serializer.data})
def func_Themnhanvienview(request, *args, **kwargs): # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "themnhanvien.html", {})