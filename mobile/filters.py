from django.db.models import fields
import django_filters
from django_filters.filters import CharFilter
from .models import *

class DeviceFilter(django_filters.FilterSet):
    price__gt = django_filters.NumberFilter(field_name='priceDev', lookup_expr='gt')
    class Meta:
        model = Device
        fields = {'nameDev':['icontains'], 'brand__name':['exact'],}
        #exclude = ['imageDev','img_dev_full_1','img_dev_full_2']

class Device2Filter(django_filters.FilterSet):
    
    model = CharFilter(field_name='modeldev',   lookup_expr='icontains')  #attrs={'class':'form-control text-white text-center',max_length="100"}))
    class Meta:
        model = Device
        fields ={
                 }
        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
        }
