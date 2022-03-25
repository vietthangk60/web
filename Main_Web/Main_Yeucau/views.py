from django.shortcuts import render
from django.http import HttpRequest
from Main_Taoyeucau.models import Taoyeucau
from Main_Taoyeucau.serializers import TaoyeucauSerializer

from Main_ThemnhanVien.models import Employees
from Main_ThemnhanVien.serializers import EmployeeSerializer

from Main_Yeucau.models import yeucaudaduyet
from Main_Yeucau.serializers import yeucaudaduyetSerializer

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
      #   yeucau.save()
         print(yeucau.NguoiyeucauId,yeucau.Nguoiyeucau,yeucau.Thongtinyeucau)
      
         yeucaudaduyet_1 =yeucaudaduyet.objects.create(NguoiyeucauId=yeucau.NguoiyeucauId,Nguoiyeucau=yeucau.Nguoiyeucau,Thongtinyeucau=yeucau.Thongtinyeucau,Lydo=yeucau.Lydo,Nguoiduyet=yeucau.Nguoiduyet,
         thoigianbatdau=yeucau.thoigianbatdau,thoigianketthuc=yeucau.thoigianketthuc,Trangthaiduyet=yeucau.Trangthaiduyet)
         
         print(yeucaudaduyet_1)
      #   yeucaudaduyet_1.save()
         yeucau.delete()

         current_user = request.user
         id=str(current_user)
         tmp_id_tontai= Taoyeucau.objects.filter(NguoiyeucauId=id).exists() 
         if tmp_id_tontai:
            tmp_chuaduyet=Taoyeucau.objects.all().filter(NguoiyeucauId=id).filter(Trangthaiduyet=0).exists() 
            if tmp_chuaduyet:
               yeucau=Taoyeucau.objects.all().filter(NguoiyeucauId=id).filter(Trangthaiduyet=0)
               Taoyeucau_serializer=TaoyeucauSerializer(yeucau,many=True)
               return render(request, "yeucaucanduyet.html",{"yeucau":yeucau})
         return render(request, "yeucaucanduyet.html", {{"yeucau":yeucau}})
    elif request.method=='POST'and 'tuchoi' in request.POST:
         idyecau=request.POST.get("duyet")
         yeucau=Taoyeucau.objects.get(YeucauId=idyecau)
         yeucau.Trangthaiduyet=2


         yeucaudaduyet =yeucaudaduyet.objects.create(NguoiyeucauId=yeucau.NguoiyeucauId,Nguoiyeucau=yeucau.Nguoiyeucau,Thongtinyeucau=yeucau.Thongtinyeucau,Lydo=yeucau.Lydo,Nguoiduyet=yeucau.Nguoiduyet,
         thoigianbatdau=yeucau.thoigianbatdau,thoigianketthuc=yeucau.thoigianketthuc,Trangthaiduyet=yeucau.Trangthaiduyet)
         yeucaudaduyet.save()
         yeucau.delete()

         current_user = request.user
         id=str(current_user)

         tmp_id_tontai= Taoyeucau.objects.filter(NguoiyeucauId=id).exists() 
         if tmp_id_tontai:
            tmp_chuaduyet=Taoyeucau.objects.all().filter(NguoiyeucauId=id).filter(Trangthaiduyet=0).exists() 
            if tmp_chuaduyet:
               yeucau=Taoyeucau.objects.all().filter(NguoiyeucauId=id).filter(Trangthaiduyet=0)
               Taoyeucau_serializer=TaoyeucauSerializer(yeucau,many=True)
               return render(request, "yeucaucanduyet.html",{"yeucau":yeucau})
         return render(request, "yeucaucanduyet.html", {{"yeucau":yeucau}})


def func_YeucauduyetView(request, *args, **kwargs): # *args, **kwargs
   if request.method=='GET':
        current_user = request.user
        id=str(current_user)
       # yeucau = Taoyeucau.objects.filter(NguoiyeucauId=id)
        #Taoyeucau_serializer=TaoyeucauSerializer(yeucau,many=True)
      #  print("YEu câu >>>>>>>>>>",yeucau)
        tmp_id_tontai= yeucaudaduyet.objects.filter(NguoiyeucauId=id).exists() 
      #  print(tmp_id_tontai)
        if tmp_id_tontai:
            tmp_chuaduyet=yeucaudaduyet.objects.all().filter(NguoiyeucauId=id).filter(Trangthaiduyet=1).exists() 
            if tmp_chuaduyet:
               yeucaudaduyet_1=yeucaudaduyet.objects.all().filter(NguoiyeucauId=id).filter(Trangthaiduyet=1)
             #  yeucaudaduyet_serializer=yeucaudaduyetSerializer(yeucaudaduyet,many=True)
               print("da chay yeu cau")
               #return render(request, "yeucaucanduyet.html",{"yeucau":yeucau})
               return render(request, "daduyet.html", {"yeucau":yeucaudaduyet_1})
   return render(request, "daduyet.html")
def func_TuchoiView(request, *args, **kwargs): # *args, **kwargs
   if request.method=='GET':
        current_user = request.user
        id=str(current_user)
       # yeucau = Taoyeucau.objects.filter(NguoiyeucauId=id)
        #Taoyeucau_serializer=TaoyeucauSerializer(yeucau,many=True)
      #  print("YEu câu >>>>>>>>>>",yeucau)
        tmp_id_tontai= yeucaudaduyet.objects.filter(NguoiyeucauId=id).exists() 
        if tmp_id_tontai:
            tmp_chuaduyet=yeucaudaduyet.objects.all().filter(NguoiyeucauId=id).filter(Trangthaiduyet=2).exists() 
            if tmp_chuaduyet:
               yeucau=yeucaudaduyet.objects.all().filter(NguoiyeucauId=id).filter(Trangthaiduyet=2)
               #Taoyeucau_serializer=TaoyeucauSerializer(yeucau,many=True)
               return render(request, "tuchoi.html", {"yeucau":yeucau})

   return render(request, "tuchoi.html")

    

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
   if request.method == "GET":
        current_user = request.user
        print("user_name", current_user)
        a = str(current_user)
        employees = Employees.objects.get(EmployeeId=a)
        return render(request, "nghiphep.html", {"nhanvien": employees})
   elif request.method == "POST":

       current_user = request.user
       print("user_name", current_user)
       idnhanvien = str(current_user)
       print("dachay>>>>>>>>>>>>>>>>>")
       name = request.POST.get("inputname")
       hinhthucnghi = request.POST.get("hinhthucnghi")
       loainghi = request.POST.get("loainghi")
       ngaybatdau = request.POST.get("ngaybatdau")
       ngayketthuc = request.POST.get("ngayketthuc")
       giobatdau = request.POST.get("thoigianbatdau")
       gioketthuc = request.POST.get("thoigianketthuc")
       lido = request.POST.get("lydo")
       print(hinhthucnghi, loainghi, ngayxinnghi, giobatdau, ngayketthuc, gioketthuc, lido)
       ngay_gio_bd = ngaybatdau+" "+giobatdau
       ngay_gio_kt = ngayketthuc+" "+gioketthuc
       thong_tin_yc =" Nghỉ phép" + " " + hinhthucnghi + " " + loainghi 
       yeucau = Taoyeucau.objects.create(NguoiyeucauId=idnhanvien, Nguoiyeucau=name, Thongtinyeucau=thong_tin_yc, Lydo=lido, Nguoiduyet="thang",
                                         thoigianbatdau=ngay_gio_bd, thoigianketthuc=ngay_gio_kt, Trangthaiduyet=0)
       yeucau.save()
       return render(request, "yeucaucanduyet.html", {})


def func_NghiviecView(request, *args, **kwargs):  # *args, **kwargs
    # print(args, kwargs)
    # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
   if request.method == "GET":
       current_user = request.user
       print("user_name", current_user)
       a = str(current_user)
       employees = Employees.objects.get(EmployeeId=a)
       return render(request, "nghiviec.html", {"nhanvien": employees})
   elif request.method == "POST":

       current_user = request.user
       print("user_name", current_user)
       idnhanvien = str(current_user)
       print("dachay>>>>>>>>>>>>>>>>>")
       name = request.POST.get("inputname")
       ngaybatdaulamviec = request.POST.get("ngaybatdaulamviec")
       ngaynghi = request.POST.get("ngaynghi")
       lido = request.POST.get("lydo")
       print(ngaybatdaulamviec, ngaynghi, lido)
       yeucau = Taoyeucau.objects.create(NguoiyeucauId=idnhanvien, Nguoiyeucau=name, Thongtinyeucau=" Nghỉ việc", Lydo=lido, Nguoiduyet="thang", Trangthaiduyet=0)
       yeucau.save()
       return render(request, "yeucaucanduyet.html", {})

       
    


# def func_NghiphepView(request, *args, **kwargs):  # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
   # return HttpResponse("<h1>Hello World</h1>") # string of HTML code
   # return render(request, "nghiphep.html", {})
 
 
# def func_NghiviecView(request, *args, **kwargs):  # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
   # return HttpResponse("<h1>Hello World</h1>") # string of HTML code
   # return render(request, "nghiviec.html", {})
