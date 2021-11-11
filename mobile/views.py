from django.shortcuts import render , get_object_or_404
from .models import *




# Create your views here.




def index(request ):
    
    slug_samsung='samsung'
    filterd_brands = Device.objects.filter(brand__slug=slug_samsung)[:10]
    
    context = {
        'device' : Device.objects.all()[:40] ,
        'brand'  : Brand.objects.all() ,
            }
    return render(request , 'index.html',context)

def get_mobile(request , id):
    
    
    return render(request )

def brand_mobs(request , slug):
    filterd_brands = Device.objects.filter(brand__slug=slug)
    context = {
            'devs' : filterd_brands ,
        }
    return render(request , 'index.html' , context)

def single_device(request , slug):
    device_detail = get_object_or_404(Device ,slug_dev=slug)
    
    filterd_spares = Spare.objects.filter(device_main__slug_dev=slug)
    #spare_detail = get_object_or_404(Spare , device_main__slug_dev=slug)
    context = {
        'dev' : device_detail ,
        'spares' : filterd_spares,
    }
    return render(request , 'pages/mobile.html' , context)

def all_brands(request):
    context = {
        'brands'  : Brand.objects.all() ,
    }
    return render(request , 'pages/brands.html' , context)


def brand_sprs(request , slug):
    filterd_brands = Spare.objects.filter(brand__slug=slug)
    context = {
            'devs' : filterd_brands ,
        }
    return render(request , 'pages/spares.html' , context)


### لقياس الوقت المستغرق لاى خوارزمية
##### start_time = time.time()
##### time_taken = time.time() - start_time