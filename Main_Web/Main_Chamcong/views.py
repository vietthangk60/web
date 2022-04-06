from email.policy import default
from django.shortcuts import render
from django.http import HttpRequest
from Main_ThemnhanVien.models import Employees
from Main_ThemnhanVien.serializers import EmployeeSerializer
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
       
 current_user = request.user
 print("user_name", current_user)
 idnhanvien = str(current_user)
 em = Employees.objects.get(EmployeeId=idnhanvien)
 print(em)

 Data = { "nhanvien": em}
 return render(request, "chamcong.html", Data)


def func_CaidatchamcongView(request, *args, **kwargs): # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "caidatchamcong.html", {})

def func_ChamcongwebView(request, *args, **kwargs):  # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "chamcongweb.html", {})
 
def func_DanhsachCamView(request, *args, **kwargs):  # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "danhsach_cam.html", {})
 
def func_LienketCamView(request, *args, **kwargs):  # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "lienket_cam.html", {})
 
def func_SuaanhnhandienView(request, *args, **kwargs): # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "idface.html", {})


def func_DXChamcongView(request, *args, **kwargs):  # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    if request.method == 'GET':

       if request.user.is_authenticated:
         return redirect(func_ChamcongView)

       return render(request, "login.html", {"data": ""})
