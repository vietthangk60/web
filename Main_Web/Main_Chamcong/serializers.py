from rest_framework import serializers
from Main_Chamcong.models import Chamcong



class ChamcongSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chamcong 
        fields=('ChamcongId','NguoichamcongId','Tennguoichamcong','Thongtin','Ngaycham','Giobatdau','Gioketthuc')
        