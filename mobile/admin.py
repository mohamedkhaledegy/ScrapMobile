from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(Device)
class DeviceImportExport(ImportExportModelAdmin):
    pass

class BrandAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name')
    ## العواميد اللى بتظهر فى الادمين داشبورد 

admin.site.register(Brand, BrandAdmin)


class SpareAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand')
    ## العواميد اللى بتظهر فى الادمين داشبورد 

@admin.register(Spare)
class SpareImportExport(ImportExportModelAdmin):
    pass

admin.site.register(Tag)