"""Main_Web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from Main_Web.Main_Screen.views import Nhansuview
#from django.views.generic import TemplateView
#from Main_Screen.views import index
#from pages.views import home_view, contact_view, about_view
from Main_Screen.views import func_Mainview,func_ChinhsuathongtinView ,func_DangxuatView ,func_DangnhapView
from Main_Nhansu.views import func_Nhansuview, func_SuanhansuView
from Main_Giaoviec.views import func_VieccuatoiView,func_DuanView
from Main_Yeucau.views import func_YeucauView, func_YeucauduyetView, func_TuchoiView, func_TaoyeucauView, func_DMVSView, func_NghiphepView, func_NghiviecView
from Main_Taoyeucau.views import yeucauApi
from Main_Chamcong.views import func_ChamcongView, func_CaidatchamcongView, func_SuaanhnhandienView
from Main_Baocao.views import func_BaocaoView
from django.urls import path
from Main_ThemnhanVien.views import employeeApi
from django.conf.urls import url,include
from django.conf import settings
from Main_Screen import views
from django.conf.urls.static import static
urlpatterns = [
    path('<int:id>/', func_Mainview, name='home'),
    path('<int:id>/index.html', func_Mainview, name='home'),
    path('', func_Mainview, name='home'),
    path('admin/', admin.site.urls),
    path('<int:id>/nhansu.html',func_Nhansuview,name='nhan su'),
    path('<int:id>/suanhansu.html', func_SuanhansuView, name='sua nhan su'),
    path('<int:id>/vieccuatoi.html',func_VieccuatoiView,name='giao viec'),
    path('<int:id>/duan.html',func_DuanView,name='du an'),
    path('<int:id>/yeucaucanduyet.html',func_YeucauView,name=' yeu cau'),
    path('<int:id>/daduyet.html',func_YeucauduyetView,name=' yeu cau da duyet'), 
    path('<int:id>/tuchoi.html',func_TuchoiView,name=' tu choi yeu cau '), 
    path('<int:id>/taoyeucau.html',func_TaoyeucauView,name=' tu choi yeu cau '),
    path('<int:id>/chamcong.html',func_ChamcongView,name=' cham cong '), 
    path('<int:id>/caidatchamcong.html',func_CaidatchamcongView, name=' cai dat cham cong'),
    path('<int:id>/idface.html',func_SuaanhnhandienView, name=' sua anh nhan dien '),
    path('<int:id>/baocao.html',func_BaocaoView, name=' bao cao '),
    path('login.html',func_DangxuatView, name=' dang xuat '),
    path('chinhsuathongtin.html',func_ChinhsuathongtinView, name=' chinh sua thong tin '),
    path('<int:id>/OTP.html', func_DangnhapView, name=' dang nhap '),
    path('<int:id>/themnhanvien.html', employeeApi, name=' them nhan vien '),
    path('<int:id>/taoyeucau.html', yeucauApi, name=' yeu cau '),
    path('<int:id>/dmvs.html', func_DMVSView, name=' di muon '),
    path('<int:id>/nghiphep.html', func_NghiphepView, name=' nghi phep '),
    path('<int:id>/nghiviec.html', func_NghiviecView, name=' nghi viec '),
    #url(r'^',include('Main_ThemnhanVien.urls')
 #   url(r'^/([0-9]+)/$', views.func_Mainview, name='home'), 

   # path('a/', TemplateView.as_view(template_name="index.html")),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
