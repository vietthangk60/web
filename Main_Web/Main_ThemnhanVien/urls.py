from django.conf.urls import url
from Main_ThemnhanVien import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
  #  url(r'^department$',views.departmentApi),
   # url(r'^department/([0-9]+)$',views.departmentApi),

    url(r'^themnhanvien.html$',views.employeeApi),
   # url(r'^themnhanvien.html$',views.register_attempt),
   # url(r'^themnhanvien.html/([0-9]+)$',views.employeeApi),

  #  url(r'^employee/savefile',views.SaveFile)
]