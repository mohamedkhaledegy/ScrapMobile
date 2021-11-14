from django.contrib import admin
from .models import *

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('slug','join_date')

# Register your models here.

admin.site.register(Profile, ProfileAdmin)