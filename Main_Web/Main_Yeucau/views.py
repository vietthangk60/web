from django.shortcuts import redirect, render
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
from django.contrib.auth import authenticate, login, decorators, logout
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
@decorators.login_required(login_url='/login.html')

def func_YeucauView(request, *args, **kwargs): # *args, **kwargs
    if request.method == 'POST':
       tmp_xacnhan = request.POST.get("sua")
       if tmp_xacnhan == "1":
          logout(request)
          return redirect(func_DXYeucauView)
       
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
      
        return render(request, "yeucaucanduyet.html",{})
    elif request.method=='POST'and 'duyet' in request.POST:
         idyeucau=request.POST.get("duyet")
         yeucau=Taoyeucau.objects.get(YeucauId=idyeucau)
         yeucau.Trangthaiduyet=1
      #   yeucau.save()
         print(yeucau.NguoiyeucauId,yeucau.Nguoiyeucau,yeucau.Thongtinyeucau)
         NguoiyeucauId_1=yeucau.NguoiyeucauId
         Nguoiyeucau_1=yeucau.Nguoiyeucau
         Thongtinyeucau_1=yeucau.Thongtinyeucau
         Lydo_1=yeucau.Lydo
         Nguoiduyet_1=yeucau.Nguoiduyet
         thoigianbatdau_1=yeucau.thoigianbatdau
         thoigianketthuc_1=yeucau.thoigianketthuc
         Trangthaiduyet_1=yeucau.Trangthaiduyet
         Ngaygui_1=yeucau.Ngaygui


        
         yeucaudaduyet_1 =yeucaudaduyet.objects.create(NguoiyeucauId=NguoiyeucauId_1,Nguoiyeucau=Nguoiyeucau_1,Thongtinyeucau=Thongtinyeucau_1,Lydo=Lydo_1,Nguoiduyet=Nguoiduyet_1,
         thoigianbatdau=thoigianbatdau_1,thoigianketthuc=thoigianketthuc_1,Trangthaiduyet=Trangthaiduyet_1,Ngaygui=Ngaygui_1)
         
       #  print(yeucaudaduyet_1)
         yeucaudaduyet_1.save()
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
         return render(request, "yeucaucanduyet.html")
    elif request.method=='POST'and 'tuchoi' in request.POST:
         idyeucau=request.POST.get("tuchoi")
         print("id",idyeucau)
         yeucau=Taoyeucau.objects.get(YeucauId=idyeucau)
         yeucau.Trangthaiduyet=2


         NguoiyeucauId_1=yeucau.NguoiyeucauId
         Nguoiyeucau_1=yeucau.Nguoiyeucau
         Thongtinyeucau_1=yeucau.Thongtinyeucau
         Lydo_1=yeucau.Lydo
         Nguoiduyet_1=yeucau.Nguoiduyet
         thoigianbatdau_1=yeucau.thoigianbatdau
         thoigianketthuc_1=yeucau.thoigianketthuc
         Trangthaiduyet_1=yeucau.Trangthaiduyet
         Ngaygui_1=yeucau.Ngaygui


        
         yeucaudaduyet_1 =yeucaudaduyet.objects.create(NguoiyeucauId=NguoiyeucauId_1,Nguoiyeucau=Nguoiyeucau_1,Thongtinyeucau=Thongtinyeucau_1,Lydo=Lydo_1,Nguoiduyet=Nguoiduyet_1,
         thoigianbatdau=thoigianbatdau_1,thoigianketthuc=thoigianketthuc_1,Trangthaiduyet=Trangthaiduyet_1,Ngaygui=Ngaygui_1)
         
       #  print(yeucaudaduyet_1)
         yeucaudaduyet_1.save()
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
         return render(request, "yeucaucanduyet.html")


def func_YeucauduyetView(request, *args, **kwargs): # *args, **kwargs
   if request.method == 'POST':
       tmp_xacnhan = request.POST.get("sua")
       if tmp_xacnhan == "1":
          logout(request)
          return redirect(func_DXDuyetView)
   
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
   if request.method == 'POST':
       tmp_xacnhan = request.POST.get("sua")
       if tmp_xacnhan == "1":
          logout(request)
          return redirect(func_DXTuchoiView)
   
   
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
        print("user_name>>>>>>>>>>",current_user)
        a=str(current_user)
        employees = Employees.objects.get(EmployeeId=a)
        return render(request, "dmvs.html", {"nhanvien":employees})
    elif request.method=="POST":

       current_user = request.user
       print("user_nam<<<<<<<<<<<<<<<<<<<<<<<<<<",current_user)
       idnhanvien=str(current_user)
       print("dachay>>>>>>>>>>>>>>>>>")
       name=request.POST.get("name")
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



       
       return redirect(func_YeucauView)

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
       name = request.POST.get("name")
       print(request.POST)
       print("dachay>>>>>>>>>>>>>>>>>",name)
       hinhthucnghi = request.POST.get("hinhthucnghi")
     #  loainghi = request.POST.get("loainghi")
       ngaybatdau = request.POST.get("ngaybatdau")
       ngayketthuc = request.POST.get("ngayketthuc")
       giobatdau = request.POST.get("giobatdau")
       gioketthuc = request.POST.get("gioketthuc")
       lido = request.POST.get("Lydo")
       print(hinhthucnghi, giobatdau, ngayketthuc, gioketthuc, lido)
       ngay_gio_bd = ngaybatdau+" "+giobatdau
       ngay_gio_kt = ngayketthuc+" "+gioketthuc
       thong_tin_yc =" Nghỉ phép" + " " + hinhthucnghi 
       yeucau = Taoyeucau.objects.create(NguoiyeucauId=idnhanvien, Nguoiyeucau=name, Thongtinyeucau=thong_tin_yc, Lydo=lido, Nguoiduyet="thang",
                                         thoigianbatdau=ngay_gio_bd, thoigianketthuc=ngay_gio_kt, Trangthaiduyet=0)
       yeucau.save()
       return redirect(func_YeucauView)


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
       name = request.POST.get("name")
      # ngaybatdaulamviec = request.POST.get("ngaybatdaulamviec")
       ngaynghi = request.POST.get("inputdate")
       lido = request.POST.get("lydo")
       print( ngaynghi, lido)
       yeucau = Taoyeucau.objects.create(NguoiyeucauId=idnhanvien, Nguoiyeucau=name, Thongtinyeucau=" Nghỉ việc", Lydo=lido, Nguoiduyet="thang", Trangthaiduyet=0,
       thoigianbatdau= ngaynghi +"00:00", thoigianketthuc= ngaynghi + "00:00")
       yeucau.save()
       return redirect(func_YeucauView)

       
    


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
def func_DXYeucauView(request, *args, **kwargs):  # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    if request.method == 'GET':

       if request.user.is_authenticated:
         return redirect(func_YeucauView)

       return render(request, "login.html", {"data": ""})

def func_DXDuyetView(request, *args, **kwargs):  # *args, **kwargs
       # print(args, kwargs)
       # print(request.user)
        #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    if request.method == 'GET':

       if request.user.is_authenticated:
         return redirect(func_YeucauView)

       return render(request, "login.html", {"data": ""})


def func_DXTuchoiView(request, *args, **kwargs):  # *args, **kwargs
    # print(args, kwargs)
    # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    if request.method == 'GET':

       if request.user.is_authenticated:
         return redirect(func_YeucauView)

       return render(request, "login.html", {"data": ""})
