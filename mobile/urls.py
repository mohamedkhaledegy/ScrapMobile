from django.urls import path
from . import views


urlpatterns = [
    path('',views.index , name='index' ),
    path('<slug:slug>/' ,views.mobile , name='mobile'),
    path('sell/',views.index , name='sell' ),
    path('<slug:slug>/' ,views.brand_mobs , name='brand_mobiles_list')

    ]