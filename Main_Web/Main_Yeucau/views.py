from django.shortcuts import render
from django.http import HttpRequest
from Main_Taoyeucau.models import Taoyeucau
from Main_Taoyeucau.serializers import TaoyeucauSerializer
from Main_ThemnhanVien.models import Employees
from Main_ThemnhanVien.serializers import EmployeeSerializer

from django.core.files.storage import default_storage
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
# Create your views here.
def func_YeucauView(request, *args, **kwargs): # *args, **kwargs
    if request.method=='GET':
        current_user = request.user
        id=str(current_user)
       # yeucau = Taoyeucau.objects.filter(NguoiyeucauId=id)
        #Taoyeucau_serializer=TaoyeucauSerializer(yeucau,many=True)
      #  print("YEu câu >>>>>>>>>>",yeucau)
        tmp_id_tontai= Taoyeucau.objects.filter(NguoiyeucauId=id).exists() 
        if tmp_id_tontai:
            tmp_chuaduyet=Taoyeucau.objects.all().filter(NguoiyeucauId=id).filter(Trangthaiduyet=0).exists() 
            if tmp_chuaduyet:
               yeucau=Taoyeucau.objects.all().filter(NguoiyeucauId=id).filter(Trangthaiduyet=0)
               Taoyeucau_serializer=TaoyeucauSerializer(yeucau,many=True)
               return render(request, "yeucaucanduyet.html",{"yeucau":yeucau})

        #,Trangthaiduyet=0
        #return render(request, "taoyeucau.html", {"yecau":yeucau})
        return render(request, "yeucaucanduyet.html")
    elif request.method=='POST'and 'duyet' in request.POST:
         idyecau=request.POST.get("duyet")
         yeucau=Taoyeucau.objects.get(YeucauId=idyecau)
         yeucau.Trangthaiduyet=1
         yeucau.save()
         current_user = request.user
         id=str(current_user)
         yeucau=Taoyeucau.objects.all().filter(NguoiyeucauId=id).filter(Trangthaiduyet=0)
         Taoyeucau_serializer=TaoyeucauSerializer(yeucau,many=True)
         return render(request, "yeucaucanduyet.html", {{"yeucau":yeucau}})
    elif request.method=='POST'and 'tuchoi' in request.POST:
         idyecau=request.POST.get("duyet")
         yeucau=Taoyeucau.objects.get(YeucauId=idyecau)
         yeucau.Trangthaiduyet=2
         yeucau.save()
         current_user = request.user
         id=str(current_user)
         yeucau=Taoyeucau.objects.all().filter(NguoiyeucauId=id).filter(Trangthaiduyet=0)
         Taoyeucau_serializer=TaoyeucauSerializer(yeucau,many=True)
         return render(request, "yeucaucanduyet.html", {{"yeucau":yeucau}})      



def func_YeucauduyetView(request, *args, **kwargs): # *args, **kwargs
   if request.method=='GET':
        current_user = request.user
        id=str(current_user)
       # yeucau = Taoyeucau.objects.filter(NguoiyeucauId=id)
        #Taoyeucau_serializer=TaoyeucauSerializer(yeucau,many=True)
      #  print("YEu câu >>>>>>>>>>",yeucau)
        tmp_id_tontai= Taoyeucau.objects.filter(NguoiyeucauId=id).exists() 
        if tmp_id_tontai:
            tmp_chuaduyet=Taoyeucau.objects.all().filter(NguoiyeucauId=id).filter(Trangthaiduyet=1).exists() 
            if tmp_chuaduyet:
               yeucau=Taoyeucau.objects.all().filter(NguoiyeucauId=id).filter(Trangthaiduyet=1)
               Taoyeucau_serializer=TaoyeucauSerializer(yeucau,many=True)
               print("da chay yeu cau")
               #return render(request, "yeucaucanduyet.html",{"yeucau":yeucau})
               return render(request, "daduyet.html", {"yeucau":yeucau})
   return render(request, "daduyet.html")
def func_TuchoiView(request, *args, **kwargs): # *args, **kwargs
   if request.method=='GET':
        current_user = request.user
        id=str(current_user)
       # yeucau = Taoyeucau.objects.filter(NguoiyeucauId=id)
        #Taoyeucau_serializer=TaoyeucauSerializer(yeucau,many=True)
      #  print("YEu câu >>>>>>>>>>",yeucau)
        tmp_id_tontai= Taoyeucau.objects.filter(NguoiyeucauId=id).exists() 
        if tmp_id_tontai:
            tmp_chuaduyet=Taoyeucau.objects.all().filter(NguoiyeucauId=id).filter(Trangthaiduyet=1).exists() 
            if tmp_chuaduyet:
               yeucau=Taoyeucau.objects.all().filter(NguoiyeucauId=id).filter(Trangthaiduyet=0)
               Taoyeucau_serializer=TaoyeucauSerializer(yeucau,many=True)
               return render(request, "tuchoi.html", {"yeucau":yeucau})

   return render(request, "tuchoi.html", {"yeucau":yeucau})

    

def func_TaoyeucauView(request, *args, **kwargs): # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "taoyeucau.html", {})


def func_DMVSView(request, *args, **kwargs):  # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    if request.method=="GET":
        current_user = request.user
        print("user_name",current_user)
        a=str(current_user)
        employees = Employees.objects.get(EmployeeId=a)
        return render(request, "dmvs.html", {"nhanvien":employees})
    elif request.method=="POST":

       current_user = request.user
       print("user_name",current_user)
       idnhanvien=str(current_user)
       print("dachay>>>>>>>>>>>>>>>>>")
       name=request.POST.get("inputname")
       ngayxinnghi=request.POST.get("inputdate")
       gionghi=request.POST.get("thoigianbatdau")
       gioketthuc=request.POST.get("thoigianketthuc")
       lido=request.POST.get("lydo")
       print(ngayxinnghi,gionghi,gioketthuc,lido)
       ngay_gio_bd=ngayxinnghi+" "+gionghi
       ngay_gio_kt=ngayxinnghi+" "+gioketthuc
       yeucau =Taoyeucau.objects.create(NguoiyeucauId=idnhanvien,Nguoiyeucau=name,Thongtinyeucau="Đi muộn về sớm ",Lydo=lido,Nguoiduyet="thang",
       thoigianbatdau=ngay_gio_bd,thoigianketthuc=ngay_gio_kt,Trangthaiduyet=0)
       yeucau.save()
       return render(request, "yeucaucanduyet.html", {})

       
    


def func_NghiphepView(request, *args, **kwargs):  # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "nghiphep.html", {})
 
 
def func_NghiviecView(request, *args, **kwargs):  # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "nghiviec.html", {})
