from django.db.models import fields
import django_filters
from .models import *

class DeviceFilter(django_filters.FilterSet):
    class Meta:
        model = Device
        fields = ['nameDev', 'brand']
        #fields = '__all__'
    