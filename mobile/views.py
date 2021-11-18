from django.shortcuts import render , get_object_or_404
from .models import *
from .filters import *
from django_user_agents.utils import get_user_agent

# Create your views here.

def index(request):
    #slug_samsung='samsung'
    #filterd_brands = Device.objects.filter(brand__slug=slug_samsung)[:10]
    devices = Device.objects.all()
    if request.GET:
        filterd_brands = Device2Filter(request.GET , queryset=devices)
    else:
        filterd_brands = Device2Filter( queryset=devices)
    devices = filterd_brands.qs
    devices_count = devices.count()
    context = {
        'devs' : devices[:200] ,
        'brand'  : Brand.objects.all() ,
        'filterd_devs' : filterd_brands , 
        'devs_count' : devices_count ,
            }
    return render(request , 'index.html',context)

def auto_detect(request ):
    family = None
    brd = None
    mobmodel = None
    if request.user_agent.is_mobile:
        print(request.user_agent.device)
        family = request.user_agent.device.family    
        brd = request.user_agent.device.brand
        mobmodel = request.user_agent.device.model
        try:
            device = Device.objects.filter(modeldev__contains=mobmodel)
            print(device.count())
            print(device.all())
        except:
            device = 'Not Found In Database'
    else:
        print(request.user_agent)
        device = 'PC'
    

    context = {
        'family' : family ,
        'brand' : brd ,
        'mobmodel':mobmodel ,
        'devs' : device ,
    }
    return render(request , 'mobily.html' , context)

def brand_mobs(request , slug):
    
    devices = Device.objects.all()
    filterd_brands = DeviceFilter(request.GET , queryset=devices)
    print(filterd_brands)    
    context = {
            'devs' : devices ,
            'filter' : filterd_brands ,
            'slug' : slug ,
        }
        
    return render(request , 'pages/brand-mobiles-list.html' , context)

def validate_devnames(request):
    devs = request.GET.get('devs')
    is_taken = Device.objects.filter()
    pass

def sell(request):
    context = {
        'devs':Device.objects.all()
    }
    return render(request , 'test.html' , context)
    
def mobile(request , slug):
    mob = get_object_or_404(Device , slug_dev=slug)
    
    spara = Spare.objects.filter(device_main=mob.id)
    if request.user_agent.is_mobile:
        print(request.user_agent.device)
    else:
        print(request.user_agent)
    context = {
        'mobile' : mob ,
        'spr' : spara ,
    }
    return render(request , 'index-mob.html' ,context )


def about (request):
    context = {
        'devs':Device.objects.all()
    }
    return render(request , 'pages/about.html' , context)







def get_mob(request , slug):
    device = get_object_or_404(Device , slug_dev=slug)
    context = { 'dev':device }
    return render(request , 'devices/device-list.html' , context)

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