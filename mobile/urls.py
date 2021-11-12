from django.urls import path
from . import views


urlpatterns = [
    path('',views.index , name='index' ),
    path('sell/',views.sell , name='sell' ),
    path('<slug:slug>/' ,views.mobile , name='mobile'), # صفحة الموبايل
    path('brand/<slug:slug>/' ,views.brand_mobs , name='brand_mobiles_list')
    ]