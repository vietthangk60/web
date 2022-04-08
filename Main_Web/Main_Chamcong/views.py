from email.policy import default
from django.shortcuts import render
from django.http import HttpRequest
from Main_ThemnhanVien.models import Employees
from Main_ThemnhanVien.serializers import EmployeeSerializer


from Main_Chamcong.models import Chamcong

from Main_Chamcong.serializers import ChamcongSerializer

from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.mail import send_mail
import math
import random
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, decorators, logout
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
@decorators.login_required(login_url='/login.html')
def func_ChamcongView(request, *args, **kwargs): # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    
   if request.method == 'POST':
         if request.method == 'POST':
            tmp_xacnhan = request.POST.get("sua")
            
            if tmp_xacnhan == "1":
               logout(request)
               return redirect(func_DXChamcongView)
            data=JSONParser().parse(request)
            print(data["date"])
            current_user = request.user
            idnhanvien = str(current_user)
            em = Employees.objects.get(EmployeeId=idnhanvien)   

            tmp_id_tontai= Chamcong.objects.filter(NguoichamcongId=idnhanvien).exists() 
      #  print(tmp_id_tontai)
            if tmp_id_tontai:
               tmp_dacheckin=Chamcong.objects.all().filter(NguoichamcongId=idnhanvien).filter(Ngaycham=data["date"]).exists() 
               print("tmp_dacheckin",tmp_dacheckin)
               if tmp_dacheckin:
                  checkin=Chamcong.objects.all().filter(NguoichamcongId=idnhanvien).get(Ngaycham=data["date"])
                  checkin.Gioketthuc=data["time"]
                  print(checkin)
                  checkin.save()
               else:
            
                  nhanvienchamcong=Chamcong.objects.create(NguoichamcongId=idnhanvien,Tennguoichamcong=em.EmployeeName,Thongtin="Gio hanh chinh",Ngaycham=data["date"],Giobatdau=data["time"],Gioketthuc=None)
                  nhanvienchamcong.save()
            else:
                  nhanvienchamcong=Chamcong.objects.create(NguoichamcongId=idnhanvien,Tennguoichamcong=em.EmployeeName,Thongtin="Gio hanh chinh",Ngaycham=data["date"],Giobatdau=data["time"],Gioketthuc=None)
                  nhanvienchamcong.save()              


   current_user = request.user
   
   idnhanvien = str(current_user)
   em = Chamcong.objects.all()
  
   print("user_name", em)
   Data = { "nhanvien": em}
   return render(request, "chamcong.html", Data)


def func_CaidatchamcongView(request, *args, **kwargs): # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
   if request.method=='GET':
      employees = Employees.objects.all()
      employees_serializer=EmployeeSerializer(employees,many=True)
    #  print(request.user.get_all_permissions())
     
      return render(request, "caidatchamcong.html", {"employee":employees_serializer.data})
   elif request.method == 'POST' and 'update' in request.POST:
      
      manhanvien = request.POST['update']
      return redirect(func_SuaanhnhandienView,manhanvien)
   elif request.method=='POST' and 'delete' in request.POST:

         manhanvien=request.POST['delete']
         employees1 = Employees.objects.get(EmployeeId=manhanvien)
         employees1.Image=None
         employees1.save()
         employees = Employees.objects.all()
         employees_serializer=EmployeeSerializer(employees,many=True)
         return render(request, "caidatchamcong.html", {"employee": employees_serializer.data})




  # return render(request, "caidatchamcong.html", {})

def func_ChamcongwebView(request, *args, **kwargs):  # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "chamcongweb.html", {})
 
def func_DanhsachCamView(request, *args, **kwargs):  # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code

 if request.method == 'POST':
      if request.method == 'POST':
           tmp_xacnhan = request.POST.get("sua")
      if tmp_xacnhan == "1":
         logout(request)
         return redirect(func_DXChamcongView)

 current_user = request.user
 print("user_name", current_user)
 idnhanvien = str(current_user)
 em = Employees.objects.get(EmployeeId=idnhanvien)
 print(em)

 Data = {"nhanvien": em}
 return render(request, "danhsach_cam.html", Data)
 
def func_LienketCamView(request, *args, **kwargs):  # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "lienket_cam.html", {})
 
def func_SuaanhnhandienView(request,id, *args, **kwargs): # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code

   if request.method=='GET':
      record = Employees.objects.get(EmployeeId=id)
      return render(request, "idface.html",{"employee":record})
   elif request.method=='POST':
        employees= Employees.objects.get(EmployeeId=id)
        file=request.FILES
        print("FIle",file)
        if 'Image' not in file:
              # myfile=employees.Avatar
              return redirect(func_CaidatchamcongView)
        else:          
            myfile = request.FILES.get('Image') 
            print("mMMMM",myfile)
            employees.Image=myfile
            employees.save()
            employees = Employees.objects.all()
            employees_serializer=EmployeeSerializer(employees,many=True)
            return redirect(func_CaidatchamcongView)
   return render(request, "idface.html", {"employee": employees_serializer.data})


def func_DXChamcongView(request, *args, **kwargs):  # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
   if request.method == 'GET':

       if request.user.is_authenticated:
         return redirect(func_ChamcongView)

       return render(request, "login.html", {"data": ""})


def func_DXCamView(request, *args, **kwargs):  # *args, **kwargs
     # print(args, kwargs)
     # print(request.user)
     #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    if request.method == 'GET':

       if request.user.is_authenticated:
         return redirect(func_LienketCamView)

       return render(request, "login.html", {"data": ""})
