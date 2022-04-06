from django.db import models


from Main_ThemnhanVien.models import Employees
# Create your models here.
class Chamcong(models.Model):
    ChamcongId = models.AutoField(primary_key=True)
    NguoichamcongId=models.CharField(max_length=10)
    Tennguoichamcong=models.CharField(max_length=10)
    Thongtin  = models.CharField(max_length=500)
    Ngaycham=models.DateField()
    Giobatdau=models.TimeField()
    Gioketthuc=models.TimeField()

class CaidatCamera(Employees):
        Image = models.ImageField(upload_to='images',null='False')
