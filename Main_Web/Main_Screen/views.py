from email.policy import default
from django.shortcuts import render
from django.http import HttpRequest
from Main_ThemnhanVien.models import Employees
from Main_ThemnhanVien.serializers import EmployeeSerializer
from django.core.mail import send_mail
import math, random
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login,decorators,logout
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
@decorators.login_required(login_url='/login.html')
def func_Mainview(request,id=None): # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    if request.method=='POST':
       tmp_xacnhan=request.POST.get("sua")
       if tmp_xacnhan=="1":
          logout(request)
          return render(request,"login.html")



    Data = {'SoLuongNhanVien': Employees.objects.count()}
    #Data = {'SoLuongDuAn': DuAn.objects.count()}
    #Data = {'SoLuongYeuCau': YeuCau.objects.count()}
    return render(request, "index.html", Data)
 
def func_ChinhsuathongtinView(request, *args, **kwargs):  # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "chinhsuathongtin.html", {})
def func_DangxuatView(request, *args, **kwargs):  # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    if request.method=='GET':

       if request.user.is_authenticated:
         return redirect(func_Mainview,int(request.user.username))

       return render(request, "login.html", {"data":""})
    else:
     # employee=Employees.objects.all()
      mail =request.POST['inputname']

     # employees_serializer=EmployeeSerializer(employee,many=True)
      has_bobs = Employees.objects.filter(Email=mail).exists()
      if has_bobs:
         o=generateOTP()
         print(o)
        # htmlgen = '<p>Your OTP is <strong>'+o+'</strong></p>'
        # send_mail('OTP request',o,'vietthangk54@gmail.com',[mail])

         record = Employees.objects.filter(Email=mail)
         id =record.values_list()[0][0]
         request.session['data'] = o

         return redirect(func_DangnhapView,id)
      else:
         return render(request, "login.html", {"data":"mail sai"})
         
def generateOTP() :
    digits = "0123456789"
    OTP = ""
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
    return OTP



      #record = Employees.objects.get(Email)
     # print(has_bobs)
    #  return render(request, "OTP.html", {})
def func_DangnhapView(request,id,*args, **kwargs):  # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    if request.method=='POST':
       print("da dang nhap",request.POST)
       record = Employees.objects.filter(EmployeeId=id)

       tmp_name =record.values_list()[0][0]
       tmp_sdt = record.values_list()[0][3]
       tmp_user=authenticate(username=tmp_name,password=tmp_sdt)
       login(request,tmp_user)
      # print(record.va)
       return redirect(func_Mainview,id)

    return render(request, "OTP.html", {})
