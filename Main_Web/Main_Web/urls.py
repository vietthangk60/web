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
from Main_Screen.views import func_Mainview, func_DangxuatView, func_DangnhapView
from Main_Nhansu.views import func_Nhansuview, func_SuanhansuView, func_DXView, func_DXThemnhanvienView
from Main_Giaoviec.views import func_VieccuatoiView, func_DuanView, func_ThemduanView, func_DXVieccuatoiView,  func_DXDuanView, func_KanBanView
from Main_Yeucau.views import func_YeucauView, func_YeucauduyetView, func_TuchoiView, func_DMVSView, func_NghiphepView, func_NghiviecView, func_DXYeucauView, func_DXDuyetView, func_DXTuchoiView
from Main_Taoyeucau.views import yeucauApi
from Main_Chamcong.views import func_ChamcongView, func_CaidatchamcongView, func_SuaanhnhandienView, func_ChamcongwebView, func_DXChamcongView, func_DanhsachCamView, func_LienketCamView, func_DXCamView
from Main_Baocao.views import func_BaocaoView, func_TinhluongView, func_TinhthuongView, func_DXBaocaoView, func_DXLuongView, func_DXThuongView
from django.urls import path
from Main_ThemnhanVien.views import employeeApi
from django.conf.urls import url,include
from django.conf import settings
from Main_Screen import views
from django.conf.urls.static import static
#func_TaoyeucauView
urlpatterns = [
    path('<int:id>/', func_Mainview, name='home'),
    path('index.html', func_Mainview, name='home'),
    path('', func_Mainview, name='home'),
    path('admin/', admin.site.urls),
    path('nhansu.html',func_Nhansuview,name='nhan su'),
    path('<int:id>/nhansu.html', func_Nhansuview, name='nhan su'),
    path('<int:id>/suanhansuclone.html', func_SuanhansuView, name='sua nhan su'),
    path('vieccuatoi.html',func_VieccuatoiView,name='giao viec'),
    path('duan.html',func_DuanView,name='du an'),
    path('kanban.html', func_KanBanView, name='du an'),
    path('themduan.html', func_ThemduanView, name='them du an'),
    path('yeucaucanduyet.html',func_YeucauView,name=' yeu cau'),
    path('daduyet.html',func_YeucauduyetView,name=' yeu cau da duyet'), 
    path('tuchoi.html',func_TuchoiView,name=' tu choi yeu cau '), 
    #path('taoyeucau.html',func_TaoyeucauView,name=' tu choi yeu cau '),
    path('chamcong.html',func_ChamcongView,name=' cham cong '), 
    path('caidatchamcong.html',func_CaidatchamcongView, name=' cai dat cham cong'),
    path('chamcongweb.html',func_ChamcongwebView, name=' cham cong web'),
    path('danhsach_cam.html', func_DanhsachCamView, name=' danh sach cam'),
    path('lienket_cam.html', func_LienketCamView, name=' lien ket cam'),
    path('<int:id>/idface.html',func_SuaanhnhandienView, name=' sua anh nhan dien '),
    path('baocao.html',func_BaocaoView, name=' bao cao '),
    path('tinhluong.html', func_TinhluongView, name=' tinh luong '),
    path('tinhthuong.html', func_TinhthuongView, name=' tinh thuong '),
    path('login.html',func_DangxuatView, name=' dang xuat '),
    path('login.html', func_DXView, name=' dx '),
    path('login.html', func_DXThemnhanvienView, name=' dx '),
    path('login.html', func_DXChamcongView, name=' dxcc '),
    path('login.html', func_DXCamView, name=' dx '),
    path('login.html', func_DXVieccuatoiView, name=' dx '),
    path('login.html', func_DXDuanView, name=' dx '),
    path('login.html', func_DXYeucauView, name=' dx '),
    path('login.html', func_DXDuyetView, name=' dx '),
    path('login.html', func_DXTuchoiView, name=' dx '),
    path('login.html', func_DXBaocaoView, name=' dx '),
    path('login.html', func_DXLuongView, name=' dx '),
    path('login.html', func_DXThuongView, name=' dx '),
    path('<int:id>/OTP.html', func_DangnhapView, name=' dang nhap '),
    path('themnhanvien.html', employeeApi, name=' them nhan vien '),
    path('taoyeucau.html', yeucauApi, name=' yeu cau '),
    path('dmvs.html', func_DMVSView, name=' di muon '),
    path('nghiphep.html', func_NghiphepView, name=' nghi phep '),
    path('nghiviec.html', func_NghiviecView, name=' nghi viec '),
    
    #url(r'^',include('Main_ThemnhanVien.urls')
 #   url(r'^/([0-9]+)/$', views.func_Mainview, name='home'), 

   # path('a/', TemplateView.as_view(template_name="index.html")),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
