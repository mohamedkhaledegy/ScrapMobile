from django.urls import path
from . import views



urlpatterns = [
    path('',views.index , name='index' ),# الصفحة الرئيسية
    path('sell/',views.sell , name='sell' ), #صفحة البيع
    path('<slug:slug>/' ,views.mobile , name='mobile'), # صفحة الموبايل
    path('mobile-<slug:slug>' ,views.get_mob , name='mob'), # صفحة الموبايل
    path('brand/<slug:slug>/' ,views.brand_mobs , name='brand_mobiles_list'), # صفحة البرندات
    ]