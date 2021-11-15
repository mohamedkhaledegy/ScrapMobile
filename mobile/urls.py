from django.urls import path
from . import views

app_name = 'mobile'

urlpatterns = [

    path('',views.index , name='index' ),# الصفحة الرئيسية
    path('device/samsung-s20/sell',views.sell , name='sell' ), #صفحة البيع
    path('device/<slug:slug>/' ,views.mobile , name='mobile'), # صفحة الموبايل
    path('device-full-info/<slug:slug>' ,views.get_mob , name='mob'), # صفحة الموبايل
    path('brand/<slug:slug>/' ,views.brand_mobs , name='brand_mobiles_list'), # صفحة البرندات
    path('about/' ,views.about , name='about'), # صفحة about
    ]