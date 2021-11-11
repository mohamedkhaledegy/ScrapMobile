from django.urls import path
from . import views


urlpatterns = [
    path('',views.index , name='index' ),
    path('sell/',views.sell , name='selll' ),
    path('<slug:slug>/' ,views.mobile , name='mobile'),
    path('<slug:slug>/' ,views.brand_mobs , name='brand_mobiles_list')
    ]