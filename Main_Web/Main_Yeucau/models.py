from django.db import models

# Create your models here.
class yeucaudaduyet(models.Model):
   # print("châu aaaaaa")
    YeucauId = models.AutoField(primary_key=True)
    NguoiyeucauId=models.CharField(max_length=10)
    Nguoiyeucau = models.CharField(max_length=500)
    Thongtinyeucau  = models.CharField(max_length=500)
    Lydo = models.CharField(max_length=5000)
    Nguoiduyet =models.CharField(max_length=1000)
    Ngaygui = models.DateField()
    thoigianbatdau=models.DateTimeField()
    thoigianketthuc=models.DateTimeField()
    Trangthaiduyet=models.CharField(max_length=10)