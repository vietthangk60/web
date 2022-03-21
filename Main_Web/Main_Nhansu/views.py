from django.shortcuts import render
from django.http import HttpRequest
from Main_ThemnhanVien.models import Employees
from Main_ThemnhanVien.serializers import EmployeeSerializer
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
# Create your views here.
def func_Nhansuview(request, *args, **kwargs): # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
   if request.method=='GET':
      employees = Employees.objects.all()
      employees_serializer=EmployeeSerializer(employees,many=True)
    #  print(request.user.get_all_permissions())
      print(employees_serializer.data)
      return render(request, "nhansu.html", {"employee":employees_serializer.data})

   elif request.method=='POST' and 'delete' in request.POST:
      if request.user.has_perm('Main_ThemnhanVien.delete_employees'):


         manhavien=request.POST['delete']
         record = Employees.objects.get(EmployeeId=manhavien)
         record.delete()
         employees = Employees.objects.all()
         employees_serializer=EmployeeSerializer(employees,many=True)
         return render(request, "nhansu.html", {"employee": employees_serializer.data})
   
      employees = Employees.objects.all()
      employees_serializer=EmployeeSerializer(employees,many=True)  
      return render(request, "nhansu.html", {"employee": employees_serializer.data})
  # if request.method == 'POST':
    #  employees = Employees.objects.all()
    #  employees_serializer = EmployeeSerializer(employees, many=True)
    #  return render(request, "suanhansu.html", {"employee": employees_serializer.data})
   elif request.method == 'POST' and 'update' in request.POST:
      print(request.POST)
      manhavien = request.POST['update']
    #  record = Employees.objects.get(EmployeeId=manhavien)
    #  record.update()
     # employees = Employees.objects.all()
     # employees_serializer = EmployeeSerializer(employees, many=True)
    #  return render(request, "nhansu.html", {"employee": employees_serializer.data})
      return redirect(func_SuanhansuView,manhavien)
   
   
   
   

def func_Themnhanvienview(request, *args, **kwargs): # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "themnhanvien.html", {})
def func_SuanhansuView(request,id, *args, **kwargs): # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code

   if request.method=='GET':
      record = Employees.objects.get(EmployeeId=id)
      return render(request, "suanhansuclone.html",{"employee":record})
     # print(record)
     # employees_serializer0 = EmployeeSerializer(record, many=True)
    #  print(">>>>>>",employees_serializer0)
   elif request.method=='POST':
        employees= Employees.objects.get(EmployeeId=id)
        myfile = request.FILES['avata'] 
        bophan={"1": "Dev","2": "Game design","3": "Art","4":"Tester"}
        Chuvu ={"1":"Nhân viên","2":"Leader","3":"Quản lý","4":"Giám đốc"}
      #  id_NV =request.POST.get('inputmnv')
        InputTen = request.POST.get('name')
        InputSoDienThoai = request.POST.get('inputTel')
        InputEmail = request.POST.get('inputEmail')
        InputBirthDate = request.POST.get('inputdate')
      #  inpurAddress=request.POST.get('inputdate')
        InputTeam = request.POST.get('inputbophan')
        Inputchucvu= request.POST.get('inputchucdanh')
        Inputdiachi=request.POST.get('diachi')
   #     print("da chay",request.user.get_all_permissions())
        print("Dachay>>>>>>>>>>>>>>>>")
        employees.EmployeeName=InputTen
        employees.Date_of_birth=InputBirthDate
        employees.PhoneNumber=InputSoDienThoai
        employees.Address_Employee=Inputdiachi

        employees.Department=bophan[str(InputTeam)]
        employees.Position_Employee=Chuvu[str(Inputchucvu)]
        employees.Email=InputEmail
        employees.Avatar=myfile
        
       # InputAvatar= myfile.name
       # print(InputTen,InputSoDienThoai,InputEmail,InputBirthDate)
        print(Chuvu[str(Inputchucvu)],Inputdiachi)
        print(InputTen,InputBirthDate,InputSoDienThoai,
        bophan[str(InputTeam)],Chuvu[str(Inputchucvu)],InputEmail,myfile)

       # employees = Employees.objects.create(EmployeeName=InputTen,Date_of_birth=InputBirthDate,PhoneNumber=InputSoDienThoai,Address_Employee=inputdiachi,Department=bophan[str(InputTeam)],Position_Employee=Chuvu[str(Inputchucvu)],Email=InputEmail,Avatar=myfile)

     #   print(employees)
        employees.save()
        employees = Employees.objects.all()
        employees_serializer=EmployeeSerializer(employees,many=True)
    #  print(request.user.get_all_permissions())
        print(employees_serializer.data)
        return render(request, "nhansu.html", {"employee":employees_serializer.data})




  # return render(request, "suanhansuclone.html",{"employee":record})


def func_GreenView(request, id, *args, **kwargs):  # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code

   if request.method == 'GET':
      record = Employees.objects.get(EmployeeId=id)
     # print(record)
     # employees_serializer0 = EmployeeSerializer(record, many=True)
    #  print(">>>>>>",employees_serializer0)

   return render(request, "suanhansuclone.html", {"employee": record})
