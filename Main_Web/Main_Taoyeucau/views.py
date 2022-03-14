from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Main_Taoyeucau.models import Taoyeucau
from Main_Taoyeucau.serializers import TaoyeucauSerializer

from django.core.files.storage import default_storage

@csrf_exempt
def yeucauApi(request):
    if request.method=='GET':
        Taoyeucau = Taoyeucau.objects.all()
        Taoyeucau_serializer=TaoyeucauSerializer(Taoyeucau,many=True)
        return render(request, "taoyeucau.html", {})
    elif request.method=='POST':
        InputTen = request.POST.get('inputname')
        InputSoDienThoai = request.POST.get('inputtel')
        InputTu = request.POST.get('inputdate1')
        InputDen = request.POST.get('inputdate2')
        inputLoaiYeuCau=request.POST.get('inputloaiyeucau')
        InputLoaiNghiPhep = request.POST.get('inputloainghiphep')
        InputLyDo= request.POST.get('inputlydo')


        print(Chuvu[str(Inputchucvu)],inputdiachi)
        print(InputTen,inputdiachi, InputSoDienThoai,bophan[str(InputTeam)],Chuvu[str(Inputchucvu)],InputEmail,myfile)

        yeucau = Yeucau.objects.create(Nguoiyeucau=InputTen, PhoneNumber=InputSoDienThoai, InputTu=inputdate1, InputDen=inputdate2, inputLoaiYeuCau=inputloaiyeucau, InputLoaiNghiPhep=inputloainghiphep, InputLyDo=inputlydo )

        employees = Employees.objects.all()
        employees_serializer=EmployeeSerializer(employees,many=True)

        return render(request, "yeucaucanduyet.html", {"employee":employees_serializer.data})
    #    return  render(request, "nhansu.html",{})
