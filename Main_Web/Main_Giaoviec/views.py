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
# Create your views here.


@csrf_exempt
@decorators.login_required(login_url='/login.html')

def func_VieccuatoiView(request, *args, **kwargs): # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    if request.method == 'POST':
        tmp_xacnhan = request.POST.get("sua")
        if tmp_xacnhan == "1":
            logout(request)
            return redirect(func_DXVieccuatoiView)
    current_user = request.user
    print("user_name", current_user)
    idnhanvien = str(current_user)
    em = Employees.objects.get(EmployeeId=idnhanvien)
    print(em)

    Data = {'SoLuongNhanVien': Employees.objects.count(), "nhanvien": em}
    return render(request, "vieccuatoi.html", Data)

def func_DuanView(request, *args, **kwargs): # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    if request.method == 'POST':
        tmp_xacnhan = request.POST.get("sua")
        if tmp_xacnhan == "1":
            logout(request)
            return redirect(func_DXDuanView)
    current_user = request.user
    print("user_name", current_user)
    idnhanvien = str(current_user)
    em = Employees.objects.get(EmployeeId=idnhanvien)
    print(em)

    Data = {'SoLuongNhanVien': Employees.objects.count(), "nhanvien": em}
    return render(request, "duan.html", Data)


def func_ThemduanView(request, *args, **kwargs):  # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code

    return render(request, "themduan.html", {})


def func_KanBanView(request, *args, **kwargs):  # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code

    return render(request, "kanban.html", {})


def func_DXVieccuatoiView(request, *args, **kwargs):  # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    if request.method == 'GET':

       if request.user.is_authenticated:
         return redirect(func_VieccuatoiView)

       return render(request, "login.html", {"data": ""})


def func_DXDuanView(request, *args, **kwargs):  # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    if request.method == 'GET':

       if request.user.is_authenticated:
         return redirect(func_DuanView)

       return render(request, "login.html", {"data": ""})
