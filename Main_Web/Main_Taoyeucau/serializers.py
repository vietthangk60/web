from rest_framework import serializers
from Main_Taoyeucau.models import Taoyeucau



class TaoyeucauSerializer(serializers.ModelSerializer):
    class Meta:
        model=Taoyeucau 
        fields=('YeucauId','NguoiyeucauId','Nguoiyeucau','Thongtinyeucau','Lydo','Nguoiduyet','Ngaygui','thoigianbatdau','thoigianketthuc','Trangthaiduyet')