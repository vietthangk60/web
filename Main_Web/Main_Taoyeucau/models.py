from django.db import models

# Create your models here.
class Taoyeucau(models.Model):
    YeucauId = models.AutoField(primary_key=True)
    Nguoiyeucau = models.CharField(max_length=500)
    Thongtinyeucau  = models.CharField(max_length=500)
    Lydo = models.CharField(max_length=5000)
    Nguoiduyet =models.CharField(max_length=1000)
    Ngaygui = models.DateField()
    #   Department = models.CharField(max_length=500)
    #   Position_Employee=models.CharField(max_length=500)
    #   Avatar = models.ImageField(upload_to='images',null='False')
    #   DateOfJoining = models.DateField()
    #   PhotoFileName = models.CharField(max_length=500)