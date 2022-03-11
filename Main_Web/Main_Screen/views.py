from django.shortcuts import render
from django.http import HttpRequest
from Main_ThemnhanVien.models import Employees
from Main_ThemnhanVien.serializers import EmployeeSerializer
from django.core.mail import send_mail
import math, random
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def func_Mainview(request,id=0): # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "index.html", {})
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
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "OTP.html", {})
