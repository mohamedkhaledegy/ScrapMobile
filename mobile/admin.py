from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(Device)
class DeviceImportExport(ImportExportModelAdmin):
    pass

@admin.register(Brand)
class BrandImportExport(ImportExportModelAdmin):
    pass