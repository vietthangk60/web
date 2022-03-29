from django.shortcuts import render
from django.http import HttpRequest
from Main_ThemnhanVien.models import Employees
from Main_ThemnhanVien.serializers import EmployeeSerializer
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, decorators, logout
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
@decorators.login_required(login_url='/login.html') 
def func_BaocaoView(request, *args, **kwargs): # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    if request.method == 'POST':
           tmp_xacnhan = request.POST.get("sua")
           if tmp_xacnhan == "1":
              logout(request)
              return redirect(func_DXBaocaoView)
    current_user = request.user
    print("user_name", current_user)
    idnhanvien = str(current_user)
    em = Employees.objects.get(EmployeeId=idnhanvien)
    print(em)
    Data = {"nhanvien": em}
    return render(request, "baocao.html", Data)


def func_TinhluongView(request, *args, **kwargs):  # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    if request.method == 'POST':
        tmp_xacnhan = request.POST.get("sua")
        if tmp_xacnhan == "1":
            logout(request)
            return redirect(func_DXLuongView)
         
    current_user = request.user
    print("user_name", current_user)
    idnhanvien = str(current_user)
    em = Employees.objects.get(EmployeeId=idnhanvien)
    print(em)
    Data = {"nhanvien": em}
    return render(request, "tinhluong.html", Data)


def func_TinhthuongView(request, *args, **kwargs):  # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    if request.method == 'POST':
        tmp_xacnhan = request.POST.get("sua")
        if tmp_xacnhan == "1":
            logout(request)
            return redirect(func_DXThuongView)

    current_user = request.user
    print("user_name", current_user)
    idnhanvien = str(current_user)
    em = Employees.objects.get(EmployeeId=idnhanvien)
    print(em)
    Data = {"nhanvien": em}
    return render(request, "tinhthuong.html", Data)


def func_DXBaocaoView(request, *args, **kwargs):  # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    if request.method == 'GET':

       if request.user.is_authenticated:
         return redirect(func_BaocaoView)

       return render(request, "login.html", {"data": ""})


def func_DXLuongView(request, *args, **kwargs):  # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    if request.method == 'GET':

       if request.user.is_authenticated:
         return redirect(func_TinhluongView)

       return render(request, "login.html", {"data": ""})


def func_DXThuongView(request, *args, **kwargs):  # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    if request.method == 'GET':

       if request.user.is_authenticated:
         return redirect(func_TinhthuongView)

       return render(request, "login.html", {"data": ""})
