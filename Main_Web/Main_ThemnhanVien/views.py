from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Main_ThemnhanVien.models import Employees
from Main_ThemnhanVien.serializers import EmployeeSerializer

from django.core.files.storage import default_storage


@csrf_exempt
def employeeApi(request):
    if request.method=='GET':
        employees = Employees.objects.all()
        employees_serializer=EmployeeSerializer(employees,many=True)
        return render(request, "themnhanvien.html", {})
        #return JsonResponse(employees_serializer.data,safe=False)
    elif request.method=='POST':
        #employee_data=JSONParser().parse(request)
       # serializer = EmployeeSerializer(data=request.data)
      #  a=request.POST['EmployeeName'] 
       # print("da chay fffsfsfs",employee_data)
       # employees_serializer=EmployeeSerializer(data=employee_data)
        
        #if employees_serializer.is_valid():
           # employees_serializer.save()
           # return JsonResponse("Added Successfully",safe=False)
       # print(employees_serializer.errors)
       # return JsonResponse("Failed to Add",safe=False)
      #  myfile = request.FILES['avata']    # lấy file từ Input Image quá Post
        myfile = request.FILES['avata'] 
        bophan={"1": "Dev","2": "Game design","3": "Art","4":"Tester"}
        Chuvu ={"1":"Nhân viên","2":"Leader","3":"Quản lý","4":"Giám đốc"}
      #  id_NV =request.POST.get('inputmnv')
        InputTen = request.POST.get('inputname')
        InputSoDienThoai = request.POST.get('inputTel')
        InputEmail = request.POST.get('inputEmail')
        InputBirthDate = request.POST.get('inputdate')
        inpurAddress=request.POST.get('inputdate')
        InputTeam = request.POST.get('inputbophan')
        Inputchucvu= request.POST.get('inputchucdanh')
        inputdiachi=request.POST.get('diachi')


       # InputAvatar= myfile.name
       # print(InputTen,InputSoDienThoai,InputEmail,InputBirthDate)
        print(Chuvu[str(Inputchucvu)],inputdiachi)
        employees = Employees.objects.create(EmployeeName=InputTen,Date_of_birth=InputBirthDate,PhoneNumber=InputSoDienThoai,Address_Employee=inputdiachi,Department=bophan[str(InputTeam)],Position_Employee=Chuvu[str(Inputchucvu)],Email=InputEmail,Avatar=myfile)

       # print(employees)
        employees.save()

        employees = Employees.objects.all()
        employees_serializer=EmployeeSerializer(employees,many=True)

        return render(request, "nhansu.html", {"employee":employees_serializer.data})


  #  elif request.method=='PUT':
  #      employee_data=JSONParser().parse(request)
 #       employee=Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
 #       employees_serializer=EmployeeSerializer(employee,data=employee_data)
 #       if employees_serializer.is_valid():
  #          employees_serializer.save()
   #         return JsonResponse("Updated Successfully",safe=False)
  #      return JsonResponse("Failed to Update")
  #  elif request.method=='DELETE':
  #      employee=Employees.objects.get(EmployeeId=id)
 #       employee.delete()
  #      return JsonResponse("Deleted Successfully",safe=False)

#def register_attempt(request):

 #   if request.method == 'POST':
   #     username = request.POST.get('inputname')
   #     print(username)
    #    phone = request.POST.get('phone')
 #      email = request.POST.get('email')
    #    password = request.POST.get('password')
        




  #  return render(request, "themnhanvien.html", {})