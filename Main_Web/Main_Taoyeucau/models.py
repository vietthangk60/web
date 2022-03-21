from django.db import models

# Create your models here.
class Taoyeucau(models.Model):
    YeucauId = models.AutoField(primary_key=True)
    NguoiyeucauId=models.CharField(max_length=10)
    Nguoiyeucau = models.CharField(max_length=500)
    Thongtinyeucau  = models.CharField(max_length=500)
    Lydo = models.CharField(max_length=5000)
    Nguoiduyet =models.CharField(max_length=1000)
    Ngaygui = models.DateField(auto_now_add=True)
    thoigianbatdau=models.DateTimeField()
    thoigianketthuc=models.DateTimeField()
    Trangthaiduyet=models.CharField(max_length=10)
    #   Department = models.CharField(max_length=500)
    #   Position_Employee=models.CharField(max_length=500)
    #   Avatar = models.ImageField(upload_to='images',null='False')
    #   DateOfJoining = models.DateField()
    #   PhotoFileName = models.CharField(max_length=500)
    