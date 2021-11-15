from django.db.models import fields
import django_filters
from .models import *

class DeviceFilter(django_filters.FilterSet):
    class Meta:
        model = Device
        fields = ['nameDev', 'brand',]
        #exclude = ['imageDev','img_dev_full_1','img_dev_full_2']

class Device2Filter(django_filters.FilterSet):
    
     class Meta:
         model = Device
         fields = ['nameDev', 'brand']
         filter_overrides = {
             models.CharField: {
                 'filter_class': django_filters.CharFilter,
                 'extra': lambda f: {
                     'lookup_expr': 'icontains',
                 },
             },
         }
