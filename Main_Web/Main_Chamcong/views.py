from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def func_Chamcongview(request): # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    if request.method=='POST':
       tmp_xacnhan=request.POST.get("sua")
       if tmp_xacnhan=="1":
          logout(request)
          return redirect(func_DangxuatView)


    return render(request, "chamcong.html", Data)

def func_DangxuatView(request, *args, **kwargs):  # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    if request.method=='GET':

       if request.user.is_authenticated:
         return redirect(func_Mainview)

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
         
 

def func_ChamcongView(request, *args, **kwargs): # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "chamcong.html", {})
 
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
 
def func_SuaanhnhandienView(request, *args, **kwargs): # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "idface.html", {})