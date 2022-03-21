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
        current_user = request.user
        id=str(current_user)
        #yeucau = Taoyeucau.objects.get(NguoiyeucauId=id)
        #Taoyeucau_serializer=TaoyeucauSerializer(Taoyeucau,many=True)
        #print("YEu câu >>>>>>>>>>",yeucau)
        return render(request, "taoyeucau.html")
    elif request.method=='POST':
 
        return render(request, "yeucaucanduyet.html")
    #    return  render(request, "nhansu.html",{})
