from rest_framework import serializers
from Main_Yeucau.models import yeucaudaduyet



class yeucaudaduyetSerializer(serializers.ModelSerializer):
    class Meta:
        model=yeucaudaduyet 
        fields=('YeucauId','NguoiyeucauId','Nguoiyeucau','Thongtinyeucau','Lydo','Nguoiduyet',
        'Ngaygui','thoigianbatdau','thoigianketthuc','Trangthaiduyet')
        